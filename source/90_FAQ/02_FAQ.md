# GBase 8s FAQ  
问题知识库  

## 自定义TASK执行后，查询ph_run，执行结果run_retcode报-23197错误  
数据库版本：ALL  
操作系统：ALL  
硬件平台：ALL  
**描述：**  
自定义TASK执行后，查询ph_run，执行结果run_retcode报-23197错误  
**解决方法：**  
-23197错误的函数是字符集错误。  
原因是业务库的的字符集与sysadmin库的默认字符集en_US.819不匹配，在sysadmin库中创建不在sysadmin库中执行的TASK时，应在tk_dbs中指定具体的业务库名称（默认的tk_dbs为sysadmin)，使TASK可以业务库的DB_LOCALE环境来执行。  

-----  

## 使用GBase MTK迁移数据后，使用ResultSetMetaData查询报java.sql.SQLException: Encoding or code set not supported.错误    
数据库版本：ALL  
操作系统：ALL  
硬件平台：ALL  
**描述：**  
使用GBase MTK迁移数据后，使用ResultSetMetaData查询报java.sql.SQLException: Encoding or code set not supported.错误  
**解决方法：**  
原因是迁移的字段是lvarchar(20),DB_LOCALE使用的是utf8。此环境下每3个字节表示一个汉字，当这个表里有7个汉字时，第7个汉字只有三分之二迁移到了数据库中，使用ResultSetMetaData查询将会报错。  
使用GB18030字符集代替，或者增大字段大小。使用IFX_USE_STRENC=true参数可避免报错。  

-----  

## Cannot Open Primary Chunk  
数据库版本：ALL  
操作系统：ALL  
硬件平台：ALL  
**描述：**  
服务器异常断电重启后，数据库启动失败，检查日志报：  
Warning：stat() failed for chunk file /data/dbs/rootdbs  
Cannot Open Primary Chunk '/data/dbs/rootdbs', errno = 2  
**解决方法：**  
原因比较明确，errno为2表示无法读取rootdbs，需要在操作系统层面上确认rootdbs所属的文件已经存在或者设备正常连接，且权限正确(660)。独立的目录，很有可能是磁盘阵列未能正确挂载。  

-----  

## no free disk space  
数据库版本：ALL  
操作系统：ALL  
硬件平台：ALL  
**描述：**  
业务报插入数据到表中错误：  
Could net insert new row into the table.  
ISAM error: no free disk space  
**解决方法：**  
检查数据库空间，表所在的dbspace上仍有剩余空间；检查表，未达到各种上限（报的是无空间，仍需要检查表）。发现有blob字段，继续检查smartblobspace空间，发现显然有空间，但MetaData的free为0。增加一个chunk，并指定较大的-Ms空间，问题解决。  

-----  

## 创建表报错误261: Cannot create file for table table-name.  
数据库版本：ALL  
操作系统：ALL  
硬件平台：ALL  
**描述：**  
创建表时第265行报261错误及102ISAM错误，该错误的原因是不能为表创建文件。  
**解决方法：**  
创建的表的语句如下：  
```text
create table tab1 (
  col1 varchar(40),
  col2 varchar(40),
  ...中间省略一些行...
  col263 date
);
```
从表结构上看，该表拥有大量的varchar/lvarchar类型的字段（大约240个），在当前的datadbs01（页大小为2KB)下创建失败，报上述错误。  
在16KB页大小的其它dbspace上创建该表能成功，通过oncheck -pt 打印该表的信息，显示如下：  
```text
[gbasedbt@instance-ihbhwu9m ~]$ oncheck -pt myttdb:tab1

TBLspace Report for myttdb:gbasedbt.tab1

    Physical Address               7:2256
    Creation date                  07/02/2020 16:49:05
    TBLspace Flags                 902        Row Locking
                                              TBLspace contains VARCHARS
                                              TBLspace use 4 bit bit-maps
    Maximum row size               17550     
    Number of special columns      244  
```
特别注意到： Number of special columns 244 （特殊字段有244个）  
继续通过oncheck -pP 打印该表的partition page页信息，显示如下：  
```text
[gbasedbt@instance-ihbhwu9m ~]$ oncheck -pP 7 2256
addr             stamp    chksum nslots flag type         frptr frcnt next     prev
7:2256           287175   6914   5      802  PARTN        2162  14198 0        0       
        slot ptr   len   flg
        1    24    136   0  
        2    160   40    0  
        3    200   1952  0  
        4    2152  0     0  
        5    2152  10    0 
```
特别注意到：frptr显示已经使用2162字节的空间。  
这时问题可以明确了：在2KB页的空间里创建该表，partition page至少需要2162字节的空间，但2KB的大小只有2048，故无法创建该表。  

