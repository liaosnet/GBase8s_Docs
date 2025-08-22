# Server安装与配置（Linux）  
本章节将介绍GBase 8s服务端安装部署及相关配置。  

## 版本说明  
根据安装环境准备申请下载数据库软件介质。  
按以下内容选择合适的软件包  
主版本号：8.7/8.8/8.9  
子版本号：详细的发行版本 2.2.0、3.0.0_1、3.3.0_2、3.5.1_3、3.6.3_3x2_1  
编译环境：编译该软件包的环境。安装环境应与此相同或者相近。   
- YHKylin4_FT 表示是飞腾平台（FT ARM64）、银河麒麟系统   
- CentOS7_aarch64 表示是aarch64通用平台、CentOS7系统  
- RHEL6_x86_64 表示是x86架构（64bit）、RHEL6系统  
- AIX5L 表示IBM Power架构、AIX5系统  
 
如：GBase8sV8.8_AEE_3.6.3_3X2_1_783c8d_RHEL6_x86_64.tar 表示适用于x86_64架构，操作系统为RHEL6（或者兼容）的软件安装包。  

## 硬件要求  
**CPU芯片要求：**  

|序号|CPU架构|CPU型号|
|:---|:---|:---|
|1|x86|intel、amd、海光、兆芯|
|2|POWER|IBM POWER、OpenPower系列|
|3|Itanium|HP-UX Itanium系列|
|4|SPARC|olaris SPARC系列|
|5|ARM|飞腾系列、鲲鹏系列|
|6|MIPS|龙芯3A、龙芯3B系列|
|7|Loongarch|龙芯3C系列|

**内存要求：**  
对于生产环境：内存配置要求不小于CPU内核数*2，swap配置不小于4GB。  

**存储要求：**
数据库为高IO基础软件，对存储IO性能要求较高，建议使用中高端存储（随机读写IOPS在5000以上），如有SSD存储，优先考虑使用SSD存储，RAID采用RAID5或者RAID10模式，数据盘存储容量根据实际数据大小分配（建议分配500GB以上），可使用裸设备或文件系统，如使用文件系统，采用xfs格式文件系统。如没有独立的备份设备，需规划能保留7天备份数据的磁盘空间用于备份。如数据库部署在云主机，划分磁盘应选择高IO高性能类型磁盘。  

**网络要求：**  
数据库网络要求千兆以上网卡，服务网络应当使用不少于两条物理线路的双网卡绑定，如配置了数据库集群，要求配置独立于服务器网络的专用心跳网络（可直连），同样使用双网卡绑定。网卡硬件厂商应提供网卡相应操作系统的网卡驱动，保证ethtool查看网卡信息可正常显示网卡状态信息。  

**备份设备要求：**  
优先使用第三方备份软件进行统一备份策略管理，GBase 8s支持NBU、爱数、鼎甲等备份软件。如没有第三方备份软件，要求准备独立于数据存储以外的存储设备对数据库进行备份，确保生产数据及备份数据不存储于同一存储设备。备份存储可使用中低端存储。

## 安装前准备  
参考 快速安装部分 [安装前准备](../01_Quick-Start/01_Install/011_Before-Install.html "安装前准备")  

## 操作系统配置  
### 设置主机名称及网络  
配置/etc/hosts，确认hostname输出的主机名与IP地址对应匹配  
例如：主机名是node02，对应的物理网卡使用的IP是192.168.0.212  
```text
# /etc/hosts
192.168.0.212	node02
```
非常重要：如果您准备使用 典型安装-自动创建实例 的方式，必须完成此操作！  

### 关闭域名反向解析功能  
在没有使用DNS的环境，可关闭域名反向解析功能，以加速网络连接  
修改/etc/nsswitch.conf配置文件，hosts参数仅保留files，注释掉其它值  
```text
# /etc/nsswitch.conf
hosts:      files # dns myhostname
```

### 关闭selinux  
临时关闭selinux，省去对数据库软件安装的影响  
修改/etc/selinux/config配置文件，修改SELINUX的值为disabled，重启系统  
```text
# /etc/selinux/config
SELINUX=disabled
```

### 关闭或者配置防火墙  
操作系统自带的防火墙可能限制了数据库端口的访问，因此，需要关闭防火墙或者设置防火墙策略，开放相应的端口。  
不同的操作系统，甚至相同操作系统的不同版本，使用的防火墙都不同，因此，关闭防火墙的方式各不同相同，同样的，开放端口的方式也不相同。  
例如，RHEL7或CentOS7中关闭防火墙的操作命令为  
```shell
# RHEL7或者CentOS7或者使用相同内核的操作系统
systemctl stop firewalld
systemctl disable firewalld
```
开放端口的操作命令为  
```shell
# RHEL7或者CentOS7或者使用相同内核的操作系统
firewall-cmd --permanent --zone=public --add-port=9088/tcp
firewall-cmd --reload
```

