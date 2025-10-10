# GBase 8s FAQ  
FAQ  

## 应用插入数据到表失败的原因  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
有哪些情况会导致应用插入数据到表失败？  
**解决方法：**  
1、dbspace 空间满。  
2、表的页数量达到上限，表（或者表分区）的页上限为 16,775,134 页左右。需要分片才能实现扩展。  
3、插入的数据某一行中包含乱码。  
4、表的锁模式为 page，可能会导致插入失败。  
5、出现长事务，导致事务回滚。  

-----

## 如何查看回滚的事务 SQL  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
如何查看当前数据库中是否有事务在回滚，如果有，具体是哪条 SQL 在回滚？  
**解决方法：**  
方法1：  
通过 onstat -u|grep RP； 可以获取相关的 sessionid。通过 onstat -g ses sid 获取 SQL；  
方法2：  
通过 onstat -x|grep "A-R"；可以定位到 userthread，例如 "686cb9e8"，然后通过 onstat -u|grep "686cb9e8" 获取到 sessionid；onstat -x 输出中的 rb_time 表示回滚的剩余时间。  

-----

## 如何查看分片的 partnum  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
分片表在 systables 系统表中的 partnum 为 0。该如何找到各个分片的 partnum？  
**解决方法：**  
可通过如下方法获取：  
```text
select t.tabname,f.partn,hex(f.partn) hex_partn 
from systables t,sysfragments f  
where t.tabid=f.tabid
and t.tabname="tab1"  -- 表名
```

-----

## 系统中如何查看表中数据量  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
对表 tab1 一次性插入 10000 行数据后，通过 systables 表中的 nrows 查看，行数依然为 0。如何查看 tab1 真实的数据量？如果 tab1 是分片表，又该如何查看每个分片中各有多少数据？  
**解决方法：**  
systables 系统表中存放的只是统计数据，需要执行 update statistics（统计更新）后才能显示真实行数。可以通过以下方法查看真实行数：  
1、如果是非分片表，可以通过 systables 中的 partnum 与 sysmaster 库 sysptnhdr 表中的 partnum 做连接。Sysptnhdr 表中的 nrows 是实时的真实行数，npdata 是真实的数据使用的页数量：  
```text
-- SQLMODE=gbase
select t.tabname,t.partnum,t.nrows,p.nrows,p.npdata
from stores_demo@gbaseserver:systables t, sysmaster@gbaseserver:sysptnhdr p
where t.partnum=p.partnum 
and t.tabname="customer";  -- 表名
```
2、如果是分片表，可以通过 sysfragments 中的 partn 与 sysmaster 库 sysptnhdr 表中的partnum 做连接；  
```text
-- SQLMODE=gbase
SELECT t.tabname,p.partnum,t.nrows,p.nrows,p.npdata
FROM systables t, sysfragments f, sysmaster:sysptnhdr p
WHERE t.tabname = 'tf'  -- 表名
AND t.tabid = f.tabid
AND f.partn = p.partnum;
```
3、可以通过 oncheck -pt dbname:tab1 查看各个分片（或非分片）表的行数、页使用情况。  

-----

## 数据库 online 但 dbaccess 无反应  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
数据库 online，但是通过 dbaccess 没有反应。  
**解决方法：**  
1、主机的 CPU 使用率长期在 85% 左右不变；  
2、主机有 48 个 core，数据库配置了 42 个 VP；  
3、可以估算出数据库的 CPU 使用率已经达到了 100%，所以对 dbaccess 的请求无法响应；  
4、抓到运行代价大的 SQL 进行优化处理。  

-----

## 通过 sysmaster 统计 CHUNK 大小不准确    
数据库版本：ALL  
操作系统：ALL  
**描述：**  
通过 sysmaster 中表统计 CHUNK 大小不准确的问题。  
**解决方法：**  
syschunks.chksize 和 syschktab.chksize 的单位是页数，但是此处页面的大小是基础页面（操作系统页面）的大小，而不是 pagesize 的大小。  
在统计 nfree 的时候也有类似的问题。  
参考以下SQL:  
```text
-- SQLMODE=gbase
SELECT trim(chk.fname) AS fname, chk.chksize * shm.sh_pagesize AS chksize, chk.nfree * shm.sh_pagesize AS freesize
FROM sysmaster:syschunks chk,sysmaster:sysshmvals shm
```

-----

## 如何实现中文拼音排序  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
如何实现中文拼音排序？  
**解决方法：**  
使用 zh_cn 字符集，并设置环境变量 GL_USEGLU=1，重启数据库后创建数据库，字段类型使用 nchar 或 nvarchar。  
**注意：整个实例应当使用相同的GL_USEGLU环境变量**  
示例：  
```text
export GL_USEGLU=1
export DB_LOCALE=zh_cn.utf8
export DB_LOCALE=zh_cn.utf8
oninit
echo "create database testdb with log" | dbaccess -
echo "create table test (cc nchar(50))" | dbaccess testdb
echo "insert into test values ('中文')" | dbaccess testdb
echo "select cc from test order by cc" | dbaccess testdb
```

-----

## 查询 systables 表报 -206 错误  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
查询 systables 表报 -206 错误，找不到表 xxx.systables，查询 gbasedbt.systables 可以正常访问。  
**解决方法或者原因：**  
原因：  
database 为 ANSI 模式，ANSI 模式数据库要求要把 schema(user) 写全才能访问到表，否则默认访问当前模式的表。  
解决办法：  
1、写全用户名；  
2、修改 database 日志模式（ANSI 模式无法直接修改为其他模式，需要导出并重新导入）  

-----