至于为什么会需要这么多空间？  
partition page的slot 3中需要8个字节来描述varchar/lvarchar/nvarchar等这样特殊字段。  

-----  

## 创建存储过程报错误282: Found a quote for which there is no matching quote.  
数据库版本：ALL  
操作系统：ALL  
硬件平台：ALL  
**描述：**  
创建存储过程时第4行报282错误，该错误的原是说引号不匹配。  
**解决方法：**  
创建的存储过程语句如下：  
```text
drop procedure if exists proc1;
create procedure proc1(out p_cursor sys_refcursor)
  define v_sqlstr lvarchar(1024);
  let v_sqlstr = "select tabid,tabname 
                  from systables
                  where tabid > 99
                    and tabtype = 'T'";
  open p_cursor for v_sqlstr;
end procedure;
```
从let 语句上看，只有简单的双引号、单引号，且存在一一对应关系，不应存在引号不匹配的情况。  
考虑到引号内存在换行，那么可能的原因就是数据库没有开启ALLOW_NEWLINE。  
在没有开启ALLOW_NEWLINE的情况下，引号内的内容不允许换行。即：语句需要改为  
```text
  -- 单行
  let v_sqlstr = "select tabid,tabname from systables where tabid > 99 and tabtype = 'T'";
  -- 或者
  let v_sqlstr = "select tabid,tabname " || 
                 "from systables " ||
                 "where tabid > 99 " ||
                 "  and tabtype = 'T'";
```
为避免出现字符串换行出现的此类问题，可以在ONCONFIG配置文件中开启ALLOW_NEWLINE（默认为0，不开启），设置为1为开启允许换行  
`ALLOW_NEWLINE 1`  
如果临时仅仅是当前会话允许使用换行，那么可以先执行过程`ifx_allow_newline('f')`  
```text
execute procedure ifx_allow_newline('t');
```
然后，该会话在关闭前或者修改allow_newline参数前，将允许字符串换行。  

-----  

## 删除表记录时，报“692: Key value for constraint ( 主键约束名称 ) is still being referenced.”  
数据库版本：ALL  
操作系统：ALL  
硬件平台：ALL  
**描述：**  
删除表记录时，报“692: Key value for constraint ( 主键约束名称 ) is still being referenced.”  
**解决方法：**  
1，报错信息明显的提示，删除的记录被外键引用了，故不能删除；  
2，如果需要删除该记录，应当先删除外键所在表的该值所有记录，以下语句可获取外键参考所在的表的名称：  
```text
select t.tabname 
from sysconstraints c, systables t, sysreferences r
where c.tabid = t.tabid 
and   c.constrid = r.constrid
and   c.constrtype = 'R'
and   r.ptabid = (select tabid from systables where tabname = '主键表名');
```
3，使用外键时，我们有时还会用到 级联删除（ON DELETE CASCADE） 功能，使用该功能：删除主表记录时，外键参考表相应的记录均删除。示例：  
```text
create table dept (
  dept_id serial, 
  dept_name varchar(60) not null, 
  manager_id int, 
  primary key(dept_id) constraint pk_dept_dept_id
);

create table emp (
  emp_id serial, 
  dept_id int, 
  foreign key (dept_id) references dept(dept_id) on delete cascade constraint fk_emp_dept_id
);
```

-----  

## 基于java的环境中，使用byte字段类型时，服务器上会产生IfxTmpFile_xxxxxxxxxxxxxx的文件。  
数据库版本：ALL  
操作系统：ALL  
硬件平台：ALL  
**描述：**  
基于java的环境中，使用byte字段类型时，服务器上会产生IfxTmpFile_xxxxxxxxxxxxxx的文件。  
**解决方法：**  
该问题产生的原因是受到了JDBC的环境变量参数LOBCACHE的影响（如果未指定，使用缺省默认值4096）。  
LOBCACHE参数确定从数据库服务器访存的大对象数据的缓冲区大小。大于 0 的数值时：  
在内存中分配来保存数据的最大字节数。如果数据大小超过 LOBCACHE 值，则将数据存储在临时文件中；如果在创建此文件期间发生安全违规，则将数据存储在内存中；为零时：始终将数据存储在文件中。如果发生安全违规，则驱动程序不尝试在内存中存储数据。为负数时：始终将数据存储在内存中。如果得不到所需的内存量，则发生错误。  
根据实际需要调整该参数即可。  

