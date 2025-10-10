# GBase 8s 常用SQL及脚本  
常用SQL及脚本  

## 查询表的空间使用  
数据库版本：ALL  
**功能描述：**  
查询表（普通表和分片表）的行数、空间占用大小（MB）、使用大小（MB）  
**SQL语句：**  
```text
-- SQLMODE=gbase
SELECT t.tabname, 'standard' AS tabtype, p.nrows AS nrows, (p.nptotal * t.pagesize)/1024/1024 total_mb, (p.npused * t.pagesize)/1024/1024 used_mb
FROM systables t, sysmaster:sysptnhdr p 
WHERE t.tabid > (SELECT tabid FROM systables WHERE tabname = ' VERSION') 
  AND t.tabtype = 'T'
-- 这里是普通表，需要修改表名
  AND t.tabname = 't1'
  AND t.partnum = p.partnum
UNION ALL
SELECT t.tabname, 'fragment' AS tabtype, sum(p.nrows) AS nrows, sum(p.nptotal * d.pagesize)/1024/1024 total_mb, sum(p.npused * d.pagesize)/1024/1024 used_mb
FROM systables t, sysfragments f, sysmaster:sysptnhdr p, sysmaster:sysdbspaces d
WHERE t.tabid > (SELECT tabid FROM systables WHERE tabname = ' VERSION') 
  AND t.tabtype = 'T'
-- 这里是分片表，需要修改表名
  AND t.tabname = 't1'
  AND t.tabid = f.tabid
  AND f.fragtype = 'T'
  AND f.partn = p.partnum
  AND f.dbspace = d.name
GROUP BY 1;
```

-----  

## 获取实例初始化时间  
数据库版本：ALL  
**功能描述：**  
获取实例初始化时间，通过rootdbs的创建时间来确定  
**SQL语句：**  
```text
-- SQLMODE=gbase
-- 获取实例初始化时间（rootdbs创建时间）
SELECT dbinfo('utc_to_datetime',d.created) AS created 
FROM sysmaster:sysdbstab d 
WHERE dbsnum = 1;
```

-----  

## 获取dbspace的创建时间  
数据库版本：ALL  
**功能描述：**  
获取dbspace的创建时间，与获取实例初始化时间语句相同  
**SQL语句：**  
```text
-- SQLMODE=gbase
-- 获取dbspace的创建时间
SELECT d.name, dbinfo('utc_to_datetime',d.created) AS created
FROM sysmaster:sysdbstab d
-- 指定dbspace名称
WHERE d.name = 'plogdbs';
```

-----  

## 获取数据库的创建时间  
数据库版本：ALL  
**功能描述：**  
获取数据库的创建时间  
**SQL语句：**  
```text
-- SQLMODE=gbase
-- 获取数据库创建时间
SELECT dbinfo('utc_to_datetime',created) AS created 
FROM sysmaster:sysdbspartn 
-- 指定数据库名称
WHERE name = 'testdb';
```

-----  

## 获取表的创建时间  
数据库版本：ALL  
**功能描述：**  
获取表的创建时间，需要包含标准表和分片表  
**SQL语句：**  
```text
-- SQLMODE=gbase
-- 获取表创建时间（本库）
SELECT t.tabname,'Normal' AS tabtype,dbinfo('utc_to_datetime',p.created) AS created
FROM systables t,sysmaster:sysptnhdr p
WHERE t.partnum = p.partnum 
AND t.tabtype = 'T'
-- 这里是普通表，需要修改表名
AND t.tabname = 'tab11'
UNION 
SELECT t.tabname,'Fragment' AS tabtype,dbinfo('utc_to_datetime',p.created) AS created
FROM systables t,sysfragments f,sysmaster:sysptnhdr p
WHERE t.tabid = f.tabid
AND f.partn = p.partnum
AND f.fragtype = 'T'
-- 这里是分片表，需要修改表名
AND t.tabname = 'tab11';
```

-----  

## 获取索引的创建时间  
数据库版本：ALL  
**功能描述：**  
获取索引的创建时间，如果是分片索引，将返回多行  
**SQL语句：**  
```text
-- SQLMODE=gbase
-- 获取索引的创建时间(本库)
SELECT f.indexname,'INDEX' AS tabtype, dbinfo('utc_to_datetime',p.created) AS created
FROM sysfragments f, sysmaster:sysptnhdr p
WHERE f.partn = p.partnum
AND f.fragtype = 'I'
-- 指定索引名称
AND f.indexname = 'ix_tab_1_col1';

-- 按表获取索引创建时间（本库）
SELECT f.indexname,'INDEX' AS tabtype, dbinfo('utc_to_datetime',p.created) AS created
FROM sysfragments f,systables tab,sysmaster:sysptnhdr p
WHERE f.tabid = tab.tabid
AND f.partn = p.partnum 
AND f.fragtype = 'I'
-- 指定表名
AND tab.tabname = 'tab1';
```

-----  

## 获取序列的创建时间  
数据库版本：ALL  
**功能描述：**  
获取序列的创建时间  
**SQL语句：**  
```text
-- SQLMODE=gbase
-- 获取序列创建时间（本库）
SELECT t.tabname,'SEQUENCE' AS tabtype,dbinfo('utc_to_datetime',p.created) AS created
FROM systables t,sysmaster:sysptnhdr p
WHERE t.partnum = p.partnum 
AND t.tabtype = 'Q'
-- 指定序列名称
AND t.tabname = 'seq1';
```

