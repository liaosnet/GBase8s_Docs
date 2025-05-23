# 数据操作  
本章节将介绍GBase 8s数据库中表相关的基本语法和示例。  

## 插入数据  
通过执行INSERT语句往表中插入数据：  
```sql  
INSERT INTO company values(0,'coname1','coaddr1');

-- 多values写法
INSERT INTO company values(0,'coname2','coaddr2'),(0,'coname3','coaddr3');
```

## 查询数据  
通过执行SELECT语句查询数据：  

- 执行如下语句查询company表中所有数据
```sql  
SELECT * FROM company;
```

- 执行如下语句对company表进行条件查询：
```sql  
SELECT * FROM company WHERE coid = 3;
```

## 修改数据  
通过执行UPDATE语句更新表中数据：  

- 执行如下语句将company表coname列字段中coname='coname1'的数据更新为coname='co'：  

```sql  
SELECT * FROM company;
```

结果：  
```text
|coid |coname  |coaddr  |
|-----|--------|--------|
|1    |coname1 |coaddr1 |
|2    |coname2 |coaddr2 |
|3    |coname3 |coaddr3 |
```

执行更新操作：  
```sql
UPDATE company SET coname='co' WHERE coname='coname1';

SELECT * FROM company;
```

结果：  
```text
|coid |coname  |coaddr  |
|-----|--------|--------|
|1    |co      |coaddr1 |
|2    |coname2 |coaddr2 |
|3    |coname3 |coaddr3 |
```

- 执行如下语句批量更新company表中的数据：  

```sql  
UPDATE company SET (coname,coaddr) = ('coname33','coaddr33') WHERE coid=3;

SELECT * FROM  company;
```

结果：  
```text
|coid |coname   |coaddr   |
|-----|---------|---------|
|1    |co       |coaddr1  |
|2    |coname2  |coaddr2  |
|3    |coname33 |coaddr33 |
```

## 删除数据  
可选DELETE和TRUNCATE TABLE两种方式对表数据进行删除：  

- 通过执行DELETE语句删除数据：  
   - 执行如下语句删除company表中coid=1的行：  
```sql  
DELETE FROM company WHERE coid = 1
```

   - 执行如下语句删除insert_tb表中所有行：  
```sql  
DELETE FROM company;
```
