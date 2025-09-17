# PHP使用ODBC方式连接到数据库（Linux）  
本章节将介绍PHP程序通过ODBC连接到GBase 8s数据库的方式。  
PHP环境使用nginx+php-fpm，使用纯编译方式。  

## 示例环境介绍  
操作系统：CentOS Linux release 7.9.2009 （aarch64）  
数据库版本：GBase 8s v8.8_3.6.3_3x2_1  
客户端连接工具：clientsdk_3.6.3_3X2_1_783c8d  
unixODBC: 系统自带  

## 依赖包  
```text
[root@gbase_host01 ~]# yum install -y autoconf openssl openssl-devel zlib zlib-devel \
    pcre pcre-devel gcc gcc-c++ libxml2-devel sqlite-devel unixODBC unixODBC-devel  
```

## 源码安装nginx  
使用nginx-1.28.0版本  
```text
[root@gbase_host01 nginx-1.28.0]# ./configure --prefix=/usr/local/nginx

[root@gbase_host01 nginx-1.28.0]# make -j 4

[root@gbase_host01 nginx-1.28.0]# make install
```

## 源码安装php  
使用 php-7.4.33  
```text
[root@gbase_host01 php-7.4.33]# ./configure --prefix=/usr/local/php -with-config-file-path=/usr/local/php/etc --enable-fpm --with-unixODBC=/usr

[root@gbase_host01 php-7.4.33]# make -j 4
```
**注1：**  
`--with-unixODBC`后需接unixODBC目录，如：=/usr  

**注2：aarch64架构下，数组函数zif_array_sum编译错误，通过修改zend_operators.h文件中ZEND_USE_ASM_ARITHMETIC的值为0来解决**  
bug地址： https://bugs.php.net/bug.php?id=81124  
```text
[root@gbase_host01 php-7.4.33]# vi Zend/zend_operators.h  
```
修改 "# define ZEND_USE_ASM_ARITHMETIC 1" 的值为0  
```text
# define ZEND_USE_ASM_ARITHMETIC 0
```
继续编译  
```text
[root@gbase_host01 php-7.4.33]# make install
```

## 配置PHP和nginx，实现nginx转发到PHP处理  
修改nginx/conf目录下nginx.conf  
```text
[root@gbase_host01 conf]# pwd
/usr/local/nginx/conf
[root@gbase_host01 conf]# vi nginx.conf
```
修改http中server中的location /  
```text
#...

http {
    #...
	
    server {
        #...
		
        location / {
            root   html;
            index  index.html index.htm index.php;		# 增加index.php
        }
		#...
		# 增加以下
		location ~* \.php$ {
            fastcgi_pass   127.0.0.1:9000;
            fastcgi_index  index.php;
            fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
            fastcgi_param  SCRIPT_NAME      $fastcgi_script_name;
            include        fastcgi_params;
        }		
	}
	#...
}
#...
```

复制php/etc/php-fpm.d/下的www.conf.default为www.conf  
```text
[root@gbase_host01 php-fpm.d]# pwd
/usr/local/php/etc/php-fpm.d
[root@gbase_host01 php-fpm.d]# cp www.conf.default www.conf
```
并修改  
```text
; 这里去掉clean_env的注释
clear_env = no

; 增加GBase 8s CSDK的安装目录  
env[GBASEDBTDIR] = /opt/gbase
; 增加DOBCINI
env[ODBCINI] = /opt/gbase/etc/odbc.ini
```

复制php/etc/下的php-fpm.conf.default为php-fpm.conf  
```text
[root@gbase_host01 etc]# pwd
/usr/local/php/etc
[root@gbase_host01 etc]# cp php-fpm.conf.default php-fpm.conf
```
并修改  
```text
; 这里去掉pid的注释
pid = run/php-fpm.pid
```

复制php源码目录下的php.ini-development到php安装目录下etc/php.ini  
```text
[root@gbase_host01 etc]# pwd
/usr/local/php/etc
[root@gbase_host01 etc]# cp /root/php-7.4.33/php.ini-development php.ini
```


## 启动php-fpm和ngnix  
环境变量文件  
```text
[root@gbase_host01 ~]# more env_web
export NGINX_HOME=/usr/local/nginx
export PHP_HOME=/usr/local/php
export PATH=$NGINX_HOME/sbin:$PHP_HOME/bin:$PHP_HOME/sbin:$PATH
```
加载环境变量，启动php-fpm和ngnix  
```text
[root@gbase_host01 ~]# . env_web
[root@gbase_host01 ~]# php-fpm
[root@gbase_host01 ~]# nginx
```

