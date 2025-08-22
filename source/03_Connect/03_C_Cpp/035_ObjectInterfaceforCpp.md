# C++语言使用GBase Object Interface for C++方式连接到数据库（Linux）  
本章节将介绍C++程序通过GBase Object Interface for C++连接到GBase 8s数据库的方式。  
GBase Object Interface for C++依赖于CSDK。  

## 示例环境介绍  
操作系统：Ubuntu 22.04.3 LTS （x86_64）  
数据库版本：GBase 8s v8.8_3.6.3_3x2_1  

## 依赖包  
```text
root@netsky:~# apt -y install autoconf gcc g++
```

## 安装GBase ClientSDK及配置ODBC  
安装目录为/opt/gbase  
参考：[CSDK安装](../../02_Install/02_CSDK_Lnx.html "CSDK安装")  

在/etc/ld.so.conf.d目录下增加GBase 8s的库目录配置文件gbase8scsdk-x86_64.conf  
```text
root@netsky:/etc/ld.so.conf.d# pwd
/etc/ld.so.conf.d
root@netsky:/etc/ld.so.conf.d# more gbase8scsdk-x86_64.conf
/opt/gbase/lib
/opt/gbase/lib/cli
/opt/gbase/lib/esql
```

设置环境变量（与server一致），并加载  
```shell
root@netsky:~# more env_csdk
export GBASEDBTSERVER=gbase01
export GBASEDBTDIR=/opt/gbase
export PATH=$GBASEDBTDIR/bin:$PATH
export LD_LIBRARY_PATH=$GBASEDBTDIR/lib:$GBASEDBTDIR/lib/cli:$GBASEDBTDIR/lib/esql:$LD_LIBRARY_PATH
export DB_LOCALE=zh_CN.utf8
export CLIENT_LOCALE=zh_CN.utf8
export GL_USEGLU=1

root@netsky:~# . env_csdk
```

## 设置系统网络连接（异机：可选，也可配置为信任连接方式）  
在用户目录下创建.netrc配置文件，权限为600，内容如下：  
```text
root@netsky:~/cpp# more ~/.netrc
# machine 目标主机名或IP地址 login 用户名 password 密码
machine 192.168.0.212 login gbasedbt password GBase123$%
```

## GBase Object Interface for C++连接测试  
### 编译测试程序TestCpp.cpp  
`TestCpp.cpp`内容如下,参考demo/c++/queryrex.cpp：  
```cpp
#include <iostream>
#include <it.h>
#include <string>
using namespace std;
 
int main(int argc, char *argv[])
{
    if (argc != 1)
        {
        cout << "Usage: " << argv[0]  << endl;
        return 1;
        }
 
    // 指定数据库
    ITConnection conn;
    conn.SetDBInfo(ITDBInfo(ITString("testdb")));
    conn.Open();
 
    // 创建query对象
    ITQuery q(conn);
 
    if (argc != 1)
        {
        cout << "Usage:./TestCpp" << endl;
    	conn.Close();
    	return 0;
        }
    // 检查表是否存在，如果不存在则创建
    q.ExecForStatus("drop table if exists company;");
    cout << "删除表: \n";

    ITRow *r1 = q.ExecOneRow(
        "select 1 from systables where tabname = 'company';");
    if ( !r1 && (!q.ExecForStatus("create table company(coid serial,coname varchar(255),coaddr varchar(255), primary key(coid))")))
    {
        cerr << "创建表 company 失败！" << endl;
        return 1;
    }
    cout << "创建表: \n";

    // 开始事务  
    conn.SetTransaction(ITConnection::Begin);

    // 插入数据
    ITString query;
    query = "insert into company values (0,'GBase','TJ'),(0,'GBase Beijin','BJ');";
    q.ExecForStatus(query);
    cout << "插入表: \n";

    // 提交事务
    conn.SetTransaction(ITConnection::Commit);

    // 显示数据库中的内容
    cout << "查询表：\n";
    ITSet *set = q.ExecToSet
        ("select * from company;"); 
    if( !set )
    {
	    cout << "查询失败！" << endl;
	    conn.SetTransaction(ITConnection::Abort);
	    conn.Close();
	    return -1;
    }
    ITValue *v;
    while ((v = set->Fetch()) != NULL)
    {
        cout << v->Printable() << endl;
        v->Release();
    } 
    set->Release();
    cout << endl;
    conn.Close();
    return 0;
}
```

### 编写Makefile  
Makefile文件内容：  
```text
CPPIFDIR	= $(GBASEDBTDIR)
CCHOME		= /usr
 
CCPP		= $(CCHOME)/bin/g++
CCPLUS		= $(CCPP) $(HEADEROPTS)
CCPPFLAGS 	= -I$(GBASEDBTDIR)/incl/dmi -I$(GBASEDBTDIR)/incl \
	-I$(GBASEDBTDIR)/incl/esql
CCPLINK		= $(CCPLUS) $(CCFLAGS) $(CCPPFLAGS)
CC		= $(CCHOME)/bin/gcc
C-COMPILE-FLAGS	= $(CCFLAGS)
CCDEFS		= -DLINUX -DIT_HAS_DISTINCT_LONG_DOUBLE \
	-DIT_COMPILER_HAS_LONG_LONG -DIT_DLLIB -DMITRACE_OFF -fPIC
CCFLAGS		= -g $(CCDEFS) -fsigned-char
 
ESQL		= $(GBASEDBTDIR)/bin/esql
 
RANLIB		= echo
 
LOCALINCL	= -I$(CPPIFDIR)/incl/c++
 
LIBS_SYSTEM	= -lm -ldl -lcrypt -lnsl
LIBS_ESQL	= -L$(GBASEDBTDIR)/lib/esql -L$(GBASEDBTDIR)/lib -lifsql \
 -lifasf -lifgen -lifos -lifgls -lifglx $(GBASEDBTDIR)/lib/esql/checkapi.o
LIBS_LIBMI	= -L$(GBASEDBTDIR)/lib/dmi -lifdmi 
LIBS_CPPIF	= -L$(CPPIFDIR)/lib/c++ -lifc++
LIBS		= $(LIBS_CPPIF) $(LIBS_LIBMI) $(LIBS_ESQL) $(LIBS_SYSTEM) 
RPATH		= $(GBASEDBTDIR)/lib:$(GBASEDBTDIR)/lib/esql:$(GBASEDBTDIR)/lib/dmi:$(GBASEDBTDIR)/lib/c++
 
PROGRAMS	= TestCpp
.SUFFIXES: .cc .o .hdr .cpp
 
.cc.o:
	@rm -f $@
	$(CCPLUS) $(CCFLAGS) $(LOCALINCL) $(CCPPFLAGS) -c $<
 
.cpp.o:
	@rm -f $@
	$(CCPLUS) $(CCFLAGS) $(LOCALINCL) $(CCPPFLAGS) -c $<
 
all: 	$(PROGRAMS)
 
TestCpp: TestCpp.o
	$(CCPLINK) -o TestCpp TestCpp.o $(SUBSYSTEMS.link) $(LIBS) -Wl,-rpath=$(RPATH)
 
clean:
	$(RM) *.o $(PROGRAMS) core
```
注：使用tab而不是8个空格  

### 编译  
编译,生成TestCpp  
```text
root@netsky:~/cpp# make
```

### 执行测试  
执行测试  
```text
root@netsky:~/cpp# ./TestCpp
删除表:
创建表:
插入表:
查询表：
1       GBase   TJ
2       GBase Beijin    BJ

```

最后更新日期： 2025-08-22  
