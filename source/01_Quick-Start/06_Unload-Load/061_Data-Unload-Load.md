# 数据导出导入  
本章将对GBase 8s dbaccess内置数据导出导入工具unload/load进行介绍及提供基础示例。    
unload/load是GBase 8s提供的客户端导入工具，用于执行文件格式的数据文件导出和导入，每次导入单个数据文件至单个表中。   
 
## 数据导出  
使用dbaccess客户端工具登陆数据库，执行unload语句导出数据  
```text
[gbasedbt@node2 temp]$ dbaccess testdb -

Database selected.

> unload to company.unl
> select * from company;

2 row(s) unloaded.
```

导出到文件company.unl，内容如下：  
```text
1|GBase|TJ|
2|GBase BeiJing|BJ|
```

## 数据导入  
使用dbaccess客户端工具登陆数据库，执行load语句导出数据  
```text
[gbasedbt@node2 temp]$ dbaccess testdb -

Database selected.

> truncate table company;

Table truncated.

Elapsed time: 0.012 sec

> select * from company;



No rows found.

Elapsed time: 0.001 sec

> load from company.unl
> insert into company;

2 row(s) loaded.

Elapsed time: 0.013 sec

> select * from company;



coid    1
coname  GBase
coaddr  TJ

coid    2
coname  GBase BeiJing
coaddr  BJ

2 row(s) retrieved.

Elapsed time: 0.001 sec
```
