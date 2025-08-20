# Python应用示例（Linux）  
本章将介绍GBase 8s的python3的基础的操作演示。  

## 示例环境介绍  
操作系统：Ubuntu 22.04.3 LTS （x86_64）  
数据库版本：GBase 8s v8.8_3.6.3_3x2_1  
Python3版本：Python 3.10.12 （系统自带）  
gbase8sdb版本：0.2.2 (https://pypi.org/project/gbase8sdb)  

## GSDK下载及安装 
GSDK驱动包的名称一般为：GSDK_3.6.3_3X2_1_1.1.0_1_eff9f1_RHEL6_x86_64.tar  
示例使用的GDSK下载地址：[https://dl.gbase8s.com:9088/GSDK/](https://dl.gbase8s.com:9088/GSDK/)  

GSDK需要使用1.1.x版本，该版本暂时需要通过GBase 8s技术支持或通过官方渠道获取。  
如下，本次使用的版本为：
GSDK_3.6.3_3X2_1_1.1.0_1_eff9f1_RHEL6_x86_64.tar  
说明：  
* 3.6.3_3X2_1：对应的数据库版本号  
* 1.1.0_1：GSDK版号本  
* eff9f1：内部GIT  
* RHEL6：编译的操作系统版本  
* x86_64：适用的架构  

上传到服务器，解压并改名  
```shell
tar -xvf GSDK_3.6.3_3X2_1_1.1.0_1_eff9f1_RHEL6_x86_64.tar -C /opt
mv /opt/GSDK_3.6.3_3X2_1_1.1.0_1_eff9f1_RHEL6_x86_64 /opt/GSDK
```

设置环境变量，并加载  
```shell
root@netsky:~# more env_gsdk
export GSDK_PATH=/opt/GSDK
export LD_LIBRARY_PATH=${GSDK_PATH}/lib:$LD_LIBRARY_PATH
export GBASEDBTDIR=${GSDK_PATH}/lib

root@netsky:~# . env_gask
```

## 确认安装python3及版本  
确认已经安装python3和pip3  
```shell
root@netsky:~# python3 --version
Python 3.10.12
root@netsky:~# pip3 --version
pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)
```
如果没有安装，建议使用apt -y install python3来安装。  

## 安装gbase8sdb  
gbase8sdb：支持的 Python 版本：3.8 至 3.13，支持的 GBase 8s 数据库版本：GBase 8s V8.8_3.6.2版本及以上，依赖 GSDK 1.1 版本。
```shell
root@netsky:~# pip3 install gbase8sdb
```
确认均已经安装  
```shell
root@netsky:~# pip3 list | grep 'gbase8sdb'
gbase8sdb              0.2.2
```

## 编写测试代码并执行测试  
测试代码`Python3Sample.py`  
```python
import gbase8sdb

# 生成dsn 
dsn = gbase8sdb.makedsn(
    server_name="gbase01",          # 数据库实例名称    
    db_name="testdb",               # 数据库名称    
    host="192.168.0.212",           # 数据库实例所在服务器的IP地址或域名    
    port=13633,                     # 数据库实例的端口号    
    db_locale='zh_CN.utf8'          # 数据库字符集
)
user = "gbasedbt"                   # 数据库用户名
password = "GBase123$%"                 # 数据库用户密码​

# 创建数据库连接
conn = gbase8sdb.connect(dsn, user, password) 

print("Connection succeed!");

# 创建游标对象
cursor = conn.cursor()

sqlstr = "drop table if exists company";
cursor.execute(sqlstr);
print("drop table company succeed!");

sqlstr = "create table company(coid serial,coname varchar(255),coaddr varchar(255), primary key(coid))";
cursor.execute(sqlstr);
print("create table company succeed!");

sqlstr = "insert into company values(0,?,?),(0,?,?)";
cursor.execute(sqlstr,("GBase","TJ","GBase BeiJing","BJ"))
# 事务操作需要手动提交  
conn.commit()
print("insert table company succeed!");

sqlstr = "select * from company";
cursor.execute(sqlstr);
print(cursor.fetchall())
print("select table company succeed!");

# 关闭游标和连接  
cursor.close()
conn.close()
```
执行测试
```shell
root@netsky:~# python3 Python3Sample.py
Connection succeed!
drop table company succeed!
create table company succeed!
insert table company succeed!
[(1, 'GBase', 'TJ'), (2, 'GBase BeiJing', 'BJ')]
select table company succeed!
```
