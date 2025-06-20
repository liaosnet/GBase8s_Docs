# 备份脚本  
## 备份脚本  
`backup.sh` 脚本  

```shell
#!/bin/bash
# filename: backup.sh
# function: GBase 8s Database Server backup shell.
# crontab(root)    : 0 1 * * * su - gbasedbt -c "/opt/gbase/script/backup.sh" >/dev/null 2>&1
# crontab(gbasedbt): 0 1 * * * . /home/gbase/.bash_profile && /opt/gbase/script/backup.sh >/dev/null 2>&1
# write by: liaosnet@gbasedbt.com 2023-12-19
export LANG=C
WORKDIR=$(cd $(dirname $0) && pwd)
LOGFILE=${WORKDIR}/backup_status.log
[ ! -f ${LOGFILE} ] && touch ${LOGFILE}
loginfo(){
  echo -e "[$(date +'%Y-%m-%d %H:%M:%S')] $*" >> ${LOGFILE}
}

## define env
# USERNAME: gbasedbt OR informix
# 指定备份方式及日期，L0DAY表示0级备份日期1，4表示周1和周4，8/9表示无效日期
L0DAY=0
L1DAY=2,5
L2DAY=1,3,4,6
KEEPDAYS=7
USERNAME=gbasedbt
DBSTATUS=$(onstat -c|grep 'On-Line'|wc -l)
BACKUPDIR=$(onstat -c TAPEDEV)
LOGSDIR=$(onstat -c LTAPEDEV)
LOGNEED=1
CURRDAY=$(date +%w)
HADBACKUP=$(onstat -g arc | awk '$1=="name"{need=1}need==1&&$3=="0"{print "1";exit}')

## check env
if [ ! x"$(whoami)" = "x${USERNAME}" ]; then
  loginfo "Must run as user: ${USERNAME}"
  exit 100
fi 

if [ ! "x${DBSTATUS}" = "x1" ]; then
  loginfo "Backup ONLY run On-Line Server which is Primary Server or Standard Server."
  exit 4
fi

if [ ! -d ${BACKUPDIR} ]; then
  loginfo "The Backup dir is not exists."
  exit 3
fi

[ x"${LOGSDIR}" = "x/dev/null" ] && LOGNEED=0
if [[ ${LOGNEED} -eq 1 && ! -d "${LOGSDIR}" ]]; then
  loginfo "The logs backup dir is not exists."
  LOGNEED=0
fi

## backup db
# delete file
KEEPDAYS=${KEEPDAYS:-30}
loginfo "Delete files at $BACKUPDIR which out ${KEEPDAYS} days."
# function find had different action for path。
# or find . -name "*L[0-2]" -type f -mtime +${KEEPDAYS} -exec rm -rf {} \;
cd $BACKUPDIR && find . -name "*L[0-2]" -type f -mtime +${KEEPDAYS} | xargs rm -rf
if [ ${LOGNEED} -eq 1 ]; then
  loginfo "Delete files at $LOGSDIR which out ${KEEPDAYS} days."
  cd $LOGSDIR && find . -name "*_Log*" -type f -mtime +${KEEPDAYS} | xargs rm -rf
fi

if [[ ${L0DAY} =~ ${CURRDAY} ]]; then
  loginfo "Execute L0 backup start..."
  ontape -s -L 0 >> ${LOGFILE} 2>&1
elif [[ ${L1DAY} =~ ${CURRDAY} ]]; then
  loginfo "Execute L1 backup start..."
  ontape -s -L 1 >> ${LOGFILE} 2>&1
elif [[ ${L2DAY} =~ ${CURRDAY} ]]; then
  loginfo "Execute L2 backup start..."
  ontape -s -L 2 >> ${LOGFILE} 2>&1
fi

BAKSTATUS=$?
if [ ${BAKSTATUS} -eq 0 ];then
  loginfo "Execute backup finished."
  exit 0
else
  loginfo "Execute backup error! Try Execute L0 backup start."
  ontape -s -L 0 >> ${LOGFILE} 2>&1
  BAKSTATUS=$?
  loginfo "Execute backup finished with CODE: ${BAKSTATUS}"
  exit ${BAKSTATUS}
fi
```

## systemd服务  
`gbase_backup.service` 备份service  

```text
[Unit]
Description=GBase 8s Database Server backup Service
Wants=network-online.target
After=network.target network-online.target
  
[Service]
Type=simple
User=gbasedbt
Group=gbasedbt
Environment="CLIENT_LOCALE=zh_CN.utf8"
Environment="DB_LOCALE=zh_CN.utf8"
Environment="GBASEDBTSERVER=gbase01"
Environment="GBASEDBTSQLHOSTS=/opt/gbase/etc/sqlhosts"
Environment="GL_USEGLU=1"
Environment="GBASEDBTDIR=/opt/gbase"
Environment="DBDATE=Y4MD-"
Environment="ONCONFIG=onconfig.gbase01"
Environment="PATH=/opt/gbase/bin:/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin"
Environment="IFX_NO_TIMELIMIT_WARNING=y"
ExecStart=/opt/gbase/script/backup.sh
  
[Install]
WantedBy=multi-user.target
```

