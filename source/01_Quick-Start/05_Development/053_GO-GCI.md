# GO-GCI应用示例（Linux）  
本章将介绍GBase 8s的GO（GO-GCI）的基础的操作演示。  

## 示例环境介绍  
操作系统：Ubuntu 22.04.3 LTS （x86_64)  
数据库版本：GBase 8s v8.8_3.6.3_3x2_1  
GO版本：go version go1.24.5 linux/amd64  

## GSDK下载及安装 
GSDK驱动包的名称一般为：GSDK_3.6.3_3X2_1_1.1.0_1_eff9f1_RHEL6_x86_64.tar  
示例使用的GDSK下载地址：[https://dl.gbase8s.com:9088/GSDK/](https://dl.gbase8s.com:9088/GSDK/)  

GSDK需要使用1.1.x版本，该版本暂时需要通过GBase 8s技术支持或通过官方渠道获取。  
如下，本次使用的版本为：
GSDK_3.6.3_3X2_1_1.1.0_1_eff9f1_RHEL6_x86_64.tar  
说明：  
* 3.6.3_3X2_1：对应的数据库版本号  
* 1.1.0_1：GSDK版号本  
* eff9f1：内部GIT  
* RHEL6：编译的操作系统版本  
* x86_64：适用的架构  

上传到服务器，解压并改名  
```shell
tar -xvf GSDK_3.6.3_3X2_1_1.1.0_1_eff9f1_RHEL6_x86_64.tar -C /opt
mv /opt/GSDK_3.6.3_3X2_1_1.1.0_1_eff9f1_RHEL6_x86_64 /opt/GSDK
```

设置环境变量，并加载  
```shell
root@netsky:~# more env_gsdk
export GSDK_PATH=/opt/GSDK
export LD_LIBRARY_PATH=${GSDK_PATH}/lib:$LD_LIBRARY_PATH
export GBASEDBTDIR=${GSDK_PATH}/lib
# for golang
export CGO_CFLAGS="-I/opt/GSDK/include"
export CGO_LDFLAGS="-L/opt/GSDK/lib -lclntsh_gbase"

root@netsky:~# . env_gask
```

## 确认安装go及版本  
确认已经安装go  
```shell
root@netsky:~# # go version
go version go1.24.5 linux/amd64
```
如果没有安装，建议使用snap install go --classic来安装。  

## 安装GO-GCI  
GO-GCI存储于gitee.com，需要设置GOPRIVATE 
```shell
root@netsky:~#  export GOPRIVATE=gitee.com
```
使用go install 安装  
```shell
root@netsky:~# go install gitee.com/GBase8s/go-gci@latest
go: downloading gitee.com/GBase8s/go-gci v0.1.1
package gitee.com/GBase8s/go-gci is not a main package
```

## 编写测试代码  
创建目录GOSample  
```shell
root@netsky:~# mkdir GOSample
```
进入目录模块初始化  
```shell
root@netsky:~# cd GOSample

root@netsky:~/GOSample# go mod init GOSample 
```
增加go-gci  
```
root@netsky:~/GOSample# go get gitee.com/GBase8s/go-gci
go: added gitee.com/GBase8s/go-gci v0.1.1
```
编写测试代码GOSample.go  
```go
package main

import (
        "database/sql"
        "fmt"
        _ "gitee.com/GBase8s/go-gci"
        "log"
)
func main() {
        // 设置DSN，这里需要注意密码的特殊字符限制。
        Gbase8sDSN := "gbase8s://gbasedbt:GBase123@192.168.0.212:13633/testdb?GBASEDBTSERVER=gbase01&PROTOCOL=onsoctcp&sqlmode=oracle&delimident=1&GOGCILogTrace=0"

        // 使用 go-gci 连接数据库
        db, err := sql.Open("gbase8s", Gbase8sDSN)
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
root@netsky:~/GOSample# go run GOSample.go          # go run -tags noPkgConfig GOSample.go
数据库连接成功！
删除表成功！
创建表成功！
正常插入！
COID:1  CONAME:GBase    COADDR:TJ
COID:2  CONAME:GBase BeiJing    COADDR:BJ
查询成功！
```