# CSDK安装与配置（Linux）  
本章节将介绍GBase 8s客户端安装部署及相关客户端、ODBC配置。  

## CSDK的安装  
CSDK可使用任意用户进行安装。  
将软件包clientsdk_3.6.3_3X2_1_783c8d_RHEL6_x86_64.tar上传至install目录中，请确认软件包是以.tar为后缀。  

### 解压缩CSDK软件包  
```text
[root@localhost ~]# mkdir csdk
[root@localhost ~]# cd csdk/
[root@localhost csdk]# tar -xvf ../clientsdk_3.6.3_3X2_1_783c8d_RHEL6_x86_64.tar
installclientsdk
doc/
doc/Glsapi_machine_notes_4.10.txt
doc/ESQLC_machine_notes_4.10.txt
doc/Odbc_machine_notes_4.10.txt
doc/Libcpp_machine_notes_4.10.txt
csdk.properties
.gbase.properties
```

### 执行静默安装，自动完成安装  
```text
[root@localhost csdk]#  ./installclientsdk -i silent \
  -DUSER_INSTALL_DIR=/opt/gbase -DLICENSE_ACCEPTED=TRUE
```
Linux下CSDK安装涉及的参数说明  

|序号|参数名称|示例参数值|说明信息|
|:---|:---|:---|:---|
|1|-i|silent|指定使用静默安装|
|2|-DUSER_INSTALL_DIR=|/opt/gbase|指定安装目录|
|3|-DLICENSE_ACCEPTED=|TRUE|指定接受协议|

## CSDK的配置  
CSDK安装完成后，需要对客户端连接进行设置。以下使用gbasedbt用户来说明。  

### 在用户的目录下的用户环境配置文件.bash_profile中增加数据库的环境。  
根据数据库的实现情况设置：  
```text
# .bash_profile
export GBASEDBTDIR=/opt/gbase
export GBASEDBTSERVER=gbase01
export PATH=${GBASEDBTDIR}/bin:${PATH}
export LD_LIBRARY_PATH=$GBASEDBTDIR/lib:$GBASEDBTDIR/lib/cli:$GBASEDBTDIR/lib/esql:$LD_LIBRARY_PATH

export DB_LOCALE=zh_CN.utf8
export CLIENT_LOCALE=zh_CN.utf8
export GL_USEGLU=1
export DBDATE="Y4MD-"
```

### 修改GBASEDBTSQLHOSTS配置文件  
在`$GBASEDBTDIR/etc/`目录下创建sqlhosts（默认的GBASEDBTSQLHOSTS）配置文件，内容为连接到数据库服务器的信息。  
```text
# GBASEDBTSQLHOSTS
gbase01 onsoctcp 192.168.0.212 13633
```

### 测试数据库连接  
```text
[gbasedbt@localhost ~]$ dbaccess - -
> connect to "testdb@gbase01" user "gbasedbt";
   输入密码：<输入用户密码>

已连接。

Elapsed time: 4.978 sec

> select dbservername from dual;

(expression)  gbase01

查询到 1 行。

Elapsed time: 0.312 sec
```

## ODBC的配置  
安装了64位的CSDK，则需要配置64位的数据源。Linux下的ODBC需要unixODBC。如果需要对所有用户生效，需要在系统级配置。  

### 确认unixODBC已经安装  
```text
[root@localhost ~]# rpm -qa | grep -i unixODBC
unixODBC-devel-2.3.1-14.el7.x86_64
unixODBC-2.3.1-14.el7.x86_64
```

### 在/etc/profile配置文件里增加CSDK的配置环境  
```text
# /etc/profile
# Add for GBase 8s ODBC
export GBASEDBTDIR=/opt/gbase
export PATH=${GBASEDBTDIR}/bin:${PATH}
export LD_LIBRARY_PATH=$GBASEDBTDIR/lib:$GBASEDBTDIR/lib/cli:$GBASEDBTDIR/lib/esql:$LD_LIBRARY_PATH

export DB_LOCALE=zh_CN.utf8
export CLIENT_LOCALE=zh_CN.utf8
export GL_USEGLU=1

export ODBCINI=/etc/odbc.ini
```

### 配置/etc/odbcinst.ini配置文件(可选)，根据CSDK环境，配置如下：  
```text
; /etc/odbcinst.ini
; ODBC Driver for GBase 8s
[GBase ODBC DRIVER] 
Driver=/opt/gbase/lib/cli/iclit09b.so 
Setup=/opt/gbase/lib/cli/iclit09b.so
APILevel=1
ConnectFunctions=YYY
DriverODBCVer=03.51
FileUsage=0
SQLLevel=1
smProcessPerConnect=Y
```

### 配置ODBCINI配置文件，根据CSDK环境，配置如下：  
```text
[ODBC Data Sources]
testdb=GBase ODBC DRIVER
;
; Define ODBC Database Driver's Below - Driver Configuration Section
;
[testdb]
;Driver=/opt/gbase/lib/cli/iclit09b.so  # 不配置odbcinst.ini时，打开这里
Driver=GBase ODBC DRIVER
Description=GBase ODBC DRIVER
Database=testdb
LogonID=gbasedbt
pwd=GBase123$%
Servername=gbase01
CursorBehavior=0
CLIENT_LOCALE=zh_CN.utf8
DB_LOCALE=zh_CN.utf8
GL_USEGLU=1
TRANSLATIONDLL=/opt/gbase/lib/esql/igo4a304.so
; ISOLATIONLEVEL=1	# 使用该参数（简写：ISOLVL）设置默认的隔离级别，0-5
;
; UNICODE connection Section
;
[ODBC]
;uncomment the below line for UNICODE connection
UNICODE=UCS-2		# 如果需要使用unicode连接数据库，这里需要去除注释，值改为UCS-2
;
; Trace file Section
;
Trace=0
TraceFile=/tmp/odbctrace.out
InstallDir=/opt/gbase
TRACEDLL=idmrs09a.so
```

### ODBC连接测试  
确认当前用户环境变量中包括 中配置的环境变量和ODBCINI已经完成。通过isql测试ODBC配置正确。  
特别说明：有的开发语言使用unicode方式访问数据库，这时需要使用iusql确认ODBC可以连接。CentOS 7默认带的unixODBC版本为2.3.1，需要升级到更高的版本。  
```text
[root@localhost ~]# env | egrep '(GBASEDBT|ODBCINI)'
GBASEDBTSERVER=gbase01
ODBCINI=/etc/odbc.ini
GBASEDBTDIR=/opt/gbase
```
**测试连接isql**  
```text
[root@localhost ~]# isql -v testdb
+---------------------------------------+
| Connected!                            |
|                                       |
| sql-statement                         |
| help [tablename]                      |
| quit                                  |
|                                       |
+---------------------------------------+
SQL> select dbservername from dual;
+---------------------------------------+
|                                       |
+---------------------------------------+
| gbase01                               |
+---------------------------------------+
SQLRowCount returns -1
1 rows fetched
>
```
**测试连接iusql**  
```text
[root@localhost ~]# iusql -v testdb
+---------------------------------------+
| Connected!                            |
|                                       |
| sql-statement                         |
| help [tablename]                      |
| quit                                  |
|                                       |
+---------------------------------------+
SQL> select dbservername from dual;
+---------------------------------------+
|                                       |
+---------------------------------------+
| gbase01                               |
+---------------------------------------+
SQLRowCount returns -1
1 rows fetched
```
