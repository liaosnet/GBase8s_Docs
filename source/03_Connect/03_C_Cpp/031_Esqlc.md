# C语言使用ESQLC方式连接到数据库（Linux）  
本章节将介绍C程序通过ESQLC连接到GBase 8s数据库的方式。  
ESQLC是CSDK的一部分，因此本操作依赖CSDK。  

## ESQL/C 是什么  
GBase 8s ESQL/C 是 SQL 应用程序编程接口（API），它使您可以直接在 C 程序中嵌入结构化查询语言（SQL）语句。   
GBase 8s ESQL/C 的预处理器 esql 将每个 SQL 语句和特定于 GBase 8s 的所有代码转换为 C 语言源代码，并启动 C 编译器进行编译它。   

## 示例环境介绍  
操作系统：CentOS Linux release 7.9.2009 （x86_64）  
数据库版本：GBase 8s v8.8_3.6.3_3x2_1  
客户端连接工具：clientsdk_3.6.3_3X2_1_783c8d  

## 依赖包  
```text
[root@localhost ~]# yum install -y autoconf gcc gcc-c++ unixODBC unixODBC-devel  
```

## 安装GBase ClientSDK  
安装目录为/opt/gbase  
参考：[CSDK安装](../../02_Install/02_CSDK_Lnx.html "CSDK安装")  

在/etc/ld.so.conf.d目录下增加GBase 8s的库目录配置文件gbase8scsdk-x86_64.conf  
```text
[root@localhost ld.so.conf.d]# pwd
/etc/ld.so.conf.d
[root@localhost ld.so.conf.d]# more gbase8scsdk-x86_64.conf
/opt/gbase/lib
/opt/gbase/lib/cli
/opt/gbase/lib/esql
```

配置环境变量  
```shell
export GBASEDBTDIR=/opt/gbase
export PATH=$GBASEDBTDIR/bin:$PATH
export LD_LIBRARY_PATH=$GBASEDBTDIR/lib:$GBASEDBTDIR/lib/cli:$GBASEDBTDIR/lib/esql:$LD_LIBRARY_PATH
```

## 设置系统网络连接（异机：可选，也可配置为信任连接方式）  
在用户目录下创建.netrc配置文件，权限为600，内容如下：  
```text
[root@localhost esqlc]# more ~/.netrc
# machine 目标主机名或IP地址 login 用户名 password 密码
machine 192.168.0.212 login gbasedbt password GBase123$%
```

## ESQLC连接测试  
### 编译测试程序TestESQLC.ec   
`TestESQLC.ec`内容如下：  
```text
#include <stdio.h>

main()
{
EXEC SQL BEGIN DECLARE SECTION;
    int  v_tabid;
    char v_tabname[ 128 ];
EXEC SQL END DECLARE SECTION;

    printf( "\nESQLC 测试程序开始运行.\n\n");
    EXEC SQL WHENEVER ERROR STOP;
    /* 这里connect to 的是库名 */
    EXEC SQL connect to 'testdb';

    EXEC SQL declare democursor cursor for
	select tabid,tabname
	   into :v_tabid, :v_tabname
	   from systables where tabid < 10;

    EXEC SQL open democursor;
    for (;;)
	{
	EXEC SQL fetch democursor;
	if (strncmp(SQLSTATE, "00", 2) != 0)
	    break;

	printf("%d\t%s\n", v_tabid, v_tabname);
	}

    if (strncmp(SQLSTATE, "02", 2) != 0)
        printf("SQLSTATE after fetch is %s\n", SQLSTATE);

    EXEC SQL close democursor;
    EXEC SQL free democursor;

    EXEC SQL disconnect current;
    printf("\nESQLC 测试程序结束运行.\n\n");

   exit(0);
}
```

### 编译成可执行文件，并执行测试  
```text
[root@localhost esqlc]# esql -o TestESQLC -glu TestESQLC.ec 

[root@localhost esqlc]# ./TestESQLC 

ESQLC 测试程序开始运行.

1	systables                                                                                                                      
2	syscolumns                                                                                                                     
3	sysindices                                                                                                                     
4	systabauth                                                                                                                     
5	syscolauth                                                                                                                     
6	sysviews                                                                                                                       
7	sysusers                                                                                                                       
8	sysdepend                                                                                                                      
9	syssynonyms                                                                                                                    

ESQLC 测试程序结束运行.
```

最后更新日期：2025-08-19  
