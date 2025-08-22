# GO语言使用ODBC方式连接到数据库（Linux）  
本章节将介绍GO程序通过ODBC连接到GBase 8s数据库的方式。  
ODBC是CSDK的一部分，因此本操作依赖CSDK；同时ODBC依赖于操作系统的unixODBC。  

## 示例环境介绍  
操作系统：Ubuntu 22.04.3 LTS （x86_64）  
数据库版本：GBase 8s v8.8_3.6.3_3x2_1  
GO版本：go version go1.24.5 linux/amd64  
alexbrainman/odbc版本:  (https://github.com/alexbrainman/odbc)  

## 依赖包  
```text
[root@netsky ~]# apt -y install autoconf gcc g++ unixodbc unixodbc-dev
```

## 安装GBase ClientSDK及配置ODBC  
安装目录为/opt/gbase  
参考：[CSDK安装](../../02_Install/02_CSDK_Lnx.html "CSDK安装")  

在/etc/ld.so.conf.d目录下增加GBase 8s的库目录配置文件gbase8scsdk-x86_64.conf  
```text
[root@netsky ld.so.conf.d]# pwd
/etc/ld.so.conf.d
[root@netsky ld.so.conf.d]# more gbase8scsdk-x86_64.conf
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

## 确认安装go及版本  
确认已经安装go  
```shell
root@netsky:~# # go version
go version go1.24.5 linux/amd64
```
如果没有安装，建议使用snap install go --classic来安装。  

## 安装alexbrainman/odbc  
使用go install 安装  
```shell
# 使用代理
root@netsky:~# go env -w GOPROXY=https://goproxy.cn

root@netsky:~# go install github.com/alexbrainman/odbc@latest
go: downloading github.com/alexbrainman/odbc v0.0.0-20250601004241-49e6b2bc0cf0
package github.com/alexbrainman/odbc is not a main package
```

## 编写测试代码  
创建目录GOOdbcSample  
```shell
root@netsky:~# mkdir GOOdbcSample
```
进入目录模块初始化  
```shell
root@netsky:~# cd GOOdbcSample

root@netsky:~/GOOdbcSample# go mod init GOOdbcSample 
```
增加alexbrainman odbc    
```
root@netsky:~/GOOdbcSample# go get github.com/alexbrainman/odbc
go: downloading golang.org/x/sys v0.0.0-20190916202348-b4ddaad3f8a3
go: added github.com/alexbrainman/odbc v0.0.0-20250601004241-49e6b2bc0cf0
go: added golang.org/x/sys v0.0.0-20190916202348-b4ddaad3f8a3
```
编写测试代码GOOdbcSample.go  
```go
package main

import (
        "database/sql"
        "fmt"
        _ "github.com/alexbrainman/odbc"
        "log"
)
func main() {

        // 对于 CM 和直连，使用 DSN 方式；若是直连，可使用 DSN-LESS 方式
        Gbase8sDSN := "DSN=testdb;UID=gbasedbt;PWD=GBase123$%;"
        db, err := sql.Open("odbc", Gbase8sDSN)
        if err != nil {
                log.Fatalf("数据库连接失败: %v\n", err)
        }
        defer db.Close()

        // 测试数据库连接
        err = db.Ping()
        if err != nil {
                log.Fatalf("无法连接到数据库: %v\n", err)
        }
        fmt.Println("数据库连接成功！")

        // 删除表
        _, err = db.Exec("drop table if exists company")
        if err != nil {
                log.Fatalf("删除表异常：%v\n", err)
                return
        }
        fmt.Println("删除表成功！")

        // 创建表
        _, err = db.Exec("create table company(coid serial,coname varchar(255),coaddr varchar(255), primary key(coid))")
        if err != nil {
                log.Fatalf("创建表异常：%v\n", err)
                return
        }
        fmt.Println("创建表成功！")

        // 插入数据
        _, err = db.Exec("insert into company values(0,?,?),(0,?,?)","GBase","TJ","GBase BeiJing","BJ")
        if err != nil {
                log.Fatalf("插入异常：%v\n", err)
                return
        }
        fmt.Println("正常插入！")

        // 查询并显示数据
        rows, err := db.Query("select * from company")
        if err != nil {
                log.Fatalf("查询异常：%v\n", err)
                return
        }
        defer rows.Close()
        for rows.Next(){
                var coid int
                var coname string
                var coaddr string
                if err := rows.Scan(&coid,&coname,&coaddr); err == nil {
                        fmt.Printf("COID:%d\tCONAME:%s\tCOADDR:%s\n",coid,coname,coaddr)
                }
        }
        fmt.Println("查询成功！")
}
```
执行测试  
```shell
root@netsky:~/GOOdbcSample# go run ~/GOOdbcSample.go
数据库连接成功！
删除表成功！
创建表成功！
正常插入！
COID:1  CONAME:GBase    COADDR:TJ
COID:2  CONAME:GBase BeiJing    COADDR:BJ
查询成功！
```

最后更新日期： 2025-08-22  