-----  

## 使用nvl2或者decode或者case时，报“800: Corresponding data types must be compatible in CASE expression or DECODE function.”错误。  
数据库版本：3.5.x之前  
操作系统：ALL  
硬件平台：ALL  
**描述：**  
使用nvl2或者decode或者case时，报“800: Corresponding data types must be compatible in CASE expression or DECODE function.”错误。  
**解决方法：**  
800错误表示case或者decode的各个条件返回值需要一致或者是兼容的。
如下，col2为datetime year to second类型，两个条件的返回值：col2 + 1为datetime year to second，而to_date的返回值的类型是datetime year to fraction(5)。系统严格的认为两个并不一致，故而报800错误。  
```text
nvl2(col2, col1 + 1, to_date('2020-05-26 00:00:00','yyyy-mm-dd hh24:mi:ss'))
```
需将某改为一致：  
```text
nvl2(col2, 
to_date(to_char(col2 + 1,'yyyy-mm-dd hh24:mi:ss'),'yyyy-mm-dd hh24:mi:ss'), 
to_date('2020-05-26 00:00:00','yyyy-mm-dd hh24:mi:ss'))
-- 或者使用强制转换
nvl2(col2, 
col1 + 1, 
to_date('2020-05-26 00:00:00','yyyy-mm-dd hh24:mi:ss')::datetime year to second)
-- 注： '::'表示转换后的类型
```

-----  

## insert into … select skip … first 报-201语法错误  
数据库版本：ALL  
操作系统：ALL  
硬件平台：ALL  
**描述：**  
语句如下：  
```text
insert into t1 (col1)
select col1 from t2 order by col1 desc skip 0 first 5;
```
单独执行select能正常执行，但整个语句会报-201语法错误。  
**解决方法：**  
当前的数据库版本为了支持limit m,n语法，支持将skip m first n后置。但使用时还是尽量使用原始的写法。  
```text
insert into t1 (col1)
select skip 0 first 5 col1 from t2 order by col1 desc;
```
将skip紧接着select 关键字。  

-----  

## 执行ids_install安装时，报“The version file is not exist.”  
数据库版本：ALL  
操作系统：ALL  
硬件平台：ALL  
**描述：**  
执行ids_install安装时，报“The version file is not exist.”  
**解决方法：**  
操作系统确少必要的unzip工具，需要安装unzip。CentOS系统中可通过yum install unzip安装。  
如果安装目录下的隐藏文件 .gbase.properties 缺失，也会出现此问题。重新解压缩安装包后，再次安装。  

-----  

## 执行ids_install安装时，报“No Java virtual machine could be found from your PATH environment variable. You must install a VM prior to running this program.”  
数据库版本：ALL  
操作系统：ALL  
硬件平台：ALL  
**描述：**  
执行ids_install安装时，报“No Java virtual machine could be found from your PATH environment variable. You must install a VM prior to running this program.”  
**解决方法：**  
提示信息为无Java虚拟机，按照提示安装JRE/JDK。支持的JRE/JDK版本为1.6及以上，如CentOS自带的java-1.8.0-openjdk。  

-----  

## 执行ids_install安装时，报“The parent directory of the user install path is not exists, please choose another one.”    
数据库版本：ALL  
操作系统：ALL  
硬件平台：ALL  
**描述：**  
执行ids_install安装时，报“The parent directory of the user install path is not exists, please choose another one.”  
**解决方法：**  
提示信息为指定的目录上级目录不存在。默认的安装目录为：/opt/GBASE/gbase，如果/opt/GBASE目录不存在，则会报这个错误。需要在安装前创建/opt/GBASE目录。  

-----  

## 执行ids_install安装时，报“User install directory is not empty, please chooose another one.”  
数据库版本：ALL  
操作系统：ALL  
硬件平台：ALL  
**描述：**  
执行ids_install安装时，报“User install directory is not empty, please chooose another one.”  
**解决方法：**  
提示信息为指定的目录非空。安装数据库需要在空目录或者不存在的目录下（上级目录需存在，系统会自动创建目录），手工指定其它非空目录或者不存在目录（上级目录需存在，系统会自动创建目录）。  

-----  

