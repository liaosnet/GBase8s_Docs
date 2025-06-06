# 安装前准备  
本章节将介绍GBase 8s服务端安装部署所需的前期准备，安装前请根据本文所述内容进行相关配置。  

演示环境如下：  

| **操作系统** | **CPU类型** | **内存大小** |
| --- | --- | --- |
| CentOS 7.9 | x86_64 | 4G |

## 服务器准备  
下表为开发环境最小配置，请根据如下配置自行调整软硬件配置。  

| **类型** | **类型说明** |
| --- | --- |
| 操作系统 | CentOS 7, Ubuntu 18.04.x LTS |
| CPU架构 | x86_64, Arm64 |
| 内存 | 2G，对于mvcc版本不少于4G |
| 硬盘 | 40G |
| 网络 | 以太网千兆 |


## 操作系统内核参数  
下表为GBase 8s数据库所需的资源限制值的最小要求，请根据下表所示将资源限制值调整为大于或等于最小要求的值。  

确认如下内核参数的值，需要更改/etc/sysctl.conf并使之生效  

```text
kernel.shmmax = 18446744073692774399
kernel.shmall = 18446744073692774399
kernel.shmmni = 4096
kernel.sem = 32000 1024000000 32000 32000
vm.swappiness = 0
```

| **参数值** | **资源项** | **描述** | **推荐值** |
| --- | --- | --- | --- |
| nofile | open files | 文件句柄 | 1048576 |
| nproc | max user processes | 最大用户线程数 | 1048576 |
| rss | max memory size | 最大内存限制 | unlimited |


执行如下命令查看系统的所有资源限制值：
```shell
[root@node2 ~]# ulimit -a
core file size          (blocks, -c) 0
data seg size           (kbytes, -d) unlimited
scheduling priority             (-e) 0
file size               (blocks, -f) unlimited
pending signals                 (-i) 19665
max locked memory       (kbytes, -l) 64
max memory size         (kbytes, -m) unlimited
open files                      (-n) 1048576
pipe size            (512 bytes, -p) 8
POSIX message queues     (bytes, -q) 819200
real-time priority              (-r) 0
stack size              (kbytes, -s) 8192
cpu time               (seconds, -t) unlimited
max user processes              (-u) 1048576
virtual memory          (kbytes, -v) unlimited
file locks                      (-x) unlimited
```

操作系统参数调整有如下两种方式，请根据自身需求选择其一进行配置：  

- 配置参数临时生效  
执行如下命令使新配置的资源限制值临时生效，重启后无效：  
```shell
[root@node2 ~]# ulimit -n 1048576
[root@node2 ~]# ulimit -u 1048576
[root@node2 ~]# ulimit -m unlimited
```

- 配置参数永久生效  
执行如下命令将参数写入/etc/security/limits.conf文件，重启后参数永久生效：  
```shell
[root@node2 ~]# cat <<EOF >> /etc/security/limits.conf
 * soft nofile 1048576
 * hard nofile 1048576
 * soft nproc 1048576
 * hard nproc 1048576
 * soft rss unlimited
 * hard rss unlimited
EOF
```

修改/etc/systemd/logind.conf配置文件，关闭RemoveIPC功能  
```text
# 去掉#号
RemoveIPC=no
```

修改/usr/lib/systemd/system/systemd-logind.service配置文件，关闭RemoveIPC功能  
```text
# 增加或者修改为以下
RemoveIPC=no
```

重启服务或重启操作系统   
```shell
systemctl daemon-reload 
systemctl restart systemd-logind.service
```

结果验证确认   
```shell
loginctl show-session | grep RemoveIPC 
systemctl show systemd-logind | grep RemoveIPC
```


## 软件包准备  
请联系技术支持或者直接从官网获取GBase 8s数据库软件包，软件包名称示例：GBase8sV8.8_TL_3.6.3_x86.tar，一键安装脚本名称示例：AutoInit_GBase8s_v1.4.13.tar  
官网下载地址：[https://www.gbase.cn/download/gbase-8s-1?category=INSTALL_PACKAGE](https://www.gbase.cn/download/gbase-8s-1?category=INSTALL_PACKAGE)    
一键安装脚本：[https://gbasedbt.com/dl/AutoInit_GBase8s/latest/](https://gbasedbt.com/dl/AutoInit_GBase8s/latest/)  
