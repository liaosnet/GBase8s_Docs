# 数据空间操作  
本章节将介绍GBase 8s数据库中数据空间相关的基本语法和示例。  
数据空间是数据库的逻辑存储结构，所有数据库对象均存储于指定的数据空间内。  

## 创建数据空间  
创建数据空间有两种方式，使用SQL管理API方式和管理命令onspaces方式  

- 使用gbasedbt用户，在sysadmin中执行CREATE DBSPACE语句创建数据空间：  

```text  
EXECUTE FUNCTION task('create dbspace','datadbs02','/data/gbase/datachk02','1024000','0','16');
或者
EXECUTE FUNCTION admin('create dbspace','datadbs02','/data/gbase/datachk02','1024000','0','16');
```

参数说明：创建dbspace，空间名称，空间使用的文件路径，大小（KB)，偏移量大小，使用的页大小（Linux下默认2KB，最大16KB，使用2KB的倍数)

对应的管理命令方式

- 使用gbasedbt用户，创建数据空间使用的文件，创建数据空间  

```text  
[gbasedbt@node2 ~]$ touch /data/gbase/datachk03

[gbasedbt@node2 ~]$ chmod 660 /data/gbase/datachk03

[gbasedbt@node2 ~]$ onspaces -c -d datadbs03 -p /data/gbase/datachk03 -o 0 -s 1024000 -k 16
```

参数说明：-c 创建，-d 空间名称，-p 空间使用的文件路径，-o 偏移量大小，-s 大小（KB），-k 页大小

## 查看数据空间  
查数据空间有两种方式，使用SQL方式和管理命令onstat 方式  

- 使用gbasedbt用户，执行SQL语句查询：  

```sql  
SELECT d.dbsnum,trim(d.name) name,d.pagesize, format_units(sum(c.chksize),'P') dbs_size
FROM sysmaster:sysdbspaces d, sysmaster:syschunks c
WHERE d.dbsnum = c.dbsnum
GROUP BY 1,2,3
ORDER BY 1;
```

输出示例  
```text  
|dbsnum |name      |pagesize |dbs_size |
|-------|----------|---------|---------|
|1      |rootdbs   |2048     |0.98 GB  |
|2      |plogdbs   |2048     |0.98 GB  |
|3      |llogdbs   |2048     |0.98 GB  |
|4      |sbspace01 |2048     |0.98 GB  |
|5      |tempdbs01 |16384    |0.98 GB  |
|6      |datadbs01 |16384    |0.98 GB  |
|7      |datadbs02 |16384    |0.98 GB  |
|8      |datadbs03 |16384    |0.98 GB  |
```

对应的管理命令方式  

- 使用gbasedbt用户，执行onstat -d 命令  

```text  
On-Line -- Up 02:52:15 -- 3378128 Kbytes

Dbspaces
address          number   flags      fchunk   nchunks  pgsize   flags    owner    name
4ddf8028         1        0x70001    1        1        2048     N  BA    gbasedbt rootdbs
50626dc8         2        0x70001    2        1        2048     N  BA    gbasedbt plogdbs
50749028         3        0x60001    3        1        2048     N  BA    gbasedbt llogdbs
50749258         4        0x68001    4        1        2048     N SBA    gbasedbt sbspace01
50749488         5        0x42001    5        1        16384    N TBA    gbasedbt tempdbs01
507496b8         6        0x60001    6        1        16384    N  BA    gbasedbt datadbs01
512af880         7        0x60001    7        1        16384    N  BA    gbasedbt datadbs02
50c5ad58         8        0x60001    8        1        16384    N  BA    gbasedbt datadbs03
 8 active, 2047 maximum

Chunks
address          chunk/dbs     offset     size       free       bpages     flags pathname
4ddf8258         1      1      0          512000     495437                PO-B-- /data/gbase/rootchk
5074a028         2      2      0          512000     11947                 PO-B-- /data/gbase/plogchk
5074b028         3      3      0          512000     11947                 PO-B-- /data/gbase/llogchk
5074c028         4      4      0          512000     477465     477465     POSB-- /data/gbase/sbspace01
                                 Metadata 34482      25659      34482
5074d028         5      5      0          64000      63947                 PO-B-- /data/gbase/tempchk01
50753028         6      6      0          64000      62829                 PO-BE- /data/gbase/datachk01
50c5a028         7      7      0          64000      63947                 PO-B-- /data/gbase/datachk02
512ad028         8      8      0          64000      63947                 PO-B-- /data/gbase/datachk03
 8 active, 32766 maximum

NOTE: The values in the "size" and "free" columns for DBspace chunks are
      displayed in terms of "pgsize" of the DBspace to which they belong.


Expanded chunk capacity mode: always
```

## 修改数据空间  
修改数据空间大小仅支持SQL管理API方式，仅能增大空间大小，而不能减小。  
使用gbasedbt用户，在sysadmin库中执行修改  
```sql  
-- 设置chunk序号为8的数据文件可扩展
EXECUTE FUNCTION task('modify chunk extendable on', 8);

-- 设置扩展chunk序号为8的数据文件扩展大小为512000KB
EXECUTE FUNCTION task('modify chunk extend', 8, 512000);
```

通过增加数据文件的方式进行扩展有两种方式，使用SQL管理API方式和管理命令onspaces方式

- 使用gbasedbt用户，在sysadmin中执行add chunk语句增加数据空间：  

```sql  
EXECUTE FUNCTION task('add chunk','datadbs03','/data/gbase/datachk03_2','512000','0');
```

参数说明：增加chunk，空间名称，空间使用的文件路径，大小（KB)，偏移量大小

对应的管理命令方式

- 使用gbasedbt用户，创建数据空间使用的文件，增加数据空间  

```text  
[gbasedbt@node2 ~]$ touch /data/gbase/datachk03_3

[gbasedbt@node2 ~]$ chmod 660 /data/gbase/datachk03_3

[gbasedbt@node2 ~]$ onspaces -a datadbs03 -p /data/gbase/datachk03_3 -o 0 -s 512000
```

参数说明：-a 增加chunk，-d 空间名称，-p 空间使用的文件路径，-o 偏移量大小，-s 大小（KB）

## 删除数据空间  
删除数据空间有两种方式，使用SQL管理API方式和管理命令onspaces方式  

- 使用gbasedbt用户，在sysadmin中执行drop chunk语句删除数据空间：  

```sql  
-- 从数据空间中删除chunk
EXECUTE FUNCTION task('drop chunk','datadbs03','/data/gbase/datachk03_3','0');

-- 删除数据空间
EXECUTE FUNCTION task('drop dbspace','datadbs02');
```

参数说明：删除chunk，空间名称，空间使用的文件路径，大小（KB)，偏移量大小；  
删除数据空间，空间名称；  
注：chunk或者数据空间中无数据，才允许被删除；空间删除，对应的操作系统并不会同时删除。  

对应的管理命令方式

- 使用gbasedbt用户，从数据空间中删除chunk，删除数据空间  

```text  
[gbasedbt@node2 ~]$ onspaces -d datadbs03 -p /data/gbase/datachk03_2 -o 0 -y

[gbasedbt@node2 ~]$ onspaces -d datadbs03 -y
```

参数说明：-d 删除空间/chunk，-p 空间使用的文件路径，-o 偏移量大小，-y 确认删除