### 系统依赖库  
数据库软件安装与运行有一定的操作系统环境需求，特别是在某些国产化操作系统中。通常情况下，GBase 8s数据库需要以下程序或者库文件支持。  
- 需要的程序，一般位于/usr/bin目录下，不同的操作系统，所在的目录不同  
    * unzip
    * tar
    * java（可选，若使用系统jre环境需要）

- 需要的库文件，一般位于/usr/lib64目录下，不同的操作系统，所在的目录不同，一般可通过的find / -name 的方式查找。  
    * libc.so.6
    * libm.so.6
    * libncurses.so.5
    * libtinfo.so.5
    * libnsl.so.1（可选，若使用系统jre环境需要）
    * libaio.so.1（可选，使用使用KAIO，需要）

注：有些操作系统中，必须使用操作系统的jre环境，这时libnsl.so.1就是必须的。  
如果缺少相应的，在有apt源或者yum源时，可直接安装。
如，使用yum安装（CentOS内核）：  
```shell
yum -y install unzip tar java-1.8.0-openjdk glibc-devel ncurses-libs libnsl libaio
```
或者（debian内核）：  
```shell
apt -y install unzip tar openjdk-8-jdk glibc-tools libncurses-dev libncurses5-dev libnsl-dev libaio-dev
```

## 数据库自定义安装  

### 创建用户组及用户  
使用root用户创建gbasedbt组  
```shell
[root@node2 install]# groupadd -g 1000 gbasedbt
```
创建gbasedbt用户  
```shell
[root@node2 install]# useradd -g gbasedbt -u 1000 -d /home/gbase -m -s /bin/bash gbasedbt
```
设置gbasedbt用户密码  
```shell
[root@node2 install]# passwd gbasedbt
```
注意1：gbasedbt用户是数据库系统管理员用户，使用操作系统验证密码访问，密码强度应当符合操作系统安全要求。  
注意2：某些操作系统中，首次设置的密码无效，需要首次通过ssh远程登陆并修改密码才能生效。  

### 磁盘规划  
GBase 8s数据库可使用本地文件系统、逻辑卷组或者LUN磁盘祼设备等各种可用设备。各种方式各有优劣，以下按本地文件系统、逻辑卷组和LUN磁盘祼设备三种方式进行配置，按实际可选择其中一个方式。  
示例安装使用以下的空间规划，使用本地文件系统：  

|数据库空间名称|路径|大小|说明|
|:---|:---|:---|:---|
|rootdbs|/data/gbase/rootchk|1GB|根数据库空间|
|plogdbs|/data/gbase/plogchk|1GB|物理日志|
|llogdbs|/data/gbase/llogchk|1GB|逻辑日志|
|sbspace01|/data/gbase/sbspace1|1GB|智能大对象空间，视需要指定大小|
|tempdbs01|/data/gbase/tempchk01|1GB|临时数据库空间，16KB页大小|
|datadbs01|/data/gbase/datachk01|1GB|数据使用的数据库空间，16KB页大小|

以下是创建目录、文件及修改权限操作示例：  
```text
[root@node2 install]# mkdir -p /data/gbase          （创建目录）

[root@node2 install]# chmod 755 /data

[root@node2 install]# chmod 755 /data/gbase

[root@node2 install]# chown gbasedbt:gbasedbt /data/gbase

[root@node2 install]# su – gbasedbt

[gbasedbt@node2 ~]$ cd /data/gbase

[gbasedbt@node2 gbase]$ touch rootchk plogchk llogchk tempchk01 sbspace01 datachk01	            （创建文件）

[gbasedbt@node2 gbase]$ chmod 0660 *            （修改权限）
```
‘### 创建安装目录  
使用root用户创建安装目录  
执行如下命令创建目录install：  
```text
[root@node2 ~]# mkdir install
```