## 查看空间中临时表属于哪个会话的方法  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
查看空间中临时表属于哪个会话的方法。（适用于临时表占用很多空间且持续时间较长。）  
**解决方法：**  
1、通过 onchechk 查看 rootdbs 中临时表的大小：  
```text
$ onstat -d|grep root
7000002930d9028 1 0x40001 1 1 4096 N B gbasedbt rootdbs
7000002930d91c0 1 1 0 2557500 188026 PO-B-  sddbs/sdqtrootdblv01

$ oncheck -pe rootdbs|tail
sysadmin:'gbasedbt'.mon_checkpoint 312381 8
sysadmin:'gbasedbt'.idx_mon_ckpt_1 312389 4
sysadmin: 'gbasedbt'.mon_vps 312393 8
sysadmin: 'gbasedbt'.mon_prof 312401 8
sysadmin: 'gbasedbt'.mon_prof_idx1 312409 6
sd3700ids3gdb:'ids3g'._temptable 312415 2245085
Total Used: 2369474
Total Free: 188026
```

2、通过这个大小确定临时表的 partnum：  
```text
$ onstat -t|grep 2245085
442 7000002bcf11930 800 1 100140 1:312001 2245085 1 0 0 1
```

3、通过这个 partnum 查看哪个会话打开了这张表：  
```text
$ onstat -g opn|grep 100140
269366 0x07000002b435ca20 49 0x0000090a 0x00000003 0x00100140 1 1 0

$ onstat -u|grep 7000002b435ca20
7000002b435ca20 B--PR-- 108420 ids3g - 70000005bed2368 0 2 87228928 23381517
```

4、查看会话信息，确定执行者及 SQL 语句：  
```text
$ onstat -g ses 108420
 On-Line (Prim) -- Up 40 days 16:46:32 -- 17474560 Kbytes
```

-----

## 查看哪些会话造成锁表  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
查看哪些会话造成了锁表（排它锁）  
**解决方法：**  
```text
-- database sysmaster
select s.owner,s.hex(rowidlk) rowid 
from syslocks s 
where dbsname='car3gdb'
and tabname='prpcmain' 
and type='X';
```

查看对 e0136b 表加锁的会话信息：  
```text
onstat -k|grep e0136b|grep 'HDR+X'|awk '{print "onstat -u|grep "$3}'|sh|awk '{print "onstat -g ses "$3}'|sh >>LK-`date +%m%d%H%M`.txt  
```

如，得到331543  
gbasedbt 用户组用户在命令行执行 `onmode -z 331543`
或执行 SQL 语句：   
```text
-- SQLMODE=gbase
execute function sysadmin:task('onmode','z','331543');
```

-----

## 发现有 corruption page    
数据库版本：ALL  
操作系统：ALL  
**描述：**  
发现有 corruption page  
**解决方法：**  
由于 corruption page 是非常可怕的错误，如果在 index 发生，必须重新建立 index。如果发生在 table 上面，那必须把数据卸载后，重新建表。  
**注释：**
一般是用户发现数据异常时，一般情况下可以通过 oncheck -cDI 来确定。如果严重的话，可能需要人工 oncheck -pP 来确认。典型的，在 ssc 环境中，出现双主，就容易出现页数据异常。（oncheck 命令具体使用请参考相应手册。）  

-----

## select into 大量数据进表造成回滚  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
一亿六千行数据共 16G select into 进表，由于锁不够用造成回滚，如何处理？  
**解决方法：**  
方法一、将表改成裸表（限单机），导入数据完成后再改成 standard 模式。裸表不加锁，使用裸表有如下好处：  
1、不记日志，不会造成长事务；  
2、不记日志可以提升效率；  
3、不会加任何锁，不会造成锁资源不够。  
方法二、也可以使用 dbload 工具将数据分批次提交。

-----

## 视图多个 union all 报错  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
视图多个 union all 报错如何处理？  
**解决方法：**  
修改视图折叠参数 `onmode -wf IFX_FOLDVIEW=0`  
**注：情况修改该参数**

-----

## 如何在唯一索引插入多个 NULL 值  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
如何在唯一索引插入多个 NULL 值？
**解决方法：**  
1、删除唯一索引；  
2、建立普通索引；  
3、创建触发器判断 NULL 以外的值是否重复。  
**注：并不支持唯一索引中多个NULL值，后续在oracle兼容版本可能实现多NULL值**

-----

## SQL 语句中引号部分换行后报错  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
SQL 语句中引号部分换行后报错如何处理？  
-282: Found a quote for which there is no matching quote.  
**解决方法：**  
临时性解决方法：在 SQL 最前执行 execute procedure ifx_allow_newline('t');  
永久解决方法：修改 ALLOW_NEWLINE 值为 1 重启数据库。  

-----

## 如何查看数据库数据文件的使用情况  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
如何查看数据库数据文件的使用情况？  
**解决方法：**  
1、数据库服务器执行 onstat -d 命令查看 free 列，空余大小为该数值乘以 pagesize 大小。  
2、通过系统表查询 `select chknum,nfree from sysmaster:syschunks`，nfree 乘以 2k （Linux默认2KB，AIX/Win下默认为4KB）为剩余空间大小。  

-----

## 如何实现分页的  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
如何实现分页的？  
**解决方法：**  
1、分页 SQL 语句：`SELECT SKIP M FIRST N FROM TABLENAME`
N 为每页的行数，M=(第几页-1)*N  
例如：
`SELECT SKIP 6 FIRST 3 * FROM systables;`  取第二页的数据，每页 3 行。  
2、兼容LIMIT M OFFSET N语法  
`SELECT * FROM systables LIMIT 3 OFFSET 6;`
3、兼容Oralce语法  
```text
-- SQLMODE=oracle
SELECT * FROM (
  SELECT *,rownum AS rn FROM systables 
  WHERE rownum <= 9
)
WHERE rn > 6;
```

-----

## 如何查询系统中有哪些锁  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
如何查询系统中有哪些锁？  
**解决方法：**  
查询系统表：  
```text
-- SQLMODE=gbase
select * from sysmaster:syslocks; 
```
表中 owner 列代表锁的拥有 session id。  

-----

