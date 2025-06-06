# 用户操作  
本章节将介绍GBase 8s数据库用户相关的基本操作
GBase 8s数据库默认仅使用操作系统用户，用户操作在操作系统层实现，授权在数据库内实现。
数据库内部用户需要通过配置才能开启，一键安装脚本安装的方式已经开启了内部用户。

以下示例均是使用内部用户的方式：  
## 创建用户  
使用gbasedbt用户，执行如下SQL命令创建新用户dbtuser2，并为其指定密码GBase123$% ：  
```sql
create user dbtuser2 with password 'GBase123$%';
```

## 创建角色  
使用gbasedbt用户，执行如下SQL命令创建新角色dbt_role ：
```sql
create role dbt_role;
```
注：角色仅在库内有限，不同库角色是无联系的。

## 授权用户  
使用gbasedbt用户，执行如下SQL命令为用户dbtuser2授予登录会话和创建资源的权限：
```sql
GRANT CONNECT TO dbtuser2;
GRANT RESOURCE to dbtuser2;
```

## 切换用户  
执行如下SQL命令切换至用户dbtuser2：
```text
[gbasedbt@node2 ~]$ dbaccess - -
> connect to 'testdb@gbase01' user 'dbtuser2';
ENTER PASSWORD:

Disconnected.


Connected.
```

注1：切换对象须具有登录会话的权限方可进行切换操作。
注2：connect to '库名@实例名' user '用户名';

## 修改密码  
执行如下SQL命令将dbtuser2用户的密码修改为1qaz@WSX ：
```sql
alter user dbtuser2 modify password '1qaz@WSX';
```

注：修改用户密码的操作需要用户本身，或者DBSA权限。

## 删除用户  
使用gbasedbt用户，执行如下SQL语句将删除用户dbtuser2 :
```sql
drop user dbtuser2;
```