`gbase_backup.timer` 定时器  

```text
[Unit]
Description=Run gbase_backup service
 
[Timer]
OnCalendar=*-*-* 01:00:00
Unit=gbase_backup.service
 
 
[Install]
WantedBy=timers.target
```

## 使用方法  

```text
需求  
1，需要使用gbasedbt或者informix用户创建定时任务，脚本需要gbasedbt或者informix用户执行；  
2，全备份以TAPEDEV为目录，逻辑日志备份以LTAPEDEV为目录；  
3，备份目录需要足够的空间；  
4，逻辑日志备份需要在ALARMPROGRAM指定的脚本中开启备份，并使用ontape备份方式：
如果ALARMPROGRAM指定的脚本是log_full.sh，需要修改以下：
# 增加cd /，将修改BACKUP_CMD为实际使用的命令
cd /
BACKUP_CMD="ontape -a -d"
如果ALARMPROGRAM指定的脚本是alarmprogram.sh，需要修改以下：
# 修改头部shell为/bin/sh，启用逻辑日志备份，增加cd /，将修改BACKUP_CMD为实际使用的命令
#!/bin/sh
BACKUPLOGS=Y
cd /
BACKUP_CMD="ontape -a -d"

定时任务示例
# 假设目录是/home/gbase/backup，环境变量文件为.bash_profile，使用的脚本为backup.sh
0 1 * * * . /home/gbase/.bash_profile && /home/gbase/backup/backup.sh

脚本说明
backup.sh       正常备份，不压缩
backup_gz.sh    正常备份，备份完成后压缩（数据备份会自动改名，逻辑日志不改名）
backup_pipgz.sh 数据备份的同时执行压缩，逻辑日志在数据备份后执行压缩

以下几个参数根据需要修改
# L0DAY，L1DAY，L2DAY分别表示0，1，2级备份的日期；0表示周日、1表示周一
# KEEPDAYS表示备份文件保存的时间，默认为30天
# USERNAME数据库安装用户。根据数据库版本，可选gbasedbt或者informix
L0DAY=0
L1DAY=1,4
L2DAY=2,3,5,6
KEEPDAYS=30
USERNAME=gbasedbt

Systemd示例  
复制gbase_backup.service和gbase_backup.timer到/usr/lib/systemd/system目录下  
gbase_backup.timer中已经默认设置每天1:00:00执行任务  
gbase_backup.service中的Environment按实际修改（注意不能使用变量方式，如：$GBASEDBTDIR）  
systemctl start gbase_backup.service  
systemctl start gbase_backup.timer  
systemctl enable gbase_backup.timer
```

## 备份时同时压缩  
备份脚本扩展，在备份的同时通过管道进行压缩  
`backup_pipgz.sh`  

