# 事务操作  
本章节将介绍GBase 8s数据库中事务相关的基本语法和示例。  
默认隔离级别（提交读）下  
提交事务前，用户在事务过程做的任何修改只有自己能看到，其他用户无法看到，并可以通过回滚操作将数据恢复。  
提交事务后，其他用户可看到修改后的数据，此时无法通过回滚操作将数据恢复。  

## 开始事务    
执行BEGIN WORK语句开始事务    
```sql  
BEGIN WORK;
```

## 提交事务  
执行COMMIT语句提交事务  
```sql  
BEGIN WORK;
CREATE TABLE tab1(col1 int, col2 varchar(255));
INSERT INTO tab1 values(1,'test001');
COMMIT;
```

## 回滚事务  
执行ROLLBACK语句回滚事务  

- 执行如下语句给tab1中增加数据  

```sql  
SELECT * FROM tab1;
```

结果：  
```text
|col1 |col2    |
|-----|--------|
|1    |test001 |
```

```sql
BEGIN WORK;
INSERT INTO tab1 values(2,'test002');
SELECT * FROM tab1;
```

结果：  
```text
|col1 |col2    |
|-----|--------|
|1    |test001 |
|2    |test002 |
```

- 执行ROLLBACK进行回滚至初始状态  

```sql  
ROLLBACK;

SELECT * FROM tab1;
```

结果：  
```text
|col1 |col2    |
|-----|--------|
|1    |test001 |
```
