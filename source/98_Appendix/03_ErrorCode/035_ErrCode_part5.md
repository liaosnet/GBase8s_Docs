# GBase 8s数据库错误代码  
第五部分  


## sql1  

|ErrCode|Description|
|:---|:---|
|-200|Identifier is too long.|
|-201|A syntax error has occurred.|
|-202|An illegal character has been found in the statement.|
|-203|An illegal integer has been found in the statement.|
|-204|An illegal floating point number has been found in the statement.|
|-205|The statement failed because you cannot use ROWID for views with union, intersect, minus, aggregates, group by, multiple tables, or derived tables.|
|-206|The specified table (%s) is not in the database.|
|-207|Cannot declare a SELECT INTO statement FOR UPDATE.|
|-208|Memory allocation failed during query processing.|
|-209|Incompatible database format.|
|-210|Explicit path name too long.|
|-211|Cannot read system catalog (%s).|
|-212|Cannot add index.|
|-213|Statement interrupted by user.|
|-214|Cannot remove file for table (%s).|
|-215|Cannot open file for table (%s).|
|-216|Cannot remove index.|
|-217|Column (%s) not found in any table in the query (or SLV is undefined).|
|-218|Synonym (%s) not found.|
|-219|Wildcard matching may not be used with non-character and non-numeric types.|
|-220|Cannot begin savepoint.|
|-221|Cannot build temporary file for new table (%s).|
|-222|Cannot write to temporary file for new table (%s).|
|-223|Duplicate table name (%s) in the FROM clause.|
|-224|Cannot open transaction log file.|
|-225|Cannot create file for system catalog (%s).|
|-226|Cannot create index for system catalog (%s).|
|-227|DDL operations on '%s' prohibited.|
|-228|UPDATE or INSERT on '%s' prohibited.|
|-229|Could not open or create a temporary file.|
|-230|Could not read a temporary file.|
|-231|Cannot perform aggregate function with distinct on expression.|
|-232|A SERIAL column (%s) may not be updated.|
|-233|Cannot read record that is locked by another user.|
|-234|Cannot insert into virtual column (%s).|
|-235|Character column size is too big.|
|-236|Number of columns in INSERT table does not match number of VALUES.|
|-237|Cannot begin work.|
|-238|Cannot commit work.|
|-239|Could not insert new row - duplicate value in a UNIQUE INDEX column (%s).|
|-240|Could not delete a row.|
|-241|Cannot rollback work.|
|-242|Could not open database table (%s).|
|-243|Could not position within a table (%s).|
|-244|Could not do a physical-order read to fetch next row.|
|-245|Could not position within a file via an index.|
|-246|Could not do an indexed read to get the next row.|
|-247|Rollforward database failed.|
|-248|Cannot commit savepoint.|
|-249|Virtual column must have explicit name.|
|-250|Cannot read record from file for update.|
|-251|ORDER BY or GROUP BY column number is too big.|
|-252|Cannot get system information for table.|
|-253|Identifier length exceeds the maximum allowed by this version of the server.|
|-254|Too many or too few host variables given.|
|-255|Not in transaction.|
|-256|Transaction not available.|
|-257|System limit on maximum number of statements exceeded, maximum is %s.|
|-258|System error - invalid statement id received by the sqlexec process.|
|-259|Cursor not open.|
|-260|Cannot execute a SELECT statement that is PREPAREd - must use cursor.|
|-261|Cannot create file for table (%s).|
|-262|There is no current cursor.|
|-263|Could not lock row for UPDATE.|
|-264|Could not write to a temporary file.|
|-265|Load or insert cursors must be run within a transaction.|
|-266|There is no current row for UPDATE/DELETE cursor.|
|-267|The cursor has been previously released and is unavailable.|
|-268|Unique constraint (%s) violated.|
|-269|Cannot add column (%s) that does not accept nulls.|
|-270|Could not position within a temporary file.|
|-271|Could not insert new row into the table.|
|-272|No SELECT permission for %s.|
|-273|No UPDATE permission for %s.|
|-274|No DELETE permission for %s.|
|-275|The Insert privilege is required for this operation.|
|-276|Cursor not found.|
|-277|UPDATE table (%s) is not the same as the cursor table.|
|-278|Cannot rollback savepoint.|
|-279|Cannot grant or revoke database privileges for table or view.|
|-280|A quoted string exceeds 256 bytes.|
|-281|Could not add index to a temporary table.|
|-282|Found a quote for which there is no matching quote.|
|-283|Found a non-terminated comment ('{' with no matching '}').|
|-284|A subquery has returned not exactly one row.|
|-285|Invalid cursor received by sqlexec.|
|-286|Default value of the primary key column %s is NULL.|
|-287|Cannot add serial column (%s) to table.|
|-288|Table (%s) not locked by current user.|
|-289|Cannot lock table (%s) in requested mode.|
|-290|Cursor not declared with FOR UPDATE clause.|
|-291|Cannot change lock mode of table.|
|-292|An implied insert column (%s) does not accept NULLs.|
|-293|IS [NOT] NULL predicate may be used only with simple columns.|
|-294|The column (%s) must be in the GROUP BY list.|
|-295|Referenced and referencing tables have to be in the same database.|
|-296|Referenced table %s not available.|
|-297|Cannot find unique constraint or primary key on referenced table (%s).|
|-298|Cannot grant permission to public with grant option.|
|-299|Cannot grant permission to self.|
|-300|There are too many GROUP BY columns.|
|-301|The total size of the GROUP BY columns is too big.|
|-302|No GRANT option or illegal option on multi-table view.|
|-303|Expression mixes columns with aggregates.|
|-304|HAVING can only have expressions with aggregates or columns in GROUP BY clause.|
|-305|Subscripted column (%s) is not of type CHAR, VARCHAR, VARCHAR2, TEXT nor BYTES.|
|-306|Subscript out of range.|
|-307|Illegal subscript definition.|
|-308|The statement failed because corresponding column data types must be compatible for each UNION, INTERSECT, or MINUS query.|
|-309|ORDER BY column (%s) must be in SELECT list.|
|-310|Table (%s) already exists in database.|
|-311|Cannot open system catalog (%s).|
|-312|Cannot update system catalog (%s).|
|-313|Not owner of table.|
|-314|Table (%s) currently in use.|
|-315|No create index permission.|
|-316|Index (%s) already exists in database.|
|-317|The statement failed because you must have the same number of selected columns in each UNION, INTERSECT, or MINUS query.|
|-318|File with the same name as specified log file already exists.|
|-319|Index does not exist.|
|-320|Not owner of index.|
|-321|Cannot group by aggregate column.|
|-322|Cannot Alter a view, Rename a view or Create a trigger on a view (%s).|
|-323|Cannot grant permission on temporary table.|
|-324|Ambiguous column (%s).|
|-325|Filename must be specified with a full path name.|
|-326|Referential constraint has too many referenced columns.|
|-327|Cannot unlock table (%s) within a transaction.|
|-328|Column (%s) already exists in table or type.|
|-329|Database not found or no system permission.|
|-330|Cannot create or rename the database.|
|-331|Cannot drop database directory.|
|-332|Cannot access audit trail name information.|
|-333|The audit trail file already exists with a different name.|
|-334|Cannot create audit trail.|
|-335|There is no audit trail for the specified table.|
|-336|Cannot create or drop audit on a temporary table (%s).|
|-337|Cannot create view on temporary table (%s).|
|-338|Cannot drop audit trail.|
|-339|The audit trail file name must be given in full directory path.|
|-340|Cannot open audit trail file.|
|-341|Could not read a row from audit trail file.|
|-342|Remote host cannot execute statement.|
|-343|Row from audit trail was added to a different position than expected.|
|-344|Cannot delete row - row in table does not match row in audit trail.|
|-345|Cannot update row - row in table does not match row in audit trail.|
|-346|Could not update a row in the table.|
|-347|Could not open table for exclusive access.|
|-348|Could not read a row from the table.|
|-349|Database not selected yet.|
|-350|Index already exists on the column (or on the set of columns).|
|-351|Database contains tables owned by other users.|
|-352|Column (%s) not found.|
|-353|No table or view specified when granting/revoking privileges.|
|-354|Incorrect database or cursor name format.|
|-355|Cannot rename file for table %s.|
|-356|Data type of the referencing and referenced columns do not match.|
|-357|Dependent table for view (%s) has been altered.|
|-358|Must close current database before CREATE, START or ROLLFORWARD.|
|-359|Cannot drop or rename the current database or any open database.|
|-360|Cannot modify table or view used in subquery.|
|-361|Column size too large.|
|-362|Can have only one column of serial/(serial8 or bigserial) type.|
|-363|CURSOR not on SELECT statement.|
|-364|Column (%s) not declared for UPDATE OF.|
|-365|Cursor must be on simple SELECT for FOR UPDATE.|
|-366|The scale exceeds the maximum precision specified.|
|-367|Sums and averages cannot be computed for character columns.|
|-368|Incompatible sqlexec module.|
|-369|Invalid serial number. Consult your installation instructions.|
|-370|Cannot drop last column.|
|-371|Cannot create unique index on column with duplicate data.|
|-372|Cannot alter table with audit trail on.|
|-373|A database or command script is inaccessible because a DBPATH entry is too long.|
|-374|Can only use column number in ORDER BY clause with UNION.|
|-375|Cannot create log file for transaction.|
|-376|Log file already exists.|
|-377|Must terminate transaction before closing database.|
|-378|Record currently locked by another user.|
|-379|Cannot revoke privilege on columns.|
|-380|Cannot erase log file.|
|-381|Cannot grant to someone who has granted you the same privilege before.|
|-382|Same number of columns must be specified for view and select clause.|
|-383|Need to specify view column names in the view definition.|
|-384|Cannot modify non simple view.|
|-385|Data value out of range.|
|-386|Column contains null values.|
|-387|No connect permission.|
|-388|No resource permission.|
|-389|No DBA permission.|
|-390|Synonym already used as table name or synonym.|
|-391|Cannot insert a null into column (%s).|
|-392|System error - unexpected null pointer encountered.|
|-393|A condition in the where clause results in a two-sided outer join.|
|-394|View (%s) not found.|
|-395|The where clause contains an outer Cartesian Product.|
|-396|Illegal join between a nested outer table and a preserved table.|
|-397|System catalog (%s) corrupted.|
|-398|Cursor manipulation must be within a transaction.|
|-399|Cannot access log file.|
|-415|Data conversion error.|
|-425|Database is currently opened by another user.|
|-458|Long transaction aborted.|


