===============================================
并行导出导入  
===============================================

说明
-----------------------------------------------

1. 使用exportdb.sh $dbname可以自动备份数据库中表结构和数据
2. 备份的结果在BAK\*目录中
3. 数据恢复的时候在BAK目录下执行：

  - 创建库（不建议带DELIMIDENT=y环境变量）
  - 检查${dbname}_env_file内容是否正确
  - importdb.sh $dbname  

脚本
-----------------------------------------------
``exportdb.sh`` 内容  

.. code:: shell

  #!/bin/bash
  #脚本功能：将数据导出成文本，迁移至其他实例
  #最后更新时间：2025-11-19
  #使用方法：
  #1.执行该脚本
  #2.输入要导出的数据库名称后回车
  #3.导出程序在后台执行，可执行 ps -ef|grep dbaccess 监控是否所有表都导出完毕
  #4.导出过程中，会在数据文件夹内自动生成数据导入 importdb.sh，执行该脚本可将数据导入至其他实例
  #5.修正三个问题，第一个是外键的自动处理；第二个用dbload替换load解决了长事务的问题；第三实现了并行的dbload
  #6.注意aix平台没有sed -i参数，可能会有问题，需要单独处理
  #7.通过dbload后台执行的方式，并行加载数据，不建议同时使用dbaccess dbname idx.sql。这样可能会带来先创建索引，后倒入数据的现象
  #8.增加对开启DELIMIDENT的处理，以及3.6之后的系统表ID改为大于999
  #9.增加-o的处理，修复-o all
  #10. 修复checkRunDba和checkRunDba1对于导出导入进程的判断。
  
  _loginfo(){
    echo -e "[$(date +'%F %T')] $*"
  }
  
  if [ $# -lt 1 ]; then
    read -p "Please input database name: " DBNAME
  else
    DBNAME=$1
  fi
  
  checkRunDba(){
    RUNDBA=$(ps -ef | grep "dbaccess ${DBNAME}" | grep -v grep | wc -l)
    if [ ${RUNDBA} -gt ${1:-20} ]; then 
      return 1
    else 
      return 0
    fi
  }
    
  BACKDIR=BAK-${DBNAME}-$(date +%Y%m%d%H%M)
  mkdir -p $BACKDIR/ctl
  mkdir -p $BACKDIR/log
  cd $BACKDIR
  
  export DBDATE=Y4MD-
  # 环境变量文件
  env | egrep '(DB_LOCALE|CLIENT_LOCALE|GL_|DBDATE|DELIMIDENT)' | awk -F'=' \
              '{if($0~/ /){print "export "$1"=\047"$2"\047"}else{print "export "$1"="$2}}' > ${DBNAME}_env_file
  
  # 不同版本的系统表ID不一样
  DBVERMID=$(onstat -version | awk -F'.' '/^Build Number:/{print $2}')
  _loginfo "DBVERMID is ${DBVERMID}"
  
  _loginfo "Dbschema out.."
  dbschema -d ${DBNAME} -q -ss ${DBNAME}.sql
  if [ ! $? -eq 0 ]; then 
    _loginfo "Dbschema out error."
    exit 1
  fi
  
  # 设置3.5以下需要获取package
  if [ ${DBVERMID:-5} -ge 5 ]; then 
    _loginfo "Dbschema package out.."
    dbschema -d ${DBNAME} -q -o all ${DBNAME}_package.sql
    if [ ! $? -eq 0 ]; then 
      _loginfo "Dbschema package out error."
      exit 1
    fi
  fi
  
  dbaccess ${DBNAME} - << EOF >/dev/null 2>&1
    unload to BAK_tabname.unl delimiter ' '
    SELECT t.tabname,t.ncols, p.nrows::int8 nrows
    FROM systables t, sysmaster:sysptnhdr p
    WHERE t.tabid > (select tabid from systables where tabname = ' VERSION')
      AND t.tabtype = 'T'
      AND t.partnum = p.partnum
    UNION
    SELECT t.tabname,t.ncols,sum(p.nrows)::int8 nrows
    FROM systables t, sysfragments f, sysmaster:sysptnhdr p
    WHERE t.tabid > (select tabid from systables where tabname = ' VERSION')
      AND t.tabtype = 'T'
      AND t.tabid = f.tabid
      AND f.fragtype = 'T'
      AND f.partn = p.partnum
    GROUP BY 1,2;
  EOF
  
  # 处理表名（开启delimident的情况）
  if [ -f BAK_tabname.unl ]; then
    while read TAB NCOL NROWS
    do
      # 当前规则：表名：第1位是小写字母及"_"，之后是小写字母、数字及"_"，不符合的认为是开了DELIMIDENT
      if [[ "$TAB" =~ ^[a-z_][a-z0-9_]*$ ]] ; then 
        echo "$TAB $NCOL $NROWS 0" >> BAK_tabname.unl_tmp
      else
        echo "$TAB $NCOL $NROWS 1" >> BAK_tabname.unl_tmp 
      fi
    done < BAK_tabname.unl
    mv BAK_tabname.unl BAK_tabname.unl_nodelimident
    if [ -f BAK_tabname.unl_tmp ]; then
      mv BAK_tabname.unl_tmp BAK_tabname.unl
    fi
  fi
  
  _loginfo "Unload tables.."
  while read TAB NCOL NROWS DEL
  do
  {
    if [ x"${DEL}" = x1 ]; then
      TMPTAB="\"${TAB}\""
    else
      TMPTAB="${TAB}"
    fi
    dbaccess ${DBNAME} - << EOF >/dev/null 2>&1
    set isolation to dirty read;
    unload to ${TAB}.unl select * from ${TMPTAB};
  EOF
  }&
    while true
    do
      checkRunDba
      if [ $? -eq 0 ]; then
        break
      else
        sleep 5
      fi
    done
  done < BAK_tabname.unl
  
  _loginfo "Waiting unload..."
  while true
  do
    checkRunDba 0
    if [ $? -eq 0 ]; then
      break
    else
      sleep 5
    fi
  done
  
  _loginfo "Unload table finish."
  
  # 建表语句和建索引语句分离，允许去除主键、约束名称
  echo "set pdqpriority 96;" > IDX_${DBNAME}.sql
  sed -n '/revoke usage /,$p' ${DBNAME}.sql >> IDX_${DBNAME}.sql
  sed -i '/revoke usage /,$d' ${DBNAME}.sql
  
  # 导出注释
  _loginfo "Export comments."
  dbaccess ${DBNAME} - << EOF >/dev/null 2>&1
    -- tabcomm, delimiter '\t' (ctrl + i)
    unload to _tmp_table_comment.unl delimiter '	'
    select 'comment on table ' || tabname || ' is ''' || replace(comments, chr(39), '''''') || ''';' as comment from syscomments;
    -- colcomm, delimiter '\t' (ctrl + i)
    unload to _tmp_column_comment.unl delimiter '	'
    select 'comment on column ' || tabname || '.' || colname || ' is ''' || replace(comments, chr(39), '''''') || ''';' as comment 
    from syscolcomments;
  EOF
  
  if [ -f _tmp_table_comment.unl ]; then
    cat _tmp_table_comment.unl > COMM_${DBNAME}.sql
    rm -f _tmp_table_comment.unl
  fi
  
  if [ -f _tmp_column_comment.unl ]; then
    cat _tmp_column_comment.unl >> COMM_${DBNAME}.sql
    rm -f _tmp_column_comment.unl
  fi
  
  cat << EOF  > importdb.sh
  #!/bin/bash
  # filename : importdb.sh newdbname
  
  if [ \$# -eq 1 ]; then
    NEWDBNAME=\$1
  fi
  OLDDBNAME=${DBNAME}
  NEWDBNAME=\${NEWDBNAME:-${DBNAME}}
  
  checkRunDbl(){
    RUNDBA=\$(ps -ef | grep "dbload \-d \${NEWDBNAME}" | grep -v grep | wc -l)
    if [ \${RUNDBA} -gt \${1:-20} ]; then 
      return 1
    else 
      return 0
    fi
  }
  
  _loginfo(){
    echo -e "[\$(date +'%F %T')] \$*"
  }
  
  if [ -f ${DBNAME}_env_file ]; then
    . ./${DBNAME}_env_file
  fi
  
  DBEXISTS=\$(echo "select count(1) as count from sysdatabases where name = '\${NEWDBNAME}'" | dbaccess sysmaster 2>/dev/null)
  DBEXISTS=\$(echo \${DBEXISTS} | awk '{print \$2}')
  if [ \${DBEXISTS} -eq 0 ]; then
    _loginfo "ERROR: database \${NEWDBNAME} not exists, please create it !"
    _loginfo "  e.g: create database \${NEWDBNAME} in datadbs01 with log; "
    exit 1
  fi
  
  if [ -f ${DBNAME}_package.sql ]; then 
    dbaccess -e \${NEWDBNAME} ${DBNAME}_package.sql 2> \${NEWDBNAME}_package_error_run.log
    if [ ! \$? -eq 0 ]; then
      _loginfo "Load package schema error! Please check if Database [ \${NEWDBNAME} ] exists, or/and DDL error/warning at \${NEWDBNAME}_package_error_run.log. "
      exit 1
    fi
  fi
  
  dbaccess -e \${NEWDBNAME} ${DBNAME}.sql 2> \${NEWDBNAME}_error_run.log
  if [ ! \$? -eq 0 ]; then
    _loginfo "Load schema error! Please check if Database [ \${NEWDBNAME} ] exists, or/and DDL error/warning at \${NEWDBNAME}_error_run.log. "
    exit 1
  fi
  
  awk -v db="\${NEWDBNAME}" '{sum+=\$3}END{printf("Rows: %d for database: "db" will load.\n",sum)}' BAK_tabname.unl
  
  while read TAB NCOL NROWS DEL
  do
    if [ x"\$DEL" = x1 ]; then 
      TMPTAB="\"\$TAB\""
    else
      TMPTAB="\$TAB"
    fi
    cat << ! > ./ctl/\${TAB}.ctl 2>/dev/null
  FILE '\${TAB}.unl' DELIMITER '|' \${NCOL};
  INSERT INTO \${TMPTAB};
  !
  done < BAK_tabname.unl
  
  while read TAB NCOL NROWS DEL
  do
  {
    dbload -d \${NEWDBNAME} -c ./ctl/\${TAB}.ctl -n 5000 -l ./log/\${TAB}.log
  }&
    
    while true
    do
      checkRunDbl
      if [ \$? -eq 0 ]; then
        break
      else
        sleep 5
      fi
    done
  done < BAK_tabname.unl
  
  _loginfo "Waiting for dbload..."
  while true
  do  
    checkRunDbl 0
    if [ \$? -eq 0 ]; then
      onmode -l && onmode -c
      break
    else
      sleep 5
    fi
  done
  
  if [ -f IDX_${DBNAME}.sql ]; then
    dbaccess -e \${NEWDBNAME} IDX_${DBNAME}.sql > ./log/IDX_\${NEWDBNAME}.log 2>&1
    if [ ! \$? -eq 0 ]; then
      _loginfo "Create index had error, check ./log/IDX_\${NEWDBNAME}.log"
    else
      _loginfo "Finish create index."
    fi
  fi
  
  if [ -f COMM_${DBNAME}.sql ]; then
    dbaccess -e \${NEWDBNAME} COMM_${DBNAME}.sql > ./log/COMM_\${NEWDBNAME}.log 2>&1
    if [ ! \$? -eq 0 ]; then
      _loginfo "Comment on table had error, check ./log/COMM_\${NEWDBNAME}.log"
    else
      _loginfo "Finish comment.."
    fi
  fi
  
  exit 0
  
  EOF
  
  chmod +x importdb.sh
  _loginfo "Finish."
  
  exit 0

最后更新日期：2025-11-19
