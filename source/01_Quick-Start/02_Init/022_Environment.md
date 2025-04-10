# 环境变量  
本章将展示数据库安装后的环境变量信息，具体以安装生成值为准。
如下一键安装方法配置的环境变量信息：
```text
export GBASEDBTDIR=/opt/gbase
export GBASEDBTSERVER=gbase01
export ONCONFIG=onconfig.$GBASEDBTSERVER
export PATH=$GBASEDBTDIR/bin:$GBASEDBTDIR/sbin:$GBASEDBTDIR/sbin:${PATH}
export GBASEDBTSQLHOSTS=/opt/gbase/etc/sqlhosts
export SERVER_LOCALE=zh_CN.utf8
export DB_LOCALE=zh_CN.utf8
export CLIENT_LOCALE=zh_CN.utf8
export GL_USEGLU=1
# export NODEFDAC=yes
export DBDATE="Y4MD-"
export DBACCESS_SHOW_TIME=1
```

具体描述如下：

| **环境变量名称** | **环境变量说明信息** |
| --- | --- |
| GBASEDBTDIR | 软件安装目录，包含产品相关程序文件。 |
| GBASEDBTSERVER | 数据库实例名称 |
| ONCONFIG | 数据库参数配置文件名称，位于GBASEDBTDIR/etc目录下 |
| PATH | 将GBASEDBTDIR/bin和GBASEDBTDIR/sbin目录下的实用程序加入到PATH，以便可以直接运行。 |
| GBASEDBTSQLHOSTS | 数据库实例连接配置文件，内容包含实例名称、协议、对应的IP和服务端口号 |
| SERVER_LOCALE | 实例使用的字符集编码 |
| DB_LOCALE | 数据库使用的字符集编码 |
| CLIENT_LOCALE | 客户端使用的字符集编码 |
| GL_USEGLU | 使用GLU（GLS for Unicode (GLU)） |
| DBDATE | 指定DATE的格式Y4MD-表示 yyyy-mm-dd |
| DBACCESS_SHOW_TIME | 在dbaccess实用程序中显示语句执行的时长 |
