# JDBC安装与配置  
本章节将介绍GBase 8s JDBC客户端安装部署。  

## JDBC安装  
JDBC以独立的jar包提供，不需要额外的安装  
可通过maven中央仓库直接获取驱动包，地址为：  
[JDBC mvn仓库](https://mvnrepository.com/artifact/com.gbasedbt/jdbc "JDBC mvn仓库")  

使用方式：  
```xml
<dependency>
  <groupId>com.gbasedbt</groupId>
  <artifactId>jdbc</artifactId>
  <version>3.6.3.32</version>
</dependency>
```

或者使用数据库版本一同分发中的jar包，文件名形如：  
```text
gbasedbtjdbc_3.6.3_3X2_1_377ee9.jar
```

最后更新日期：2025-08-18  