## 执行数据库初始化或者启动数据库时，报分配内存失败  
数据库版本：ALL  
操作系统：ALL  
硬件平台：ALL  
**描述：**  
执行数据库初始化或者启动数据库时，报  
```text
Allocating and attaching to shared memory…FAILED
WARNING: server initialization failed or timed out.
Check the message log, online.log, for errors.
```
**解决方法：**  
出现问题，根据提示要求查看online.log，使用onstat -m命令可查看最近20行online.log日志信息。如果日志里包含类似以下信息：  
```text
19:03:42 shmget: [EEXIST][17]: key 52564801: shared memory already exists
19:03:42 mt_shm_init: can’t create resident segment，
```  
表示数据库的内存段已经被占用，可能的情况是：  
1，当前实例已经启动，即通过onstat -命令检查状态，如果已经是On-Line状态，即
`GBase Database Server Version 12.10.FC4G1AEE – On-Line – Up 00:07:02 – 208516 Kbytes`  
表示数据库不需要再初始化或者重新启动，保持现有状态即可。  
2，当前实例未启动，即通过onstat -命令检查状态，如果已经是未启动状态，即  
`shared memory not initialized for GBASEDBTSERVER 'ol_gbasedbt1210'`   
则表示之前的数据库关闭或者异常时，内存未能及时释放，执行onclean -ky命令强制清理内存，然后通过ipcs -m命令查看key中与报错信息中一致的0x52564801是否存在，如果不存在，可以重新启动数据库实例；如果存在，使用root用户执行`ipcrm -M 0x52564801`清理共享内存，同时清理0x525648XX 开头各个内存段，完成后可以重新启动数据库实例。  

-----  

## 执行数据库初始化或者启动数据库时，报打开主块失败  
数据库版本：ALL  
操作系统：ALL  
硬件平台：ALL  
**描述：**  
执行数据库初始化或者启动数据库时，报  
```text
Opening primary chunks…FAILED
oninit: Fatal error in shared memory initialization
WARNING: server initialization failed or timed out.
Check the message log, online.log, for errors. 
```
**解决方法：**  
出现问题，根据提示要求查看online.log，使用onstat -m命令可查看最近20行online.log日志信息。如果日志里包含类似以下信息：  
1，`19:07:08 The chunk '/opt/gbase/storage/rootdbs' must have READ/WRITE permissions for owner and group (660).`  
表示数据库使用的chunk对应的文件或者文件系统权限不对，按提示要求修改为属主及属组均为gbasbedbt，权限为660（即：`chown gbasedbt:gbasedbt /opt/gbase/storage/rootdbs` , `chmod 660 /opt/gbase/storage/rootdbs`），完成后重新启动数据库。  
2，`19:10:51 The chunk '/opt/gbase/storage/rootdbs' must have READ/WRITE permissions for owner (600).`  
数据库使用的chunk对应的文件或者文件系统权限应为属主及属组均为gbasbedbt，权限为660，这里提示需要600权限。说明oninit可执行文件的属主及权限不对，或者是非root用户安装的数据库。我们要求使用root用户来安装数据库。故在`$GBASEDBTDIR`目录下，使用root用户执行RUNasroot.installserver脚本以完成对所有已安装的文件的权限修正。同时修改chunk文件或者文件系统的属主及属组均为gbasbedbt，权限为660（即：`chown gbasedbt:gbasedbt /opt/gbase/storage/rootdbs` , `chmod 660 /opt/gbase/storage/rootdbs`），完成后重新初始化实例或者重启实例。  

-----  

## 连接数据库时，报 “908: Attempt to connect to database server (ol_gbasedbt1210) failed.”  
数据库版本：ALL  
操作系统：ALL  
硬件平台：ALL  
**描述：**  
连接数据库时，报 “908: Attempt to connect to database server (ol_gbasedbt1210) failed.” 
**解决方法：**  
根据提示信息，表示当前无法连接到指定的数据库。对于此问题，需要从最底层往上排查。  
首先，检查数据库的侦听是否正常，命令onstat -g ntt的输出结果中，thread name为soctcplst对应的address中应包括 主机名或IP地址|服务名称或者端口号|scotcp（如localhost.localdomain|ol_gbasedbt1210|soctcp），该信息来源地sqlhosts配置文件（建议在sqlhosts配置文件中指定IP地址及端口，而不是使用主机名或者服务名称）。如果不存在符合条件的soctcplst，则需要修改sqlhosts为正确配置，并重启数据库。如果存在soctcplst，但IP是本地loop地址（127.0.0.1），也需修改为实际物理IP，并重启数据库。  
如果侦听正常，则继续检查操作系统防火墙设置，请关闭防火墙或者放通数据库使用的端口。  