### 安装数据库软件     
将软件包GBase8sV8.8_TL_3.6.3_3X2_1_x86.tar上传至install目录中，请确认软件包是以.tar为后缀，如果是.7z后缀，需要使用7zip工具先解压。  
```text
[root@node2 install]# tar -xvf GBase8sV8.8_AEE_3.6.3_3X2_1_783c8d_RHEL6_x86_64.tar

[root@node2 install]# ls -al
total 684916
drwxr-xr-x 4 root root      4096 Aug 18 15:16 .
drwxr-xr-x 4 root root      4096 Aug 18 15:16 ..
-rwxr-xr-x 1 root root      1035 Apr 29 21:02 .gbase.properties
-rw-r--r-- 1 root root 350720000 Aug 18 15:16 GBase8sV8.8_AEE_3.6.3_3X2_1_783c8d_RHEL6_x86_64.tar
drwxr-xr-x 2 root root      4096 Apr 29 21:02 PluginPak
drwxr-xr-x 2 root root      4096 Apr 29 20:54 doc
-rw-r--r-- 1 root root      1864 Apr 29 21:02 ids.properties
-rwxr-xr-x 1 root root 350513258 Apr 29 21:02 ids_install
-rwxr-xr-x 1 root root     82770 Apr 29 21:02 onsecurity
```
执行安装  
```text
[root@node2 install]# ./ids_install -i silent \
-DLICENSE_ACCEPTED=TRUE -DUSER_INSTALL_DIR=/opt/gbase       （执行静默安装）
```

### 配置、初始化数据库实例  
初始化数据库实例的步骤大致为：配置用户环境变量，数据库配置文件，初始化数据库实例，调整数据库使用的空间。  
#### 配置用户环境变量配置文件.bash_profile  
编辑或者创建gbasedbt用户目录下的.bash_profile配置文件，内容如下：  
```text
# .bash_profile
export GBASEDBTDIR=/opt/gbase									（安装目录）
export GBASEDBTSERVER=gbase01									（实例名称）
export ONCONFIG=onconfig.$GBASEDBTSERVER						（配置文件名称）
export PATH=$GBASEDBTDIR/bin:${PATH}							（加入PATH）
export GBASEDBTSQLHOSTS=/opt/gbase/etc/sqlhosts					（SQLHOSTS路径）

export DB_LOCALE=zh_CN.utf8										（数据库编码）
export CLIENT_LOCALE=zh_CN.utf8									（客户端编码）
export GL_USEGLU=1												（启用GLU）
export DBDATE="Y4MD-"											（指定DBDATE）
export DBACCESS_SHOW_TIME=1
```

#### 配置ONCONFIG配置文件onconfig.gbase01  
复制`$GBASEDBTDIR/etc/onconfig.std`为$ONCONFIG配置文件，修改主要参数内容如下：  
```text
ROOTPATH /data/gbase/rootchk						# ROOTDBS路径
ROOTSIZE 1024000									# ROOTDBS大小
PHYSBUFF 1024										# 物理日志缓存
LOGBUFF 1024										# 逻辑日志缓存
DBSPACETEMP tempdbs01								# 默认的临时数据库空间
SBSPACENAME sbspace01								# 默认的智能大对象空间
DBSERVERNAME gbase01 								# 实例名称
NETTYPE soctcp,1,100,NET							# 网络连接
MULTIPROCESSOR 1									# 启用多CPU
VPCLASS cpu,num=2,noage								# CPU VP数量
CLEANERS 32											# 页清理数量
LOCKS 2000000										# 初始锁的数量
DEF_TABLE_LOCKMODE row								# 默认锁的类型
SHMVIRTSIZE 512000									# 虚拟内存大小
LTAPEDEV /dev/null									# 逻辑日志备份目录
STACKSIZE 2048										# 堆栈大小
ALLOW_NEWLINE 1										# 允许字符型字段换行
DS_TOTAL_MEMORY 1024000								# 决策性操作使用的内存
DS_NONPDQ_QUERY_MEM 256000							# 非决策性操作使用的内存
TEMPTAB_NOLOG           1							# 指定临时表不使用日志
DUMPSHMEM 0											# 不DUMP内存
USERMAPPING ADMIN									# 使用内部用户
BUFFERPOOL size=16k,buffers=50000,lrus=8,lru_min_dirty=50,lru_max_dirty=60
```

#### 配置GBASEDBTSQLHSOTS配置文件sqlhosts  
编辑或者创建sqlhosts配置文件  
```text
# 实例名称 网络协议 IP地址 端口号
gbase01 onsoctcp 0.0.0.0 9088
```
注：这里的`0.0.0.0`表示本机上的任意IP均可侦听  

#### 配置内部用户使用的allowed.surrogates（位于/etc/gbasedbt目录下）  
创建/etc/gbasedbt目录，创建allowed.surrogates配置文件    
```text
[root@node2 ~]# more /etc/gbasedbt/allowed.surrogates
```
内容如下：  
```text
# 指定使用daemon用户为代理用户
USERS:daemon
```

