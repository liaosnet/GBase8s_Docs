# Docker部署  
本章节介绍Linux环境下Docker方式部署GBase 8s。  
镜像基于CentOS 7.8系统构建  

## docker pull 方式  
提交在dockerhub上的镜像，最新版本是3.5.1_3x2_8  
直接docker pull即可  
```shell
docker pull docker.io/liaosnet/gbase8s:v8.8_3513x28_csdk_x64
或者
docker pull liaosnet/gbase8s:v8.8_3513x28_csdk_x64
```
通过docker images查看当前的镜像  
```text
[root@h01 ~]# docker images
REPOSITORY         TAG                       IMAGE ID            CREATED       SIZE
liaosnet/gbase8s   v8.8_3513x28_csdk_x64     0e9c03ffad9b        4 weeks ago   636MB
```

## 自构建镜像方式  
自构建镜像，需要下载镜像的压缩包   
下载地址为：
链接：https://pan.baidu.com/s/1RweIxOb8Zr8AGxQschKt_g?pwd=8kqo  
提取码：8kqo  

下载下来的文件名称为3513x28_csdk_x64_20250317.tar.gz  
当前目录解压，并构建镜像  
```shell
tar -zxvf 3513x28_csdk_x64_20250317.tar.gz   

docker build -t liaosnet/gbase8s:v8.8_3513x28_x64 .
```
通过docker images查看当前的镜像  
```text
[root@h01 ~]# docker images
REPOSITORY         TAG                       IMAGE ID            CREATED       SIZE
liaosnet/gbase8s   v8.8_3513x28_csdk_x64     0e9c03ffad9b        4 weeks ago   636MB
```

## 创建容器，运行GBase 8s  
创建容器，并运行GBase 8s   
```shell
docker run -d -p 19088:9088 \
  --name node01 --hostname node01 \
  --privileged=true \
  -e SERVERNAME=gbase01 \
  -e USERPASS=GBase123$% \
  -e CPUS=1 \
  -e MEMS=2048 \
  -v /data/docker:/opt/gbase/data \
  liaosnet/gbase8s:v8.8_3513x28_csdk_x64
```
以上参数中：  
端口9088为数据库使用的内部端口，需要在容器中映射，如使用19088端口    
SERVERNAME对应的是默认服务名称：gbase01  
USERPASS对应的是默认gbasedbt用户密码：GBase123$%  
CPUS对应的是限制容器中使用的cpu数量：1  
MEMS对应的是限制容器中使用的内存总量： 2048 MB  

通过docker ps -a 查看正在运行的容器   
```text
[root@h01 docker]# docker ps -a
CONTAINER ID        IMAGE                                    COMMAND                  CREATED             STATUS              PORTS                     NAMES
98eb1d1998a9        liaosnet/gbase8s:v8.8_3513x28_csdk_x64   "docker_entrypoint.sh"   9 seconds ago       Up 7 seconds        0.0.0.0:19088->9088/tcp   node01
```

## 进入容器  
进入容器查看GBase 8s的部署  
```shell
docker exec -it node01 bash
```
容器ID来源于docker ps -a 的输出  
进入到容器，切换为gbasedbt用户  
```shell
su - gbasedbt
```
即为GBase 8s在docker容器中的环境  