## rename database 提示有锁，如何解锁？  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
rename database 提示有锁，如何解锁？  
**解决方法：**  
找出打开某个数据库的 session：  
```text
-- SQLMODE=gbase
select name,hex(rowid) 
from sysmaster:sysdatabases 
where name='dbname';
```

根据找出某数据库的 rowid 找出打开该库的 session：  
```text
onstat -k|grep -w 206|awk '{print "onstat -u |grep "$3}'|sh
onmode -z sessionid
```

-----

## SQL 语句缓存开启  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
SQL 语句缓存开启（SQL Statement Cache， SSC）  
**解决方法：**  
可以使用 onmode -e <mode> 实用程序来启用、打开/关闭或清除 SSC，其中<mode> :={ENABLE|ON|OFF|FLUSH}。如果 SSC 模式设为 ENABLE，那么只有显式地请求使用 SSC 的各个会话才会使用 SSC。这使得那些很少执行特定查询的应用程序可以利用 SSC 的优点，而不让大量来自其他应用程序的特定查询浪费空间或者迫使缓存的语句从 SSC 中移出。会话通过 SSC 的环境（STMT_CACHE=1）或者通过执行 SET STATEMENT CACHE ON 来请求对 SSC 的使用。  
**SSC 配置参数**  
对于每个应用程序，都可以使用一组参数对 SQL 语句缓存进行配置。这些参数还用于决定哪些语句应该输入到缓存中：  
STMT_CACHE_HITS —— 这个参数用于指定一条查询在数据库服务器为其在缓存中设立完全缓存条目之前应该执行过的次数。如果查询执行过的次数少于这个值，那么服务器将在缓存中为这条语句设立一个 key-only 条目，这种条目只包含该语句的文本。以后该语句每执行一次，hits 列的数字就加 1。当该语句执行过的次数达到这个参数的值时，数据库服务器将为其在缓存中设立一个完全缓存条目，这种条目包含语句和查询数据结构。  
STMT_CACHE_SIZE —— 这个变量用于指定语句缓存的大小。SSC 大小的默认值是 512 千字节。  
STMT_CACHE_NOLIMIT —— 这个变量用于指定是否将缓存的大小限制为 TMT_CACHE_SIZE 值。默认情况下，即使缓存的大小超过了 STMT_CACHE_SIZE 值，服务器也会将语句输入到缓存中。  
STMT_CACHE_NUMPOOL —— 当服务器需要在语句缓存中创建一个完全缓存条目时，默认情况下它会只从单个池中分配内存。当应用程序的用户数量非常大时，这会对性能产生负面影响。在这种情况下，可以使用这个参数将池的数量配置得更大一些。  
**使用 onstat 实用程序监视 SSC 的使用情况**  
onstat -g ssc 选项显示语句缓存中的完全缓存条目。输出中的 hits 列表明同一条语句执行过的次数。因此，hits 列中的值较大就意味着我们更有效地使用了 SQL 语句缓存来共享查询结构，从而也就提高了性能。#hits 列与 STMT_CACHE_HITS 配置参数相对应。  
**注释：**  
SSC 是共享内存中的一块区域，用于存储和共享各用户会话间相同语句的数据结构。下面是使用 SSC 功能所带来的好处：  
- 减少了内存消耗，因为查询数据结构是在不同用户间共享的。
- 查询处理时间更快，因为对存在于缓存中的语句，数据库服务器可以跳过解析和优化阶段，从而可以为查询提供更好的响应。  

如果 SSC 功能已启用，数据库服务器会做以下事情：  
当某个用户 user1 发出一条 SQL 语句时，数据库服务器检查语句缓存，查看缓存中是否存在相同的语句。如果缓存中不存在这样的语句，数据库服务器将解析、优化并执行该语句。  
它还将检查该语句是否适于输入到缓存中。如果该语句可以输入到缓存中，那么数据库服务器将为该语句在缓存中添加一个条目。  
当用户 user2 执行同样的语句时，数据库服务器将检查缓存并且在缓存中找到这条语句。  
因此它不会再次解析和优化该语句，而只是使用缓存中的信息执行该语句。  
一条语句要想输入到缓存中，应满足一组条件。以下是这些条件中的一部分：  
- 该语句应该是 SELECT、UPDATE、DELETE 和 INSERT 这四种语句之一。
- 该语句不应包含任何用户定义例程。
- 该语句不能包含任何 Temporary 或 Remote 表。
- 该语句不应包含子查询。  

-----

## -271 Could not insert new row into the table. 如何解决定位？    
数据库版本：ALL  
操作系统：ALL  
**描述：**  
-271 Could not insert new row into the table. 如何解决定位？  
**解决方法：**  
This problem has many possible causes, including a locked table or a full disk. Check the accompanying ISAM error code for more information.  
存储测分析：  
1、每个表分片的最大 extent 个数 (pagesize - 150 )/8  
a)、oncheck -pt 查看当前表的情况  
b)、使用如下 SQL，可检查数据实例内，所有表分配 extent 的情况：  
```text
-- SQLMODE=gbase
select t.tabname, t.dbsname, i.ti_nextns ext_nums, i.ti_nrows rows
from sysmaster:systabnames t, sysmaster:systabinfo i
where t.partnum =i.ti_partnum and i.ti_nextns >= 150 and i.ti_nrows > 10000
order by 3 desc
```
c)、当已分配的 extent 数等于最大值时，可采取如下操作  
- 1）、需要重建该表，并指定 first extent 及 next extent size 来避免 extent 超限。  
- 2）、优化分片，规避单片表的 extent 物理限制。  

2、每个表分片的最大物理页 2^24 表分片的物理页个数为 16,775,134，使用 oncheck -pt 可以查看表当前物理页的使用量。Number of pages allocated 条目显示了表分片总共的物理页数量，该值不能超过 16,775,134 的最大值。达到物理页上限时，需要对表进行分片。  

