# 表操作  
本章节将介绍GBase 8s数据库中表相关的基本语法和示例。  
表是数据库用来存放数据的一个集合，一般与实体对象一一对应，如人员表、部门表、公司表等，一般由行和列这两个二维信息来组织表数据。  

## 创建表  
执行create table 语句创建表  
```sql
CREATE TABLE company(
  coid serial,
  coname varchar(255),
  coaddr varchar(255)
);
```

## 查看表  
通过查询systables视图查看当前库中已存在的表名称：  
```sql
SELECT *
FROM systables
WHERE tabid > 999
AND tabtype = 'T';
```
注：在3.6.x版本之后，系统表的tabid改为小于1000。  

执行SELECT语句查看表中具体信息：  
```sql
select *
from company;
```

### 查看表字段  
查看表的字段，在dbaccess中可以直接使用  
```sql
info columns for comany;
```

也可通过sql语句：  
```sql
SELECT c.colno,c.colname,c.coltypename2
FROM syscolumnsext c, systables t
WHERE c.tabid = t.tabid
AND t.tabname = 'company';
```

## 修改表  
执行语句修改表的相关属性：  

- 执行如下语句修改表名称  
```sql
RENAME TABLE company TO company_1;
```

- 执行如下语句给表增加字段  
```sql
ALTER TABLE company_1 ADD (copost varchar(10));
```

- 执行如下语句修改表中列字段的数据类型：  
```sql
ALTER TABLE company_1 MODIFY (copost int);
```

## 删除表  
执行DROP TABLE语句删除表：
```sql
DROP TABLE company_1;
```
