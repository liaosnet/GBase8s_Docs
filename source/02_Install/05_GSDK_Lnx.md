# GSDK安装与配置（Linux）  
本章节将介绍GBase 8s客户端安装部署及配置。  

## 什么是GCI（GSDK）  
GBase8s 调用接口 （GCI） 是一种应用程序编程接口 （API），可用于创建使用函数调用访问 GBase8s 数据库并控制 SQL 语句执行和数据访问的所有阶段的应用程序。   
使用GCI的替代方法： ODBC 驱动程序  
GCI 支持 C 和 C++ 的数据类型、调用约定、语法和语义。  
GSDK 不需要额外安装CSDK。  

## 版本说明  
根据安装环境准备申请下载数据库软件介质。  
按以下内容选择合适的软件包  
主版本号：对应数据库版本，如：3.6.3_3x2_1   
子版本号：详细的发行版本，如：1.1.0_1  
编译环境：编译该软件包的环境。安装环境应与此相同或者相近。   
- YHKylin4_FT 表示是飞腾平台（FT ARM64）、银河麒麟系统   
- CentOS7_aarch64 表示是aarch64通用平台、CentOS7系统  
- RHEL6_x86_64 表示是x86架构（64bit）、RHEL6系统  
- AIX5L 表示IBM Power架构、AIX5系统  
 
如：GSDK_3.6.3_3X2_1_1.1.0_1_eff9f1_RHEL6_x86_64.tar 表示适用于x86_64架构，操作系统为RHEL6（或者兼容），适配的数据库版本是3.6.3_3X2_1的软件安装包。  

## GSDK的安装与配置  
GSDK可使用任意用户进行安装。  
将软件包GSDK_3.6.3_3X2_1_1.1.0_1_eff9f1_RHEL6_x86_64.tar上传至install目录中，请确认软件包是以.tar为后缀。  

### 解压缩GSDK软件包  
解压，并改名称  
```text
[root@localhost install]# tar -xvf GSDK_3.6.3_3X2_1_1.1.0_1_eff9f1_RHEL6_x86_64.tar -C /opt/

[root@localhost install]# mv /opt/GSDK_3.6.3_3X2_1_1.1.0_1_eff9f1_RHEL6_x86_64 /opt/GSDK
```

### 设置环境变量  
加lib加入到LD_LIBRARY_PATH中  
```text
export GSDK_PATH=/opt/GSDK
export LD_LIBRARY_PATH=${GSDK_PATH}/lib:$LD_LIBRARY_PATH
```

最后更新日期：2025-08-20  