3、表所在数据空间（dbspace）的空闲空间大小  
a)、使用如下 SQL 计算每个 dbspace 的空间使用率：  
```text
-- SQLMODE=gbase
select name dbspace, sum( chksize) allocated, sum( nfree) free,
round(((sum(chksize)-sum(nfree))/sum(chksize))*100) pcused
from sysmaster:sysdbspaces d, sysmaster:syschunks c
where d.dbsnum=c.dbsnum
group by 1
order by 4 desc;
```
b)、如果表所在的 dbspace 空间使用率接近 100% , 需要向该 dbspace 增加 CHUNK。表空间分配的最小 extent 是 4page，因此数据库无法利用 dbspace 中小于 4 page 的空闲空间。因此当 dbspace 空闲空间不为 0 时，由于 extent 分配失败，数据也不能插入。  

-----

## 锁等待定位  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
如何进行锁等待定位？  
-113 ISAM error: the file is locked.  
-244 Could not do a physical-order read to fetch next row.  
-245 Could not position within a file via an index.  
**解决方法：**  
1、找出被锁表的 partnum：  
```text
-- SQLMODE=gbase
select hex(t.partnum) as partnum
from systables t
where t.tabname = 'gy'   -- 标准表名
union all
select hex(f.partn) as partnum
from systables t, sysfragments f
where t.tabname = 'gy'   -- 分片（区）表名
and t.tabid = f.tabid
and f.fragtype = 'T';
```
如：partnum = 0x0010005E  

2、onstat -k 查找相关的锁的 owner：  
```text
$ onstat -k |grep -i 10005e
10a2ca328 0 10e9442 10a2c9ef0 HDR+X 10005e 0 0
```
得到10e9442

3、onstat -u 中查找相应的 user 信息：  
```text
$ onstat -u |grep 10e9442
10e9442 Y--P--- 2073 gbasedbt 16 10f861738 0 2 0 0  
```
得到会话号2073  

4、onstat -g ses sid 查出具体的 session 信息。  
5、onmode -z 2073 如果有必要杀死相关会话解锁。

-----

## 索引监控  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
索引监控  
**解决方法：**  
层数监控：  
```text
-- SQLMODE=gbase, database sysmaster
select idxname, levels from sysindexes order by 2 desc
```
levels 超过 4 层就要考虑重建  

检查命中率不高的索引（nrows 和 unique 越接近越好，即唯一性）：  
```text
-- SQLMODE=gbase
select tabname, idxname, nrows, nunique
from systables t, sysindexes I
where t.tabid =i.tabid and t.tabid > (select tabid from systables where tabname = ' VERSION')
and nrows > 0 and nunique > 0
```
当索引的效率不高的时候，需要根据实际情况修改。  

-----

## 需要 GBase 8s 提供 guid 数据类型  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
.net EF Core 连接 GBase 8s，应用中使用 guid 数据需要数据库提供对应的数据类型。经测试若直接使用 char(36) 进行替代，应用读取数据报错。需要 GBase 8s 提供 guid 数据类型。  
**解决方法：**  
使用 GBase 8s 自定义数据类型语法创建 guid 类型，解决了 GBase 8s 缺失 guid 数据类型问题：  
```text
CREATE DISTINCT TYPE GUID AS CHAR(36);
DROP CAST(GUID AS CHAR(36));
DROP CAST(CHAR(36) AS GUID);
CREATE IMPLICIT CAST (GUID AS CHAR(36));
CREATE IMPLICIT CAST (CHAR(36) AS GUID);
```
-----

## group by 子句报错  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
group by 子句报错。  
**解决方法：**  
group by 子句必须包含 select 的字段，或者在 SQL 语句的外面再嵌套一个 select 子句，对嵌套的 select 语句进行去重。  
**注：之后mysql兼容版本支持该语法**

-----

## Select 查询中强制转换语法  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
Select 查询中强制转换语法如何写？  
**解决方法：**  
语法示例：null 强制转换为 int  
```text
-- SQLMODE=gbase
select null::int from sysmaster:sysdual 
union 
select tabid from systables;
```
还可以使用cast语法，如：`select cast(null as int) from dual`  

-----

## 报错断言失败: 来自 KAIO 资源  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
数据库报错信息为“断言失败：KAIO 资源耗尽，提示：初始化KAIO 失败，增加 KAIO 内核参数，可参考机器说明”。该如何进行配置？  
具体英文描述o类似如下:  
```text
Assert Failed: out of KAIO resources  
21:38:01 GBase 8s V8.7 Database Server Version 12.10.FC4G1
21:38:01  Who: Session(54, gbasedbt@gbaseserver1, 0, (nil))
                Thread(760, kaio, 0, 21)
                File: kaioapi.c Line: 203
21:38:01  Results: initializing KAIO failed
21:38:01  Action: increase KAIO kernel parameter (see also: machine notes)
```
**解决方法：**  
原因是 kaio 设置的太小，先动态增加：  
```text
# echo 131072 > /proc/sys/fs/aio-max-nr
```
调整内核参数：  
```text
# echo '
kernel.shmmni=4096
kernel.sem=5010 641280 5010 128
fs.aio-max-size = 131072
fs.aio-max-nr = 131072
fs.file-max=6491589
net.ipv4.ip_local_port_range=1024 65000' >> /etc/sysctl.conf
```
aio-max-nr 相关的参数是 fs.aio-max-nr。  
aio-max-size 不同大小的性能影响。  
aio-max-size 的大小基本可用从下规则来界定：如果是决策支持系统（DSS），则进行大量的连续 IO， 所以使用较大的值（1M 甚至更大）；如果是联机事务处理（OLTP），则进行大量的小型交易，所以 default 的 128K 能够提供良好的性能。  

-----

## 在线打开和关闭 sqltrace  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
在不需要重启数据库的前提下，如何打开和关闭 sqltrace？  
**解决方法：**  
通过 sysadmin 库 task 函数动态打开和关闭 sqltrace。例如：  
```text
echo 'execute function task("set sql tracing on", 50000,"4k","high","global")'|dbaccess sysadmin
```
停止收集 sql 语句信息：  
```text
echo 'execute function task("SET SQL TRACING OFF")' |dbaccess sysadmin
```

