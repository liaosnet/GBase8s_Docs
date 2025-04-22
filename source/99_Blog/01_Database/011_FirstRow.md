# mysql group by兼容写法FIRST_ROW  
从mysql迁移库，存在非聚集列不在group by 的语句。
这样的sql会被认为是不合法的sql，因为：
- 1，order by后面的列必须是在select后面存在的
- 2，select、having或order by后面存在的非聚合列必须全部在group by中存在

通用情况下，mysql可以通过以下三种方式解决报错问题
- 1，修改sql使其遵守only_full_group_by规则
- 2，关闭only_full_group_by规则
- 3，降级数据库版本在5.7以下

对于迁移数据，仅有一种选择（即修改sql，使其符合 非聚集列在group by 语句中)，为非聚集列加上常用min(),max()等聚集函数，当然这将导致结果集与之前的mysql有差异，如果客户希望保留原有结果集，我们也可以通过创建自定义聚集函数的方式，返回非取集列返回第一行的写法。  
如下：  
```sql
DROP FUNCTION IF EXISTS my_first_row_init;
CREATE dba FUNCTION  my_first_row_init (dummy varchar(255))
  RETURNING varchar(255) with (not variant);
  RETURN '##FIRSTROW##';
END FUNCTION;
 
DROP FUNCTION IF EXISTS my_first_row_iter;
CREATE dba FUNCTION  my_first_row_iter (result varchar(255), value varchar(255))
  RETURNING varchar(255) with (not variant);
  if result[1,12] = '##FIRSTROW##' then
    return value;
  else
    return result;
  end if;
END FUNCTION;
 
DROP FUNCTION IF EXISTS my_first_row_combine;
CREATE dba FUNCTION  my_first_row_combine(partial1 varchar(255), partial2 varchar(255))
  RETURNING varchar(255) with (not variant);
  RETURN '';
END FUNCTION;
 
DROP aggregate if exists first_row;
create aggregate first_row with
(
  INIT = my_first_row_init,
  ITER = my_first_row_iter,
  COMBINE = my_first_row_combine
);
```

示例：  
```sql
SELECT col1,first_row(col2)
FROM tab11
GROUP BY col1;
```
col2返回分组的第一行。