-----  

## 执行ids_install安装时，报"./ids_install: line 3319: /tmp/install.dir.15072/Linux/resource/jre/jre/bin/java: cannot execute binary file"  
数据库版本：ALL  
操作系统：ALL  
硬件平台：ALL  
**描述：**  
执行ids_install安装时，报  
```text
./ids_install: line 3319: /tmp/install.dir.15072/Linux/resource/jre/jre/bin/java: cannot execute binary file
./ids_install: line 3319: /tmp/install.dir.15072/Linux/resource/jre/jre/bin/java: Success
```
**解决方法：**  
提示信息是数据库安装包里自带的java命令是不能执行的二进制文件，原因是：当前的平台与数据库安装包使用的平台不同（如x86平台上使用了其它平台（飞腾、龙芯、Power等）的安装包）。X86平台对应的文件名后缀是x86_64.tar，飞腾平台对应的文件名后缀是FT.tar，龙芯平台对应的文件名后缀是Loongson3B.tar。  

-----  

## 执行ids_install时，报“java.lang.Error: java.io.FileNotFoundException: /tmp/install.dir.4858/Linux/resource/jre/jre/lib/tzdb.dat (没有那个文件或目录)”  
数据库版本：ALL  
操作系统：ALL  
硬件平台：ALL  
**描述：**  
执行ids_install时，报“java.lang.Error: java.io.FileNotFoundException: /tmp/install.dir.4858/Linux/resource/jre/jre/lib/tzdb.dat (没有那个文件或目录)”  
**解决方法：**  
tzdb.dat是一个链接文件，链接到 tzdb.dat -> /usr/share/javazi-1.8/tzdb.dat，若发现不存在这个目录和文件，可以创建链接至系统的tzdb.dat。如：mkdir -p /usr/share/javazi-1.8 && ln -s /usr/lib/jvm/java-8-openjdk-amd64/jre/lib/tzdb.dat /usr/share/javazi-1.8/tzdb.dat。  

-----  

## 执行ids_install时，报“libjvm.so preloadLibrary(/tmp/install.dir.33990/Linux/resource/jre/jre/lib/amd64/libjava.so): libnsl.so.1: 无法打开共享对象文件: 没有那个文件或目录”  
数据库版本：ALL  
操作系统：Kylin V10Sp2或者UOS20（1021a）  
硬件平台：ALL  
**描述：**  
执行ids_install时，报“libjvm.so preloadLibrary(/tmp/install.dir.33990/Linux/resource/jre/jre/lib/amd64/libjava.so): libnsl.so.1: 无法打开共享对象文件: 没有那个文件或目录”    
**解决方法：**  
安装libnsl： `yum -y install libnsl`

-----  

## 安装过程中报“One or more prerequisite system libraries are not installed on your computer. Install libncurses.so.5 and then restart the installation program.”  
数据库版本：ALL  
操作系统：USO20（1021a）  
硬件平台：ALL  
**描述：**  
安装过程中报“One or more prerequisite system libraries are not installed on your computer. Install libncurses.so.5 and then restart the installation program.”  
**解决方法：**  
1，安装ncurses-devel：`yum -y install ncurses-devel`  
2，创建相应的链接文件为so.5  
```text
cd /usr/lib64
ln -s libncurses.so.6.1 libncurses.so.5
ln -s libtinfo.so.6.1 libtinfo.so.5
```

-----  

## java addbatch时，每批行数多时，会报java.net.SocketException:Socket closed。   
数据库版本：ALL  
操作系统：ALL  
硬件平台：ALL  
**描述：**  
java addbatch时，每批行数多时，会报java.net.SocketException:Socket closed。    
**解决方法：**  
增加以下参数 `IFX_SOC_TIMEOUT=600000;IFX_SOC_KEEPALIVE=true;SOCKET_REC_BUF=1073741824`  

-----  

## PDO_GBASEDBT 返回的元数据为大写   
数据库版本：ALL  
操作系统：ALL  
硬件平台：ALL  
**描述：**  
PDO_GBASEDBT 返回的元数据为大写，需要返回小写  
**解决方法：**  
`PDO::ATTR_CASE`默认为`PDO::CASE_UPPER`，需设置为`PDO::CASE_NATURAL`  
PDO_GBASEDBT 默认返回的元数据为大写，连接的属性上增加 
```php
$dbh->setAttribute(PDO::ATTR_CASE, PDO::CASE_NATURAL);
```

最后更新日期：2025-10-10  