-----

## 查看顺序扫描和锁等待多的表  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
如何查看数据库中哪些表的顺序扫描最多，锁等待最多？  
**解决方法：**  
通过 sysmaster 库中的 sysptprof 表可以定位。  
```text
-- SQLMODE=gbase
SELECT p.dbsname,p.tabname,p.seqscans,p.lockwts
FROM sysmaster:sysptprof p
ORDER BY 3 desc;
```

-----

## 需要调整 NLSCASE SENSITIVITY  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
在创建数据库的时候设置了 NLSCASE SENSITIVITY，然后如何调整？  
**解决方法：**  
需要重建数据库。  
1、dbexport 导出；  
2、dbimport 导入。  
**注释：**  
1、默认情况下，GBase 8s 创建的数据库是大小写敏感的，排序取决于 locale 环境变量，默认为美式英语区域（US English locale），小写字母升序排列在大写字母之前，如：  
```text
CREATE DATABASE stores IN dbsp1 WITH LOG;
```
也可以显式指定数据库创建为大小写敏感，如：  
```text
CREATE DATABASE stores IN dbsp1 WITH LOG NLSCASE SENSITIVE;
```
以上对大小写敏感显式指定和不指定的语句效果相同，对字符类型的 CHAR、LVARCHAR、VARCHAR、NCHAR 、NVARCHAR，均视为区分大小写的。  
2、创建 NLSCASE 不敏感的数据库：  
```text
CREATE DATABASE stores IN dbsp2 WITH BUFFERED LOG NLSCASE INSENSITIVE;
```
该库将所有其他内置字符数据类型（CHAR、LVARCHAR、VARCHAR、VARCHAR2）视为区分大小写，对 NCHAR、NVARCHAR和NVARCHAR2 数据类型的字符串不区分大小写。在NCHAR、NVARCHAR和NVARCHAR2值的所有操作中，例如，排序、分组或标识重复行，数据库服务器忽略任何字母情况变量，并将字符串 "Mi" 和 "mI" 视为相同的值，数据库服务器将内置字符串操作函数和字符串运算符的结果也会转换为NCHAR、NVARCHAR和NVARCHAR2 数据类型的上下文。NLSCASE INSENSITIVE 与 Case-sensitive 数据库 connect 会报错；但可以与系统数据库 sysmaster 等进行 connect；onload 和 onunload 工具不支持 insensitive 数据库。  

-----

## 插入数据到表中报错 no free disk  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
业务报插入数据到表中错误：  
Could not insert new row into the table.  
ISAM error: no free disk space  
**解决方法：**  
检查数据库空间，表所在的 dbspace 上仍有剩余空间；检查表，未达到各种上限（报的是无空间，仍需要检查表）。发现有 blob 字段，继续检查 smartblobspace 空间，发现显然有空间，但 MetaData 的 free 为 0。增加一个 chunk，并指定较大的 -Ms 空间，可以解决问题。  
**注释：**  
若要指定元数据区域的大小和位移，请在 onspaces 命令中指定 -Ms 和 -Mo 标志。如果不使用 -Ms 标志，数据库服务器使用 AVG_LO_SIZE 的值来估计要为元数据区域分配的空间量。
监视 sbspace 元数据区域、用户数据区域和保留区域中的空间的命令：  
`onstat -g smb c` 或者 `oncheck -pe` 或者 message log 中 FREE_RE and CHKADJUP 相关日志记录  

-----

## 设置 chunk 自动扩展的方法  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
如何设置 chunk 自动扩展？  
**解决方法：**  
使用数据库系统管理员用户，一般是 gbasedbt。在 sysadmin 库中执行：  
如：设置编号为 1 的 chunk 自动扩展：  
```text
execute function task('modify chunk extendable on',1);
```
如：在设置了可以扩展之后，可指定 chunk 扩展增加 2000000KB：  
```text
execute function task('modify chunk extend',1,2000000);
```

-----

## 重建 sysmaster 库的方法  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
如何重建 sysmaster 库？  
**解决方法：**  
重建 sysmaster 库的主要原因是：系统表损坏。删除 sysmaster 库，需要使用数据库系统管理员用户，一般是 gbasedbt。  
为了保证删除顺利，最好在单用户模式下，以便保证没有其他用户连到 sysmaster 库。并且保证 sysadmin 系统库没有被使用。执行如下命令：  
```text
cd $GBASEDBTDIR/etc/sysadmin
dbaccess sysadmin db_uninstall.sql
onmode -j

dbaccess - <<!
database sysmaster;
delete from systables where tabid > (select tabid from systables where tabname = ' VERSION');
close database;
drop database sysmaster;
!
```
重启数据库，系统将自动重建 sysmaster 库。  

-----

## 设置 bufferpool 参数后报 operation system error  
数据库版本：ALL  
操作系统：ALL  
硬件平台：龙芯  
**描述：**  
数据库设置中设置 16K 的 bufferpool 个数为 250000 时，命令 onstat – 报错：操作系统错误，无法附加到共享内存。  
报错同时使用 dbaccess 命令登录数据库正常，能查询系统表。日志没有报错信息。  
英文描述如下：  
12:18:16 shmat: [22]: operating system error
12:18:16 client could not attach sever share memory segment,use IFX_XFER_SHMBASE. 
 onstat: Cannot attach to shared memory. errorno = 22  
**解决方法：**  
把 ONCONFIG 参数 SHMBASE 的 6 个 0 改为 7 个 0，重启数据库。  

-----