## sql2  

|ErrCode|Description|
|:---|:---|
|-500|Clustered index (%s) already exists in the table.|
|-501|Index (%s) is already not clustered.|
|-502|Cannot cluster index.|
|-503|Too many tables locked.|
|-504|Cannot lock a view.|
|-505|Number of columns in UPDATE does not match number of VALUES.|
|-506|Do not have permission to update all columns|
|-507|Cursor (%s) not found.|
|-508|Cannot rename a temporary table.|
|-509|Cannot rename a column in a temporary table.|
|-510|Cannot create synonym for temporary table (%s).|
|-511|Cannot modify system catalog (%s).|
|-512|No References privilege on the referenced columns.|
|-513|Statement not available with this database server.|
|-514|Only a DBA can create, drop, grant, or revoke for another user.|
|-515|Constraint %s has already been dropped.|
|-516|System error - temporary output file not created yet.|
|-517|The total size of the index is too large or too many parts in index.|
|-518|Child constraint %s not found.|
|-519|Cannot update column to illegal value.|
|-520|Cannot open database tblspace.|
|-521|Cannot lock system catalog (%s).|
|-522|Table (%s) not selected in query.|
|-523|Can only recover, repair, truncate or drop table.|
|-524|Lock table can only be used within a transaction.|
|-525|Failure to satisfy referential constraint %s.|
|-526|Updates are not allowed on a scroll cursor.|
|-527|Lock mode is not available on this system.|
|-528|Maximum output rowsize (320M) exceeded.|
|-529|Cannot attach to transaction.|
|-530|Check constraint (%s) failed.|
|-531|Duplicate column (%s) exists in view.|
|-532|Cannot alter temporary table (%s).|
|-533|Extent size too small, minimum size is %sk.|
|-534|Cannot open EXPLAIN output file.|
|-535|Already in transaction.|
|-536|Number of columns in child constraint does not match number of cols in parent constraint.|
|-537|Constraint column %s not found in table.|
|-538|Cursor (%s) has already been declared.|
|-539|DBTEMP too long.|
|-540|write failed on constraints.|
|-541|User does not have ALTER privilege.|
|-542|Cannot specify a column more than once in a constraint, trigger, or index.|
|-543|ESCAPE character must be only one byte.|
|-544|Cannot have aggregates within aggregates.|
|-545|No write permission for table %s.|
|-546|Cannot have host variables when creating a view (%s).|
|-547|Must rollforward database in the directory where the database is.|
|-548|No referential constraint or trigger allowed on a TEMP table.|
|-549|Column (%s) in UNIQUE constraint is not a column in the table.|
|-550|Total length of columns in constraint is too long.|
|-551|The constraint contains too many columns.|
|-552|Blob host variables are disallowed in multi-statement prepares.|
|-553|Mkdbsdir not found in $GBASEDBTDIR/bin. Consult your installation instructions.|
|-554|Syntax disallowed in this database server.|
|-555|Cannot use a select or any of the database statements in a multi-query prepare.|
|-556|Cannot create, drop, or modify an object that is external to current database.|
|-557|Cannot locate table that is external to the current database after %s levels of synonym mapping.|
|-558|Changrp not found in $GBASEDBTDIR/bin. Consult your installation instructions.|
|-559|Cannot create a synonym on top of another synonym.|
|-560|Synonym with tabid %s not found in systables.|
|-561|Sums and averages cannot be computed on datetime values.|
|-562|Database conversion failed.|
|-563|Cannot acquire exclusive lock for database conversion.|
|-564|Cannot sort rows.|
|-565|Cannot read sorted rows.|
|-566|Cannot initiate sort.|
|-567|Cannot write sorted rows.|
|-568|Cannot reference an external database without logging.|
|-569|Cannot reference an external database with logging.|
|-570|Cannot reference an external ANSI database.|
|-571|Cannot reference an external non-ANSI database.|
|-572|The specified wait duration is too long.|
|-573|Cannot set log to buffered in a mode ANSI database.|
|-574|A subquery has returned not exactly one column.|
|-575|LENGTH() requires string type values.|
|-576|Cannot specify CONSTRAINT name for TEMP table.|
|-577|A constraint of the same type already exists on the column set.|
|-578|Owner name is too long.|
|-579|Not owner of synonym.|
|-580|Cannot revoke permission.|
|-581|Error loading message file.|
|-582|Database does not have logging.|
|-583|View permissions are no longer valid.|
|-584|Cannot rename system catalog.|
|-585|Cannot rename column in system catalog.|
|-586|Cursor is already open.|
|-587|Cannot delete file (%s).|
|-588|Invalid host variable number.|
|-589|Cannot update multiple database servers within a single transaction.|
|-590|Routine cache corrupted.|
|-591|Invalid default value for column/variable (%s).|
|-592|Cannot specify column to be not null when the default value is null.|
|-593|Cannot specify default value for SERIAL column.|
|-594|Cannot specify non-null default value for blob column.|
|-595|Bad use of aggregate in this context.|
|-596|Bad EXIT/CONTINUE statement. Not within a %s loop.|
|-597|[Internal] Premature End Of Buffer.|
|-598|Bad cursor name (%s).|
|-599|Cannot mix GBasedbt Dynamic Server syntax with GBASEDBT-SE syntax.|
|-600|Cannot create blob.|
|-601|Cannot delete blob.|
|-602|Cannot open blob.|
|-603|Cannot close blob.|
|-604|Cannot read blob.|
|-605|Cannot write blob.|
|-606|Invalid blob space name.|
|-607|Text/Byte subscript error.|
|-608|Illegal attempt to convert Text/Byte blob type.|
|-609|Illegal attempt to use Text/Byte host variable.|
|-610|Index not allowed on TEXT or BYTE columns.|
|-611|Scroll cursor can't select blob columns.|
|-612|Blobs are not allowed in the 'group by' clause.|
|-613|Blobs are not allowed in the 'distinct' clause.|
|-614|Blobs are not allowed in the 'order by' clause.|
|-615|Blobs are not allowed in this expression.|
|-616|A blob subscript is not allowed within this context.|
|-617|A blob data type must be supplied within this context.|
|-618|Error occurred while trying to copy TEXT or BYTE data.|
|-619|A blob error has occurred in the front-end application.|
|-620|Unable to update next extent size.|
|-621|Unable to update new lock level.|
|-622|Error on locating constraint index (%s).|
|-623|Unable to find CONSTRAINT (%s).|
|-624|Unable to drop CONSTRAINT (%s).|
|-625|Constraint name (%s) already exists.|
|-626|Cannot obtain or set serial value.|
|-627|Cannot prepare coordinator for two-phase commit.|
|-628|Cannot end two-phase commit transaction at coordinator.|
|-629|Cannot end heuristically rolled back transaction.|
|-630|Cannot prepare database server %s for commit.|
|-631|Cannot create optical cluster on non-blob column (%s).|
|-632|Cannot create optical cluster.|
|-633|Cannot drop optical cluster.|
|-634|Object does not exist.|
|-635|Not owner of object.|
|-636|Total size of key fields is too large or there are too many key fields.|
|-637|Cannot alter optical cluster.|
|-638|Cannot cluster blob columns on non-optical media.|
|-639|Cannot cluster blob columns on different optical families.|
|-640|QPlan sanity failure (%s).|
|-641|Cannot reserve/release family on non-optical media.|
|-642|Family name must be a character string.|
|-643|Volume must be a number.|
|-644|FAMILY(), VOLUME(), and DESCR() require BLOB column on optical medium.|
|-645|Cannot reserve volume.|
|-646|Cannot release volume.|
|-647|Error evaluating math library function(%s).|
|-648|Cannot open DEBUG file for SPL routine trace.|
|-649|The debug file name must be a NON-NULL CHAR, VARCHAR or VARCHAR2.|
|-650|Maximum varchar or varchar2 size has been exceeded.|
|-651|Reserved column size > maximum column size (varchar or varchar2).|
|-652|Local variables do not allow default values.|
|-653|Variables declared as LIKE cannot be global.|
|-654|Bad use of PROCEDURE declaration type.|
|-655|RETURN value count does not match procedure declaration.|
|-656|Routine is not declared to return values.|
|-657|Cannot create a procedure or a trigger within a procedure.|
|-658|Variables declared as GLOBAL require a default value.|
|-659|INTO TEMP table required for SELECT statement.|
|-660|Loop variable(%s) cannot be modified.|
|-661|Number of variables does not match number of values returned.|
|-662|Loop variable(%s) specified more than once.|
|-663|You are using more than one procedure-calling syntax for procedure(%s).|
|-664|Wrong number of arguments to system function(%s).|
|-665|Internal error on semantics - %s.|
|-666|Variable(%s) must be declared INTEGER or SMALLINT.|
|-667|Variable(%s) not declared.|
|-668|The system command cannot be executed or it exited with a non-zero status.|
|-669|Variable(%s) redeclared.|
|-670|Variable(%s) declared as SERIAL type.|
|-671|Routine invocation(%s) has duplicate parameter name.|
|-672|Invalid data structure (%s).|
|-673|Another routine (%s) with same signature already exists in database.|
|-674|Routine (%s) can not be resolved.|
|-675|Illegal SQL statement in SPL routine.|
|-676|Invalid check constraint column.|
|-677|Check constraint cannot contain subqueries or procedures.|
|-678|Invalid subscript for column (%s) in check constraint.|
|-679|Cannot read constraint violation data for constraint (%s).|
|-680|Cannot write constraint violation data for constraint (%s).|
|-681|Column specified more than once in the INSERT list.|
|-682|Error reading constraint index on table (%s).|
|-683|Specified STEP expression will not traverse RANGE.|
|-684|Function (%s) returns too many values.|
|-685|Function (%s) returns too few values.|
|-686|Function (%s) has returned more than one row.|
|-687|Set debug file before tracing SPL routines.|
|-688|Variable(%s) must be declared CHAR, VARCHAR or VARCHAR2.|
|-689|Global variable(%s) declared inconsistently.|
|-690|Cannot read keys from referencing table (%s).|
|-691|Missing key in referenced table for referential constraint (%s).|
|-692|Key value for constraint (%s) is still being referenced.|
|-693|System command expects a non-null value.|
|-694|Too many arguments passed to procedure (%s).|
|-695|Argument is not a parameter of procedure (%s).|
|-696|Variable (%s) has undefined value.|
|-697|STEP expression evaluated to ZERO.|
|-698|Inconsistent transaction. Number and names of servers rolled back - %s.|
|-699|Transaction heuristically rolled back.|


