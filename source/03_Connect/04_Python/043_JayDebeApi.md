# Python使用jaydebeapi方式连接到数据库（Linux）  
本章节将介绍Python程序通过jaydebeapi连接到GBase 8s数据库的方式。  
jaydebeapi依赖jdbc驱动，因此需要jre运行环境。   

## 示例环境介绍  
* 操作系统：Ubuntu 22.04.3 LTS （x86_64）  
* 数据库版本：GBase 8s v8.8_3.6.3_3x2_1  
* JDBC驱动版本：
* Python3版本：Python 3.10.12 （系统自带）  
* JayDeBeApi版本：1.2.3 (https://pypi.org/project/JayDeBeApi)  
* JDK版本：1.8.0_462 （系统自带）  

## 确认安装python3及版本  
确认已经安装python3和pip3  
```text
root@netsky:~# python3 --version
Python 3.10.12

root@netsky:~# pip3 --version
pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)
```
如果没有安装，建议使用apt -y install python3来安装。  

## 确认安装JDK及版本  
确认已经安装JDK  
```text
root@netsky:~# java -version
openjdk version "1.8.0_462"
OpenJDK Runtime Environment (build 1.8.0_462-8u462-ga~us1-0ubuntu2~22.04.2-b08)
OpenJDK 64-Bit Server VM (build 25.462-b08, mixed mode)
```
如果没有安装，建议使用apt -y install openjdk-8-jdk来安装。  

## 安装JayDeBeApi及依赖模块  
The JayDeBeApi module allows you to connect from Python code to databases using Java JDBC. It provides a Python DB-API v2.0 to that database.  
```text
root@netsky:~# pip3 install JayDeBeApi

root@netsky:~# pip3 install jpype1==1.5.2
```
确认已经安装
```text
root@netsky:~# pip3 list | egrep '(JayDeBeApi|jpype1)'
JayDeBeApi             1.2.3
jpype1                 1.5.2
```

## 复制jdbc驱动  
复制JDBC驱动包 `gbasedbtjdbc_3.6.3_3X2_1_377ee9.jar`  到目录  

## 编写测试代码并执行测试  
测试代码`Python3JayDebeApiSample.py`  
```python
import sys
import jaydebeapi

print("\nPython JayDeBeApi JDBC 测试程序开始运行.\n")
conn = jaydebeapi.connect("com.gbasedbt.jdbc.Driver",
                           "jdbc:gbasedbt-sqli://192.168.0.212:13633/testdb:GBASEDBTSERVER=gbase01;DB_LOCALE=zh_CN.utf8;CLIENT_LOCALE=zh_CN.utf8;IFX_LOCK_MODE_WAIT=60",
                           ["gbasedbt", "GBase123$%"],
                           "/root/gbasedbtjdbc_3.6.3_3X2_1_377ee9.jar")

mycursor = conn.cursor()
mycursor.execute("drop table if exists company")
print("drop table company succeed!")

mycursor.execute("create table company(coid serial,coname varchar(255),coaddr varchar(255))")
print("create table company succeed!")

mycursor.execute("insert into company values(0,?,?),(0,?,?)",("GBase","TJ","GBase BeiJing","BJ"))
print("insert table company succeed!")

mycursor.execute("select * from company")
print(mycursor.fetchall())
print("select table company succeed!")

mycursor.close()
conn.close()

print("\nPython JayDeBeApi JDBC 测试程序结束运行.\n")
sys.exit(0)
```
执行测试  
```text
root@netsky:~# python3 Python3JayDebeApiSample.py

Python JayDeBeApi JDBC 测试程序开始运行.

drop table company succeed!
create table company succeed!
insert table company succeed!
[(1, 'GBase', 'TJ'), (2, 'GBase BeiJing', 'BJ')]
select table company succeed!

Python JayDeBeApi JDBC 测试程序结束运行.

```

最后更新日期：2025-08-20  