-----  

## 获取视图的创建日期（仅日期）  
数据库版本：ALL  
**功能描述：**  
获取视图的创建日期（仅日期）  
**SQL语句：**  
```text
-- SQLMODE=gbase
-- 获取视图创建日期（本库）
SELECT t.tabname,'VIEW' AS tabtype, t.created AS created
FROM systables t
WHERE t.tabtype = 'V'
-- 指定视图名称
AND t.tabname = 'view_systables';
```

-----  

## 位于rootdbs上的非系统库  
数据库版本：ALL  
**功能描述：**  
获取位于rootdbs上的非系统库的名称及表名  
**SQL语句：**  
```text
-- SQLMODE=gbase
-- 数据库位于rootdbs上
select t.dbsname database, 
       d.name dbspace,
       t.tabname 
from sysdbstab d,syschunks c,sysextents t 
where t.chunk = c.chknum 
and c.dbsnum = d.dbsnum 
and t.dbsname NOT IN ('sysmaster','sysuser','sysutils','sysadmin','sysha','sys','gbasedbt','syscdr','syscdcv1','onpload')
and t.tabname != 'TBLSpace'
and d.name = 'rootdbs';
```

-----  

## 数据库表区段数量检查  
数据库版本：ALL  
**功能描述：**  
数据库表区段数量检查  
**SQL语句：**  
```text
-- SQLMODE=gbase
-- 数据库表区段数量检查
select {+ ordered, index(a, syspaghdridx) } -- necessary
    c.tabname, -- the table or index
    c.dbsname, -- the database
    b.name,    -- the dbspace
    -- 每区段需要10个字节描述
    trunc(a.pg_frcnt / 10) frext    -- the free extents
from sysmaster:sysdbspaces b,
sysmaster:syspaghdr a,
sysmaster:systabnames c
where a.pg_partnum = sysmaster:partaddr(b.dbsnum, 1)
and sysmaster:bitval(a.pg_flags, 2) = 1
and a.pg_nslots = 5
and c.partnum = sysmaster:partaddr(b.dbsnum, a.pg_pagenum)
-- and c.dbsname[1,3] != 'sys'
-- 小于40个区段
and a.pg_frcnt < 400
order by 4 asc; 
```

-----  

## 数据库表索引层数  
数据库版本：ALL  
**功能描述：**  
数据库表索引层数  
**SQL语句：**  
```text
-- SQLMODE=gbase
-- 数据库表索引层数
SELECT FIRST 20 dbinfo('dbname') dbname, t.tabname, i.idxname, i.levels 
FROM systables t, sysindexes i
WHERE t.tabid = i.tabid
AND t.tabid > (SELECT tabid FROM systables WHERE tabname = ' VERSION')
-- 大于4层
AND i.levels > 4
ORDER BY 4 DESC;
```

-----  

## 数据库表索引唯一性  
数据库版本：ALL  
**功能描述：**  
数据库表索引唯一性（需要统计更新）  
**SQL语句：**  
```text
-- SQLMODE=gbase
-- 数据库表索引唯一性
SELECT FIRST 20 dbinfo('dbname')  dbname,
                t.tabname  tabname,
                i.idxname  idxname,
                t.nrows    nrows,
                i.nunique  nunique,
                ROUND((i.nunique/t.nrows)*100,2) pcniq
FROM systables t, sysindexes i
WHERE t.tabid = i.tabid
AND t.tabid > (SELECT tabid FROM systables WHERE tabname = ' VERSION')
AND t.nrows > 0
ORDER BY 4 DESC, 6 DESC;
```

-----  

## 用户使用逻辑日志  
数据库版本：ALL  
**功能描述：**  
用户会话使用逻辑日志情况  
**SQL语句：**  
```text
-- SQLMODE=gbase
-- 用户使用逻辑日志
select
  t.username,
  t.sid,
  tx_logbeg,
  tx_loguniq,
  hex(tx_logpos) tx_logpos
from sysmaster:systrans x, sysmaster:sysrstcb t
where tx_owner = t.address;
```

-----  

## 获取表的锁类型  
数据库版本：ALL  
**功能描述：**  
获取表的锁类型  
**SQL语句：**  
```text
-- SQLMODE=gbase
-- 表锁类型
select tabname,nrows,locklevel
from systables
where tabid > (SELECT tabid FROM systables WHERE tabname = ' VERSION')
and tabtype = 'T'
-- R为行锁，P为页锁
--and locklevel = 'R'
and locklevel = 'P';
```

-----  

## 索引首字段重复  
数据库版本：ALL  
**功能描述：**  
获取索引首字段重复，用于重复索引判定  
**SQL语句：**  
```text
-- SQLMODE=gbase
-- 索引首字段重复
select 
  t.tabname,
  t.tabid,
  -- abs(i.part1) AS idx_col1,
  (SELECT c.colname FROM syscolumns c WHERE c.tabid = t.tabid AND c.colno = abs(i.part1)) AS idx_col1,
  count(*) cnt
from systables t, sysindexes i
where t.tabid = i.tabid 
and t.tabid > (SELECT tabid FROM systables WHERE tabname = ' VERSION')
group by 1,2,3
having count(*) > 1
order by 4 desc;
```

最后更新日期：2025-10-10  
