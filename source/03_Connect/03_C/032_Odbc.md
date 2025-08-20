# C语言使用ODBC方式连接到数据库（Linux）  
本章节将介绍C程序通过ODBC连接到GBase 8s数据库的方式。  
ODBC是CSDK的一部分，因此本操作依赖CSDK；同时ODBC依赖于操作系统的unixODBC。  

## 依赖包  
```text
[root@localhost ~]# yum install -y autoconf gcc gcc-c++ unixODBC unixODBC-devel  
```

## 安装GBase ClientSDK  
安装目录为/opt/gbase  
参考：[CSDK安装](../../02_Install/02_CSDK_Lnx.html "CSDK安装")  

在/etc/ld.so.conf.d目录下增加GBase 8s的库目录配置文件gbase8scsdk-x86_64.conf  
```text
[root@localhost ld.so.conf.d]# pwd
/etc/ld.so.conf.d
[root@localhost ld.so.conf.d]# more gbase8scsdk-x86_64.conf
/opt/gbase/lib
/opt/gbase/lib/cli
/opt/gbase/lib/esql
```

## ODBC连接测试  
### 编译测试程序TestCOdbc.c   
`TestCOdbc.c`内容如下：  
```text
/////////////////////////////////////////////////////////////
// GBase 8s ODBC Applicatin Examples
//

// TestCOdbcDemo "DSN=odbc1"
// TestCOdbcDemo "DRIVER=/opt/gbase/lib/cli/iclis09b.so;SERVER=gbase01;DATABASE=db1;HOST=x.x.x.x;PROTOCOL=onsoctcp;SERVICE=5555;UID=user1;PWD=xyz;";

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#ifdef _WIN32
#include <windows.h>
#define strdup _strdup
#endif

#ifdef DRIVER_MANAGER
#include "sql.h"
#include "sqlext.h"
#else
#include <infxcli.h>
#endif

void GetDiagRec(SQLRETURN rc, SQLSMALLINT htype, SQLHANDLE hndl, char *szMsgTag);
int ReadResult(SQLHDBC hdbc, char *SqlSelect);
void  MyServerSetup(SQLHDBC hdbc);


int main(int argc, char *argv[])
{
    // 可使用DSN，需配置好ODBCINI
    SQLCHAR     ConnStrIn[1024] = "DSN=odbc1";
    SQLHANDLE   henv = NULL;
    SQLHANDLE   hdbc = NULL;
    int         rc = 0;

    char   *MyLocalConnStr = "DRIVER=/opt/gbase/lib/cli/iclis09b.so;SERVER=srv1;DATABASE=xb1;HOST=xyz.abc.com;PROTOCOL=onsoctcp;SERVICE=5550;UID=user1;PWD=xyz;";

    if (argc == 1)
    {
        if (sizeof(int *) == 8)  // 64bit application
        {
            // 显示指定连接串
            MyLocalConnStr = "DRIVER=/opt/gbase/lib/cli/iclis09b.so;HOST=192.168.0.212;SERVER=gbase01;SERVICE=13633;PROTOCOL=onsoctcp;DATABASE=testdb;UID=gbasedbt;PWD=GBase123$%;DB_LOCALE=zh_CN.utf8;CLIENT_LOCALE=zh_CN.utf8;";
        }
        strcpy((char *)ConnStrIn, MyLocalConnStr);

    }
    else if (argc == 2)
    {
        strcpy( (char *)ConnStrIn,  argv[1] );
    }
    else
    {
        strcpy((char *)ConnStrIn, MyLocalConnStr);

        if (0)
        {
            printf("\n Usage option is :");
            printf("\n %s    <Connection String>", argv[0]);
            printf("\n Example :");
            printf("\n %s   \"DSN=MyOdbcDsnName; uid=MyUserName; pwd=MyPassword;\" ", argv[0]);
            printf("\n OR ");
            printf("\n %s  \"%s\" ", argv[0], MyLocalConnStr);
            printf("\n\n");
            exit(0);
        }
    }


    rc = SQLAllocHandle(SQL_HANDLE_ENV, SQL_NULL_HANDLE, &henv);

    rc = SQLSetEnvAttr(henv, SQL_ATTR_ODBC_VERSION, (void*)SQL_OV_ODBC3, 0);

    rc = SQLAllocHandle(SQL_HANDLE_DBC, henv, &hdbc);
    rc == 0 ? 0 : GetDiagRec(rc, SQL_HANDLE_ENV, henv, "SQLAllocHandle");

    printf("\n***************************************************\n");
    printf("\n Connecting with : \n [%s] \n", (char *)ConnStrIn);
    printf("\n***************************************************\n");

    rc = SQLDriverConnect(hdbc, NULL, ConnStrIn, SQL_NTS, NULL, 0, NULL, SQL_DRIVER_NOPROMPT);
    if (rc != 0)
    {
        printf("\n Connection Error (:- \n");
        GetDiagRec(rc, SQL_HANDLE_DBC, hdbc, "SQLDriverConnect");
        goto Exit;
    }
    else
    {
        printf("\n Connection Success! \n");
    }

    if (1)
    {
        // Try Basic Setup
        MyServerSetup(hdbc);
        ReadResult(hdbc, "SELECT * FROM t1");
    }


Exit:
    SQLDisconnect(hdbc);
    SQLFreeHandle(SQL_HANDLE_DBC, hdbc);
    SQLFreeHandle(SQL_HANDLE_ENV, henv);

    return(0);
}


void GetDiagRec(SQLRETURN rc, SQLSMALLINT htype, SQLHANDLE hndl, char *szMsgTag)
{
    SQLCHAR message[SQL_MAX_MESSAGE_LENGTH + 1];
    SQLCHAR sqlstate[SQL_SQLSTATE_SIZE + 1];
    SQLINTEGER sqlcode = 0;
    SQLSMALLINT length = 0;

    if (szMsgTag == NULL)
    {
        szMsgTag = "---";
    }

    printf("\n %s: %d : ", szMsgTag, rc);
    if (rc >= 0)
    {
        printf(" OK [rc=%d] \n", rc);
    }
    else
    {
        int i = 1;
        printf(" FAILED : %i", rc);
        while (SQLGetDiagRec(htype,
            hndl,
            i,
            sqlstate,
            &sqlcode,
            message,
            SQL_MAX_MESSAGE_LENGTH + 1,
            &length) == SQL_SUCCESS)
        {
            printf("\n SQLSTATE          = %s", sqlstate);
            printf("\n Native Error Code = %ld", sqlcode);
            printf("\n %s", message);
            i++;
        }
        printf("\n-------------------------\n");
    }
}


void  MyServerSetup(SQLHDBC hdbc)
{
    SQLRETURN   rc = 0;
    SQLHSTMT    hstmt = NULL;    int         i = 0;

    static unsigned char *SetupSqls[] =
    {
        "DROP TABLE t1;",
        "CREATE TABLE t1 ( c1 INT, c2  char(15),  c3 FLOAT, c4 char(10) )",
        "INSERT INTO  t1 VALUES ( 1, 'aaa-1', 11.55, 'bbbb-1' );",
        "INSERT INTO  t1 VALUES ( 2, 'aaa-2', 12.55, 'bbbb-2' );",
        NULL,
    };

    rc = SQLAllocHandle(SQL_HANDLE_STMT, hdbc, &hstmt);
    rc == 0 ? 0 : GetDiagRec(rc, SQL_HANDLE_DBC, hdbc, "MyServerSetup::SQLAllocHandle::SQL_HANDLE_STMT");

    for (i = 0; SetupSqls[i] != NULL; ++i)
    {
        rc = SQLExecDirect(hstmt, SetupSqls[i], SQL_NTS);
        printf("\n[%d] %s", rc, SetupSqls[i]);
    }


    if (hstmt)
    {
        SQLFreeStmt(hstmt, SQL_CLOSE);
        SQLFreeHandle(SQL_HANDLE_STMT, hstmt);
    }
}


int ReadResult(SQLHDBC hdbc, char *SqlSelect)
{
    SQLRETURN       rc = 0;
    SQLHSTMT        hstmt = NULL;
    SQLCHAR         ReadBuffer[1024];
    int             ReadBufferSize = sizeof(ReadBuffer) - 2;

    printf("\n\n ----ReadResult ----");


    rc = SQLAllocHandle(SQL_HANDLE_STMT, hdbc, &hstmt);
    rc == 0 ? 0 : GetDiagRec(rc, SQL_HANDLE_DBC, hdbc, "SQLAllocHandle:SQL_HANDLE_STMT");


    rc = SQLExecDirect(hstmt, SqlSelect, SQL_NTS);
    if ((rc == SQL_SUCCESS || rc == SQL_SUCCESS_WITH_INFO))
    {
        SQLSMALLINT     ColumnCount = 0;
        int             RowNum = 0;

        rc = SQLNumResultCols(hstmt, &ColumnCount);
        printf("\nNumber of colum in the result is %d ---\n", ColumnCount);


        while ((rc = SQLFetch(hstmt)) != SQL_NO_DATA)
        {
            SQLLEN StrLen_or_IndPtr = 0;
            int NumBytes = 0;
            int col = 0;

            ++RowNum;
            printf("\n\n -Fetching Row# %d-", RowNum);

            for (col = 1; col <= ColumnCount; ++col)
            {

                memset(ReadBuffer, 0, sizeof(ReadBuffer));
                StrLen_or_IndPtr = 0;

                rc = SQLGetData(hstmt, col, SQL_C_CHAR, ReadBuffer, ReadBufferSize, &StrLen_or_IndPtr);
                if (rc == SQL_NO_DATA)
                {
                    break;
                }
                if (rc < 0)
                {
                    GetDiagRec(rc, SQL_HANDLE_STMT, hstmt, "SQLGetData");
                    break;
                }

                NumBytes = (int)((StrLen_or_IndPtr > ReadBufferSize) || (StrLen_or_IndPtr == SQL_NO_TOTAL) ? ReadBufferSize : StrLen_or_IndPtr);

                ReadBuffer[NumBytes] = 0;
                printf("\nColum_%d = %s", col, ReadBuffer);
            }
        }

    }
    else
    {
        GetDiagRec(rc, SQL_HANDLE_STMT, hstmt, SqlSelect);
    }

    if (hstmt)
    {
        SQLFreeStmt(hstmt, SQL_CLOSE);
        rc = SQLFreeStmt(hstmt, SQL_UNBIND);
        rc = SQLFreeStmt(hstmt, SQL_RESET_PARAMS);
        SQLFreeHandle(SQL_HANDLE_STMT, hstmt);
    }

    printf("\n");
    return (0);
}
```

