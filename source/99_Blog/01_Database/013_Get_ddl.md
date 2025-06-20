# 获取表结构的存储过程  

## 通过存储过程获取建表语句  

```sql
drop PROCEDURE if exists get_ddl(varchar,varchar,varchar,smallint);
/*******************************************************************
 * PROCEDURE: get_ddl(OBJECT_TYPE, OWNER, OBJECT_NAME, DELIMIDENT
 * DESCRIPTION: get schema for OBJECT_NAME
 *              OBJECT_TYPE : table, indexes, view, synonym, procedure
 *              OWNER not use now.
 * USAGE EG : get_dll('table', 'gbasedbt', 'Tab1', 1)
 * WRITE BY : liaosnet@gbasedbt.com 2024-10-21
 * UPDATE   : 2025-04-03 support DELIMIDENT
 * UPDATE   ：2025-06-18 fix indexes oracle mode 201 error 
 *******************************************************************/
create PROCEDURE get_ddl(p_type varchar(40), p_user varchar(32), p_name varchar(128), p_del smallint default 0)
returning lvarchar(32000) as ddl;
  define v_numtab int;
  define v_tabname varchar(128);
  define v_ddl lvarchar(32000);
  define v_colname varchar(128);
  define v_coltype_name varchar(128);
  define v_nullable varchar(128);
  define v_defvalue varchar(254);
  define v_deftype  varchar(10);
  define v_collength int;
  define v_decimal_p int;
  define v_decimal_s int;
  define v_pk_collist lvarchar(2048);
  define v_pk_name varchar(128);
  define v_pk_owner varchar(128);
  define v_idx_name varchar(128);
  define v_idx_sqls lvarchar(2048);
  define v_view_text nchar(256);
  define v_proc_text nchar(256);
  define v_comments varchar(255);
  define v_synonym_tabname varchar(128);

  on exception
    return null;
  end exception;

--set debug file to '/home/gbase/spl.debug';
--trace on;
  -- exists table, delimident=y only for tablename
  let v_tabname = '';
  let v_numtab = 0;
  let v_ddl = '';
  if p_del = 1 then
    let v_tabname = p_name;
  else
    let v_tabname = lower(p_name);
  end if;

case lower(p_type)
  when 'table' then
    -- table
	select count(*) into v_numtab from systables where tabname = v_tabname and tabtype = 'T';
	if v_numtab = 0 then
	  return null;
	end if;
    let v_ddl = 'CREATE TABLE ' || case when p_del = 1 and regexp_like(v_tabname,'^[a-z_][a-z0-9_]*$') = 'f' then chr(34) || v_tabname || chr(34) else v_tabname end || '(' || chr(10);
    -- colname, coltype, nullable, default_value, default_type_flag
    foreach SELECT tmp.colname,tmp.coltype_name,
              CASE d.type
                  WHEN 'L' THEN gbasedbt.get_default_value(tmp.coltype, tmp.extended_id, tmp.collength, d.default::lvarchar(256))::VARCHAR(254)
                  WHEN 'C' THEN 'current year to second'::VARCHAR(254)
                  WHEN 'S' THEN 'dbservername'::VARCHAR(254)
                  WHEN 'U' THEN 'user'::VARCHAR(254)
                  WHEN 'T' THEN 'today'::VARCHAR(254)
                  WHEN 'E' THEN de.default::VARCHAR(254)
                  ELSE          NULL::VARCHAR(254)
              END AS def_value,
              tmp.nullable,
              d.type,
              tmp.collength
            INTO v_colname, v_coltype_name, v_defvalue, v_nullable, v_deftype, v_collength
            FROM (
                SELECT ce.tabid, ce.colno, ce.colname,ce.coltype,ce.extended_id,ce.collength,ce.coltypename2::varchar(128) AS coltype_name,
                CASE WHEN bitand(ce.coltype,256) = 256 THEN 'NOT NULL' ELSE '' END AS nullable
                FROM syscolumnsext ce, systables t
                WHERE ce.tabid = t.tabid
                AND t.tabname = v_tabname
				-- order by colno default
                ORDER BY ce.colno) tmp LEFT JOIN sysdefaults d ON (tmp.tabid = d.tabid AND tmp.colno = d.colno)
                    LEFT JOIN sysdefaultsexpr de ON (tmp.tabid = de.tabid AND tmp.colno = de.colno and de.type='T')

      -- no column found, return null
      if v_colname is null or v_colname = '' then
        return null;
      end if;

      IF v_coltype_name in ('DECIMAL','MONEY') THEN
        let v_decimal_p = v_collength / 256;
        let v_decimal_s = mod(v_collength,256);
        if v_decimal_s = 255 then
          let v_coltype_name = v_coltype_name || '(' || v_decimal_p || ')';
        else
          let v_coltype_name = v_coltype_name || '(' || v_decimal_p || ',' || v_decimal_s || ')';
        end if;
      END IF;

      -- default values with function not do.
      if v_deftype = 'E' then
        let v_defvalue = 'DEFAULT (' || v_defvalue || ')';
      elif v_deftype = 'L' and v_coltype_name[1,4] in ('CHAR','VARC','LVAR','NCHA','NVAR') then
        let v_defvalue = 'DEFAULT ''' || v_defvalue || '''';
      elif v_defvalue is not null then
        let v_defvalue = 'DEFAULT ' || v_defvalue;
      end if;

      -- column: colname coltype default nullable  
      let v_ddl = v_ddl || '  ' || case when p_del = 1 and regexp_like(v_colname,'^[a-z_][a-z0-9_]*$') = 'f' then chr(34) || v_colname || chr(34) else v_colname end  || ' ' || v_coltype_name  || ' ' || v_defvalue || ' ' || v_nullable || ',' || chr(10);
    end foreach;

    let v_ddl = rtrim(v_ddl, ',' || chr(10)) || ');' || chr(10);

    -- indexes, from proc_idxsql(idxname)
    let v_idx_name = '';
    foreach select si.idxname
          into v_idx_name
          from sysindexes si, systables st
         where si.tabid = st.tabid
           and st.tabname = v_tabname
           -- and si.idxname[1,1] != ' '
		   -- order by default
      call proc_idxsql(v_idx_name) returning v_idx_sqls;
      let v_ddl = v_ddl || v_idx_sqls || chr(10) ;
    end foreach;

    -- primary key
	-- create UNIQUE index and alter TABNAME add constraint primary key lead to duplicate. 2024-10-21
    let v_pk_collist = '';
    let v_pk_name = '';
	let v_pk_owner = '';
    foreach SELECT so.owner,so.constrname,
        rtrim((select sc.colname from syscolumns sc where sc.tabid = st.tabid and sc.colno = ABS(si.part1)) || ',' ||
              (select sc.colname from syscolumns sc where sc.tabid = st.tabid and sc.colno = ABS(si.part2)) || ',' ||
              (select sc.colname from syscolumns sc where sc.tabid = st.tabid and sc.colno = ABS(si.part3)) || ',' ||
              (select sc.colname from syscolumns sc where sc.tabid = st.tabid and sc.colno = ABS(si.part4)) || ',' ||
              (select sc.colname from syscolumns sc where sc.tabid = st.tabid and sc.colno = ABS(si.part5)) || ',' ||
              (select sc.colname from syscolumns sc where sc.tabid = st.tabid and sc.colno = ABS(si.part6)) || ',' ||
              (select sc.colname from syscolumns sc where sc.tabid = st.tabid and sc.colno = ABS(si.part7)) || ',' ||
              (select sc.colname from syscolumns sc where sc.tabid = st.tabid and sc.colno = ABS(si.part8)) || ',' ||
              (select sc.colname from syscolumns sc where sc.tabid = st.tabid and sc.colno = ABS(si.part9)) || ',' ||
              (select sc.colname from syscolumns sc where sc.tabid = st.tabid and sc.colno = ABS(si.part10)) || ',' ||
              (select sc.colname from syscolumns sc where sc.tabid = st.tabid and sc.colno = ABS(si.part11)) || ',' ||
              (select sc.colname from syscolumns sc where sc.tabid = st.tabid and sc.colno = ABS(si.part12)) || ',' ||
              (select sc.colname from syscolumns sc where sc.tabid = st.tabid and sc.colno = ABS(si.part13)) || ',' ||
              (select sc.colname from syscolumns sc where sc.tabid = st.tabid and sc.colno = ABS(si.part14)) || ',' ||
              (select sc.colname from syscolumns sc where sc.tabid = st.tabid and sc.colno = ABS(si.part15)) || ',' ||
              (select sc.colname from syscolumns sc where sc.tabid = st.tabid and sc.colno = ABS(si.part16)), ',') as keys
          INTO v_pk_owner, v_pk_name, v_pk_collist
          FROM  systables st, sysconstraints so, sysindexes si
          WHERE st.tabname = v_tabname
          AND st.tabid = so.tabid
          AND so.constrtype = 'P'
          AND so.idxname = si.idxname
    end foreach;

    if v_pk_collist = '' or v_pk_collist is null then
      let v_ddl = v_ddl;
    elif v_pk_name[1,1] = 'u' then
      let v_ddl = v_ddl || 'ALTER TABLE ' || case when p_del = 1 and regexp_like(v_tabname,'^[a-z_][a-z0-9_]*$') = 'f' then chr(34) || v_tabname || chr(34) else v_tabname end || ' ADD CONSTRAINT PRIMARY KEY(' || v_pk_collist || ');' || chr(10);
    else
      let v_ddl = v_ddl || 'ALTER TABLE ' || case when p_del = 1 and regexp_like(v_tabname,'^[a-z_][a-z0-9_]*$') = 'f' then chr(34) || v_tabname || chr(34) else v_tabname end || ' ADD CONSTRAINT PRIMARY KEY(' || v_pk_collist || ') CONSTRAINT ' || chr(34) || trim(v_pk_owner) || chr(34) || '.' || v_pk_name || ';' || chr(10);
    end if;

    -- has syscomments table, version 2.0 and older has not comments.  2024-09-13
    select tabname 
	into v_comments 
	from systables 
	where tabname = 'syscomments';
	if v_comments = 'syscomments' then 
      -- comment table;
  	  foreach select replace(comments, chr(39), '''''') into v_comments
  	         from syscomments
  			 where tabname = v_tabname
  	    let v_ddl = v_ddl || 'COMMENT ON TABLE ' || case when p_del = 1 and regexp_like(v_tabname,'^[a-z_][a-z0-9_]*$') = 'f' then chr(34) || v_tabname || chr(34) else v_tabname end || ' IS ''' || v_comments || ''';' || chr(10);
  	  end foreach;
  	
  	  -- comment column;
  	  foreach select colname,replace(comments, chr(39), '''''') into v_colname, v_comments
  	          from syscolcomments
  			 where tabname = v_tabname
        let v_ddl = v_ddl || 'COMMENT ON COLUMN ' || case when p_del = 1 and regexp_like(v_tabname,'^[a-z_][a-z0-9_]*$') = 'f' then chr(34) || v_tabname || chr(34) else v_tabname end || '.' || case when p_del = 1 and regexp_like(v_colname,'^[a-z_][a-z0-9_]*$') = 'f' then chr(34) || v_colname || chr(34) else v_colname end || ' IS ''' || v_comments || ''';' || chr(10);
  	  end foreach;
    end if;

  when 'indexes' then
    -- indexes, from proc_idxsql(idxname,del)
	select count(*) into v_numtab from sysindexes where idxname = v_tabname;
	if v_numtab = 0 then
	  return null;
	end if;
    call proc_idxsql(v_tabname,p_del) returning v_idx_sqls;
    let v_ddl = v_idx_sqls ;

  when 'view' then
    -- view
	select count(*) into v_numtab from systables where tabname = v_tabname and tabtype = 'V';
	if v_numtab = 0 then
	  return null;
	end if;
    foreach select v.viewtext
              into v_view_text
              from systables t,sysviews v
             where t.tabid = v.tabid
               and t.tabtype = 'V'
               and t.tabname = v_tabname
             order by v.seqno
      let v_ddl = v_view_text;
    end foreach;

  when 'procedure' then
    -- procedure / function
	select count(*) into v_numtab from sysprocedures where procname = v_tabname;
	if v_numtab = 0 then
	  return null;
	end if;
    foreach select b.data
              into v_proc_text
              from sysprocedures p, sysprocbody b
             where p.procid = b.procid
               and p.procname = v_tabname
               and b.datakey = 'T'
             order by b.seqno
      let v_ddl = v_proc_text;
    end foreach;

  when 'synonym' then 
    -- SYNONYM, local OR remote
	select count(*) into v_numtab from systables where tabname = v_tabname and tabtype = 'S';
	if v_numtab = 0 then
	  return null;
	end if;
	foreach select nvl(case when regexp_like(syn.tabname,'^[a-z_][a-z0-9_]*$') = 'f' then chr(34) || syn.tabname || chr(34) else syn.tabname end, s.dbname || '@' || nvl(s.servername,DBSERVERNAME) || ':' || chr(34) || trim(s.owner) || chr(34) || '.' || case when regexp_like(s.tabname,'^[a-z_][a-z0-9_]*$') = 'f' then chr(34) || s.tabname || chr(34) else s.tabname end) AS rtabname
	          into v_synonym_tabname
	          from syssyntable s LEFT JOIN systables syn
	            ON s.btabid = syn.tabid, systables t1 
	         WHERE s.tabid = t1.tabid
	           AND t1.tabname = v_tabname
      let v_ddl = 'CREATE SYNONYM ' || case when p_del = 1 and regexp_like(v_tabname,'^[a-z_][a-z0-9_]*$') = 'f' then chr(34) || v_tabname || chr(34) else v_tabname end || ' FOR ' || v_synonym_tabname || ';';			   
	end foreach;
  
  else
    let v_ddl = 'NOT_SUPPORTED';
end case;
  return v_ddl;
end PROCEDURE;


/*****************************************************
 * PROCEDURE: proc_idxsql(idxname)
 * DESCRIPTION: build index sql from idxname
 * USAGE: call proc_idxsql(idxname);
 * WRITE BY: liaosnet@gbasedbt.com 2023-12-19
 * UPDATE  : 2025-04-03 support DELIMIDENT
 * UPDATE  : 2025-06-18 index name filter, skip pk.
 *****************************************************/
DROP PROCEDURE IF EXISTS proc_idxsql(varchar,smallint);
CREATE PROCEDURE proc_idxsql(p_idxname varchar(128), p_del smallint default 0) returning lvarchar(1024) as idxsql;
  define v_idxsql lvarchar(1024);
  define v_idx_typename varchar(20);
  define v_tabid int;
  define v_tabname varchar(128);
  define v_idxtype char(1);
  define v_idxcluster char(1);
  define v_idxowner varchar(128);
  define v_idxkeys varchar(128);
  define v_idxkeyarr varchar(128);
  define v_funcname varchar(128);
  define v_procid varchar(128);
  define v_start int;
  define v_end   int;
  define v_colno int;
  define v_colname varchar(128);
  define curr int;
  define tmp varchar(128);
  define v_desc varchar(10);
  
  ON EXCEPTION
    RETURN NULL;
  END EXCEPTION;
--set debug file to '/home/gbase/spl.1';
--trace on;  

  -- primary key or constraints default name.
  IF regexp_like(p_idxname,'^ [0-9]+_[0-9]+$') = 't' then
    RETURN '';
  END IF;
  -- GET INDEXKEYS
  SELECT t.tabid, t.tabname, i.owner,i.idxtype,clustered, i.indexkeys::lvarchar
  INTO v_tabid, v_tabname, v_idxowner, v_idxtype, v_idxcluster,v_idxkeys
  FROM sysindices i,systables t
  WHERE i.tabid = t.tabid AND i.idxname = p_idxname;
  
  IF v_tabname is null or v_tabname = '' then 
    RETURN '';
  END IF;
  
  let v_idx_typename = '';
  if v_idxtype = 'U' then
    let v_idx_typename = 'UNIQUE';
  elif v_idxcluster = 'C' then
    let v_idx_typename = 'CLUSTER';
  end if;
  LET v_idxsql = 'CREATE ' || v_idx_typename;
  LET v_idxsql = rtrim(v_idxsql) || ' INDEX ' || chr(34) || trim(v_idxowner) || chr(34) || '.' || case when p_del = 1 and regexp_like(p_idxname,'^[a-z_][a-z0-9_]*$') = 'f' then chr(34) || p_idxname || chr(34) else p_idxname end || ' ON ' || v_tabname || ' (' ;
  
  -- process IDXKEYS
  let v_funcname = '';
  IF substr(v_idxkeys,1,1) = '<' THEN
    let v_start = 2;
    let v_end = instr(v_idxkeys,'>');
    let v_procid = substr(v_idxkeys, v_start, v_end - v_start);
    SELECT procname INTO v_funcname
    FROM sysprocedures
    WHERE procid = v_procid::int;
    let v_start = instr(v_idxkeys,'(') + 1;
    let v_end = instr(v_idxkeys,')');
    -- 1,2,
    let v_idxkeys = substr(v_idxkeys, v_start, v_end - v_start) || ',';
    
    let tmp = v_funcname || '(';
    while v_idxkeys != '' 
      let curr = instr(v_idxkeys, ',');
      let v_colno = substr(v_idxkeys, 1, curr - 1)::int;
      SELECT colname
      INTO v_colname
      FROM syscolumns
      WHERE tabid = v_tabid
      AND colno = v_colno;
      let tmp = tmp || v_colname || ',';
      let v_idxkeys = substr(v_idxkeys, curr + 1);
    END while;
    let tmp = rtrim(tmp,',') || ')';

  ELSE
    let v_idxkeys = replace(v_idxkeys, ' [1]') || ',';
    let tmp = '';
    let v_desc = '';
    while v_idxkeys != '' 
      let curr = instr(v_idxkeys, ',');
      let v_colno = substr(v_idxkeys, 1, curr - 1)::int;
      IF v_colno < 0 THEN
        let v_desc = ' DESC';
      END IF;
      SELECT colname
      INTO v_colname
      FROM syscolumns
      WHERE tabid = v_tabid
      AND colno = abs(v_colno);
      let tmp = tmp || v_colname || v_desc || ',';
      let v_idxkeys = substr(v_idxkeys, curr + 1);
    END while;
    let tmp = rtrim(tmp,',');   
  
  END IF;
  
  LET v_idxsql = v_idxsql || tmp || ');';   
  RETURN v_idxsql;
END PROCEDURE;
```

