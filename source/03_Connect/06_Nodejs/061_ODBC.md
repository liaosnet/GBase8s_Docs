# Node.js使用ODBC方式连接到数据库（Linux）  
本章节将介绍Node.js程序通过ODBC连接到GBase 8s数据库的方式。  
ODBC是CSDK的一部分，因此本操作依赖CSDK；同时ODBC依赖于操作系统的unixODBC。  

## 示例环境介绍  
操作系统：Ubuntu 22.04.3 LTS （x86_64）  
数据库版本：GBase 8s v8.8_3.6.3_3x2_1  
NodeJs版本：v22.18.0(LTS) (https://nodejs.org/en/download)  

## 依赖包  
```text
rootnetsky:~# apt -y install autoconf gcc g++ unixodbc unixodbc-dev
```

## 安装GBase ClientSDK及配置ODBC  
安装目录为/opt/gbase  
参考：[CSDK安装](../../02_Install/02_CSDK_Lnx.html "CSDK安装")  

在/etc/ld.so.conf.d目录下增加GBase 8s的库目录配置文件gbase8scsdk-x86_64.conf  
```text
rootnetsky:/etc/ld.so.conf.d# pwd
/etc/ld.so.conf.d
rootnetsky:/etc/ld.so.conf.d# more gbase8scsdk-x86_64.conf
/opt/gbase/lib
/opt/gbase/lib/cli
/opt/gbase/lib/esql
```

设置环境变量，并加载  
```shell
root@netsky:~# more env_csdk
export GBASEDBTDIR=/opt/gbase
export PATH=$GBASEDBTDIR/bin:$PATH
export LD_LIBRARY_PATH=$GBASEDBTDIR/lib:$GBASEDBTDIR/lib/cli:$GBASEDBTDIR/lib/esql:$LD_LIBRARY_PATH
# ODBCINI
export ODBCINI=/opt/gbase/etc/odbc.ini

root@netsky:~# . env_csdk
```

配置ODBCINI配置文件，根据CSDK环境，配置如下：  
```text
[ODBC Data Sources]
testdb=GBase ODBC DRIVER
;
; Define ODBC Database Driver's Below - Driver Configuration Section
;
[testdb]
Driver=/opt/gbase/lib/cli/iclit09b.so
Driver=GBase ODBC DRIVER
Description=GBase ODBC DRIVER
Database=testdb
LogonID=gbasedbt
pwd=GBase123$%
Servername=gbase01
CursorBehavior=0
CLIENT_LOCALE=zh_CN.utf8
DB_LOCALE=zh_CN.utf8
GL_USEGLU=1
TRANSLATIONDLL=/opt/gbase/lib/esql/igo4a304.so
; ISOLATIONLEVEL=1	# 使用该参数（简写：ISOLVL）设置默认的隔离级别，0-5
;
; UNICODE connection Section
;
[ODBC]
;uncomment the below line for UNICODE connection
UNICODE=UCS-2		# 如果需要使用unicode连接数据库，这里需要去除注释，值改为UCS-2
;
; Trace file Section
;
Trace=0
TraceFile=/tmp/odbctrace.out
InstallDir=/opt/gbase
TRACEDLL=idmrs09a.so
```

## 安装Node.js  
安装Node.js可直接下载二进制包的方式。示例使用Node.js v22.18.0(LTS)  
下载、解压  
```text
root@netsky:~# wget https://nodejs.org/dist/v22.18.0/node-v22.18.0-linux-x64.tar.xz

root@netsky:~# tar -Jxf node-v22.18.0-linux-x64.tar.xz

root@netsky:~# mv node-v22.18.0-linux-x64 /usr/local/node
```

设置环境变量文件（也可以写入到/etc/profile中）  
```text
# node.js的目录NODEDIR
export NODEDIR=/usr/local/node
export PATH=$NODEDIR/bin:$PATH
```

加载环境变量，确认版本  
```text
root@netsky:~# node --version
v22.18.0
root@netsky:~# npm --version
10.9.3
```

## Node.js安装node-gyp和odbc  
通过npm安装node-gyp和odbc  
```text
root@netsky:~# npm install node-gyp

root@netsky:~# npm install odbc

# 验证
root@netsky:~# npm list | egrep '(node-gyp|odbc)'
├── node-gyp@11.4.1
└── odbc@2.4.9
```

## 编写测试代码  
编写测试程序`TestNodejsODBC.js`  
`Node.js`使用odbc方式，参考：https://www.npmjs.com/package/odbc  
```js
const odbc = require('odbc');

async function DB() {
    const connectionConfig = {
        // 使用DSN连接
        connectionString: 'DSN=testdb',
        // 也可以使用DSN-Less连接
        // connectionString: 'DRIVER=/opt/gbase/lib/cli/iclis09b.so;HOST=192.168.0.212;SERVER=gbase01;SERVICE=13633;PROTOCOL=onsoctcp;DATABASE=testdb;UID=gbasedbt;PWD=GBase123$%;DB_LOCALE=zh_CN.utf8;CLIENT_LOCALE=zh_CN.utf8;',
        connectionTimeout: 10,
        loginTimeout: 10,
    }
    const connection = await odbc.connect(connectionConfig);

    const statement = await connection.createStatement();
    await statement.prepare('drop table if exists company;');
    await statement.execute();
    console.log('删除表');

    await statement.prepare('create table company(coid serial,coname varchar(255),coaddr varchar(255), primary key(coid));');
    await statement.execute();
    console.log('创建表');

    // 事务
    await connection.beginTransaction();
    await statement.prepare('insert into company values (0,?,?),(0,?,?);');
    await statement.bind(['GBase','TJ','GBase Beijin','BJ']);
    await statement.execute();
    await connection.commit();
    console.log('插入表');

    await statement.prepare('select * from company;');
    const result = await statement.execute();
    console.log(result);
    console.log('查询表');
}

DB();
```
执行测试  
```text
root@netsky:~# node TestNodejsODBC.js
删除表
创建表
插入表
[
  { coid: 1, coname: 'GBase', coaddr: 'TJ' },
  { coid: 2, coname: 'GBase Beijin', coaddr: 'BJ' },
  statement: 'select * from company;',
  parameters: [],
  return: undefined,
  count: -1,
  columns: [
    {
      name: 'coid',
      dataType: 4,
      dataTypeName: 'SQL_INTEGER',
      columnSize: 10,
      decimalDigits: 0,
      nullable: false
    },
    {
      name: 'coname',
      dataType: 12,
      dataTypeName: 'SQL_VARCHAR',
      columnSize: 255,
      decimalDigits: 0,
      nullable: true
    },
    {
      name: 'coaddr',
      dataType: 12,
      dataTypeName: 'SQL_VARCHAR',
      columnSize: 255,
      decimalDigits: 0,
      nullable: true
    }
  ]
]
查询表
```

最后更新日期： 2025-08-22  