### 编写makefile文件  
内容如下：  
```text
#gcc -g -m64 -I/work/csdk/incl/cli -c TestCOdbc.c
#gcc -g -m64 -o TestCOdbc TestCOdbc.o -L/work/csdk/lib/cli -lifdmr -lthcli


#GBASEDBTDIR=/work/csdk
ODBCLIB_DIR  = -L$(GBASEDBTDIR)/lib/cli   -lthcli

INCLDIR  = -I$(GBASEDBTDIR)/incl/cli
CFLAGS  = -g
CC = gcc
RM = rm

TARGET = TestCOdbc

all : $(TARGET)

$(TARGET) : $(TARGET).o
        $(CC) $(CFLAGS)  -m64 -o $(TARGET) $(TARGET).o  $(ODBCLIB_DIR)

$(TARGET).o : $(TARGET).c
        $(CC) $(CFLAGS) -m64 $(INCLDIR) -c $(TARGET).c

clean :
        $(RM) $(TARGET) $(TARGET).o

```
注意：需使用tab缩进makefile文件  


### 编译成可执行文件，并执行测试  
```text
[root@localhost c]# make
gcc -g -m64 -I/opt/gbase/incl/cli -c TestCOdbc.c
gcc -g  -m64 -o TestCOdbc TestCOdbc.o  -L/opt/gbase/lib/cli   -lthcli
```
使用DSN时使用：  
```shell
TestCOdbc "DSN=testdb" 
```
使用程序内的字符串时:  
```shell
TestCOdbc 
```
使用指定DSN-Less（自定义DSN字符串）时：  
```shell  
TestCOdbc "DRIVER=/opt/gbase/lib/cli/iclis09b.so;HOST=192.168.0.212;SERVER=gbase01;SERVICE=13633;PROTOCOL=onsoctcp;DATABASE=testdb;UID=gbasedbt;PWD=GBase123$%;DB_LOCALE=zh_CN.utf8;CLIENT_LOCALE=zh_CN.utf8;" 
```
方式进行测试。  
测试输出：  
```text
[root@localhost c]# ./TestCOdbc

***************************************************

 Connecting with :
 [DRIVER=/opt/gbase/lib/cli/iclis09b.so;HOST=192.168.0.212;SERVER=gbase01;SERVICE=13633;PROTOCOL=onsoctcp;DATABASE=testdb;UID=gbasedbt;PWD=GBase123$%;DB_LOCALE=zh_CN.utf8;CLIENT_LOCALE=zh_CN.utf8;]

***************************************************

 Connection Success!

[-1] DROP TABLE t1;
[0] CREATE TABLE t1 ( c1 INT, c2  char(15),  c3 FLOAT, c4 char(10) )
[0] INSERT INTO  t1 VALUES ( 1, 'aaa-1', 11.55, 'bbbb-1' );
[0] INSERT INTO  t1 VALUES ( 2, 'aaa-2', 12.55, 'bbbb-2' );

 ----ReadResult ----
Number of colum in the result is 4 ---


 -Fetching Row# 1-
Colum_1 = 1
Colum_2 = aaa-1
Colum_3 = 11.55
Colum_4 = bbbb-1

 -Fetching Row# 2-
Colum_1 = 2
Colum_2 = aaa-2
Colum_3 = 12.55
Colum_4 = bbbb-2
```

最后更新日期：2025-08-19  