使用方法：

```sql
-- call get_ddl(类型,属主,名称,DELIMIDENT标识);
call get_ddl('table','gbasedbt','Tab1',1);
```

结果：  

```text
ddl                                                                                       |
------------------------------------------------------------------------------------------|
CREATE TABLE tabdec(
    col1 INTEGER  NOT NULL,
    col2 DECIMAL(10,2)  ,
    col3 DECIMAL(10)  NOT NULL);
ALTER TABLE tabdec ADD CONSTRAINT PRIMARY KEY(col1) CONSTRAINT "gbasedbt".u1018_19;       |
```

## 通过存储过程获取表结构（类似mysql）  

```sql
drop PROCEDURE if exists get_tableschema(varchar);
/*******************************************************************
 * PROCEDURE: get_tableschema(tabname)
 * DESCRIPTION: get table schema 
 * USAGE EG : get_tableschema('table1')
 * WRITE BY : liaosnet@gbasedbt.com 2025-05-27
 *******************************************************************/
-- return colname,coltypename,nullable,pk,default,extra
create PROCEDURE get_tableschema(p_name varchar(128))
returning nvarchar(128) as field,varchar(128) as type,varchar(10) as null,varchar(10) as key,varchar(255) as default,varchar(128) as extra;
  define v_tabname varchar(128);
  define v_numtab int; 
  define v_tabid  int;
  define v_colno  int;
  define v_colname nvarchar(128);
  define v_coltype_name varchar(128);
  define v_isnullable varchar(10);
  define v_isprimarykey varchar(10);
  define v_defvalue varchar(254);
  define v_collength int;
  define v_extra varchar(128);
  define v_decimal_p int;
  define v_decimal_s int;

  on exception
    return ;
  end exception;

  let v_numtab = 0;
  let v_tabname = lower(p_name);

  select count(*) into v_numtab from systables where tabname = v_tabname and tabtype = 'T';
  if v_numtab = 0 then
	return ;
  end if;
  
  -- colname, coltype_name, nullable, default_value, collength
  foreach SELECT tmp.tabid,tmp.colno,tmp.colname,tmp.coltype_name,tmp.nullable,
              CASE d.type
                  WHEN 'L' THEN gbasedbt.get_default_value(tmp.coltype, tmp.extended_id, tmp.collength, d.default::lvarchar(256))::VARCHAR(254)
                  WHEN 'C' THEN 'current year to second'::VARCHAR(254)
                  WHEN 'S' THEN 'dbservername'::VARCHAR(254)
                  WHEN 'U' THEN 'user'::VARCHAR(254)
                  WHEN 'T' THEN 'today'::VARCHAR(254)
                  WHEN 'E' THEN de.default::VARCHAR(254)
                  ELSE          NULL::VARCHAR(254)
              END AS def_value,
              tmp.collength
          INTO v_tabid,v_colno,v_colname,v_coltype_name,v_isnullable,v_defvalue,v_collength
          FROM (
                SELECT ce.tabid, ce.colno, ce.colname,ce.coltype,ce.extended_id,ce.collength,ce.coltypename2::varchar(128) AS coltype_name,
                CASE WHEN bitand(ce.coltype,256) = 256 THEN 'NO' ELSE 'YES' END AS nullable
                FROM syscolumnsext ce, systables t
                WHERE ce.tabid = t.tabid
                AND t.tabname = v_tabname
                ORDER BY ce.colno
            ) tmp LEFT JOIN sysdefaults d ON (tmp.tabid = d.tabid AND tmp.colno = d.colno)
                  LEFT JOIN sysdefaultsexpr de ON (tmp.tabid = de.tabid AND tmp.colno = de.colno and de.type='T')

      -- no column found, return null
      if v_colname is null or v_colname = '' then
        return ;
      end if;

      -- decimal type 
      IF v_coltype_name in ('DECIMAL','MONEY') THEN
        let v_decimal_p = v_collength / 256;
        let v_decimal_s = mod(v_collength,256);
        if v_decimal_s = 255 then
          let v_coltype_name = v_coltype_name || '(' || v_decimal_p || ')';
        else
          let v_coltype_name = v_coltype_name || '(' || v_decimal_p || ',' || v_decimal_s || ')';
        end if;
      END IF;
      
      -- primary key
      let v_isprimarykey = NULL;
      SELECT 'PRI' INTO v_isprimarykey
      FROM sysconstraints so, sysindexes si
      WHERE so.tabid = v_tabid
      AND so.constrtype = 'P'
      AND so.idxname = si.idxname
      AND (si.part1 = v_colno OR si.part2 = v_colno OR si.part3 = v_colno OR si.part4 = v_colno
        OR si.part5 = v_colno OR si.part6 = v_colno OR si.part7 = v_colno OR si.part7 = v_colno
        OR si.part8 = v_colno OR si.part10 = v_colno OR si.part11 = v_colno OR si.part12 = v_colno
        OR si.part13 = v_colno OR si.part14 = v_colno OR si.part15 = v_colno OR si.part16 = v_colno
      );
      
      -- extra
      let v_extra = NULL;
      IF v_coltype_name IN ('SERIAL','SERIAL8','BITSERIAL') THEN 
        let v_extra = 'AUTO_INCREMENT';
      END IF;
      
      RETURN v_colname,v_coltype_name,v_isnullable,v_isprimarykey,v_defvalue,v_extra WITH resume;
  end foreach;
end PROCEDURE;
```