## online.log 出现 errno = 43 导致宕机  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
online.log 出现 errno = 43 导致宕机如何处理，如：  
14:45:01 Assert Failed: semop: errno = 43  
**解决方法：**  
增大系统信号量内核参数后启动数据库。  
如：修改 /etc/sysctl.conf 以下信号量参数：  
```text
kernel.sem = 32000 1024000000 32000 32000  
```
sysctl –p 生效  

-----

## server 端开启 sqlidebug 跟踪 server 执行 SQL  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
如何在 server 端开启 sqlidebug 跟踪 server 执行 SQL 的过程？  
**解决方法：**  
增加 vp：`onmode -p +1 sqli_dbg`
每个 session 在 $GBASEDBTDIR/tmp 下生成一个 sqli.sessionid 的文件  
解析 debug 文件：`sqliprint -o trace.out sqli.30`  
注：sqliprint需要安装csdk。  

-----

## last committed read 报 -246 错误  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
测试 last committed read 隔离时遇到了 -246 错误。  
**解决方法：**  
数据库默认的锁的级别是 page， 在 last committed read 隔离级别下，需要将表的锁级别修改为行锁，`alter table test_lock lock mode(row);`  

-----

## 数据文件的换行符导致加载失败  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
在 Windows 平台中产生的文本文件上传到 Linux 后，文本中的换行符会变成 ^M （cat -v 可以查看），导致数据不能通过 load、dbload 等工具导入数据库。该如何调整？  
**解决方法：**  
通过`tr -s "\r" "\n" <a.txt >a1.txt` 将 a.txt 中的 ^M 符号去掉后定向到 a1.txt 中。  
也可通过 `dos2unix a.txt > a1.txt` 方式。  

-----

## 外部表导入数据时提示 Conversion 错误  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
导入数据时提示 conversion 错误，界面如下：  
26168: Conversion err: (file, offset, reason, col)=(ucts_data.unl, 1, UNSUPPORTED_ROW_SIZE. <none>).  
Error in line 1  
Near character position 52  
**解决方法：**  
根据导入数据时错误提示，判断为文件字符集问题。经过研究得到两种解决方案：  
修改 gbasedbt 环境变量的字符集，和文件的保持一致。麻烦一点，而且影响已存在的数据库。  
注：修改 gbasedbt 配置文件 .bash_profile 文件  
```text
export LANG=zh_CN.UTF-8
export DB_LOCALE=zh_CN.utf8
export CLIENT_LOCALE=zh_CN.utf8
```
修改文件的编码方式为 ANSI 格式，这样更简单而且对数据库的其他数据无影响。  
注：Linux 中修改文件编码方式  
比如将一个 UTF-8 编码的文件转换成 GBK 编码  
```text
iconv -f GBK -t UTF-8 file1 -o file2
iconv -f GBK -t UTF-8 -o file
```

-----

## 数据库备份恢复出错  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
在数据库备份恢复功能测试中，配置逻辑日志自动备份后，备份目录下没有逻辑日志文件或无反应或者恢复时出现问题。  
**解决方法：**  
在验证逻辑日志自动备份是否成功时需要切换逻辑日志和检查点（onmode -l，onmode -c），并且最重要的是要记得重启数据库使配置文件生效，这点是必须的，否则之后会报错，不容易排查，在错误日志中不显示。

-----

## load 导入数据报错空间已经用完  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
在数据导入导出性能测试中，用 load 命令将大量的数据从文件中导入所建立的表中，导入过程中出现问题，显示空间已经用完。  
**解决方法：**  
创建额外的逻辑日志表空间（`onspaces -c -d llogdbs`）并对表空间进行逻辑日志的创建分
割（`onparams -a -d llogdbs`）。  

-----

## 通过 dbschema 无法获取 aqt 开头的表名  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
aqt 开头表名通过 dbschema 无法获取，如何处理？  
**解决方法：**  
`export AQT=1` 来避免系统将其当做关键字。
注释：AQT 是加速查询表的英文缩写，是 IWA 功能使用的中间表的标识，该方法对系统其他关键字无效，是 gbasedbt 刻意要求。  

-----

## 修改数据库字符集  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
当前数据库字符集为 utf8；如何修改为 GB18030-2000？  
**解决方法：**  
需要重建数据库。  
1、设置 DB_LOCALE=zh_CN.utf8; CLIENT_LOCALE=zh_CN.GB18030-2000;  
2、dbexport 导出；  
3、设置 DB_LOCALE=zh_CN.GB18030-2000; CLIENT_LOCALE=zh_CN.GB18030-2000;  
4、dbimport 导入。  

-----

## 查询 ph_run 结果报错 -23197  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
自定义 TASK 执行后，查询 ph_run，执行结果 run_retcode 报 -23197 错误。  
**解决方法：**  
-23197 错误的函数是字符集错误。  
原因是业务库的的字符集与 sysadmin 库的默认字符集 en_US.819 不匹配，在 sysadmin 库中创建不在 sysadmin 库中执行的 TASK 时，应在 tk_dbs 中指定具体的业务库名称（默认的 tk_dbs 为 sysadmin)，使 TASK 可以在业务库的 DB_LOCALE 环境下来执行。  

-----

## ontape 修改数据库日志模式报错  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
ontape 修改数据库日志模式报错：  
178:isam error: database is locked;  
pending change to logging mode  
**解决方法：**  
ondblog cancel testdb  
重新修改日志模式。  

-----

## 数据库无日志模式切换日志模式  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
如何将数据库无日志模式切换成带日志模式？  
**解决方法：**  
1、使用ondblog命令：`ondblog unbuf dbname`，之后做个虚假备份`onbar -b -F`   
2、使用ontape命令：`ontape -s -U dbname`  

-----

## 日志切换报 178 错误  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
日志切换后，报错 178: ISAM error: Database is locked; pending change to logging mode. 如何解决？  
**解决方法：**  
可以使用 finderr 178 命令查看报错原因：  
数据库从无日志向缓冲式日志模式转换的时候，需要做一次零级备份。  

-----