## sql3  

|ErrCode|Description|
|:---|:---|
|-700|Statement is invalid within a global transaction.|
|-701|Statement is invalid within the XA environment.|
|-702|Cannot open database in exclusive mode.|
|-703|Primary key on table (%s) has a field with a null key value.|
|-704|Primary key already exists on the table.|
|-705|Cannot drop/modify procedure (%s). It is currently in use.|
|-706|Execute privilege denied on procedure (%s).|
|-707|Blob columns in optical cluster must be distinct.|
|-708|Optical cluster (%s) already exists.|
|-709|Blob column (%s) is already clustered.|
|-710|Table (%s) has been dropped, altered or renamed.|
|-711|Cannot insert encoded BLOB descriptor.|
|-712|Cannot insert encoded BLOB descriptor in non-optical BLOB columns.|
|-713|Cannot decode encoded BLOB descriptor.|
|-714|Cannot encode BLOB descriptor.|
|-715|Transaction state error.|
|-716|Possible inconsistent transaction. Unknown servers are %s.|
|-717|Invalid argument passed to system function(%s).|
|-718|Statement is invalid while a global transaction is suspended.|
|-719|Loop variable(%s) cannot be declared GLOBAL.|
|-720|The number of returned values and of SPL variables do not match.|
|-721|SPL routine(%s) is no longer valid.|
|-722|Out of stack space.|
|-723|Cannot disable logging in an ANSI-compliant database.|
|-724|System initialization file $GBASEDBTDIR/%s is missing.|
|-725|Error occurred while reading system initialization file $GBASEDBTDIR/%s.|
|-726|First argument to dbinfo() must be a quoted string constant.|
|-727|Invalid or NULL TBLspace number given to dbinfo(dbspace).|
|-728|Unknown first argument of dbinfo(%s).|
|-729|Trigger has no triggered action.|
|-730|Cannot specify REFERENCING if trigger does not have FOR EACH ROW.|
|-731|Invalid use of column reference in trigger body.|
|-732|Incorrect use of old or new values correlation name inside trigger.|
|-733|Cannot reference procedure variable in %s statement.|
|-734|Object name matches old or new values correlation name.|
|-735|Cannot reference table that participates in cascaded delete.|
|-736|Resolution or Sampling size are not meaningful for LOW mode.|
|-737|Confidence or Sampling size are not meaningful for HIGH mode.|
|-738|DROP DISTRIBUTIONS is only valid in LOW mode.|
|-739|Confidence must be in the range [0.80, 0.99] (inclusive).|
|-740|Resolution must be greater than 0.005 and less than, or equal to, 10.0.|
|-741|Trigger for the same event already exists.|
|-742|Trigger and referential constraint cannot co-exist.|
|-743|Object (%s) already exists in database.|
|-744|Illegal SQL statement in trigger.|
|-745|Trigger execution has failed.|
|-746|%s|
|-747|Table or column matches object referenced in triggering statement.|
|-748|Exceeded limit on maximum number of cascaded triggers.|
|-749|Remote cursor operation disallowed with pre-5.01 server.|
|-750|Invalid distribution format found for %s|
|-751|Remote procedure execution disallowed with pre-5.01 server.|
|-752|All Smart Disk devices are busy.|
|-753|Access denied - Single user limit has been exceeded.|
|-754|Cannot access the license file.|
|-755|Cannot access the license file to release license.|
|-756|Evaluation version has expired.|
|-757|File open for light append can't pseudo close.|
|-758|Cannot implicitly reconnect to the new server (%s)|
|-759|Cannot use database commands in an explicit database connection.|
|-760|Remote procedure must commit or rollback before returning.|
|-761|GBASEDBTSERVER does not match either DBSERVERNAME or DBSERVERALIASES.|
|-762|Stack overflow occurred during statement parse.|
|-763|Error in auditing environment initialization.|
|-764|Only DBA can run update statistics on a database in this mode.|
|-765|Cannot EXECUTE a statement that has been DECLAREd.|
|-766|String must be null terminated.|
|-767|Cannot update/insert to a remote table through views with check options.|
|-768|Internal error in routine %s.|
|-769|Internal - iterator execution/phase error %s.|
|-770|Bad fragment id specified.|
|-771|Bad table lock id specified.|
|-772|Record/Key doesn't qualify for any table/index fragment.|
|-773|Expression required for new fragment.|
|-774|Cannot specify fragment expressions with a round robin fragmentation.|
|-775|Fragment partition (%s) not used by table/index.|
|-776|Alter fragment error: unable to move row(s) to new fragmentation scheme.|
|-777|Internal - function not valid on fragmented table.|
|-778|Unable to alter fragmentation scheme on index or table.|
|-779|Duplicate table name in the alter fragment specification.|
|-780|Table/Index is not fragmented.|
|-781|Cannot alter fragmentation on a temp table.|
|-782|Attached table is fragmented.|
|-783|Cannot attach because of incompatible schema.|
|-784|Cannot detach because of the existing referential constraints.|
|-785|Cannot drop column because of table or index fragmentation.|
|-786|Cannot attach to this table because it is not in the list of tables in the ATTACH clause.|
|-787|This index is attached it cannot be altered.|
|-788|Unknown operator/type.|
|-789|Internal error, expression not properly defined.|
|-790|Cannot create interval fragment.|
|-791|Cannot find fragment for the row.|
|-792|Cannot update the sysfragments system catalog table for an interval fragment.|
|-793|Page size of the dbspace does not match page size of the table or index.|
|-794|One or more dbspaces for interval fragments do not exist.|
|-795|One or more dbspaces for interval fragments are unusable.|
|-796|Fragment position for the row exceeds the maximum allowed.|
|-797|Fragment is not empty.|
|-798|No permission on table to create an interval fragment.|
|-800|Corresponding data types must be compatible in CASE expression or DECODE function.|
|-801|SQL Edit buffer is full.|
|-802|Cannot open file for run.|
|-803|The file is too large for internal editing.|
|-804|Comment has no end.|
|-805|Cannot open file for load.|
|-806|Cannot open file for unload.|
|-807|Cannot open file for output.|
|-808|Cannot open file for choose.|
|-809|SQL Syntax error has occurred.|
|-810|Cannot open file for save.|
|-811|Cannot open printer for output.|
|-812|Cannot open pipe for output.|
|-813|Cannot write to pipe for output ( no reading process ).|
|-816|Cannot write file (check file permissions).|
|-817|Cannot read file (check file permissions).|
|-818|Specified user menu not found.|
|-819|There are no menu items in the menu.|
|-820|No more data to display.|
|-821|Cannot open file for default report.|
|-822|Statements are already saved.|
|-823|There are no statements to run.|
|-824|Missing values clause on insert statement.|
|-825|Program not found.|
|-826|Fork system call failed.|
|-827|Database not found.|
|-828|Command file not found.|
|-829|Form not found.|
|-830|Report not found.|
|-831|Error found in Report specifications.|
|-832|Error found in Form specifications.|
|-833|Saceprep could not compile Report.|
|-834|Sformbld could not compile Form.|
|-835|Current clause is invalid in interactive mode.|
|-836|Insert statement has no values clause.|
|-837|There is not enough memory available.|
|-838|A line in the load file is too long.|
|-839|Table not found.|
|-840|Name is too long.|
|-841|Name must start with a letter or '_' and contain letters, digits, or '_'.|
|-842|Cannot read temp file.|
|-843|Cannot write temp file.|
|-844|Statement is too long -- out of memory.|
|-845|There are no user-menus in the database.|
|-846|Number of values in load file is not equal to number of columns.|
|-847|Error in load file row %s.|
|-848|Form4gl could not compile Form.|
|-849|Warning found in Form specifications.|
|-850|User does not have permission to modify this menu.|
|-851|Cannot drop file (check file permissions).|
|-852|Write failed. %u rows unloaded (check ulimit or disk space).|
|-853|Current transaction has been rolled back due to error   or missing COMMIT WORK.|
|-855|Cannot drop rowids on a non-fragmented table.|
|-856|Rowids already exist on table.|
|-857|Rowids do not exist on table.|
|-858|Cannot specify the same partition/space name twice in a fragmentation specification.|
|-859|'Distributions Only' is not meaningful in an update statistics LOW request.|
|-860|A fragmented object must have at least one fragment.|
|-861|Cannot create new PDQ thread.|
|-862|Alter fragment attach must have at least one consumed table specified.|
|-863|Cannot detach a table with rowids.|
|-864|Cannot attach a table with rowids.|
|-865|Cannot add or drop the rowid column or the cdrserver and cdrtime columns in combination with other alter table options.|
|-866|Cannot attach tables that contain serial fields.|
|-867|Cannot generate new rowid.|
|-868|Cannot check constraints on the attaching table.|
|-869|Subqueries and procedures are not allowed in fragmentation expressions.|
|-870|Cannot specify duplicate remainder fragments.|
|-871|Remainder fragment must be specified last.|
|-872|Invalid fragment strategy or expression for the unique index.|
|-873|Invalid fragment expression column.|
|-874|General exception error has occurred in the optimizer.|
|-875|Incompatible Access Mode and Isolation Level.|
|-876|Cannot issue 'Set Transaction' in an active transaction.|
|-877|Isolation Level previously set by 'Set Transaction'.|
|-878|Invalid operation for a READ-ONLY transaction.|
|-879|Trim character must be null or have a length of 1.|
|-880|Trim character and trim source must be of string data type.|
|-881|The resulting string length from CONCAT, LPAD, REPLACE, JSON_EXTRACT, JSON_REPLACE or RPAD is longer than the maximum.|
|-882|Cannot create rowids on a non-fragmented table.|
|-883|Cannot evaluate the fragmentation expression.|
|-884|Cannot alter an index on a temporary table.|
|-885|Invalid or NULL utc time given to dbinfo(utc_to_datetime).|
|-886|Cannot drop table or view because of existing dependencies.|
|-887|Cannot revoke because of dependent privileges, views or constraints.|
|-888|Cannot attach a table with primary-key constraints.|
|-889|Internal dataskip condition, should reposition to next row and continue.|
|-890|Cursor must be declared on an INSERT statement with a VALUES clause.|
|-891|Temporary table objects can only be enabled.|
|-892|Cannot disable object (%s) due to other active objects using it.|
|-893|Cannot activate/create object (%s) because of its dependencies.|
|-894|Cannot find object (%s).|
|-895|Cannot create violations/diagnostics table.|
|-896|Violations table is not started for the target table.|
|-897|Cannot modify/drop a violations/diagnostics table.|
|-898|Cannot alter a table which has associated violations/diagnostics tables.|
|-899|Too many violations.|
|-900|Cannot read network user authorization file.|
|-901|User not found in network user authorization file.|
|-902|User not authorized or too many entries in authorization file.|
|-903|Licensed GBASEDBT-SQL server not accessible.|
|-904|Authorization file not on licensed GBASEDBT-SQL server.|
|-905|Cannot locate sqlexec service/tcp service in /etc/services.|
|-906|Cannot locate database server (check DBPATH).|
|-907|Cannot create socket on current database server.|
|-908|Attempt to connect to database server (%s) failed.|
|-909|Invalid database name format.|
|-910|Cannot create an GBasedbt Dynamic Server database from an GBASEDBT-SE client.|
|-911|System error - Cannot read from pipe.|
|-912|Network error - Could not write to database server.|
|-913|Network error - Could not read from database server.|
|-914|System error - Cannot write to pipe.|
|-915|Cannot create an GBASEDBT-SE database from an GBasedbt Dynamic Server client.|
|-916|NFS mount table error.|
|-917|Must close current database before using a new database.|
|-918|Unexpected data received from another database server.|
|-919|System error.  Wrong number of arguments to database server process.|
|-920|Cannot read host address in network data base.|