#### 初始化数据库  
gbasedbt用户通过oninit -ivy初始化数据库实例。  
**警告：-i参数仅限第一次初始化数据库实例时使用，后期启动时应使用oninit。**  
```text
[gbasedbt@node2 ~]$ oninit -ivy								（初始化实例）
Reading configuration file '/opt/gbase/etc/onconfig.gbase01'...succeeded
Creating /GBASEDBTTMP/.infxdirs...succeeded
Allocating and attaching to shared memory...succeeded
Creating resident pool 279630 kbytes...succeeded
Creating infos file "/opt/gbase/etc/.infos.gbase01"...succeeded
Linking conf file "/opt/gbase/etc/.conf.gbase01"...succeeded
Initializing rhead structure...rhlock_t 262144 (8192K)... rlock_t (265625K)... Writing to infos file...succeeded
Initialization of Encryption...succeeded
Initializing ASF...succeeded
Initializing Dictionary Cache and SPL Routine Cache...succeeded
Bringing up ADM VP...succeeded
Creating VP classes...succeeded
Forking main_loop thread...succeeded
Initializing DR structures...succeeded
Forking 1 'soctcp' listener threads...succeeded
Starting tracing...succeeded
Initializing 32 flushers...succeeded
Initializing log/checkpoint information...succeeded
Initializing dbspaces...succeeded
Opening primary chunks...succeeded
Validating chunks...succeeded
Creating database partition...succeeded
Initialize Async Log Flusher...succeeded
Starting B-tree Scanner...succeeded
Init ReadAhead Daemon...succeeded
Init DB Util Daemon...succeeded
Initializing DBSPACETEMP list...succeeded
Init Auto Tuning Daemon...succeeded
Checking database partition index...succeeded
Initializing dataskip structure...succeeded
Checking for temporary tables to drop...succeeded
Updating Global Row Counter...succeeded
Forking onmode_mon thread...succeeded
Creating periodic thread...succeeded
Creating periodic thread...succeeded
Starting scheduling system...succeeded
Verbose output complete: mode = 5
```
检查数据库侦听，确认已经启动  
```text
[gbasedbt@node2 ~]$ onstat -g ntt

On-Line -- Up 00:06:47 -- 1716640 Kbytes

global network information:
  #netscb connects         read        write    q-free  q-limits  q-exceed alloc/max
   2/   3       11         4262         4261    2/   2  170/  10    0/   0    2/   2

Individual thread network information (times):
          netscb thread name    sid     open     read    write address                  
        586e1bb0 soctcplst        3 11:08:08 11:11:12          0.0.0.0|9088|soctcp      
        57100ab0 soctcppoll       2 11:08:09  

```
查询数据库运行日志online.log，4个sys开头的系统库均已经创建完成，表示实例初始化完成。  
```text
[gbasedbt@node2 ~]$ tail -n 1000 /opt/gbase/tmp/online.log | grep 'sys'
11:08:09  Building 'sysmaster' database ...
11:08:15  'sysmaster' database built successfully.
11:08:16  'sysutils' database built successfully.
11:08:16  'sysuser' database built successfully.
11:08:22  Building 'sysadmin' database ...
11:08:22  'sysadmin' database built successfully.
```

