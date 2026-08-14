# Python使用gbase8sdb方式连接到数据库（Linux）  
本章节将介绍Python程序通过gbase8sdb连接到GBase 8s数据库的方式。  

## 示例环境介绍  
* 操作系统：Debian GNU/Linux 12 (bookworm) (x86_64)    
* 数据库版本：GBase 8s v8.8_3.6.5_2L1_1  
* Python3版本：Python 3.11.2 （系统自带）  
* gbase8sdb版本：1.0.0 (https://pypi.org/project/gbase8sdb)  
注：gbase8sdb v1.0.0版本之后不再需要GSDK的支持  

## 确认安装python3及版本  
确认已经安装python3和pip3  
```text
root@netsky:~# python3 --version
Python 3.11.2

root@netsky:~# pip3 --version
pip 23.0.1 from /usr/lib/python3/dist-packages/pip (python 3.11)
```
如果没有安装，建议使用apt -y install python3来安装。

## 安装gbase8sdb  
gbase8sdb：支持的 Python 版本：3.8 至 3.13，支持的 GBase 8s 数据库版本：GBase 8s V8.8_3.6.2版本及以上。  
源码安装：  
```text
root@netsky:~# pip3 install gbase8sdb-1.0.0.tar.gz
```
确认已经安装
```text
root@netsky:~# pip3 list | grep gbase8sdb
gbase8sdb              1.0.0
```

## 编写测试代码并执行测试  
测试代码`Python3Sample.py`  
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gbase8sdb

# 生成dsn
dsn = gbase8sdb.makedsn(
    server_name="gbase01",          # 数据库实例名称
    db_name="testdb",               # 数据库名称
    host="192.168.0.212",           # 数据库实例所在服务器的IP地址或域名
    port=36521,                     # 数据库实例的端口号
    db_locale='zh_CN.utf8'          # 数据库字符集
)
user = "gbasedbt"                   # 数据库用户名
password = "GBase123$%"             # 数据库用户密码

# 创建数据库连接
conn = gbase8sdb.connect(dsn, user, password)

print("Connection succeed!");

# 创建游标对象
cursor = conn.cursor()

sqlstr = "drop table if exists company";
cursor.execute(sqlstr);
print("成功删除表 company !");

sqlstr = "create table company(coid serial,coname varchar(255),coaddr varchar(255), primary key(coid))";
cursor.execute(sqlstr);
print("成功创建表 company !");

sqlstr = "insert into company values(0,?,?),(0,?,?)";
cursor.execute(sqlstr,("GBase","TJ","GBase BeiJing","BJ"))
conn.commit()
print("成功插入数据到表 company !");

sqlstr = "select * from company";
cursor.execute(sqlstr);
print(cursor.fetchall())
print("成功查询表 company !");

cursor.close()
conn.close()
```
执行测试  
```text
root@netsky:~# python3 Python3Sample.py
Connection succeed!
成功删除表 company !
成功创建表 company !
成功插入数据到表 company !
[(1, 'GBase', 'TJ'), (2, 'GBase BeiJing', 'BJ')]
成功查询表 company !
```

最后更新日期：2026-08-14  
