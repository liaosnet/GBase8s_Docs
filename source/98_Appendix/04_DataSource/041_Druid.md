# DRUID连接池建议配置参数  

GBase 8s 数据库使用druid连接池参数建议  

## 基本属性  

|参数名称|参数说明|默认值|建议值及说明|
|:---|:---|:---|:---|
|name|配置这个属性的意义在于，如果存在多个数据源，监控的时候可以通过名字来区分开来。|"DataSource-" + System.identityHashCode(this)|自定义或者默认|
|url|连接数据库的url，不同数据库不一样。| |jdbc:gbasedbt-sqli://<IP>:<PORT>/<DBNAME>:GBASEDBTSERVER=<dbservername>;....|
|username|连接数据库的用户名| |数据库用户名|
|password|连接数据库的用户名对应的密码| |数据库用户对应的密码|
|driverClassName|这一项可配可不配，如果不配置druid会根据url自动识别dbType，然后选择相应的driverClassName|根据url自动识别|com.gbasedbt.jdbc.Driver|

## 连接池大小  

|参数名称|参数说明|默认值|建议值及说明|
|:---|:---|:---|:---|
|initialSize|初始化时建立物理连接的个数。初始化发生在显示调用init方法，或者第一次getConnection时|0|视业务需要，如50|
|maxActive|最大连接池数量|8|视业务需求，如100|
|minIdle|最小连接池数量|0|视业务需求，如50，不应小于initialSize|
|maxWait|获取连接时最大等待时间，单位毫秒。配置了maxWait之后，缺省启用公平锁，并发效率会有所下降，如果需要可以通过配置useUnfairLock属性为true使用非公平锁。|-1|2000|

## 连接检测  

|参数名称|参数说明|默认值|建议值及说明|
|:---|:---|:---|:---|
|testOnBorrow|申请连接时执行validationQuery检测连接是否有效，做了这个配置会降低性能。|false|true|
|testOnReturn|归还连接时执行validationQuery检测连接是否有效，做了这个配置会降低性能。|false|false|
|testWhileIdle|申请连接的时候检测，如果空闲时间大于timeBetweenEvictionRunsMillis，执行validationQuery检测连接是否有效。|false|true,建议配置为true，不影响性能，并且保证安全性。|
|timeBetweenEvictionRunsMillis|有两个含义：<br>1) Destroy线程会检测连接的间隔时间，如果连接空闲时间大于等于minEvictableIdleTimeMillis则关闭物理连接。<br>2) testWhileIdle的判断依据。|60000|120000|
|maxEvictableIdleTimeMillis|连接空闲时间大于该值，不管minidle是多少都关闭这个连接。|25200000|默认值|
|minEvictableIdleTimeMillis|连接空闲时间大于该值并且池中空闲连接数大于minidle则关闭这个连接。|1800000|默认值|
|PhyTimeoutMillis|物理连接打开的时间超过这个超时时间，并且不再使用时会关闭这个物理连接|-1|-1|
|validationQuery|用来检测连接是否有效的sql，要求是一个查询语句，常用select 'x'。|null|select 1 from dual|
|validationQueryTimeout|检测连接是否有效的超时时间。|-1|5|
|keepAlive|连接池中的minIdle数量以内的连接，并且连接的空闲时间大于keepAliveBetweenTimeMillis但小于minEvictableIdleTimeMillis，则会执行validationQuery来保持连接的有效性。|false|true|
|keepAliveBetweenTimeMillis|打开KeepAlive时，当连接的空闲时间超过该值，会使用validationQuery执行一次查询，检查连接是否可用。|120000|120000，默认值|

## 缓存语句  

|参数名称|参数说明|默认值|建议值及说明|
|:---|:---|:---|:---|
|poolPreparedStatements|是否缓存preparedStatement，也就是PSCache。PSCache对支持游标的数据库性能提升巨大，比如说oracle。|false|false，关闭|
|maxPoolPreparedStatementPerConnectionSize|要启用PSCache，必须配置大于0，当大于0时，poolPreparedStatements自动触发修改为true。|10|-1，需关闭|

示例：  
```text
# ========================
# 数据源基础配置
# 使用application.properties配置文件时，需要使用  kebab-case（短横线分隔）格式
# ========================
spring.datasource.type=com.alibaba.druid.pool.DruidDataSource
spring.datasource.driver-class-name=com.gbasedbt.jdbc.Driver
# 参数说明：
# LOGINTIMEOUT=60000;GBASEDBTCONRETRY=3;GBASEDBTCONTIME=60; 登陆超时为60000毫秒(60秒)，60秒内重试3次
# IFX_SOC_TIMEOUT=600000;IFX_SOC_KEEPALIVE=true; SOCKET超时为600000毫秒（600秒），SOCKET保活为真
spring.datasource.url=jdbc:gbasedbt-sqli://192.168.80.215:9088/testdb:GBASEDBTSERVER=gbase01;DB_LOCALE=zh_CN.utf8;CLIENT_LOCALE=zh_CN.utf8;IFX_LOCK_MODE_WAIT=30;SQLMODE=mysql;LOGINTIMEOUT=60000;GBASEDBTCONRETRY=3;GBASEDBTCONTIME=60;IFX_SOC_TIMEOUT=600000;IFX_SOC_KEEPALIVE=true
spring.datasource.username=gbasedbt
spring.datasource.password=********

# ========================
# Druid 连接池配置
# ========================
spring.datasource.druid.initial-size=5
spring.datasource.druid.min-idle=5
spring.datasource.druid.max-active=20
spring.datasource.druid.max-wait=60000
# 1) Destroy线程会检测连接的间隔时间，如果连接空闲时间大于等于minEvictableIdleTimeMillis则关闭物理连接。2) testWhileIdle的判断依据
spring.datasource.druid.time-between-eviction-runs-millis=60000
# 连接空闲时间大于该值并且池中空闲连接数大于minidle则关闭这个连接
spring.datasource.druid.min-evictable-idle-time-millis=300000
spring.datasource.druid.validation-query=SELECT 1 FROM DUAL
# 连接池中的minIdle数量以内的连接，并且连接的空闲时间大于keepAliveBetweenTimeMillis但小于minEvictableIdleTimeMillis，则会执行validationQuery来保持连接的有效性。
spring.datasource.druid.keep-alive=true
# 申请连接的时候检测，如果空闲时间大于timeBetweenEvictionRunsMillis，执行validationQuery检测连接是否有效。
spring.datasource.druid.test-while-idle=true
# 该参数视需要开启
spring.datasource.druid.test-on-borrow=false
# 申请连接时执行validationQuery检测连接是否有效，做了这个配置会降低性能。
spring.datasource.druid.test-on-return=false
```

> **<font color="blue">注意</font>**  
> 说明：不同版本的默认值可能不一样，某些版本需要显式指定。  
> 使用application.properties配置文件时，需要使用  kebab-case（短横线分隔）格式  

参考：https://github.com/alibaba/druid/wiki/DruidDataSource%E9%85%8D%E7%BD%AE%E5%B1%9E%E6%80%A7%E5%88%97%E8%A1%A8  



最后修改时间：2026-06-30  
