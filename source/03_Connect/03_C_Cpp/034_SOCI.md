# C++语言使用SOCI方式连接到数据库（Linux）  
本章节将介绍C++程序通过SOCI连接到GBase 8s数据库的方式。  
SOCI依赖于ODBC，需要安装CSDK。  

## 示例环境介绍  
操作系统：Ubuntu 22.04.3 LTS （x86_64）  
数据库版本：GBase 8s v8.8_3.6.3_3x2_1  
Cmake3版本：3.31  
SOCI版本：4.1.2 (https://github.com/SOCI/soci)  

## 依赖包  
```text
root@netsky:~# apt -y install autoconf gcc g++ unixodbc unixodbc-dev
```
cmake3  
```text
root@netsky:~# snap install cmake --channel=3.31/stable --classic
```
设置环境变量文件（也可以写入到/etc/profile中）  
```shell
# 增加到PATH
export PATH=/snap/bin:$PATH
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

设置环境变量，并加载  
```shell
root@netsky:~# more env_csdk
export GBASEDBTDIR=/opt/gbase
export PATH=$GBASEDBTDIR/bin:$PATH
export LD_LIBRARY_PATH=$GBASEDBTDIR/lib:$GBASEDBTDIR/lib/cli:$GBASEDBTDIR/lib/esql:$LD_LIBRARY_PATH
# ODBCINI
export ODBCINI=/opt/gbase/etc/odbc.ini

root@netsky:~# . env_csdk
```

配置ODBCINI配置文件，根据CSDK环境，配置如下：  
```text
[ODBC Data Sources]
testdb=GBase ODBC DRIVER
;
; Define ODBC Database Driver's Below - Driver Configuration Section
;
[testdb]
Driver=/opt/gbase/lib/cli/iclit09b.so
Driver=GBase ODBC DRIVER
Description=GBase ODBC DRIVER
Database=testdb
LogonID=gbasedbt
pwd=GBase123$%
Servername=gbase01
CursorBehavior=0
CLIENT_LOCALE=zh_CN.utf8
DB_LOCALE=zh_CN.utf8
GL_USEGLU=1
TRANSLATIONDLL=/opt/gbase/lib/esql/igo4a304.so
; ISOLATIONLEVEL=1	# 使用该参数（简写：ISOLVL）设置默认的隔离级别，0-5
;
; UNICODE connection Section
;
[ODBC]
;uncomment the below line for UNICODE connection
UNICODE=UCS-2		# 如果需要使用unicode连接数据库，这里需要去除注释，值改为UCS-2
;
; Trace file Section
;
Trace=0
TraceFile=/tmp/odbctrace.out
InstallDir=/opt/gbase
TRACEDLL=idmrs09a.so
```

## 安装SOCI  
SOCI需要预先安装cmake3（3.23及之后）, gcc-c++   
下载地址：https://github.com/SOCI/soci.git  
或者 https://sourceforge.net/projects/soci/files/soci/   
```text
root@netsky:~# wget https://netactuate.dl.sourceforge.net/project/soci/soci/soci-4.1.2/soci-4.1.2.tar.gz

root@netsky:~# tar -zxvf soci-4.1.2.tar.gz && cd soci-4.1.2
```

设置环境变量文件（也可以写入到/etc/profile中）  
```shell
# 增加到LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/usr/local/lib:/usr/local/lib64:$LD_LIBRARY_PATH
```

使用cmake编译安装SOCI  
```text
root@netsky:~/soci-4.1.2# cmake -DWITH_BOOST=ON

root@netsky:~/soci-4.1.2# make

root@netsky:~/soci-4.1.2# make install
```

## 编写测试代码  
编写测试程序脚本TestSOCIOdbc.cpp  
```cpp
#include <soci/soci.h>
#include <soci/odbc/soci-odbc.h>
#include<iostream>
#include<istream>
#include<ostream>
#include<string>
#include<exception>

using namespace std;
using namespace soci;

int main() {
    cout<<"SOCI 测试程序开始运行.\n\n";
    try {
        // 使用DSN-Less方式
        string GBase8sDSN = "Driver=/opt/gbase/lib/cli/iclit09b.so;HOST=192.168.0.212;SERV=13633;PROT=onsoctcp;SRVR=gbase01;DB=testdb;UID=gbasedbt;PWD=GBase123$%;DLOC=zh_CN.utf8;CLOC=zh_CN.utf8";
        // 也可使用DSN
        // string GBase8sDSN = "DSN=testdb;PWD=GBase123$%";
        session sql(odbc,GBase8sDSN);
        // 删除和创建表
        sql<< "drop table if exists company";
        cout<<"删除表成功\n";

        sql<< "create table company(coid serial,coname varchar(255),coaddr varchar(255), primary key(coid))";
        cout<<"创建表成功\n";

        // 插入记录
        string cn1 = "GBase";
        string ca1 = "TJ";
        string cn2 = "GBase BeiJing";
        string ca2 = "BJ";
        sql<< "insert into company values(0,:cn1,:ca1),(0,:cn2,:ca2)",use(cn1), use(ca1),use(cn2),use(ca2);
        cout<<"插入数据成功\n";

        // 查询记录
        rowset<row> rs = (sql.prepare << "select * from company");
        for (rowset<row>::iterator it = rs.begin(); it != rs.end(); ++it)
        {
            const row& row = *it;
            cout << "coid:" << row.get<int>(0)
                 << " coname:" << row.get<string>(1)
                 << " coaddr:" << row.get<string>(2) << endl;
        }
        cout<<"查询表成功\n";
    } catch (exception const &e) {
        cerr<<"Error:" <<e.what()<<endl;
    }
    cout<<"\nSOCI 测试程序结束运行.\n";
}
```

编译程序  
```text
root@netsky:~# g++ -Wall -g -o TestSOCIOdbc TestSOCIOdbc.cpp -lsoci_core -lsoci_odbc
```

执行测试  
```text
root@netsky:~# ./TestSOCIOdbc
SOCI 测试程序开始运行.

删除表成功
创建表成功
插入数据成功
coid:1 coname:GBase coaddr:TJ
coid:2 coname:GBase BeiJing coaddr:BJ
查询表成功

SOCI 测试程序结束运行.
```

最后更新日期： 2025-08-22  