在nginx/html目录下编写phpinfo.php  
```text
[root@gbase_host01 html]# pwd
/usr/local/nginx/html
[root@gbase_host01 html]# more phpinfo.php
<?php
        phpinfo();
```

执行查看phpinfo  
```text
[root@gbase_host01 html]# php -e phpinfo.php
phpinfo()
PHP Version => 7.4.33

System => Linux gbase_host01 4.18.0-193.28.1.el7.aarch64 #1 SMP Wed Oct 21 16:25:35 UTC 2020 aarch64
Build Date => Aug 15 2025 12:16:32

...省略...

```

**注：**  
重启php-fpm和nginx方法  
```text
[root@gbase_host01 ~]# nginx -s quit && nginx
[root@gbase_host01 ~]# kill -INT $(cat /usr/local/php/var/run/php-fpm.pid) && php-fpm
```

## 安装GBase ClientSDK  
安装目录为/opt/gbase  
参考：[CSDK安装](../../02_Install/02_CSDK_Lnx.html "CSDK安装")  

在/etc/ld.so.conf.d目录下增加GBase 8s的库目录配置文件gbase8scsdk-aarch64.conf  
```text
[root@gbase_host01 ld.so.conf.d]# pwd
/etc/ld.so.conf.d
[root@gbase_host01 ld.so.conf.d]# more gbase8scsdk-aarch64.conf
/opt/gbase/lib
/opt/gbase/lib/cli
/opt/gbase/lib/esql
```


## 测试ODBC连接到数据库  
编写测试代码php_odbc.php，内容如下：  
```php
<?php
    header('Content-type:text/html;charset=utf-8');
    echo "连接到数据库<br> \n";
    # $conn=odbc_connect("testdb",'','');            # 连接到 dsn = testdb
    $conn=odbc_connect("DRIVER=/opt/gbase/lib/cli/iclis09b.so;HOST=192.168.0.212;SERV=13633;PROT=onsoctcp;SRVR=gbase01;DB=testdb;DLOC=zh_CN.utf8;CLOC=zh_CN.utf8","gbasedbt","GBase123$%");
    if (!$conn)
        {exit("Connection Failed: " . $conn);}
 
    echo "初始化表 tabodbc<br> \n";
    echo "drop table tabodbc<br> \n";
    $sql="drop table if exists tabodbc";
    $rs=odbc_exec($conn,$sql);
 
    echo "create table tabodbc<br> \n";
    $sql="create table tabodbc(col1 int, col2 varchar(255), primary key(col1))";
    $rs=odbc_exec($conn,$sql);
 
    echo "insert into tabodbc<br> \n";
    $sql="insert into tabodbc values(?,?)";
    $stmt=odbc_prepare($conn,$sql);
    $params=array(1,"南大通用");
    $rs=odbc_execute($stmt, $params);
    $params=array(2,"南大通用北京分公司");
    $rs=odbc_execute($stmt, $params);
 
    echo "select from tabodbc<br> \n";
    $sql="select * from tabodbc";
 
    $rs=odbc_exec($conn,$sql);
    if (!$rs)
        {exit("Error in SQL");}
 
    echo "<table> \n<tr>";
    echo "<th>col1</th>";
    echo "<th>col2</th></tr> \n";
 
    while (odbc_fetch_row($rs))
    {
        $col1=odbc_result($rs,"col1");
        $col2=odbc_result($rs,"col2");
        echo "<tr><td>$col1</td>";
        echo "<td>$col2</td></tr> \n";
    }
 
    odbc_close($conn);
 
    echo "</table> \n";

```
执行测试  
```text
[root@gbase_host01 html]# php -e pdo_odbc.php
连接到数据库<br>
初始化表 tabodbc<br>
drop table tabodbc<br>
create table tabodbc<br>
insert into tabodbc<br>
select from tabodbc<br>
<table>
<tr><th>col1</th><th>col2</th></tr>
<tr><td>1</td><td>南大通用</td></tr>
<tr><td>2</td><td>南大通用北京分公司</td></tr>
</table>
```

最后更新日期：2025-09-16  
