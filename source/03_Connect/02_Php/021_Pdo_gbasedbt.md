# PHP使用PDO_GBASEDBT方式连接到数据库（Linux）  
本章节将介绍PHP程序通过PDO_GBASEDBT连接到GBase 8s数据库的方式。  
PHP环境使用nginx+php-fpm，使用纯编译方式。  

## 示例环境介绍  
操作系统：CentOS Linux release 7.9.2009 （aarch64）  
数据库版本：GBase 8s v8.8_3.6.3_3x2_1  
客户端连接工具：clientsdk_3.6.3_3X2_1_783c8d  

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
[root@gbase_host01 php-7.4.33]# ./configure --prefix=/usr/local/php -with-config-file-path=/usr/local/php/etc --enable-fpm

[root@gbase_host01 php-7.4.33]# make -j 4
```
**注：aarch64架构下，数组函数zif_array_sum编译错误，通过修改zend_operators.h文件中ZEND_USE_ASM_ARITHMETIC的值为0来解决**  
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
env[GBASEDBTDIR]=/opt/gbase
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

## php集成安装PDO_GBASEDBT  
下载`PDO_GBASEDBT-1.3.6`（当前版本） [PDO_GBASEDBT](https://gbasedbt.com/dl/PDO_GBasedbt "PDO_GBASEDBT") 
按平台下载版本（`PDO_GBASEDBT-1.3.6.tgz`为原始代码，`PDO_GBASEDBT-1.3.6_aarch64_patch.tgz`为修复aarch64问题的包），解压  

集成，编译  
```text
[root@gbase_host01 PDO_GBASEDBT-1.3.6]# pwd
/root/PDO_GBASEDBT-1.3.6
[root@gbase_host01 PDO_GBASEDBT-1.3.6]# phpize
[root@gbase_host01 PDO_GBASEDBT-1.3.6]# ./configure --with-pdo-gbasedbt=/opt/gbase
[root@gbase_host01 PDO_GBASEDBT-1.3.6]# make -j 4
[root@gbase_host01 PDO_GBASEDBT-1.3.6]# make install
```

最终在php/lib/php/extensions/no-debug-non-zts-20190902/下生成pdo_gbasedbt.so  
```text
[root@gbase_host01 PDO_GBASEDBT-1.3.6]# ls -al /usr/local/php/lib/php/extensions/no-debug-non-zts-20190902/
total 7144
drwxr-xr-x. 2 root root      64 Aug 15 13:23 .
drwxr-xr-x. 3 root root      39 Aug 15 12:51 ..
-rwxr-xr-x. 1 root root 4608134 Aug 15 12:51 opcache.a
-rwxr-xr-x. 1 root root 2539208 Aug 15 12:51 opcache.so
-rwxr-xr-x. 1 root root  192928 Aug 15 13:23 pdo_gbasedbt.so
```

复制php源码目录下的php.ini-development到php安装目录下etc/php.ini  
```text
[root@gbase_host01 etc]# pwd
/usr/local/php/etc
[root@gbase_host01 etc]# cp /root/php-7.4.33/php.ini-development php.ini
```
在php.ini中增加  
```text
extension=pdo_gbasedbt.so
```

重启php-fpm和nginx  
```text
[root@gbase_host01 ~]# nginx -s quit && nginx
[root@gbase_host01 ~]# kill -INT $(cat /usr/local/php/var/run/php-fpm.pid) && php-fpm
```

重新查看phpinfo.php，应当有pdo_gbasedbt条目  

## 测试PDO_GBASEDBT连接到数据库  
编写测试代码pdo_gbasedbt.php，内容如下：  
```php
<?php
<?php
    header('Content-type:text/html;charset=utf-8');
    # 按实际修改地址、端口、用户及密码
    $dbh = new PDO("gbasedbt:HOST=192.168.0.212;SERV=13633;PROT=onsoctcp;SRVR=gbase01;DB=testdb;DLOC=zh_CN.utf8;CLOC=zh_CN.utf8","gbasedbt","GBase123$%");
    # 指定数据库连接指令

    echo "初始化表 tabpdogbasedbt<br>" . "\n";
    echo "drop table tabpdogbasedbt<br>" . "\n";
    $sql="drop table if exists tabpdogbasedbt";
    $dbh->exec($sql);

    echo "create table tabpdogbasedbt<br>" . "\n";
    $sql="create table tabpdogbasedbt(col1 int, col2 varchar(255), primary key(col1))";
    $dbh->exec($sql);

    echo "insert into tabpdogbasedbt<br>" . "\n";
    $sql="insert into tabpdogbasedbt values(?,?)";
    $stmt = $dbh->prepare($sql);
    $stmt->execute([1,'南大通用']);
    $stmt = $dbh->prepare($sql)->execute([2,'南大通用北京分公司']);

    echo "select from tabpdogbasedbt<br>" . "\n";
    $sql="select * from tabpdogbasedbt";
    $stmt = $dbh->query($sql);
    $rows = $stmt->fetchAll();

    echo "<table><tr>";
    echo "<th>col1</th>";
    echo "<th>col2</th></tr>";

    foreach($rows as $row) {
        # 需要使用大写字段名称
        echo "<tr><td>$row[0]</td>";
        echo "<td>$row[COL2]</td></tr>" . "\n";
    }

    echo "</table>";
```
执行测试  
```text
[root@gbase_host01 html]# php -e pdo_gbasedbt.php
初始化表 tabpdogbasedbt<br>
drop table tabpdogbasedbt<br>
create table tabpdogbasedbt<br>
insert into tabpdogbasedbt<br>
select from tabpdogbasedbt<br>
<table><tr><th>col1</th><th>col2</th></tr><tr><td>1</td><td>南大通用</td></tr>
<tr><td>2</td><td>南大通用北京分公司</td></tr>
</table>
```

**附注：aarch64架构中，需要在源码中的pdo_gbasedbt.c以下内容**  
即：`PDO_GBASEDBT-1.3.6.tgz`和`PDO_GBASEDBT-1.3.6_aarch64_patch.tgz`间的差异  
```text
zend_function_entry pdo_gbasedbt_functions[] =
{
//	PHP_FE(confirm_pdo_gbasedbt_compiled, NULL)	/* For testing, remove later. */
//	{
//		NULL, NULL, NULL
//	}	/* Must be the last line in pdo_gbasedbt_functions[] */
};
```
修改为  
```text
zend_function_entry pdo_gbasedbt_functions[] =
{
    PHP_FE_END
};
```

最后更新日期：2025-08-19  
