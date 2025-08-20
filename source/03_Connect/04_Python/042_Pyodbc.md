# Python使用pyodbc方式连接到数据库（Linux）  
本章节将介绍Python程序通过pyodbc连接到GBase 8s数据库的方式。  
pyodbc依赖CSDK版本。  

## 示例环境介绍  
* 操作系统：Ubuntu 22.04.3 LTS （x86_64）  
* 数据库版本：GBase 8s v8.8_3.6.3_3x2_1  
* Python3版本：Python 3.10.12 （系统自带）  
* pyodbc版本：5.2.0 (https://pypi.org/project/pyodbc)  

## 安装GBase ClientSDK  
安装目录为/opt/gbase  
参考：[CSDK安装](../../02_Install/02_CSDK_Lnx.html "CSDK安装")  

在/etc/ld.so.conf.d目录下增加GBase 8s的库目录配置文件gbase8scsdk-x86_64.conf  
```text
[root@localhost ld.so.conf.d]# pwd
/etc/ld.so.conf.d
[root@localhost ld.so.conf.d]# more gbase8scsdk-x86_64.conf
/opt/gbase/lib
/opt/gbase/lib/cli
/opt/gbase/lib/esql
```

配置环境变量  
```shell
export GBASEDBTDIR=/opt/gbase
export PATH=$GBASEDBTDIR/bin:$PATH
export LD_LIBRARY_PATH=$GBASEDBTDIR/lib:$GBASEDBTDIR/lib/cli:$GBASEDBTDIR/lib/esql:$LD_LIBRARY_PATH
export ODBCINI=/opt/gbase/etc/odbc.ini
```

配置ODBCINI  
```text
;---------------------------------------------------------------------------
; GBase ODBC Sample File
;
; File:         odbc.ini
;
;---------------------------------------------------------------------------
[ODBC Data Sources]
testdb=GBase ODBC DRIVER
;
; Define ODBC Database Driver's Below - Driver Configuration Section
;
[testdb]
Driver=/opt/gbase/lib/cli/iclis09b.so
Description=GBase ODBC DRIVER
Database=testdb
LogonID=gbasedbt
pwd=GBase123$%
Servername=gbase01
CursorBehavior=0
CLIENT_LOCALE=zh_CN.utf8
DB_LOCALE=zh_CN.utf8
TRANSLATIONDLL=/opt/gbase/lib/esql/igo4a304.so
;
; UNICODE connection Section
;
[ODBC]
;uncomment the below line for UNICODE connection
UNICODE=UCS-2
;
; Trace file Section
;
Trace=0
TraceFile=/tmp/odbctrace.out
InstallDir=/opt/gbase
TRACEDLL=idmrs09a.so
```

## 确认安装python3及版本  
确认已经安装python3和pip3  
```text
root@netsky:~# python3 --version
Python 3.10.12

root@netsky:~# pip3 --version
pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)
```
如果没有安装，建议使用apt -y install python3来安装。  

## 安装pyodbc  
pyodbc is an open source Python module that makes accessing ODBC databases simple. It implements the DB API 2.0 specification but is packed with even more Pythonic convenience.  
```text
root@netsky:~# pip3 install pyodbc
```
确认已经安装
```text
root@netsky:~# pip3 list | grep pyodbc
pyodbc              5.2.0
```

## 编写测试代码并执行测试  
测试代码`Python3PyodbcSample.py`  
```python
import sys
import pyodbc

# 使用DSN需要PWD关键字
conn = pyodbc.connect("DSN=testdb;PWD=GBase123$%")
# conn = pyodbc.connect("DRIVER=/opt/gbase/lib/cli/iclis09b.so;HOST=192.168.0.212;SERVER=gbase01;SERVICE=13633;PROTOCOL=onsoctcp;DATABASE=testdb;DB_LOCALE=zh_CN.utf8;CLIENT_LOCALE=zh_CN.utf8;UID=gbasedbt;PWD=GBase123$%");
# set connection encoding
conn.setencoding(encoding='UTF-8')

mycursor = conn.cursor()
mycursor.execute("drop table if exists company")
print("drop table company succeed!")

mycursor.execute("create table company(coid serial,coname varchar(255),coaddr varchar(255), primary key(coid))")
print("create table company succeed!")

mycursor.execute("insert into company values(0,?,?),(0,?,?)","GBase","TJ","GBase BeiJing","BJ")
conn.commit()
print("insert table company succeed!")

cursor1 = conn.cursor()
cursor1.execute("select * from company")
print(cursor1.fetchall())
print("select table company succeed!")

conn.close()
sys.exit(0)
```
执行测试  
```text
root@netsky:~# python3 Python3OdbcSample.py
drop table company succeed!
create table company succeed!
insert table company succeed!
[(1, 'GBase', 'TJ'), (2, 'GBase BeiJing', 'BJ')]
select table company succeed!
```

最后更新日期：2025-08-20  
