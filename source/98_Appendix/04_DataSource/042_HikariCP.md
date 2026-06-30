# HikariCP连接池建议配置参数  

GBase 8s 数据库使用hikaricp连接池参数建议  

## 基本属性  

|参数名称|参数说明|默认值|建议值及说明|
|:---|:---|:---|:---|
|jdbcUrl|连接数据库的url，不同数据库不一样。| |jdbc:gbasedbt-sqli://<IP>:<PORT>/<DBNAME>:GBASEDBTSERVER=<dbservername>;....|
|username|连接数据库的用户名| |数据库用户名|
|password|连接数据库的用户名对应的密码| |数据库用户对应的密码|
|driverClassName|driverClassName| |com.gbasedbt.jdbc.Driver|

## 连接池大小  

|参数名称|参数说明|默认值|建议值及说明|
|:---|:---|:---|:---|
|minimumIdle|最小空闲连接数量|10|视业务需求，如50|
|maximumPoolSize|连接池最大连接数|10|视业务需求，如100|
|poolName|连接池名称|随机|自定义或者默认|

## 连接检测  

|参数名称|参数说明|默认值|建议值及说明|
|:---|:---|:---|:---|
|connectionTestQuery|连接测试语句| |select 1 from dual|
|connectionTimeout|连接超时|30000|30000|
|idleTimeout|空闲连接存活最大时间|600000|600000|
|maxLifetime|连接最大存活时间，值0表示无限生命周期|1800000|1800000|
|keepaliveTime|保持连接活跃的检查间隔|120000|120000，小于 maxLifetime 和数据库超时|
|validationTimeout|验证连接有效性最大时间|5000|5000|

最后更新日期：2026-03-30  