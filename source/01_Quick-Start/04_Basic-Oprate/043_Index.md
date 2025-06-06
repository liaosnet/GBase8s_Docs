# 索引操作  
本章节将介绍GBase 8s数据库中索引相关的基本语法和示例。  
索引是一种物理的对数据库表中一列或多列的值进行排序的存储结构，它是某个表中一列或若干列值的集合，是指向表中物理标识这些值所在行的逻辑指针清单。  

## 创建索引  
执行CREATE INDEX语句创建索引：  
```sql
CREATE TABLE company(coid serial, coname varchar(255), coaddr varchar(255));

CREATE INDEX ix_company_coname ON company(coname);
```

## 查看索引  
通过查询sysindexes视图查看当前用户的索引信息：  
```sql
SELECT *
FROM sysindexes
WHERE tabid > 999;
```
注：在3.6.x版本之后，系统表的tabid改为小于1000。  

## 删除索引  
通过DROP INDEX语句删除索引  
```sql
DROP INDEX ix_company_coname;
```
