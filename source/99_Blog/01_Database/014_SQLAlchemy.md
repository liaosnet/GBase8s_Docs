# GBase 8s数据库使用sqlalchemy框架  

## 测试环境  
* 操作系统：Ubuntu 22.04.3 LTS （x86_64)  
* 数据库版本：GBase 8s v8.8_3.6.3_3x2_1  
* Python3版本：Python 3.10.12 （系统自带）  
* gbase8s-sqlalchemy版本：2.0.1 (https://pypi.org/project/gbase8s-sqlalchemy)  
* gbase8sdb版本：0.2.2 (https://pypi.org/project/gbase8sdb)  
* SQLAlchemy版本：2.0.42 (~=2.0)  


## 确认安装python3及版本  
确认已经安装python3和pip3  
```shell
root@netsky:~# python3 --version
Python 3.10.12
root@netsky:~# pip3 --version
pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)
```
如果没有安装，建议使用apt -y install python3来安装。  

## 安装gbase8s-sqlalchemy，gbase8sdb，SQLAlchemy  
gbase8s-sqlalchemy：GBase 8s数据库的SQLAlchemy方言, 支持的 Python 版本：Python >=3.7，支持GBase 8s V8.8_3.6.2版本及以上。  
```shell
root@netsky:~# pip3 install gbase8s-sqlalchemy
```
gbase8sdb：支持的 Python 版本：3.8 至 3.13，支持的 GBase 8s 数据库版本：GBase 8s V8.8_3.6.2版本及以上，依赖 GSDK 1.1 版本。
```shell
root@netsky:~# pip3 install gbase8sdb
```
SQLAlchemy：支持的 Python 版本：Python >=3.7
```shell
root@netsky:~# pip3 install SQLAlchemy~=2.0
```
确认均已经安装  
```shell
root@netsky:~# pip3 list | egrep '(gbase8s|SQLAlchemy)'
gbase8s-sqlalchemy     2.0.1
gbase8sdb              0.2.2
SQLAlchemy             2.0.42
```

## 安装GSDK  
GSDK需要使用1.1.x版本，该版本暂时需要通过GBase 8s技术支持或通过官方渠道获取。  
如下，本次使用的版本为：
GSDK_3.6.3_3_1.1.0_1P20250403_b793cf_RHEL6_x86_64.tar  
说明：  
* 3.6.3_3：对应的数据库版本号  
* 1.1.0_1P20250605：GSDK版号本  
* b793cf：内部GIT  
* RHEL6：编译的操作系统版本  
* x86_64：适用的架构  

上传到服务器，解压并改名  
```shell
tar -xvf GSDK_3.6.3_3_1.1.0_1P20250403_b793cf_RHEL6_x86_64 -C /opt
mv /opt/GSDK_3.6.3_3_1.1.0_1P20250403_b793cf_RHEL6_x86_64 /opt/GSDK
```

设置环境变量，并加载  
```shell
root@netsky:~# more env_gsdk
export GSDK_PATH=/opt/GSDK
export LD_LIBRARY_PATH=${GSDK_PATH}/lib:$LD_LIBRARY_PATH
export GBASEDBTDIR=${GSDK_PATH}/lib

root@netsky:~# . env_gask
```

## 编写测试代码并执行测试  
测试代码test_gbase8s_sqlalchemy.py  
```python
from sqlalchemy import create_engine,Column,String,Table
from sqlalchemy.orm import sessionmaker,declarative_base

username = 'gbasedbt'
password = 'GBase123$%'
ip = '192.168.0.212'
port = 9088
dbname = 'testdb'
servername = 'gbase01'
url = f'gbase8s+gbase8sdb://{username}:{password}@{ip}:{port}/{dbname}?GBASEDBTSERVER={servername}&DB_LOCALE=zh_CN.utf8'
# 或使用sqlhosts文件连接
# url = f'gbase8s+gbase8sdb://{username}:{password}@{dbname}?GBASEDBTSERVER={servername}&DB_LOCALE=zh_CN.utf8&SQLH_FILE=/path/to/sqlhosts'
engine = create_engine(url, echo=True)

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 创建对象
Base.metadata.create_all(engine)

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()

# 创建新User对象:
new_user = User(id='2', name='测试用户')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='2').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
# 关闭Session:
session.close()
```
执行测试：  
```shell
root@netsky:~# python3 test_gbase8s_sqlalchemy.py
2025-08-07 01:59:52,362 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-08-07 01:59:52,362 INFO sqlalchemy.engine.Engine select count(*) from systables
            where tabname=? and tabtype in (?,?)

2025-08-07 01:59:52,363 INFO sqlalchemy.engine.Engine [raw sql] ('user', 'T', 'V')
2025-08-07 01:59:52,381 INFO sqlalchemy.engine.Engine
CREATE TABLE "user" (
        id VARCHAR(20) NOT NULL,
        name VARCHAR(20),
        PRIMARY KEY (id)
)


2025-08-07 01:59:52,382 INFO sqlalchemy.engine.Engine [no key 0.00017s] ()
2025-08-07 01:59:52,403 INFO sqlalchemy.engine.Engine COMMIT
2025-08-07 01:59:52,408 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-08-07 01:59:52,411 INFO sqlalchemy.engine.Engine INSERT INTO "user" (id, name) VALUES (?, ?)
2025-08-07 01:59:52,412 INFO sqlalchemy.engine.Engine [generated in 0.00050s] ('2', '测试用户')
2025-08-07 01:59:52,441 INFO sqlalchemy.engine.Engine COMMIT
2025-08-07 01:59:52,446 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-08-07 01:59:52,450 INFO sqlalchemy.engine.Engine SELECT "user".id AS user_id, "user".name AS user_name
FROM "user"
WHERE "user".id = ?
2025-08-07 01:59:52,450 INFO sqlalchemy.engine.Engine [generated in 0.00036s] ('2',)
type: <class '__main__.User'>
name: 测试用户
2025-08-07 01:59:52,484 INFO sqlalchemy.engine.Engine ROLLBACK
```
注：此为第一次测试，如进行第二次测试，将会报（ERROR: -268:  23000 : 完整性限制违反）错，原因是数据已经存在。  

注：
使用sqlalchemy1.4.x版本，请使用以下对应关系。其它的保持不变。  
gbase8s-sqlalchemy版本：1.4.2 (https://pypi.org/project/gbase8s-sqlalchemy)  
SQLAlchemy版本：1.4.54 (~=1.4) 