## sql4  

|ErrCode|Description|
|:---|:---|
|-980|Within Temp Table Create or Write or Execute is fault.|
|-998|Reserved for internal use.|
|-999|Not implemented yet.|
|-921|System error.  Illegal or wrong number of arguments to sqlexec server.|
|-922|Cannot get name of current working directory.|
|-923|GBase is licensed to access the current database server only.|
|-924|GBase is not licensed to access the specified database server.|
|-925|The protocol type should be tcp.|
|-926|The database server is not licensed for distributed data access.|
|-927|Exceeded limit on maximum number of servers you can reference.|
|-928|The database server is not licensed for distributed data access.|
|-929|SQLI Protocol Error.  Session terminated.|
|-930|Cannot connect to database server (%s).|
|-931|Cannot locate %s service/tcp service in /etc/services.|
|-932|Error on network connection, %s system call failed.|
|-933|Unknown network type specified in DBNETTYPE.|
|-934|Connection to remote site no longer valid.|
|-935|Cannot obtain IPX address for service name %s.|
|-936|Error on remote connection, %s.|
|-937|User Defined Routine error.|
|-938|VALUES clause may not have expressions if a cursor is declared on an INSERT.|
|-939|Due to large number of messages, some have been skipped.|
|-940|The statement failed because the WITH CHECK OPTION keywords are not supported in UNION, INTERSECT, or MINUS views.|
|-941|String processing error while evaluating function %s.|
|-942|Transaction commit failed - transaction will be rolled back.|
|-943|Found a non-terminated comment ('/*' with no matching '*/').|
|-944|Cannot use 'first', 'limit', 'top' or 'skip' in this context.|
|-945|Invalid parameter given to dbinfo(version).|
|-946|Source string for UPPER, LOWER and INITCAP must be of string type.|
|-947|Declaration of an SPL variable named 'null' conflicts with SQL NULL value.|
|-948|Cannot rename constraint index.|
|-949|Unable to alter fragmentation scheme when indexes disabled.|
|-950|User %s is not known on the database server.|
|-951|Incorrect password or user %s is not known on the database server.|
|-952|User (%s)'s password is not correct for the database server.|
|-953|Network server could not exec sqlexec program.|
|-954|Client is not known to database server.|
|-955|Database server could not receive data from client.|
|-956|Client host or user %s is not trusted by the server.|
|-957|Cannot create/access database on NFS mount.|
|-958|Temp table (%s) already exists in session.|
|-959|The current transaction has been rolled back due to an internal error.|
|-960|Invalid user per the SECURITY_LOCALCONNECTION configuration parameter.|
|-961|The password is too simple.|
|-962|Password is out of date. Password is out of date.|
|-963|The user is locked.|
|-964|The user is not known on the database server.|
|-965|Illeagl time for the user to login.|
|-966|Security authtication model is invalid by its error.|
|-967|The password is not set.|
|-968|Materialized view (%s) not found.|
|-969|DML operation is not legal on this view (%s).|
|-970|Materialized view name or table name length should not exceeds (%d).|
|-971|Integrity violations detected.|
|-972|Unable to alter table %s.|
|-973|Cannot insert from the violations table to the target table.|
|-974|Cannot drop not null constraint on the serial column.|
|-975|Invalid object and object mode combination.|
|-976|Table must be fragmented by expression to grant fragment authority.|
|-977|No permission on fragment (%s).|
|-978|No insert permission on the violations/diagnostics tables.|
|-979|Error encountered when parsing routine signature.|
|-981|INSERT operation disallowed on virtual columns.|
|-982|UPDATE operation disallowed on virtual columns.|
|-983|Virtual column is referenced in a column expression.|
|-984|Cannot modify data-type of virtual column.|
|-985|Virtual expression's value too large for the virtual column.|
|-986|Real column cannot have an expression.|
|-987|Column to be dropped or modified is used in a virtual column expression.|
|-988|Specified data type is not supported for a virtual column.|
|-989|Invalid column expression was specified.|
|-990|The maximum number of group items in rollup,cube,groupingsets is 255.|
|-991|The group by contains a maximum of 1000 group items.|
|-992|START value shouldn't be smaller than current.|
|-993|NEXT value shouldn't be smaller than current.|
|-994|START value minus current shouldn't be more than 24 hours.|
|-995|NEXT value should be later than START value.|
|-996|NEXT value minus current shouldn't be more than 24 hours.|
|-997|The NEXT value must exist.|
|-6501|Each the expression projection column in view query should be named.|
|-9400|User-defined aggregate %s already exists.|
|-9401|Cannot re-define or drop builtin aggregate %s.|
|-9402|Multiple occurrences of the %s modifier.|
|-9403|The %s modifier must be specified.|
|-9404|User-defined aggregate %s does not exist.|
|-9405|Must be owner of user-defined aggregate %s or DBA.|
|-9406|Cannot resolve support function for user-defined aggregate %s.|
|-9407|Set-up paramter to the aggregate %s cannot contain non-group columns.|
|-9408|User-defined aggregate %s has no arguments.|
|-9409|User-defined aggregate %s has too many arguments.|
|-9410|User-defined aggregate %s has two arguments but no INIT function specified.|
|-9411|User-defined aggregate support function %s does not handle nulls.|
|-9412|Return type of the support function %s does not match the aggregate state type.|
|-9421|Cannot use LOCKSSFU on queries resulting in table scan.|
|-9422|JDK 1.2 cannot be used with kernel AIO.|
|-9423|Transaction request %s failed to execute.|
|-9424|Server JDBC failed to get a row from the server.|
|-9425|Internal error with the Java memory pool.|
|-9426|Can't use Native threads in this configuration.|
|-9427|Can't use Green threads in this configuration.|
|-9428|Java configuration (%s) parameter error.|
|-9429|Java initialization failed, unable to find the library/routine (%s).|
|-9430|JNI internal error. Unable to find or execute JNI call (%s).|
|-9431|Can't find system class or method or library (%s).|
|-9432|Variable length UDTs are not supported in this version of Java.|
|-9433|Cannot position Blob/Clob.|
|-9434|Unexpected failure during initialization of Java virtual processor.|
|-9435|Unexpected failure during Java procedure execution.|
|-9436|Java UDR's VP class must be CLASS_JAVA.|
|-9437|Unable to get SQLException information.|
|-9438|Feature or method (%s) is not supported for opaque types.|
|-9439|Feature or method (%s) is not supported for distinct types.|
|-9440|Server JDBC failed to open cursor.|
|-9441|Cannot create UDR Thread (%s).|
|-9442|Error loading Java UDR class (%s).|
|-9443|Cannot find class for type (%s).|
|-9444|Initialization of Java virtual processor failed: (%s).|
|-9445|Java language manager operation failed (%s).|
|-9446|Execution of Java user-defined routine failed: (%s).|
|-9447|Cannot perform Java-to-SQL type mapping for type (%s).|
|-9448|Unequal number of parameters in SQL and Java signature (%s).|
|-9449|Java UDR method not found or is not static: (%s).|
|-9450|Java method invocation failed (%s).|
|-9451|Error instantiating user-defined-type mapping class (%s).|
|-9452|Error processing null argument. Use Java object form of type (%s).|
|-9453|The JDBC command doesn't return any rows.|
|-9454|Error getting length for user-defined type (%s).|
|-9455|Cannot access large object.|
|-9456|Cannot get large object length.|
|-9457|Cannot convert large object handle to byte[].|
|-9458|Cannot start large object search.|
|-9459|Large object Error: (%s).|
|-9460|Wrong connection for large object.|
|-9461|Cannot read (%s) bytes off binary stream.|
|-9462|Driver being shutdown.|
|-9463|Cannot load the specified IfxProtocol class: (%s).|
|-9464|Must specify user=name in the URL.|
|-9465|Must specify dbname in the URL.|
|-9466|Must specify password=value in the URL.|
|-9467|Driver shutdown, no new connection.|
|-9468|Cannot make UDR connection in non-UDR thread.|
|-9469|UDR connection failed.|
|-9470|Cannot establish JDBC connection for embedding application.|
|-9471|Database server connection failed.|
|-9472|Error creating Solano connection: (%s).|
|-9473|Connection to database failed.|
|-9474|Could not connect to database (%s).|
|-9475|Connection is closed.|
|-9476|Database server JDBC error: (%s).|
|-9477|Cannot obtain UDR environment.|
|-9478|VM too low on memory: (%s) bytes left.|
|-9479|Unknown throwable: (%s).|
|-9480|Unknown iterator code.|
|-9481|Internal Error: (%s).|
|-9482|Deployment descriptor file (%s) is not in the right format.|
|-9483|Unrecognized type: (%s).|
|-9484|Invalid jar name.|
|-9485|Attempt to install an existing jar: (%s).|
|-9486|Invalid URL.|
|-9487|Attempt to remove or alter path for non-existing jar: (%s).|
|-9488|Invalid jar removal. All dependent UDRs not dropped.|
|-9489|Invalid jar replacement. Class (%s) from old jar is still referenced.|
|-9490|No manifest file found for jar (%s).|
|-9491|User threads are not allowed in this context, must be a DBAThread.|
|-9492|Unsupported feature: (%s).|
|-9493|Unsupported command from deployment descriptor: (%s).|
|-9494|Java not supported in this IDS server or Error loading Java language module.|
|-9495|Database server JDBC internal error. Check with your administrator.|
|-9496|Unable to map Java type to an SQL type or SQL type to a Java type.|
|-9497|Scroll cursor is not a supported feature on the server JDBC yet.|
|-9498|Incorrect path to JAR file specified: (%s).|
|-9499|Internal JAR handling error. Check with your administrator.|
|-5801|HASH_AM: Cannot use hash access method to create index.|
|-5802|HASH_AM: No parameters specified.|
|-5803|HASH_AM: Syntax error in hashkey specification.|
|-5804|HASH_AM: Hashkey contains unknown column.|
|-5805|HASH_AM: Hashkey contains non-hashable column.|
|-5806|HASH_AM: Unknown or missing mode.|
|-5807|HASH_AM: Unknown parameter.|
|-5808|HASH_AM: Row size too big to fit the page with given fillfactor.|
|-5809|HASH_AM: Number_of_rows parameter is mendatory for static hashed table.|
|-5810|HASH_AM: Illegal or missing value for Number_of_rows parameter.|
|-5811|HASH_AM: Hashkey paramater is mendatory for a static hashed table.|
|-5812|HASH_AM: Table has columns of complex types.|
|-5813|HASH_AM: Average_rowsize specified is too small.|
|-5814|HASH_AM: Average_rowsize specified is too large.|
|-5815|HASH_AM: Illegal or missing value for average_rowsize.|
|-5816|HASH_AM: Average_rowsize specified for fixed length records.|
|-5817|HASH_AM: Illegal or missing value for fillfactor.|
|-5818|HASH_AM: Fillfactor is too large or too small.|
|-5819|HASH_AM: Unsupported fragmentation strategy.|
|-5820|HASH_AM: Fragment by expression columns must be subset of the hashkey.|
|-5821|HASH_AM: Hash key column of the inserted row has null value.|
|-5822|HASH_AM: A clustered index cannot be created on a hashed table.|
|-5823|HASH_AM: An index cannot be altered to cluster on a hashed table.|
|-5824|Improper target access method used to alter table or index.|
|-5848|A row with constraint violations exists.|
|-5849|The sub-query flattening settings for the query plan and the current value of NO_SUBQF environment variable do not match.|
|-5851|Invalid value specified to SUBSTRING function.|
|-5852|Invalid date.|
|-5853|The format element: (%s) does not have equivalent in GBasedbt.|
|-5854|Unrecognized format element: (%s).|
|-5855|The target string is not long enough to contain the converted format.|
|-5856|Maximum precision value for FLOAT data type must be between 1 and 16.|
|-5857|Using NULL in the RANGE or STEP expression is not possible.|
|-5901|Can't truncate table because an enabled referential integrity constraint exists.|
|-5902|Truncate Table cannot be rolled back|
|-5903|Only COMMIT WORK command is valid after  TRUNCATE  inside a transaction|
|-5904|Truncate Table cannot be used inside a transaction that already started|
|-9600|Internal error.|
|-9601|Variable (%s) has NULL value.|
|-9602|Illegal attempt to convert a collection type into another type.|
|-9603|Illegal attempt to use collection host variable.|
|-9604|Index not allowed on collections.|
|-9605|Scroll cursor can't select collection columns.|
|-9606|Collections are not allowed in the 'group by' clause.|
|-9607|Collections are not allowed in the 'distinct' clause.|
|-9608|Collections are not allowed in the 'order by' clause.|
|-9609|Collections are not allowed in the expression.|
|-9610|A collection data type must be supplied within this context.|
|-9611|FROM clause cannot have a join when one of the table is a collection.|
|-9612|No WHERE, GROUPBY, HAVING or ORDERBY clause are allowed on a collection.|
|-9613|Select list cannot have expression when selecting from a collection.|
|-9614|Derived column list is not allowed for this statement.|
|-9615|AT keyword is not allowed when inserting in a base table.|
|-9616|Position value should be specified through a constant or a variable.|
|-9617|Source for the SET clause should be a simple expression.|
|-9618|Aliasing is not allowed for a collection of ROW types.|
|-9619|Variable (%s) is not of collection type.|
|-9620|Can not select the collection variable (%s).|
|-9621|The number of derived columns do not match the actual number of columns.|
|-9622|Collection variable (%s) cannot be defined as Global.|
|-9623|Internal length must be greater than zero and smaller than 32760.|
|-9624|Maximum length must be greater than zero and smaller than 32740.|
|-9625|Alignment must be set to 1, 2, 4 or 8.|
|-9626|Maximum length should be set for variable-sized opaque types only.|
|-9627|Passedbyvalue can only be set if length is 1, 2, or 4.|
|-9628|Type (%s) not found.|
|-9629|Not owner of type.|
|-9630|Cannot drop type (%s): still in use.|
|-9631|Opaque type (%s) already exists in database.|
|-9632|Value does not match the type of column (%s).|
|-9633|ALTER TABLE can not modify column (%s) type.  Need a cast from the current type to the new type.|
|-9634|No cast from %s.|
|-9635|An attempt has failed to convert an opaque type into another type without a cast function.|
|-9636|Opaque type exceeded its maximum length.|
|-9637|Cast function (%s) does not exist.|
|-9638|Grant/Revoke under on base types disallowed.|
|-9639|Grant/Revoke under on distinct of non-row types disallowed.|
|-9640|Cannot drop type (%s): distinct type defined over the type.|
|-9641|Drop type can only drop opaque type or distinct type.|
|-9642|A quoted string exceeds 2147483648 bytes.|
|-9643|Type (%s) is not hashable.|
|-9644|Type (%s) does not have Equal function.|
|-9645|Cannot execute cast from user-defined data type to character format.|
|-9646|Result of a boolean expression is not of boolean type.|
|-9647|Cannot drop type (%s): cast(s) defined for the type.|
|-9648|Invalid value specified for a boolean type.|
|-9649|Cannot transport a user-defined type to client versions earlier than version 9.|
|-9650|Right hand side of IN expression must be a COLLECTION type.|
|-9651|The statement failed because binary large objects are not allowed in the Union, Intersect, or Minus queries.|
|-9652|Grant/Revoke UNDER on untyped table is not allowed.|
|-9653|UNDER privilege required to create subtype/subtable.|
|-9654|Element types of collection are not unique, explicit casting required.|
|-9655|Cannot rename a column in a typed table.|
|-9656|Cannot create a distinct type of type (%s)|
|-9657|Cannot determine the data type of a collection in the given expression.|
|-9700|Routine (%s) ambiguous - more than one routine resolves to given signature.|
|-9701|An EXTERNAL PROCEDURE cannot have a RETURN clause.|
|-9702|When a FUNCTION is created, the RETURN clause must be specified.|
|-9703|Modifiers VARIANT and NOT VARIANT cannot be used in the same routine.|
|-9704|For SPL routine, parameter must be named.|
|-9705|The modifier (%s) is not valid for SPL routines.|
|-9706|END PROCEDURE/FUNCTION does not match with CREATE PROCEDURE/FUNCTION.|
|-9707|Modifiers COMMUTATOR, NEGATOR and ITERATOR are not allowed for a PROCEDURE.|
|-9708|SELFUNC/SELCONST modifiers can be used only in FUNCTIONs.|
|-9709|More than one distinct type of the parameter type has cast from argument type.|
|-9710|Overloading of built-in functions is not allowed.|
|-9711|Late bound functions cannot have different number of return values.|
|-9712|Late bound functions cannot have different return types or lengths or precision/scale.|
|-9713|Identifier length exceeds the maximum allowed by this version of the server.|
|-9714|OUT parameter can only be the last parameter of a routine.|
|-9715|A procedure cannot have any OUT parameters.|
|-9716|This routine (%s) has the same specific name as another routine.|
|-9717|Owner name specified in the routine name and specific name must be the same.|
|-9718|Owner name specified in the specific name must be the current user.|
|-9719|A routine and an aggregate cannot share the same name.|
|-9720|Module name or language name specified is not valid.|
|-9721|Module named could not be unloaded while in use.|
|-9722|Specify a non-zero SQL error number in the RAISE EXCEPTION statement.|
|-9740|Execution of remote routine (%s) with non-built-in types is not allowed.|
|-9741|Internal error - cannot pass arguments in C style to routine requiring casts.|
|-9742|Implicit system cast failed.|
|-9743|Internal error - unable to determine all routines in statement.|
|-9744|BUILTIN routine %s defintion does not match internal operator.|
|-9745|Passing arguments in C style not yet supported for SPL routines.|
|-9746|(EV1 only) passing arguments in C style not supported for BUILTIN routines.|
|-9747|Passing arguments in C style not yet supported when using parameter defaults.|
|-9748|Cannot convert argument types when passing arguments by name, routine %s.|
|-9749|External functions are not yet supported in an iterator (cursory procedure) context.|
|-9750|Routine (%s) determined during PREPARE and BIND/EXECUTE return different types.|
|-9751|Cannot determine the return types of a routine routine_name acting on a collection-derived table during PREPARE.|
|-9752|Argument must be a Statement Local Variable or SPL variable or argument for an OUT or INOUT parameter.|
|-9753|Unable to find User Defined Routine with the given id.|
|-9754|No usage privilege.|
|-9755|Modifiers SELCONST and SELFUNC cannot be used in the same routine.|
|-9756|Modifiers COSTFUNC and PERCALL_COST cannot be used in the same routine.|
|-9757|Remote iterator function is not supported in this context.|
|-9780|SLV (%s) cannot be produced from a UDR called from outside the WHERE clause.|
|-9781|SLV cannot be an argument to a function invoked explicitly by EXECUTE or CALL.|
|-9782|Statement Local Variable (%s) has already been defined.|
|-9783|Statement local variable (%s) must be identified as a select number in the GROUP BY list.|
|-9784|SLV (%s) has no producer-UDR; or is outside the scope of the producer-UDR.|
|-9785|SLV (%s) cannot be accessed before it is produced by a UDR.|
|-9786|Only iterative UDR allowed in this context.|
|-9787|SLV's not allowed in the from clause.|
|-9788|Only OP_UDR is allowed as part of iterator derived table.|
|-9790|Language Manager initialization failed.|
|-9791|User Defined Routine (%s) execution failed.|
|-9792|User Defined Routine Language initialization failed.|
|-9793|User Defined Routine (%s) module load failed.|
|-9794|User Defined Routine (%s) load failed.|
|-9795|User Defined Routine unload failed.|
|-9796|User Defined Routine module unload failed.|
|-9797|User Defined Routine Language shutdown failed.|
|-9798|User Defined Routine Language lookup failed.|
|-9799|User Defined Routine (%s) VP context switch failed.|
|-9661|The statement failed because constraint (%s) cannot be enabled with NOVALIDATE option.|
|-9659|The server does not support the specified UPDATE operation on JSON documents.|
|-9660|The database server operation failed due to an invalid JSON document.|
|-9662|No user permission for %s|
|-9663|Cannot %s tenant database.|
|-9664|The length of rowtype exceeds the maximum length.|
|-9665|Max variable number of procedure exceeded.|
|-6000|Package (%s) can not be resolved.|
|-6050|Package subroutine (%s) redeclared.|
|-6051|Procedure (%s) already exists in database.|
|-6052|Package (%s) already exists in database.|
|-6053|Package (%s) spec must been created first.|
|-6054|Inconsistent name for package or procedure.|
|-6055|The routine name is error.|
|-6056|Constraint (%s) already exists in database.|
|-6057|Trigger (%s) already exists in database.|
|-6058|Index (%s) already exists in database.|
|-6059|Subroutine (%s) must be defined in the package body.|
|-6060|Package name cannot use reserved words.|
|-6100|Invalid package instance parameter (%s).|
|-6101|(%s) cannot be parsed, maybe be no permit, or no defined.|
|-6102|Package instance (%s) is not found.|
|-6103|Package instance(%s) is invalid, existing state of the package has been discarded, try again to re-instantiate.|
|-6104|Failed to get the definition for (%s).|
|-6105|Collection variable (%s) is not allowed in package.|
|-6106|(%s) cannot be found in package instance.|
|-6107|Cannot assign to constant vavlue (%s).|
|-6108|Blob variable (%s) is not allowed in package.|
|-6109|Invalid package exception (%s).|
|-6110|Package exception (%s) cannot be parsed, maybe be no permit, or no defined.|
|-6111|Package cursor (%s) cannot be parsed, maybe be no permit, or no defined.|
|-6112|Invalid package exception (%s).|
|-6113|Subprogram(%s) cannot be invoked, maybe be no permit, or no defined.|
|-6114|Previous use of '%s' conflicts with this use.|
|-6115|Invalid or missing procedure, function, or package name.|
|-6116|Identifier '%s' must be declared.|
|-6117|At most one declaration for '%s' is permitted.|
|-6118|A subprogram body must be defined for the forward declaration of %s.|
|-6119|Can not do ddl for global temp table because of existing dependencies.|
|-6120|The table is doing ddl,please wait for the ddl done.|
|-6121|The virtual column is not in the statement.|
|-6122|table must have at least 1 column that is not virtual.|
|-6123|group function is not allowed here.|
|-6124|column ambiguously defined.|
|-6125|Cache entry is still being used.|
|-6126|Statement control block has not been initialized.|
|-6127|Argument is out of range.|
|-6128|table %s does not have a materialized view log.|
|-6129|table %s does not contain a primary key constraint.|
|-6130|there is no materialized view log on table %s.|
|-6131|a materialized view log already exists on table %s.|
|-6132|create materialized view with fast method cannot contain %s .|
|-6133|create materialized view with fast method must contain the tables %s 's all primary key.|
|-6134|can not name a table start with 'mlog$_' or 'mtab$_'.|
|-6135|can not create or drop a trigger start with 'mtrg$_'.|
|-6136|can not create or drop a index start with 'midx$_'.|
|-6137|can not rename or alter a table with materialized view log.|
|-6138|can not rename a materialized view log.|
|-6139|can not rename a index start with 'midx$_'.|
|-6140|can not rename or alter a table dependent on a materialized view.|
|-6142|The pivot aggregate functions * the In arguments cannot be greater than 1024.|
|-6143|Can not do DDL for global temp table in a transaction, please commit the transaction.|
|-6144|Must name this expression with a column alias.|
|-6145|Inconsistent datatypes: expected - got %s.|
|-6200|WHEN clause cannot be used with table level triggers.|
|-6229|The TRIGGER reservation error.|
|-6230|Cursor Variables cannot be declared as part of a package.|
|-6231|TYPE attribute can not be applied to %s.|
|-6232|with ROWTYPE attribute, %s must name a table, cursor or cursor-variable.|
|-6240|Bind variable does not exist.|
|-6241|Not all variables bound.|
|-6242|Reference to uninitialized Collection/Record.|
|-6243|Component '%s' must be declared.|
|-6244|Subscript beyond count.|
|-6245|No function with name '%s' exists in this scope.|
|-6246|Expression is of wrong type.|
|-6247|Pipelined functions must have a supported collection return type.|
|-6248|Return statement in a pipelined function cannot contain an expression.|
|-6249|Wrong number or types of arguments in call to '%s'.|
|-6250|Cursor expression not allowed.|
|-6251|FOR UPDATE of this query expression is not allowed.|
|-6252|IN cursor '%s' cannot be OPEN'ed.|
|-6253|Cannot do an exact FETCH on a query with Nested cursors.|
|-6254|An INTO clause is expected in this SELECT statement.|
|-6255|Subscript outside of limit.|
|-6256|Inappropriate INTO.|
|-6257|CURSOR are not allowed in the 'order by' clause.|
|-6258|not a single-group group function.|
|-6259|must specify table name for nested table column or attribute.|
|-6260|'%s' name is already used by an existing object.|
|-6261|failure in creating storage table for nested table column '%s'.|
|-6262|specified column or attribute is not a nested table type.|
|-6263|cannot access rows from table item.|
|-6264|column of datatype Named Table Type cannot be unique or a primary key.|
|-6265|must specify table name for nested table column or attribute.|
|-6266|cannot create index on expression with datatype NAMED TABLE TYPE.|
|-6267|cannot create constraint on column of datatype Named Table Type.|
|-6268|Direct insert/update on SYS_NC columns are disallowed.|
|-6299|The ORACLE TYPE reservation error.|
|-6300|illegal ORACLE error number %s for PRAGMA EXCEPTION_INIT.|
|-6301|active autonomous transaction detected and rolled back.|
|-6302|Pragma AUTONOMOUS_TRANSACTION cannot be specified here.|
|-6303|Pragma AUTONOMOUS_TRANSACTION cannot be declared twice.|
|-6510|unhandled user-defined exception.|
|-6600|Specified partition does not exist|
|-6701|cannot perform a DML operation on a read-only view|
|-6702|The session has been restricted to read-only mode and can only perform select|
|-6703|The IP address is denied access,please contact the administrator.|
|-6704|'%s' already exists,please change the dblink name.|
|-6705|'%s' dblink is not exitsts.|
|-6706|Operate system table of dblink failute,please check sys.link$.|
|-6707|Get Database hostname,ip or port failture.|
|-6708|dblink does not support '%s' database, currently supports 'oracle' and 'gbase' databases.|
|-6709|DDL operations are not allowed on a remote database.|
|-6710|The length of dblink name exceeded 128 bytes.|
|-6711|the dblink '%s' connection description for remote database not found.|
|-6712|column of datatype TIME/TIMESTAMP WITH TIME ZONE cannot be unique or a primary key.|
|-6713|Operate system table of public synonym failute,please check sys.syn$.|
|-6714|In the using field,servername or dbname is null.|
|-6801|Another routine (%s) with same signature already exists in this WITH FUNCTION statement.|
|-6802|Specified partition does not exist.|
|-6803|The number of columns in the table can not be greater than 32767|
|-6804|The parameter type of the bin_to_num() function is incorrect.|
|-6805|Value exceeds string column length.column:%s.|
|-6811|The input datetime format or datetime string is invalidate.|
|-6812|Time is out of bounds.|
|-6813|Time conflicts with Julian date.|
|-6814|Format appears multiple times.|
|-6815|Format conflicts exist between the formats.|
|-6820|The memory is not enough for hash table, please reset memory size.|
|-6821|group function is not allowed here.|
|-6826|Json path error: (%s).|
|-6827|Invalid JSON text: (%s).|
|-6831|OR expression number exceeds the maximum 32767.|
|-6850|The number of columns in the IN clause does not match.|
|-6880|Cannot comment on a TempTable.|
|-6901|outer join operator (+) not allowed in operand of OR or IN.|
|-6902|illegal use of the outer join operator(+).|
|-6903|a column may not be outer-joined to a subquery.|
|-6904|two tables cannot be outer-joined to each other.|
|-6905|a predicate may reference only one outer-joined table.|
|-6906|an outer join cannot be specified on a correlation column.|
|-6907|The inserted comment description contains more than 4096 bytes.|
|-6908|an outer join cannot be specified on a trigger variable.|