使用方法：  

```sql
-- call get_tableschema(表名);
call get_tableschema('tab1');
```

结果：  

```text
field |type          |null |key |default |extra |
------|--------------|-----|----|--------|------|
col1  |INTEGER       |NO   |PRI |        |      |
col2  |DECIMAL(10,2) |YES  |    |        |      |
col3  |DECIMAL(10)   |NO   |    |        |      |
```

## 通过SQL获取表结构（类似mysql）  

```sql
SELECT
    tmp.colname AS field,
    CASE WHEN tmp.coltype_name IN ('DECIMAL','MONEY') THEN
            CASE WHEN mod(tmp.collength,256) = 255 THEN  tmp.coltype_name || '(' || (tmp.collength / 256)::int || ')' 
                 ELSE tmp.coltype_name || '(' || (tmp.collength / 256)::int || ',' || mod(tmp.collength,256) || ')' 
            END
        ELSE tmp.coltype_name
    END AS type,
    tmp.nullable AS null,
    (SELECT 'PRI' 
       FROM sysconstraints so, sysindexes si
      WHERE so.tabid = tmp.tabid
        AND so.constrtype = 'P'
        AND so.idxname = si.idxname
        AND (   si.part1 = tmp.colno OR si.part2 = tmp.colno OR si.part3 = tmp.colno OR si.part4 = tmp.colno
             OR si.part5 = tmp.colno OR si.part6 = tmp.colno OR si.part7 = tmp.colno OR si.part7 = tmp.colno
             OR si.part8 = tmp.colno OR si.part10 = tmp.colno OR si.part11 = tmp.colno OR si.part12 = tmp.colno
             OR si.part13 = tmp.colno OR si.part14 = tmp.colno OR si.part15 = tmp.colno OR si.part16 = tmp.colno
        )
    ) AS key,
    CASE d.type
        WHEN 'L' THEN gbasedbt.get_default_value(tmp.coltype, tmp.extended_id, tmp.collength, d.default::lvarchar(256))::VARCHAR(254)
        WHEN 'C' THEN 'current year to second'::VARCHAR(254)
        WHEN 'S' THEN 'dbservername'::VARCHAR(254)
        WHEN 'U' THEN 'user'::VARCHAR(254)
        WHEN 'T' THEN 'today'::VARCHAR(254)
        WHEN 'E' THEN de.default::VARCHAR(254)
        ELSE          NULL::VARCHAR(254)
    END AS default,
    CASE WHEN tmp.coltype_name IN ('SERIAL','SERIAL8','BITSERIAL') THEN 'AUTO_INCREMENT' ELSE NULL END AS extra
FROM (
      SELECT ce.tabid, ce.colno, ce.colname,ce.coltype,ce.extended_id,ce.collength,ce.coltypename2::varchar(128) AS coltype_name,
      CASE WHEN bitand(ce.coltype,256) = 256 THEN 'NO' ELSE 'YES' END AS nullable
      FROM syscolumnsext ce, systables t
      WHERE ce.tabid = t.tabid
      AND t.tabname = 'tab1'  -- table_name here.
      ORDER BY ce.colno
  ) tmp LEFT JOIN sysdefaults d ON (tmp.tabid = d.tabid AND tmp.colno = d.colno)
        LEFT JOIN sysdefaultsexpr de ON (tmp.tabid = de.tabid AND tmp.colno = de.colno and de.type='T');
```