## 执行 SQL 报错“事务不可用”  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
在标准 SQL 能力的功能测试中，第 12、13 项（Truncate.sql 和 CommitRollback.sql）测试有问题，显示 transaction not available，即事务不能被获得。  
**解决方法：**  
因为建立数据库的时候默认无日志模式，所以会显现这样的错误信息。应该建立或添加日志模式。  

-----

## 服务器断电重启后数据库启动失败  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
服务器异常断电重启后，数据库启动失败，检查日志报：  
Warning：stat() failed for chunk file /data/dbs/rootdbs  
Cannot Open Primary Chunk '/data/dbs/rootdbs', errno = 2  
**解决方法：**  
原因比较明确，errno 为 2 表示无法读取 rootdbs，需要在操作系统层面上确认 rootdbs 所属的文件已经存在或者设备正常连接，且权限正确（660）。独立的目录，很有可能是磁盘阵列未能正确挂载。  

-----

## Windows CSDK 中使用 dbaccess  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
如何在 Windows CSDK 中使用 dbaccess？  
**解决方法：**  
1、配置 CSDK 中 Setnet32，调通 ConnectTest Demo；  
2、在系统环境变量中设置以下环境变量：  
我的电脑-->高级-->环境变量-->新建环境变量  
GBASEDBTDIR=CSDK 的安装目录  
GBASEDBTSERVER=实例名  
GBASEDBTSQLHOSTS=sqlhosts 文件路径和名字  
（拷贝 server 的 sqlhosts 文件到 Windows 下 CSDK 目录下）  
3、cmd 打开 Windows 命令行界面  
1）、dbaccess  
菜单界面 connect 实例  
2）、dbaccess - -  
> connect to '@gbaseserver' user gbasedbt;  
ENTER PASSWORE: gbasedbt  
Connected.  
>  
**注释：**  
Windows 下 dbaccess - - 连接进去时用户不是 gbasedbt，必须执行 connect to 指定用户名和密码才可以正常执行 SQL。  

-----

## 实例不能启动问题  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
实例不能启动问题。  
**解决方法：**  
1、首先检查环境变量中 GBASEDBTDIR、ONCONFIG、GBASEDBTSERVER 是否配置正确。  
2、检查 rootchunk 的属性是否是正常。  
3、检查 sqlhosts 文件通讯是否正常。  

-----

## 数据库重复初始化报错  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
数据库初始化失败，日志信息提示如下：  
```text
Initializing ASF...succeeded
Initializing Dictionary Cache and SPL Routine Cache...succeeded
Bringing up ADM VP...succeeded
Creating VP classes...succeeded
Forking main_loop thread...succeeded
Initializing DR structures...succeeded
Forking 1 'soctcp' listener threads...succeeded
Forking 1 'ipcstr' listener threads...succeeded
Starting tracing...succeeded
Initializing 32 flushers...succeeded
oninit: Fatal error in shared memory initialization

WARNING: server initialization failed or timed out.
Check the message log, online.log, for errors.
```
运行日志online.log中：  
```text
09/30/25 10:27:36  GBase Database Server Version 12.10.FC4G1AEE Software Serial Number AAA#B000000
09/30/25 10:27:36  DISK INITIALIZATION ABORTED: potential instance overwrite detected.
To disable this check, set FULL_DISK_INIT to 1 in your config file and retry.

09/30/25 10:27:36  oninit: Fatal error in shared memory initialization

09/30/25 10:27:36  GBase Database Server Stopped.

10:27:36  mt_shm_remove: WARNING: may not have removed all/correct segments
```
**解决方法：**  
FULL_DISK_INIT 这个参数，对当前已经初始化的 dbspace 进行保护，若是需要初始化dbspace，需要更改这个参数为 1。  
**注释：**  
如果对数据库初始化，现有用户数据会丢失，需谨慎操作。  

-----

## 数据库状态有提示 BLOCKED：CKPT  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
使用 onstat - 命令状态显示为在线，但有 BLOCKED：CKPT 提示  
**解决方法：**  
使用 `onstat -l` 命令查看逻辑日志空间。如果绝大部分空间已被占用，则是由于逻辑日志写满所致，可以使用 `ontape -a` 备份日志即可解决。  
如果不需要逻辑日志备份，可将逻辑日志备份到空`onmode -wf LTAPEDEEV=/dev/null`  

-----

## 启动停止 GBase 8s 自动任务的方法  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
如何启动停止 GBase 8s 自动任务？  
**解决方法：**  
1、启动 schedure：  
```text
DATABASE sysadmin;
EXECUTE FUNCTION task('scheduler start');  
```
2、停止 schedure：  
```text
DATABASE sysadmin;  
EXECUTE FUNCTION task('scheduler stop');  
```
3、永久停止 schedure：  
```text
touch $GBASEDBTDIR/etc/sysadmin/stop  
```

-----

## 数据库静默安装  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
数据库静默安装  
**解决方法：**  
普通方式安装数据库一次，并录制模板文件，然后再次安装，可以根据模板进行静默安装。  
1、录制模板：手动安装 ids，目的录制模板文件。 命令：`./ids_install –r /home/gbasedbt/bundle.properties`  
2、静默安装：`./ids_install –i silent –f /home/gbasedbt/bundle.properties`  

-----

