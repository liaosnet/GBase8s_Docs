# 产品安装  
本章节将介绍Linux环境下单机方式的GBase 8s数据库服务端安装部署方式，请确保已根据安装前准备章节进行有关配置，本文以GBase8sV8.8_TL_3.6.3_3X1_1_x86.tar软件包为例进行阐述 。  
如需安装其他部署方式的GBase 8s数据库，请参考安装部署章节。  

## 创建安装目录  
使用root用户创建安装目录  
执行如下命令创建目录install：  
```text
[root@node2 ~]# mkdir install
```

## 上传软件包  
将软件包GBase8sV8.8_TL_3.6.3_3X1_1_x86.tar和一键安装脚本AutoInit_GBase8s_v1.4.13.tar上传至install目录中，请确认软件包是以.tar为后缀，如果是.7z后缀，需要使用7zip工具先解压。  
解压一键安装脚本AutoInit_GBase8s_v1.4.13.tar，并查看解压后目录中所有文件，请将解压命令后的脚本包名称更改为实际使用的脚本包名称：  
```text
[root@node2 install]# tar -xf AutoInit_GBase8s_v1.4.13.tar

[root@node2 install]# ll
总用量 338352
-rwxr-xr-x. 1 root root     23073 5月  17 10:02 AutoInit_GBase8s.sh
-rw-r--r--. 1 root root     51200 5月  17 12:12 AutoInit_GBase8s_v1.4.13.tar
-rwxr-xr-x. 1 root root      3108 5月  17 10:02 autoOptimize.sh
-rwxr-xr-x. 1 root root      3344 5月  17 10:02 CheckEnv.sh
-rwxr-xr-x. 1 root root      1699 5月  17 10:02 CleanAll.sh
-rw-r--r--. 1 root root 350638080 5月   7 09:15 GBase8sV8.8_TL_3.6.3_3X1_1_x86.tar
-rw-r--r--. 1 root root      1736 4月  17 13:01 gbasedbt.service
-rw-r--r--. 1 root root      2321 6月  28 2024 HOW_TO_USE.txt
-rw-r--r--. 1 root root      3669 5月  17 09:41 README.txt
```

## 执行安装部署  
直接运行一键安装脚本AutoInit_GBase8s.sh进行安装，也可指定部分参数。  
```text
[root@node2 install]# bash AutoInit_GBase8s.sh -h
Usage:
    AutoInit_GBase8s.sh [-d path] [-i path] [-p path] [-s y|n] [-l locale] [-u user] [-o y|n]
                        [-n servername] [-c num_of_cpu] [-m num_of_memory] [-t type_of_instance]
                        [-a y|n]

        -d path    The path of dbspace.
        -i path    The path of install software.
        -p path    The path of home path.
        -s y|n     Value of dbspace is 1GB? Yes/No, default is N.
        -u user    The user name for SYSDBA, gbasedbt/informix, default is gbasedbt
        -l locale  DB_LOCALE/CLIENT_LOCALE/SERVER_LOCALE value.
        -o y|n     Only install software? Yes/No, default is N.
        -n NAME    Servername, default is gbase01.
        -c NUM     Number of CPU use.
        -m NUM     Number of MB Memory use.
        -t TYPE    Type of instance will install, [small], if use this, ignore -c and -m.
        -a y|n     Security need, default N.
```

使用按自动配置（使用1G的数据文件），过程中自动安装依赖包（有互联网连接）、软件安装、初始化实例。  

```text
[root@node2 install]# bash AutoInit_GBase8s.sh -s y
[2024-06-18 17:28:40] The SYSDBA user is: gbasedbt
PING 1.2.4.8 (1.2.4.8) 56(84) bytes of data.
64 bytes from 1.2.4.8: icmp_seq=1 ttl=128 time=29.4 ms
64 bytes from 1.2.4.8: icmp_seq=2 ttl=128 time=29.8 ms
64 bytes from 1.2.4.8: icmp_seq=3 ttl=128 time=31.6 ms
64 bytes from 1.2.4.8: icmp_seq=4 ttl=128 time=29.4 ms
64 bytes from 1.2.4.8: icmp_seq=5 ttl=128 time=29.0 ms
(中间过程省略)
[2024-06-18 17:31:03] Finish.

(完成安装的信息提示)
--=\= GBase 8s Information for this install =\=--
$GBASEDBTSERVER : gbase01
$GBASEDBTDIR    : /opt/gbase
USER HOME       : /home/gbase
DBSPACE DIR     : /data/gbase
IP ADDRESS      : 0.0.0.0
PORT NUMBER     : 9088
$DB_LOCALE      : zh_CN.utf8
$CLIENT_LOCALE  : zh_CN.utf8
JDBC URL        : jdbc:gbasedbt-sqli://IPADDR:9088/testdb:GBASEDBTSERVER=gbase01;DB_LOCALE=zh_CN.utf8;CLIENT_LOCALE=zh_CN.utf8;IFX_LOCK_MODE_WAIT=10
JDBC USERNAME   : gbasedbt
JDBC PASSWORD   : GBase123$%
INNER USERNAME  : dbtuser
INNER PASSWORD  : GBase123$%
```

## 连接数据库  
执行如下命令连接至GBase 8s数据库服务端  
```text
[gbasedbt@node2 ~]$ dbaccess testdb -

Database selected.

>

```