#### 增加数据库空间  
刚初始化的实例，仅有一个根数据库空间rootdbs。实际业务环境需要有独立的物理日志、逻辑日志、临时数据库空间、智能大对象空间和业务数据库空间。  
```text
[gbasedbt@node2 ~]$ onstat -d

On-Line -- Up 00:05:38 -- 1716640 Kbytes

Dbspaces
address    number   flags      fchunk   nchunks  pgsize   flags    owner    name
5657e028   1        0x40001    1        1        2048     N  BA    gbasedbt rootdbs
 1 active, 2047 maximum

Chunks
address    chunk/dbs  offset  size    free    bpages     flags pathname
5657e258   1      1   0       512000  446665             PO-B-- /data/gbase/rootchk
 1 active, 32766 maximum

NOTE: The values in the "size" and "free" columns for DBspace chunks are
      displayed in terms of "pgsize" of the DBspace to which they belong.


Expanded chunk capacity mode: always
```
通过onspaces创建相应的空间  
```text
# 物理日志使用的数据库空间
[gbasedbt@node2 ~]$ onspaces -c -d plogdbs -p /data/gbase/plogchk -o 0 -s 1024000
Verifying physical disk space, please wait ...
Space successfully added.

** WARNING **  A level 0 archive of Root DBSpace will need to be done.

# 逻辑日志使用的数据库空间
[gbasedbt@node2 ~]$ onspaces -c -d llogdbs -p /data/gbase/llogchk -o 0 -s 1024000
Verifying physical disk space, please wait ...
Space successfully added.

** WARNING **  A level 0 archive of Root DBSpace will need to be done.

# 临时数据库空间
[gbasedbt@node2 ~]$ onspaces -c -d tempdbs01 -t -k 16 -p /data/gbase/tempchk01 -o 0 -s 1024000
Verifying physical disk space, please wait ...
Space successfully added.

# 智能大对象空间
[gbasedbt@node2 ~]$ onspaces -c -S sbspace01 -p /data/gbase/sbspace01 -o 0 -s 1024000
Verifying physical disk space, please wait ...
Space successfully added.

** WARNING **  A level 0 archive of Root DBSpace will need to be done.

# 业务使用的数据库空间
[gbasedbt@node2 ~]$ onspaces -c -d datadbs01 -k 16 -p /data/gbase/datachk01 -o 0 -s 1024000
Verifying physical disk space, please wait ...
Space successfully added.

** WARNING **  A level 0 archive of Root DBSpace will need to be done.
```
完成创建空间后的输出  
```text
[gbasedbt@node2 ~]$ onstat -d

On-Line -- Up 00:24:19 -- 1716640 Kbytes

Dbspaces
address    number   flags      fchunk   nchunks  pgsize   flags    owner    name
5657e028   1        0x60001    1        1        2048     N  BA    gbasedbt rootdbs
5a737da8   2        0x60001    2        1        2048     N  BA    gbasedbt plogdbs
5a723d78   3        0x60001    3        1        2048     N  BA    gbasedbt llogdbs
5a744520   4        0x42001    4        1        16384    N TBA    gbasedbt tempdbs01
5a99ad78   5        0x68001    5        1        2048     N SBA    gbasedbt sbspace01
597eeaf8   6        0x60001    6        1        16384    N  BA    gbasedbt datadbs01
 6 active, 2047 maximum

Chunks
address    chunk/dbs     offset     size    free    bpages  flags pathname
5657e258   1      1      0          512000  446663          PO-B-- /data/gbase/rootchk
5a3cd028   2      2      0          512000  511947          PO-B-- /data/gbase/plogchk
5a732028   3      3      0          512000  511947          PO-B-- /data/gbase/llogchk
5a409028   4      4      0          64000   63947           PO-B-- /data/gbase/tempchk01
5a447028   5      5      0          512000  477465  477465  POSB-- /data/gbase/sbspace01
                           Metadata 34482   25659   34482   
5a824028   6      6      0          64000   63947           PO-B-- /data/gbase/datachk01
 6 active, 32766 maximum

NOTE: The values in the "size" and "free" columns for DBspace chunks are
      displayed in terms of "pgsize" of the DBspace to which they belong.


Expanded chunk capacity mode: always
```
将物理日志从根数据库空间移到物理日志专用的数据库空间  
```text
# 移动物理日志，并改变大小
[gbasedbt@node2 ~]$ onparams -p -s 1000000 -d plogdbs -y
Log operation started. To monitor progress, use the onstat -l command.
** WARNING ** Because the physical log has been modified, a level 0 archive 
must be taken of the following spaces before an incremental archive will be 
permitted for them: rootdbs plogdbs 
(see Database Server Administrator's manual)

# 查看物理日志位置及大小（phybegin,pyhsize）
[gbasedbt@node2 ~]$ onstat -l

On-Line -- Up 00:31:03 -- 1716640 Kbytes

Physical Logging
Buffer bufused  bufsize  numpages   numwrits   pages/io
  P-2  5        512      534        16         33.38
      phybegin         physize    phypos     phyused    %used   
      2:53             500000     0          5          0.00  
```
将逻辑日志文件从根数据库空间移到逻辑日志专用的数据库空间，默认初始化时有6个逻辑日志文件位于rootdbs上，逻辑日志只有已经备份或者新加未使用的情况下才能删除，同时整个实例中不能少于3个逻辑日志。按照这样的规则：在逻辑日志专用的数据库空间上创建新的逻辑日志文件，然后将当前的逻辑日志移动到逻辑日志专用的数据库空间上，删除在rootdbs上的逻辑日志文件，以达到移动逻辑日志的目的。  
```text
# 当前的逻辑日志位于rootdbs上
[gbasedbt@node2 ~]$ onstat -l

On-Line -- Up 00:31:03 -- 1716640 Kbytes

Physical Logging
Buffer bufused  bufsize  numpages   numwrits   pages/io
  P-2  5        512      534        16         33.38
      phybegin         physize    phypos     phyused    %used   
      2:53             500000     0          5          0.00    

Logical Logging
Buffer bufused  bufsize  numrecs    numpages   numwrits   recs/pages pages/io
  L-1  0        512      166624     14241      3765       11.7       3.8     
	Subsystem    numrecs    Log Space used
	OLDRSAM      166297     23906880      
	SBLOB        5          252           
	HA           15         660           
	DDL          307        106836        

address          number   flags    uniqid   begin                size     used    %used
566f0f88         1        U-B----  1        1:25263              5000     5000   100.00
5917a570         2        U-B----  2        1:30263              5000     5000   100.00
5917a5d8         3        U---C-L  3        1:35263              5000     4241    84.82
5917a640         4        A------  0        1:40263              5000        0     0.00
5917a6a8         5        A------  0        1:45263              5000        0     0.00
5917a710         6        A------  0        1:50263              5000        0     0.00
 6 active, 6 total

# 在llogdbs上增加10个逻辑日志，每个大小是100MB
[gbasedbt@node2 ~]$ for i in {1..10}
> do
>   onparams -a -d llogdbs -s 100000
> done
Log operation started. To monitor progress, use the onstat -l command.
Logical log successfully added.
Log operation started. To monitor progress, use the onstat -l command.
Logical log successfully added.
Log operation started. To monitor progress, use the onstat -l command.
Logical log successfully added.
Log operation started. To monitor progress, use the onstat -l command.
Logical log successfully added.
Log operation started. To monitor progress, use the onstat -l command.
Logical log successfully added.
Log operation started. To monitor progress, use the onstat -l command.
Logical log successfully added.
Log operation started. To monitor progress, use the onstat -l command.
Logical log successfully added.
Log operation started. To monitor progress, use the onstat -l command.
Logical log successfully added.
Log operation started. To monitor progress, use the onstat -l command.
Logical log successfully added.
Log operation started. To monitor progress, use the onstat -l command.
Logical log successfully added.

# 显示新增加的逻辑日志，位于logdbs上
[gbasedbt@node2 ~]$ onstat -l

On-Line -- Up 00:36:32 -- 1716640 Kbytes

Physical Logging
Buffer bufused  bufsize  numpages   numwrits   pages/io
  P-2  0        512      579        27         21.44
      phybegin         physize    phypos     phyused    %used   
      2:53             500000     45         0          0.00    

Logical Logging
Buffer bufused  bufsize  numrecs    numpages   numwrits   recs/pages pages/io
  L-3  0        512      166697     14273      3797       11.7       3.8     
	Subsystem    numrecs    Log Space used
	OLDRSAM      166359     23911564      
	SBLOB        5          252           
	HA           26         1144          
	DDL          307        106836        

address          number   flags    uniqid   begin                size     used    %used
566f0f88         1        U-B----  1        1:25263              5000     5000   100.00
5917a570         2        U-B----  2        1:30263              5000     5000   100.00
5917a5d8         3        U---C-L  3        1:35263              5000     4273    85.46
5917a640         4        A------  0        1:40263              5000        0     0.00
5917a6a8         5        A------  0        1:45263              5000        0     0.00
5917a710         6        A------  0        1:50263              5000        0     0.00
58cf95b0         7        A------  0        3:53                50000        0     0.00
58cf9680         8        A------  0        3:50053             50000        0     0.00
58cf9618         9        A------  0        3:100053            50000        0     0.00
58cf96e8         10       A------  0        3:150053            50000        0     0.00
58cf9758         11       A------  0        3:200053            50000        0     0.00
58cf97d0         12       A------  0        3:250053            50000        0     0.00
58cf9850         13       A------  0        3:300053            50000        0     0.00
58cf98d8         14       A------  0        3:350053            50000        0     0.00
58cf9968         15       A------  0        3:400053            50000        0     0.00
58cf9a00         16       A------  0        3:450053            50000        0     0.00
 16 active, 16 total

# 切换当前逻辑日志到uniqid 7上逻辑日志文件上
[gbasedbt@node2 ~]$ onmode -l && onmode -l && onmode -l && onmode -l && onmode -c

# 查看当前逻辑是否位于uniqid 7上
[gbasedbt@node2 ~]$ onstat -l

On-Line -- Up 00:42:56 -- 1716640 Kbytes

Physical Logging
Buffer bufused  bufsize  numpages   numwrits   pages/io
  P-2  0        512      579        27         21.44
      phybegin         physize    phypos     phyused    %used   
      2:53             500000     66         9          0.00    

Logical Logging
Buffer bufused  bufsize  numrecs    numpages   numwrits   recs/pages pages/io
  L-3  0        512      166762     14285      3809       11.7       3.8     
	Subsystem    numrecs    Log Space used
	OLDRSAM      166423     23918348      
	SBLOB        5          252           
	HA           27         1188          
	DDL          307        106836        

address          number   flags    uniqid   begin                size     used    %used
566f0f88         1        U-B----  1        1:25263              5000     5000   100.00
5917a570         2        U-B----  2        1:30263              5000     5000   100.00
5917a5d8         3        U-B----  3        1:35263              5000     4274    85.48
5917a640         4        U-B----  4        1:40263              5000        1     0.02
5917a6a8         5        U-B----  5        1:45263              5000        7     0.14
5917a710         6        U-B----  6        1:50263              5000        1     0.02
58cf95b0         7        U---C-L  7        3:53                50000        8     0.02
58cf9680         8        A------  0        3:50053             50000        0     0.00
58cf9618         9        A------  0        3:100053            50000        0     0.00
58cf96e8         10       A------  0        3:150053            50000        0     0.00
58cf9758         11       A------  0        3:200053            50000        0     0.00
58cf97d0         12       A------  0        3:250053            50000        0     0.00
58cf9850         13       A------  0        3:300053            50000        0     0.00
58cf98d8         14       A------  0        3:350053            50000        0     0.00
58cf9968         15       A------  0        3:400053            50000        0     0.00
58cf9a00         16       A------  0        3:450053            50000        0     0.00
 16 active, 16 total

# 删除uniqid 1至6的逻辑日志文件
[gbasedbt@node2 ~]$ for i in {1..6}
> do
>   onparams -d -l $i -y
> done
Logical log 1 successfully dropped.
Logical log 2 successfully dropped.
Logical log 3 successfully dropped.
Logical log 4 successfully dropped.
Logical log 5 successfully dropped.
Logical log 6 successfully dropped.

# 移动逻辑日志文件完成后
[gbasedbt@node2 ~]$ onstat -l

On-Line -- Up 00:46:48 -- 1716640 Kbytes

Physical Logging
Buffer bufused  bufsize  numpages   numwrits   pages/io
  P-2  0        512      625        35         17.86
      phybegin         physize    phypos     phyused    %used   
      2:53             500000     91         0          0.00    

Logical Logging
Buffer bufused  bufsize  numrecs    numpages   numwrits   recs/pages pages/io
  L-3  0        512      166826     14309      3833       11.7       3.7     
	Subsystem    numrecs    Log Space used
	OLDRSAM      166481     23923400      
	SBLOB        5          252           
	HA           33         1452          
	DDL          307        106836        

address          number   flags    uniqid   begin                size     used    %used
58cf95b0         7        U---C-L  7        3:53                50000       26     0.05
58cf9680         8        A------  0        3:50053             50000        0     0.00
58cf9618         9        A------  0        3:100053            50000        0     0.00
58cf96e8         10       A------  0        3:150053            50000        0     0.00
58cf9758         11       A------  0        3:200053            50000        0     0.00
58cf97d0         12       A------  0        3:250053            50000        0     0.00
58cf9850         13       A------  0        3:300053            50000        0     0.00
58cf98d8         14       A------  0        3:350053            50000        0     0.00
58cf9968         15       A------  0        3:400053            50000        0     0.00
58cf9a00         16       A------  0        3:450053            50000        0     0.00
 10 active, 10 total
```

