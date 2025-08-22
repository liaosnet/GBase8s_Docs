# 数据库实例启停  
本章节将介绍GBase 8s数据库的实例启停方式。数据库安装过程中将实例自动切换成On-Line状态  

## 数据库实例基本启停操作  
### 检查状态  
切换到gbasedbt用户，执行如下命令查看当前实例状态，状态显示为 On-Line  
```text
[root@node2 install]# su - gbasedbt
上一次登录：二 6月 18 17:30:52 CST 2024pts/1 上

[gbasedbt@node2 ~]$ onstat -
On-Line -- Up 00:13:17 -- 3378128 Kbytes
```

### 关闭实例  
执行如下命令关闭GBase 8s数据库服务，状态显示为 共享内存未初始化  
```text
[gbasedbt@node2 ~]$ onmode -ky

[gbasedbt@node2 ~]$ onstat -
shared memory not initialized for GBASEDBTSERVER 'gbase01'
```

### 启动实例  
启动数据库服务，最终状态显示为 On-Line  
```text
[gbasedbt@node2 ~]$ oninit -y

[gbasedbt@node2 ~]$ onstat -
On-Line -- Up 00:00:15 -- 3378128 Kbytes
```

注：如需进行正常的数据库操作，请将实例切换至On-Line。  

## 数据库服务方式启停操作  
### 检查状态  
检查服务状态  
```text
root@netsky:~# systemctl status GBaseService_gbase01.service
```

### 关闭实例  
关闭实例  
```text
root@netsky:~# systemctl stop GBaseService_gbase01.service

root@netsky:~# systemctl status GBaseService_gbase01.service
○ GBaseService_gbase01.service - GBase 8s Database Server
     Loaded: loaded (/lib/systemd/system/GBaseService_gbase01.service; enabled; vendor preset: enabled)
     Active: inactive (dead)
       Docs: file:/opt/gbase/release/en_us/0333
```

### 启动实例  
启动实例  
```text
root@netsky:~# systemctl start GBaseService_gbase01.service

root@netsky:~# systemctl status GBaseService_gbase01.service
● GBaseService_gbase01.service - GBase 8s Database Server
     Loaded: loaded (/lib/systemd/system/GBaseService_gbase01.service; enabled; vendor preset: enabled)
     Active: active (running) since Wed 2025-08-20 09:27:30 UTC; 18s ago
       Docs: file:/opt/gbase/release/en_us/0333
    Process: 186328 ExecStart=/opt/gbase/bin/oninit (code=exited, status=0/SUCCESS)
   Main PID: 186330 (oninit)
      Tasks: 25 (limit: 4514)
     Memory: 543.5M
        CPU: 1.480s
     CGroup: /system.slice/GBaseService_gbase01.service
    ......
```

注：正常运行的状态是：active (running)  

最后更新日期：2025-08-20  