```shell
#!/bin/bash
# filename: backup_pipgz.sh
# function: GBase 8s Database Server backup shell.
# crontab(root)    : 0 1 * * * su - gbasedbt -c "/opt/gbase/script/backup_pipgz.sh" >/dev/null 2>&1
# crontab(gbasedbt): 0 1 * * * . /home/gbase/.bash_profile && /opt/gbase/script/backup_pipgz.sh >/dev/null 2>&1
# write by: liaosnet@gbasedbt.com 2024-04-25
export LANG=C
WORKDIR=$(cd $(dirname $0) && pwd)
LOGFILE=${WORKDIR}/status_backup_pipgz.log
[ ! -f ${LOGFILE} ] && touch ${LOGFILE}
loginfo(){
  echo -e "[$(date +'%Y-%m-%d %H:%M:%S')] $*" >> ${LOGFILE}
}

## define env
# USERNAME: gbasedbt OR informix
# L0DAY: level 0 backup
# L1DAY: level 1 backup
# L2DAY: level 2 backup
# 0 = Sun ... 6 = Sat, other = Invalid Date
L0DAY=6
L1DAY=0,1,2,3,4,5
L2DAY=8
KEEPDAYS=14
USERNAME=gbasedbt
DBSTATUS=$(onstat -c|grep 'On-Line'|wc -l)
BACKUPDIR=$(onstat -c TAPEDEV)
LOGSDIR=$(onstat -c LTAPEDEV)
HOSTNAME=$(hostname)
SERVNUM=$(onstat -c SERVERNUM)
LOGNEED=1
CURRDAY=$(date +%w)
HADBACKUP=$(onstat -g arc | awk '$1=="name"{need=1}need==1&&$3=="0"{print "1";exit}')

## check env
if [ ! x"$(whoami)" = "x${USERNAME}" ]; then
  loginfo "Must run as user: ${USERNAME}"
  exit 100
fi 

if [ ! "x${DBSTATUS}" = "x1" ]; then
  loginfo "Backup ONLY run On-Line Server which is Primary Server or Standard Server."
  exit 4
fi

if [ ! -d ${BACKUPDIR} ]; then
  loginfo "The Backup dir is not exists."
  exit 3
fi

[ x"${LOGSDIR}" = "x/dev/null" ] && LOGNEED=0
if [[ ${LOGNEED} -eq 1 && ! -d "${LOGSDIR}" ]]; then
  loginfo "The logs backup dir is not exists."
  LOGNEED=0
fi

ZIPTYPE=gz
ZIPCMD=gzip
if [ -x /usr/bin/xz ]; then
  ZIPTYPE=xz
  ZIPCMD=xz
fi

## backup db
# delete file
KEEPDAYS=${KEEPDAYS:-30}
loginfo "Delete files at $BACKUPDIR which out ${KEEPDAYS} days."
# function find had different action for path。
# or find . -name "*L[0-2]" -type f -mtime +${KEEPDAYS} -exec rm -rf {} \;
cd $BACKUPDIR && find . -name "*L[0-2].[gx]z" -type f -mtime +${KEEPDAYS} | xargs rm -rf
if [ ${LOGNEED} -eq 1 ]; then
  loginfo "Delete files at $LOGSDIR which out ${KEEPDAYS} days."
  cd $LOGSDIR && find . -name "*_Log*.[gx]z" -type f -mtime +${KEEPDAYS} | xargs rm -rf
fi

DATESTR=$(date +%Y%m%d_%H%M%S)
BACKUPPIPGZ=${BACKUPDIR}/${HOSTNAME}_${SERVNUM}_${DATESTR}
if [[ ${L0DAY} =~ ${CURRDAY} ]]; then
  loginfo "Execute L0 backup start and ${ZIPCMD}..."
  ontape -s -L 0 -t STDIO | ${ZIPCMD} > ${BACKUPPIPGZ}_L0.${ZIPTYPE} #>> ${LOGFILE} 2>&1
elif [[ ${L1DAY} =~ ${CURRDAY} ]]; then
  loginfo "Execute L1 backup start and ${ZIPCMD}..."
  ontape -s -L 1 -t STDIO | ${ZIPCMD} > ${BACKUPPIPGZ}_L1.${ZIPTYPE} #>> ${LOGFILE} 2>&1
elif [[ ${L2DAY} =~ ${CURRDAY} ]]; then
  loginfo "Execute L2 backup start and ${ZIPCMD}..."
  ontape -s -L 2 -t STDIO | ${ZIPCMD} > ${BACKUPPIPGZ}_L2.${ZIPTYPE} #>> ${LOGFILE} 2>&1
fi

BAKSTATUS=$?
if [ ${BAKSTATUS} -eq 0 ];then
  loginfo "Backup file: ${BACKUPPIPGZ}_L*.${ZIPTYPE}"
  loginfo "Execute backup finished with code 0"
else
  loginfo "Execute backup error! Try Execute L0 backup start and ${ZIPCMD}."
  ontape -s -L 0 -t STDIO | ${ZIPCMD} > ${BACKUPPIPGZ}_L0.${ZIPTYPE} #>> ${LOGFILE} 2>&1
  BAKSTATUS=$?
  loginfo "Execute backup finished with CODE: ${BAKSTATUS}"
fi

loginfo "Change filename for data backup if need."
cd $BACKUPDIR
for FILE in $(ls *L[0-2] 2>/dev/null)
do
  # modify ${HOSTNAME}_${SERVERNUM}_L${LEVEL} to ${HOSTNAME}_${SERVERNUM}_yyyymmdd_hh24miss_L${LEVEL}
  FILETIME=$(stat $FILE | awk '/Modify:/{gsub("-","");gsub(":","");print $2"_"substr($3,1,6)}')
  NEWFILE=${FILE%_*}_${FILETIME}_${FILE##*_}
  ISSERVNUM=${FILE%_*}
  ISSERVNUM=${ISSERVNUM##*_}
  if [ ! ${#ISSERVNUM} -eq 6 ]; then
    loginfo "Rename ${FILE} to ${NEWFILE}"
    mv ${FILE} ${NEWFILE}
  fi
done
cd $BACKUPDIR
DATAFILE=$(find . -name "*L[0-2]" -type f)
if [ ! x"${DATAFILE}" = x ];then
  loginfo "${ZIPCMD} data backup."
  loginfo "${ZIPCMD} file(s): ${DATAFILE}"
  ${ZIPCMD} ${DATAFILE}
fi
if [ ${LOGNEED} -eq 1 ]; then
  cd $LOGSDIR 
  LOGSFILE=$(find . -name "*_Log*" ! -name "*.[gx]z" -type f)
  if [ ! x"${LOGSFILE}" = x ];then
    loginfo "${ZIPCMD} logs backup."
    loginfo "${ZIPCMD} file(s): ${LOGSFILE}"
    ${ZIPCMD} ${LOGSFILE}
  fi
fi

exit 0
```