### 创建数据库内部用户  
创建数据库内部用户，需要创建内部用户使用的映射目录，可创建一个默认用户（default user），使其包含默认的配置信息。  
创建映射目录  
```text
[gbasedbt@node2 ~]$ mkdir -p $HOME/users

[gbasedbt@node2 ~]$ chmod 777 $HOME/users
```
创建默认用户，创建一个数据库用户dbtuser，并设置密码  
```text
[gbasedbt@node2 ~]$ dbaccess sysuser -
> CREATE DEFAULT USER WITH PROPERTIES USER daemon HOME '/home/gbase/users';
> CREATE USER dbtuser WITH PASSWORD 'GBase123$%';
```
注：使用`Ctrl + c`或者`Ctrl + \ `退出dbaccess 交互模式
测试内部用户登陆，交互工输入密码  
```text
[gbasedbt@node2 ~]$ dbaccess - -
> CONNECT TO 'testdb@gbase01' USER 'dbtuser';
```

## 数据库参数优化  
### 配置参数优化  
数据库性能优化需要根据业务使用情况进行调整，通过尽可能少的磁盘访问获得所需要的数据。  
数据库配置文件ONCONFIG包含了常用、默认的参数，根据实际硬件资源及业务实际访问情况，优化与调整部分参数。以下是常用的需要调整的参数。  

