# 数据结构导出导入  
本章将对GBase 8s内置结构导出工具dbschema进行介绍及提供基础示例。  
dbschema工具是GBase 8s的配套结构导出工具。  
用户可通过使用dbschema工具将GBase 8s数据库中的表结构、索引、约束等所有数据生成一个元数据文件。  

## 数据结构导出  
使用dbschema命令导出表结构到sql文件中  
```text
[gbasedbt@node2 temp]$ dbschema -d testdb -t company -ss company.sql
```

参数说明：-d 指定库，-t 指定表名，不指定该参数则是全库，-ss 生成特定于服务器的语法，最后的.sql是生成的sql文件名称  

## 表结构导入  
dbschema生成的表结构sql文件，可通过dbaccess直接执行  
```text
[gbasedbt@node2 temp]$ dbaccess testdb -

Database selected.

> rename table company to company_1;

Table renamed.

Elapsed time: 0.013 sec

[gbasedbt@node2 temp]$ dbaccess testdb company.sql
```