## 如何查找用时最长 SQL 并进行调优  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
如何查找用时最长 SQL 并进行调优？  
**解决方法：**  
打开 sqltracing：  
```text
EXECUTE FUNCTION task('SET SQL TRACING ON');
```
关闭 sqltracing：  
```text
EXECUTE FUNCTION task(’ SET SQL TRACING OFF');
```
对指定数据库进行跟踪：  
```text
EXECUTE FUNCTION task('SET SQL TRACING DATABASE ADD','库名');
```
找到"实际运行时间"最长的 SQL 语句，并进行调优。  
打开 SQL tracing，过一段时间后执行如下 SQL 语句：  
```text
-- SQLMODE=gbase
select first 20 sql_id 
from sysmaster:syssqltrace
where sql_runtime > 0
order by sql_runtime desc;
```
使用上面的 SQL 语句得到一些 sql_id 后，再通过下面的 SQL 语句得到这些 sql_id 对应的 SQL 语句的信息（将下面 SQL 语句中的 my_sql_id 替换成这些 sql_id）：  
```text
-- SQLMODE=gbase
SELECT sql_sid, sql_uid,
dbinfo('UTC_TO_DATETIME',sql_finishtime) as finishtime,
TRUNC(sql_runtime,7) || ' Sec' AS sql_runtime,
sql_actualrows, sql_statement, sql_database
FROM sysmaster:syssqltrace 
WHERE sql_id = my_sql_id
```

-----

## 刷脏页效率的检查和提升方式  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
刷脏页的效率可以通过什么方式检查和提升？  
**解决方法：**  
1、检查存储的读写性能：（混合读写不要使用 dd，使用如下命令）  
```text
fio -filename=/dev/sdb1 -direct=1 -iodepth 1 -thread -rw=randrw \
  -rwmixread=70 -ioengine=psync -bs=16k -size=2G -numjobs=10 \
  -runtime=60 -group_reporting -name=mytest -ioscheduler=noop
```
2、通过 onstat -g ckp 检查刷脏页性能。  
3、查找系统中写操作最多的表，并均匀分布到多个 dbspace 进行优化。    

-----

## 数据库 SQL 语句性能缓慢问题  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
数据库 SQL 语句性能缓慢问题。  
**解决方法：**  
对于 SQL 运行缓慢的问题，建议搜集下面信息：  
```text
onstat –u
onstat –g ses 0
onstat –k
```
可以查询 sysexplain 表找到 CPU COST 成本最高的几个 SQL，并且打印这些 SQL 的执行计划，在执行计划中查看是否有全表扫描，或者没有利用 index。增加 index 并且作字段级别的高级统计更新。  

-----

## 统计更新：所有表的首字段高优、整个表中优  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
生成数据库中所有表的首字段做高优、整个表做中优的 SQL 语句。  
**解决方法：**  
执行如下的 SQL，并执行该 SQL 语句：  
```text
-- SQLMODE=gbase
unload to upd.sql delimiter ''
select 'update statistics high for table '||trim(tabname)||"("||trim(a.colname)||");"
from syscolumns a,systables b,sysindexes c
where a.tabid=b.tabid 
and a.tabid=c.tabid
and b.tabid>(select tabid from systables where tabname = ' VERSION') 
and b.tabtype='T'
and a.colno=c.part1
union
select 'update statistics medium for table '||trim(tabname)||";"
from systables
where tabid>(select tabid from systables where tabname = ' VERSION') 
and tabtype='T';
```

-----

## 客户端连接数据库报错  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
客户端连接数据库报错：  
-23103 Code-set conversion function failed due to an illegal sequence or invalid value  
**解决方法：**  
可能的原因：  
1、数据库驱动或者客户端软件目录有中文。  
2、数据库启动环境变量与数据库访问环境变量不一致（onstat -g env 可以查看），修正后重启。  

-----

## 参数 DELIMIDENT=y 可以解决的问题  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
参数 DELIMIDENT=y 可以解决哪些问题？  
**解决方法：**  
1、Utf8 下中文字段名问题，中文字段名加双引号，使用该参数可以正常运行；  
2、datastudio 导出的 SQL 中 units 之类被识别为关键字会加双引号包围，该参数可以正常运行这样的带双引号的 SQL；  
3、该参数可以加在 JDBC 连接串中。  
4、特定版中delimident 参数控制大小写系统行为简单总结如下：  
- server 端： caseshift=y（默认值） JDBC： delimident=y caseshift 不设置； 输出（查询显示）全大写。  
- server 端： caseshift=n JDBC： delimident=y caseshift=n ； 输出（查询显示）大小写敏感。  
- server 端： caseshift=y（默认值） JDBC： delimident=y caseshift=n； 输出（查询显示）全小写。  


-----

## 如何修改 GBase 8s JDBC 默认时间格式  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
如何修改 GBase 8s JDBC 默认时间格式？  
**解决方法：**  
1、在 URL 中增加 GL_DATE 参数，形如：GL_DATE=%d%m%Y。  
2、在获取日期类型数据时通过 getString 方法，使其自动进行 to_char 格式转化。  

-----

## SSC集群主节点故障哪个节点接管为主节点  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
SSC集群主节点故障哪个节点接管为主节点  
**解决方法：**  
集群中最先加入集群的节点接管为主节点。  

-----

## 高可用集群搭建完成后辅节点连接失败  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
搭建高可用集群时，互信配置完成。集群搭建完成后，辅节点连接不上主节点。  
**解决方法：**  
这种情况产生的原因大多是互信出现问题。解决方法是检查互信的配置是否正常。也可能是防火墙没有关闭造成的，查看一下防火墙是否关闭。  

-----

## 主辅节点的 CM 无法互相访问题  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
主辅节点的 CM 无法互相访问题  
**解决方法：**  
防火墙处于关闭状态，排除防火墙解决方法，查看 /etc/hosts 文件，将 localhost.localdomain 改成了主机名，改回 localhost.localdomain 就可以了。  

-----

## 安装HAC集群问题  
数据库版本：ALL  
操作系统：ALL  
**描述：**  
onmode -d 操作集群状态不改变或者onspaces 添加存储备机无法同步的问题  
**解决方法：**  
关闭DNS。  
解决步骤：  
1、检查DNS  
```text
cat /etc/resolv.conf
```
2、注释掉ifcfg-sbond文件下的 DNS信息  
```text
vi /etc/sysconfig/network-scripts/ifcfg-sbond
```
3、重启一下network  
```text
systemctl restart network
```
4、再次查看 /etc/resolv.conf没有DNS信息  
```text
cat /etc/resolv.conf
```