结果：  

```text
field |type          |null |key |default |extra |
------|--------------|-----|----|--------|------|
col1  |INTEGER       |NO   |PRI |        |      |
col2  |DECIMAL(10,2) |YES  |    |        |      |
col3  |DECIMAL(10)   |NO   |    |        |      |
```

注意修改表名的位置。  


## 通过存储过程获取表结构（类似oracle）  

```sql
drop PROCEDURE if exists get_tableschema(varchar);
/*******************************************************************
 * PROCEDURE: get_tablechema(tabname)
 * DESCRIPTION: get table schema 
 * USAGE EG : get_tablechema('tab1')
 * WRITE BY : liaosnet@gbasedbt.com 2025-06-17
 * UPDATE   : sysdefaultsexpr may has muti rows.  2025-06-18
 *******************************************************************/
-- columnName,dataType,dataLength,nullable,datadefault,dataScale,comments,isPrimaryKey
create PROCEDURE get_tableschema(p_name varchar(128))
returning nvarchar(128) as columnName,varchar(128) as dataType,int as dataLength,
          char(1) as nullable, varchar(255) as datadefault,int as dataScale,
          varchar(255) as comments, varchar(3) as isPrimaryKey, varchar(4000) as virtualcolumn;
  define v_tabname varchar(128);
  define v_numtab int; 
  define v_tabid  int;
  define v_colno  int;
  define v_colname nvarchar(128);
  define v_coltype_name varchar(128);
  define v_isnullable char(1);
  define v_isprimarykey varchar(3);
  define v_defvalue varchar(255);
  define v_collength int;
  define v_decimal_p int;
  define v_decimal_s int;
  define v_comments varchar(255);
  define v_coltype int;
  define v_extended_id int;
  define v_isvtcol char(1);
  define v_vcolexpr varchar(4000);
  define v_tmpcolexpr varchar(4000);

  on exception
    return ;
  end exception;
  
  --set debug file to '/home/gbase/spl.log';
  --trace on;
  
  let v_numtab = 0;
  let v_tabname = p_name;
  select count(*) into v_numtab 
  from systables 
  where tabname = v_tabname 
  and tabtype = 'T';
  if v_numtab = 0 then
	return ;
  end if;
  
  -- columnName, coltype_name, nullable, default_value, collength
  foreach SELECT tmp.tabid,tmp.colno,tmp.colname,tmp.coltype_name,tmp.nullable,
              tmp.collength,cc.comments,
			  tmp.coltype,tmp.extended_id,tmp.isvtcol
          INTO v_tabid,v_colno,v_colname,v_coltype_name,v_isnullable,v_collength,v_comments,v_coltype,v_extended_id,v_isvtcol
          FROM (
                SELECT ce.tabid, t.tabname, ce.colno, ce.colname,ce.coltype,ce.extended_id,ce.collength,ce.coltypename2::varchar(128) AS coltype_name,
                CASE WHEN bitand(ce.coltype,256) = 256 THEN 'N' ELSE 'Y' END AS nullable,
				CASE WHEN bitand(ce.colattr,768) = 768 THEN 'Y' ELSE 'N' END AS isvtcol
                FROM syscolumnsext ce, systables t
                WHERE ce.tabid = t.tabid
                AND t.tabname = v_tabname
                ORDER BY ce.colno
            ) tmp left join syscolcomments cc on (tmp.tabname = cc.tabname and tmp.colname = cc.colname)

      -- no column found, return null
      if v_colname is null or v_colname = '' then
        return ;
      end if;
	  
	  -- default value 
	  SELECT CASE d.type
               WHEN 'L' THEN get_default_value(v_coltype, v_extended_id, v_collength, d.default::lvarchar(256))::VARCHAR(254)
               WHEN 'C' THEN 'current year to second'::VARCHAR(254)
               WHEN 'S' THEN 'dbservername'::VARCHAR(254)
               WHEN 'U' THEN 'user'::VARCHAR(254)
               WHEN 'T' THEN 'today'::VARCHAR(254)
               WHEN 'E' THEN de.default::VARCHAR(254)
               ELSE          NULL::VARCHAR(254)
             END AS def_value
	  INTO v_defvalue
	  FROM sysdefaults d 
	  LEFT JOIN sysdefaultsexpr de ON (d.tabid = de.tabid AND d.colno = de.colno AND de.type = 'T')
	  WHERE de.tabid = v_tabid
	  AND de.colno = v_colno;
	  
	  -- virtual column
	  let v_vcolexpr = '';
	  if v_isvtcol = 'Y' then     
	    foreach SELECT de.default 
		        INTO v_tmpcolexpr
		        FROM sysdefaultsexpr de 
				WHERE de.tabid = v_tabid AND de.colno = v_colno AND de.type = 'T'
		  let v_vcolexpr = v_vcolexpr || v_tmpcolexpr;
		end foreach;
	  end if;

      -- data_type
      let v_decimal_p = 0;
      let v_decimal_s = 0;
      if v_coltype_name like '%CHAR%' then
        let v_coltype_name = regexp_substr(v_coltype_name,'[^(]+',1);
        let v_decimal_p = mod(v_collength,65536);
        let v_decimal_s = v_collength / 65536;
        let v_collength = v_decimal_p;
      end if;
      
      -- decimal type 
      IF v_coltype_name in ('DECIMAL','MONEY') THEN
        let v_decimal_p = v_collength / 256;
        let v_decimal_s = mod(v_collength,256);
        if v_decimal_s = 255 then
          let v_decimal_s = 0;
        end if;
        let v_collength = v_decimal_p;
      END IF;
	        
      -- primary key
      let v_isprimarykey = '';
      SELECT 'YES' INTO v_isprimarykey
      FROM sysconstraints so, sysindexes si
      WHERE so.tabid = v_tabid
      AND so.constrtype = 'P'
      AND so.idxname = si.idxname
      AND (si.part1 = v_colno OR si.part2 = v_colno OR si.part3 = v_colno OR si.part4 = v_colno
        OR si.part5 = v_colno OR si.part6 = v_colno OR si.part7 = v_colno OR si.part7 = v_colno
        OR si.part8 = v_colno OR si.part10 = v_colno OR si.part11 = v_colno OR si.part12 = v_colno
        OR si.part13 = v_colno OR si.part14 = v_colno OR si.part15 = v_colno OR si.part16 = v_colno
      );
      if v_isprimarykey is null or v_isprimarykey = '' then 
        let v_isprimarykey = 'NO';
      end if;
  
      RETURN v_colname,v_coltype_name,v_collength,v_isnullable,v_defvalue,v_decimal_s,v_comments,v_isprimarykey,v_vcolexpr WITH resume;
  end foreach;
end PROCEDURE;
```

使用方法：  

```sql
-- call get_tableschema(表名);
call get_tableschema('tab1');
```

结果：  

```text
columnname |datatype |datalength |nullable |datadefault  |datascale |comments       |isprimarykey |virtualcolumn |
-----------|---------|-----------|---------|-------------|----------|---------------|-------------|--------------|
col1       |INTEGER  |4          |N        |             |0         |主键           |YES          |              |
col2       |DECIMAL  |10         |Y        |3.14         |2         |字段2含默认值  |NO           |              |
col3       |DECIMAL  |10         |Y        |             |0         |字段3          |NO           |              |
```