|参数名称|修改后的参数值|参数说明|
|:---|:---|:---|
|PHYSBUFF|2048|物理日志缓冲区大小，建议|
|LOGBUFF|2048|逻辑日志缓冲区大小，建议|
|DBSPACETEMP|tempdbs01|临时数据库空间名称，可多个|
|SBSPACENAME|sbspace01|智能大对象默认空间，仅一个|
|SYSSBSPACENAME|sbspace01|智能大对象空间系统管理空间|
|NETTYPE|soctcp,2,200,NET|网络连接池配置，建议配置为不超过1/4的CPUVP的数量。|
|NUMFDSERVERS|4|网络线程池连接交换服务数量|
|MULTIPROCESSOR|1|开启使用多CPU|
|VPCLASS|cpu,num=80,aff=(40-79,120-159),noage|指定CPU VP的数量，建议CPU数-1<br>若是NUMA架构，建议使用2个NODE；如果各NODE节点间的内存延时相近，可适当增加。|
|AUTO_TUNE|0|关闭系统部分参数的自动调整|
|AUTO_REPREPARE|1|自动重新预处理|
|CLEANERS|128|页清理线程的数量|
|LOCKS |100000000|指定初始锁的数量<br>根据硬件和业务需求调整。如16G内存500万，32G内存时可1000万。|
|DEF_TABLE_LOCKMODE|row|指定默认的表锁模式|
|SHMVIRTSIZE|40960000|指定虚拟内存段大小，单位是KB<br>根据硬件调整|
|SHMADD|10240000|指定虚拟内存段扩展大小<br>根据硬件调整|
|SHMTOTAL|0|指定数据库使用的最大内存量，可指定至操作系统内存的80-90%|
|STACKSIZE|2048|指定堆栈大小|
|ALLOW_NEWLINE|1|允许字符类字段内换行|
|USELASTCOMMITTED|NONE|指定使用最后提交读|
|DS_MAX_QUERIES|5|同时支持的决策并行查询数量|
|DS_TOTAL_MEMORY|40960000|决策并行查询使用的内存大小<br>根据硬件和业务需求调整|
|DS_NONPDQ_QUERY_MEM|10240000|非决策并行查询使用的内存大小，最大为DS_TOTAL_MEMORY的1/4|
|TEMPTAB_NOLOG|1|指定临时表使用无日志方式|
|MAX_FILL_DATA_PAGES|1|数据页填充，1为尽可能填充。<br>初始化环境及更新较少的环境，可设置为1。|
|OPT_GOAL|0|优化器快速返回。<br>0表示找到合适的行即返回。|
|DUMPSHMEM|0|指定断言失败时，不DUMP内存|
|BUFFERPOOL|size=2k,buffers=1000000,lrus=128,lru_min_dirty=50,lru_max_dirty=60|指定2K页面使用的缓冲池<br>根据硬件和业务需求调整|
|BUFFERPOOL|size=16k,buffers=5000000,lrus=128,lru_min_dirty=50,lru_max_dirty=60|指定16K页面使用的缓冲池<br>根据硬件和业务需求调整|

### 数据库空间自动扩展（chunk自动扩展）  
使用文件系统时，如果有空间自动扩展需求，需开启chunk自动扩展功能。  
使用gbasedbt用户登陆，在sysadmin库中执行管理函数task或者admin，设置相应的chunk为自动扩展，及最扩展最大大小。  
```text
[gbasedbt@node2 ~]$ dbaccess sysadmin –
> execute function task('modify chunk extendable on',6);

> EXECUTE FUNCTION task ('modify space sp_sizes' ,'datadbs01', '10', '100000', '204800000');
```
其中：  
第一个语句中的第二个参数数字6为对应的chunk编号。  
第二个语句中的第二个参数表示空间名称，第三个参数为创建大小（0-100之前表示百分比、大于1000表示KB），第四个参数为最小扩展大小，第五个参数为最大扩展到的大小（即最大限制）  
