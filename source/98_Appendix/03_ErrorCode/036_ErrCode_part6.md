# GBase 8s数据库错误代码  
第六部分  

## sql5  

|ErrCode|Description|
|:---|:---|
|-8300|The specified sequence object (%s) is not in the database.|
|-8301|Sequence (%s) already exists in the database.|
|-8302|A Sequence object definition value is invalid or out of range.|
|-8303|Duplicate or conflicting (%s) specification in sequence definition.|
|-8304|MAXVALUE cannot be less than MINVALUE.|
|-8305|INCREMENT 0 is not allowed in sequences.|
|-8306|CACHE size should be in the range of 1 to 2,147,483,647.|
|-8307|CACHE size should be less than one cycle. The default CACHE size is 20.|
|-8308|Cannot set START value less than MINVALUE or greater than MAXVALUE.|
|-8309|Cannot RESTART the sequence at a value less than MINVALUE or greater than MAXVALUE.|
|-8310|MINVALUE cannot be set to exceed current value.|
|-8311|MAXVALUE cannot be set to be lesser than the current value.|
|-8312|No options specified for ALTER SEQUENCE.|
|-8313|Sequence (%s) exceeds its MAXVALUE.|
|-8314|Sequence (%s) goes below its MINVALUE.|
|-8315|Sequence (%s) CURRVAL is not yet defined in this session.|
|-8316|Cannot rename a sequence object using a synonym.|
|-8317|A sequence object cannot appear in the FROM clause.|
|-8318|This action is not allowed on sequence object.|
|-8319|Sequence object cannot be used here.|
|-8320|Only SELECT and ALTER are valid privileges for sequence objects.|
|-8321|Not owner of sequence object.|
|-8322|Remote sequences are not supported currently.|
|-8323|Remote sequence is not supported currently.|
|-8324|Serial foreign keys should not refer to serial unique keys.|
|-8325|Distinct clause is not allowed on a sequence.|
|-8328|Write failed. %.0lf rows unloaded (check ulimit or disk space).|
|-8329|Write failed. %lld rows unloaded (check ulimit or disk space).|
|-8331|Invalid table or view name (%s) in the REFERENCING clause of the CREATE PROCEDURE or CREATE FUNCTION statement.|
|-8332|Only NEW value of the column reference can be modified.|
|-8333|Invalid invocation of the routine with referencing clause.|
|-8334|REFERENCING clause cannot be used in external routines.|
|-8335|Usage of the Boolean function (%s) is not valid in this context.|
|-8336|Undefined symbol (%s).|
|-8337|New value of column reference (%s) cannot be modified.|
|-8351|Function (%s) Invalid input XML document or input XPATH string.|
|-8352|Function (%s) Empty input XML document.|
|-8353|Function (%s) NULL input XML document.|
|-8354|Function (%s) Exception received for ICU memory allocation.|
|-8355|Function (%s) Error parsing the input XML document.|
|-8356|Function (%s) Returned multiple nodes for the query.|
|-8357|Function (%s) Out of memory exception.|
|-8358|Function (%s) Connection Open Failed.|
|-8359|Function (%s) Error allocating temporary clob file.|
|-8360|Function (%s) Large Object spec init failed.|
|-8361|Function (%s) Failed to create a large object.|
|-8362|Function (%s) Failed to write to a large object.|
|-8363|Function (%s) NULL argument to the function.|
|-8364|Function (%s) NULL buffer passed.|
|-8365|Function (%s) NULL row descriptor.|
|-8366|Function (%s) Null type ID.|
|-8367|Function (%s) Null type descriptor.|
|-8368|Function (%s) Buffer size exceeds maximum size.|
|-8369|Function (%s) Memory allocation for internal buffer failed.|
|-8370|Function (%s) init failed.|
|-8371|Function (%s) create failed.|
|-8372|Function (%s) stat failed.|
|-8373|Function (%s) stat size failed.|
|-8374|Function (%s) write with seek failed.|
|-8375|General Exception.|
|-8376|Function (%s) null input large object handle.|
|-8377|Function %s failed because the first argument is too long.|
|-8378|Function %s failed because the second argument is too long.|
|-9200|Purpose routine (%s) is not yet supported with JVTI.|
|-9201|Secondary access method with Java am_purpose routine is not supported.|
|-9202|JVTI only supports external am_sptype in this release.|
|-9250|Xadatasource type (%s) already exists in database.|
|-9251|Xadatasource (%s) already exists in database.|
|-9252|Xadatasource type (%s) not found.|
|-9253|Xadatasource (%s) not found.|
|-9254|Improper purpose function (%s) used for xadatasource type.|
|-9255|Duplicate purpose function (%s) used for xadatasource type.|
|-9256|Required purpose function (%s) was not used for xadatasource type.|
|-9257|Improper value used for purpose function (%s) for xadatasource type.|
|-9258|Not an owner of xadatasource type or DBA.|
|-9259|Not an owner of xadatasource or DBA.|
|-9260|Cannot drop xadatasource type (%s) that is still in use.|
|-9261|Cannot drop xadatasource (%s) that is still in use.|
|-9262|Error %s purpose function.|
|-9263|Can't execute CREATE/DROP XADATASOURCE statements in non logging database.|
|-9265|Invalid xadatasource name.|
|-9266|Not in a transaction.|
|-9267|Xadatasource name is not present in the database.|
|-9268|Xadatasource name is not registered in the transaction.|
|-9269|xa_open purpose function of xadatasource has returned an error.|
|-9270|Type (%s) is unsupported in distributed queries.|
|-9271|Type (%s) is not identically defined in all the databases used in the distributed queries.|
|-9272|The data type (%s) is not supported for current client/server configuration.|
|-9273|Cannot create duplicate table (%s).|
|-9274|Complex type name length(%s) exceeds maximum allowed 65535.|
|-9275|Decimal data precision exceeds the allowable limit for DRDA connections.|
|-9300|Cannot set clear flag for UDT (%s) in global jar list.|
|-9301|Cannot set remove flag for jar(%s) in gloabl JVP list.|
|-9302|Cannot set new path flag for %s.|
|-9303|User SQL Exception. %s|
|-9304|Updatable scroll cursor features are not supported in this version.|
|-9800|Table (%s) is typed.|
|-9801|Can not alter table (%s) to add type. Incompatible.|
|-9802|Can not alter typed table (%s).|
|-9803|Can not create typed view (%s). Incompatible.|
|-9804|Can not generate ROWIDS on typed table (%s).|
|-9805|Serial/Serial8 datatypes allowed only as table column types.|
|-9806|Can not have duplicate/null field names in unnamed row types.|
|-9807|Temporary table (%s) can not be created with a type.|
|-9808|Subtable's type must be a subtype of supertable's type.|
|-9809|Cannot specify BLOBspace names on TEXT/BYTE field types.|
|-9810|Smart-large-object error.|
|-9811|Invalid smart-large-object fd (%d).|
|-9812|Can not do implicit begin work.|
|-9813|Can not do implicit commit work.|
|-9814|Invalid default sbspace name (%s).|
|-9815|Invalid filename specification (%s).|
|-9816|Btree index not allowed on blob/clob columns.|
|-9817|Functional key allowed only for Btree index.|
|-9818|Error detected in sql smart-large-object hash table.|
|-9819|Column (%s) incorrect type for storage in sbspace.|
|-9820|Sbspace (%s) does not exist.|
|-9821|Space (%s) is not an sbspace.|
|-9822|Can not delete smart-large-object.|
|-9823|Inconsistent use of procedure named return parameters.|
|-9824|Cannot perform more than one online create/drop index operation on table.|
|-9825|Online create/drop index not allowed on VII indexes.|
|-9826|Cannot perform online create/drop index operation along with storage optimization operation.|
|-9827|The sbspace specified by the SYSSBSPACENAME configuration parameter does not exist (%s).|
|-9831|Could not find opclass id (%d) while resolving compare routine for index.|
|-9832|Could not find routine (%s) while resolving compare routine.|
|-9833|Could not find extended type (%d) for index.|
|-9834|[Internal] Could not find routine env (%d) for functional key.|
|-9835|Could not find routine id (%d) for functional key.|
|-9836|Could not initialize sequence for routine (%s)|
|-9837|[Internal] Could not commute expression.|
|-9838|Cannot create operator class for a primary access method.|
|-9839|Cannot mix generic and specific operators in an operator class.|
|-9840|Invalid number of strategies or support function for btree.|
|-9841|Operator class for key part not specified or invalid.|
|-9842|Specification of ASC/DESC only applicable to btree.|
|-9843|Invalid number of arguments for functional key.|
|-9844|Invalid function (%s) used in a functional key.|
|-9845|Access method (%s) does not exist in database.|
|-9846|Operator class (%s) does not exist in database.|
|-9847|[Internal] Error while trying to set up start or end key for index read [%s]|
|-9848|Functional key part cannot use a variant function (%s)|
|-9849|Compare routine (%s) cannot be in SPL|
|-9850|Compare routine (%s) cannot be a variant function.|
|-9851|Access method (%s) already exists in database.|
|-9852|Improper purpose (%s) used for access method.|
|-9853|Duplicate purpose (%s) used for access method.|
|-9854|Required purpose (%s) not used for access method.|
|-9855|Improper value used for purpose (%s) for access method.|
|-9856|Index not created because the access method of the table does not support rowids.|
|-9857|Unknown space (%s) used for virtual table/index.|
|-9858|Unsupported option (%s) used for a virtual table/index.|
|-9859|Index not created because its access method does not support unique keys.|
|-9860|Improper access method used.|
|-9861|Improper access method parameter information used for a virtual table/index.|
|-9862|Could not initialize or execute access method routine.|
|-9863|Opclass (%s) already exists in database.|
|-9864|Improper strategy definition.|
|-9865|Improper support definition.|
|-9866|Cannot create external partition number.|
|-9867|Access method (%s) not found.|
|-9868|Not owner of access method.|
|-9869|Cannot drop access method (%s): still in use.|
|-9870|Cannot alter access method (%s): still in use.|
|-9871|Alter fragment attach/detach for virtual table not supported.|
|-9872|Cannot drop operator class (%s): still in use.|
|-9873|Not owner of operator class|
|-9874|Cannot rename database if it has a virtual table or index.|
|-9875|Bad internal structure for collection data: unknown flag value.|
|-9876|Opclass (%s) is not defined for this access method.|
|-9877|NULL without cast not allowed for row/collection constructed type.|
|-9878|An implied insert column does not accept NULLs.|
|-9879|Access method does not support clustered index.|
|-9880|Storage space (%s) is incompatible with the access method.|
|-9882|Access method AM_SPTYPE purpose value (%s) is invalid.|
|-9883|Could not determine the type of storage space (%s).|
|-9884|No default storage space exists for the access method.|
|-9885|Variant user defined routine cannot be used in check constraint or fragment expression.|
|-9886|User defined routine which generates OUTPUT parameter can not be used in check constraint or fragment expression.|
|-9887|Remote user defined routine or cross database user defined routine can not be used in check constraint or fragment expression.|
|-9888|Can not unidle a shared user defined routine sequence.|
|-9889|Cannot drop procedure (%s). It is currently in use by a casting function in either check constraint or fragmentation expression.|
|-9890|User defined function (%s) used in fragment expression does not match with any strategy functions of operator class.|
|-9901|Domains are not supported.|
|-9902|Domain (%s) not found.|
|-9903|Not owner of domain.|
|-9904|[Internal] Invalid extended type text.|
|-9905|[Internal] No extended type information for domain.|
|-9906|Cannot modify column datatype to collection type.|
|-9907|Not allowed to modify collection type column.|
|-9908|Columns of a row type may not contain fields of type text, byte, serial, serial8 or bigserial.|
|-9909|Nested row type not supported.|
|-9910|Byte, Text, Serial, Serial8 or Bigserial datatypes in collection or row type not allowed.|
|-9911|Defaults on collection type column not allowed.|
|-9912|Constraints on collection type column not allowed.|
|-9913|Collection derived table columns cannot be referenced in the 'where' clause of select, update, or delete statements or the projection list of select statements.|
|-9914|Cannot set the start serial value when creating named row types.|
|-9919|Cast already exists in database.|
|-9920|Cannot create a cast between identical types or between built-in types.|
|-9921|Cannot locate source type xid (%d).|
|-9923|Cannot create cast between incompatible types.|
|-9924|Return type of %s function does not match the expected type.|
|-9925|Must use default type parameter for distinct of %s type.|
|-9926|The statement failed becuase row-type or collection columns were referenced in ORDER BY, DISTINCT, UNIQUE, INDEX, UNION, INTERSECT, or MINUS specifications, or in primary key, foreign key, or unique constraints.|
|-9927|Cannot use distinct of TEXT/BLOB as a parameter type.|
|-9928|Must supply a cast function for cast between incompatible types.|
|-9929|Failure while getting unique constraints violations from table (%s).|
|-9930|Byte, Text, Serial, Serial8 or Bigserial datatypes in collection types not allowed.|
|-9931|Byte and Text datatypes in row and collection types not allowed.|
|-9932|External Directives feature is currently disabled.|
|-9933|Invalid Directive specification for external directives.|
|-9934|Only DBA is authorized to do this operation.|
|-9935|External Directives already exist for the query.|
|-9940|Bad constructor type information.|
|-9941|Expecting subtype for constructor (%s).|
|-9942|Function (%s) needs cast to more specific type.|
|-9943|The collection format is out of date. Recreate the collection data.|
|-9944|Cannot seek in non-scrollable collection|
|-9945|Cannot modify a read-only collection|
|-9946|Cannot open subquery collection twice|
|-9950|Field referencing is not possible for non-row type expressions.|
|-9951|One of the names in dotted sequence is  not right.|
|-9952|Aggregate within a ROW in a SELECT projection list is not allowed.|
|-9953|An aggregate function is not allowed in this context.|
|-9960|Combination of table/index fragmentation not allowed (%s)|
|-9961|Cannot drop inherited object (%s).|
|-9962|Non-collection host variable on right hand side of IN clause.|
|-9963|Cannot explicitly cast to sendrecv type.|
|-9964|Duplicate blob storage specification for column (%s)|
|-9965|The maximum number of allowable sbspaces (%s) has been exceeded.|
|-9966|Cannot create table with ref unless table is a typed table.|
|-9967|No privilege to grant on type.|
|-9968|Reference data type must reference a named row type (%s).|
|-9969|Corrupted collection type information.|
|-9970|Cannot determine host variable type during bind.|
|-9971|Cannot determine the return types of a query or return types are inconsistent.|
|-9972|ROW Type expected.|
|-9973|Row buffer for collection of fixed size elements not of correct size.|
|-9974|Cannot delete element from a ROW Type.|
|-9975|Type of a table must be unique within a table hierarchy.|
|-9976|Manipulation of NULL collection disallowed.|
|-9977|Internal Error: hash value out of sync.|
|-9978|Insertion of NULLs into a collection disallowed.|
|-9979|Updating of a collection element to NULL is disallowed.|
|-9980|LIST expected when inserting AT position.|
|-9981|Delete disallowed on collection with other cursor references.|
|-9982|Update disallowed on collection with other cursor references.|
|-9983|Deleting a non-existing element.|
|-9984|Cannot free a collection with other cursor references.|
|-9985|Internal Error: invalid change log.|
|-9986|Internal Error: corrupted collection.|
|-9987|Cursor already registered.|
|-9988|Cannot flatten a collection with other cursor references.|
|-9989|Incorrect number of fields in the ROW Type.|
|-9990|Cannot drop named row type (%s): still in use.|
|-9991|Named row type (%s) already exists in database.|
|-9992|Named row type (%s) not found.|
|-9993|Not owner of named row type.|
|-9994|Cannot use ONLY(TABLE(str)) over collections|
|-9995|Table (%s) is not typed.|
|-9996|Distinct type (%s) already exists in database.|
|-9997|No usage privilege on data type (%s).|
|-9998|No privilege to drop a cast of this DISTINCT data type.|
|-9999|Routine collcompare() is not supported.|


## sql6  

|ErrCode|Description|
|:---|:---|
|-19800|Role name already exists as a user or role.|
|-19801|Role name cannot be %s.|
|-19802|Name cannot appear as both the role grantor and the role grantee.|
|-19803|Only role administrator or DBA can grant, revoke or drop role.|
|-19804|Role does not exist.|
|-19805|No privilege to set to the role.|
|-19806|Cannot grant database privileges or default role to a role.|
|-19807|Cannot grant privileges to a role WITH GRANT OPTION.|
|-19808|Username already exists as a rolename in the database.|
|-19809|Invalid password to access the database.|
|-19810|Cannot set database password for a role.|
|-19811|DBpassword should not exceed 8 characters.|
|-19812|Illegal usage of replication shadow columns.|
|-19813|Cannot add CRCOLS when table already has replication shadow columns.|
|-19814|Cannot drop CRCOLS when table does not have replication shadow columns.|
|-19815|Cannot create a temp table with CRCOLS.|
|-19816|Cannot perform this operation on a table defined for replication.|
|-19990|Use of CRCOLS must be consistent across the table hierarchy.|
|-19817|Invalid syntax for STMT_CACHE_DEBUG environment variable.|
|-19818|Cannot open file for statement cache debug|
|-19819|An ON clause has an invalid table reference.|
|-19820|GBasedbt OUTER JOIN and ANSI JOIN in the same query block.|
|-19821|Cannot rename a table using a synonym.|
|-19822|Cannot alter or truncate a table or drop a table or view using a synonym.|
|-19823|Cannot use EXECUTE PROCEDURE INTO with the INSTEAD OF trigger.|
|-19824|Cannot use BEFORE or AFTER action with the INSTEAD OF trigger.|
|-19825|Cannot use WHEN clause if INSTEAD OF trigger is defined.|
|-19826|Cannot create INSTEAD OF trigger for a select event.|
|-19827|Cannot create an INSTEAD OF trigger on a table (%s).|
|-19828|ORDER BY column or expression must be in SELECT list in this context.|
|-19829|LVARCHAR/RAW column size exceeds 32739.|
|-19830|This operation is not allowed on a table where the type is raw.|
|-19831|Referential constraints are not allowed on tables of type raw.|
|-19832|Cannot alter table type in combination with other alter table options.|
|-19833|Table type raw not allowed together with access method.|
|-19834|Error in unload due to invalid data : row number %d.|
|-19835|Cannot create an attached index with a collation different from that of DB_LOCALE|
|-19836|Extent size is too large.  Maximum size of an extent is %sk.|
|-19837|Invalid PDQ priority value specified.|
|-19838|Invalid partition accessed by dirty reader.|
|-19839|Invalid OPTCOMPIND value specified.|
|-19840|Invalid session environment variable.|
|-19844|Tables of type raw are not allowed in a logged database on an HDR primary server.|
|-19845|You cannot alter the logging mode of a table in a logged database on a primary server.|
|-19846|You cannot access a nonlogging table (%s) in a logged database on a secondary server.|
|-19841|Error In Specifying Automatically (Server) Generated Keys.|
|-19842|Invalid USELASTCOMMITTED value specified.|
|-19843|Invalid IFX_AUTO_REPREPARE value specified.|
|-19847|Incorrect session optimization environment variable.|
|-19848|Incorrect STAR_JOIN value specified.|
|-19849|Error in unload due to invalid data : row number %s.|
|-19850|Invalid OPT_SEEK_FACTOR value specified.|
|-19851|Invalid OPT_CPUCOST_FACTOR value specified.|
|19800|QUERY:|
|19801|Subquery:|
|19802|Estimated Cost:|
|19803|Estimated # of Rows Returned:|
|19804|Union Query|
|19805|Temporary Files Required For:|
|19806|REMOTE PATH|
|19807|SEQUENTIAL SCAN|
|19808|AUTOINDEX PATH|
|19809|INDEX PATH|
|19810|Remote SQL Request:|
|19811|Filters:|
|19812|Index Keys:|
|19813|(Key-Only)|
|19814|Lower Index Filter:|
|19815|Upper Index Filter:|
|19816|(Temp Table For View)|
|19817|PostIndex Filter:|
|19818|<subquery>|
|19819|agg|
|19820|cursor declaration(%s) hides outer declaration|
|19821|variable declaration(%s) hides outer declaration|
|19822|identifier(%s) is a variable, not a column|
|19823|SORT SCAN:|
|19824|MERGE JOIN|
|19825|Merge Filters:|
|19826|Other Join Filters:|
|19827|expression:|
|19828|for statement|
|19829|iteration of cursory procedure|
|19830|end cursor|
|19831|error string =|
|19832|trace expression :|
|19833|illegal trace option|
|19834|start select cursor.|
|19835|start procedure cursor.|
|19836|select cursor iteration.|
|19837|for loop variable|
|19838|evaluates to|
|19839|global variable|
|19840|default value|
|19841|raise exception :|
|19842|SQL error|
|19843|ISAM error|
|19844|Participant site %s heuristically rolled back.|
|19845|Prepared participant site %s did not respond.|
|19846|Prepared participant site %s not responding.|
|19847|Mixed transaction result.|
|19848|Possible mixed transaction result.|
|19849|Transaction heuristically rolled back.|
|19850|Line %d:|
|19851|exception : looking for handler|
|19852|exception : handler FOUND|
|19853|exception : no appropriate handler|
|19854|Error initializing data dictionary hash table.|
|19855|Error initializing cache.|
|19856|Error initializing SPL routine hash table.|
|19857|Scan will use Smart Disk|
|19858|Smart Disk not used because:|
|19859|skinhibit is set|
|19860|the table is not accessible to Smart Disk|
|19861|no Smart Disk capability|
|19862|table is too small|
|19863|of insufficient memory|
|19864|no suitable filter was found|
|19865|before actions:|
|19866|end before actions|
|19867|for each row actions:|
|19868|after actions:|
|19869|end for each row actions|
|19870|end after actions|
|19871|Error initializing data distribution hash table.|
|19872|(expression)|
|19873|(Aggregate)|
|19874|Parallel|
|19875|Serial|
|19876|ALL|
|19877|NONE|
|19878|(FALSE)|
|19879|DYNAMIC HASH JOIN|
|19880|(Build Outer)|
|19881|Dynamic Hash Filters:|
|19882|Maximum Threads|
|19883|(TRUE)|
|19884|Access mode set.|
|19885|Scan uses Hash Filter|
|19886|Data source accessed using gateway (%s) might be in an inconsistent state.|
|19887|Gateway diagnostics: %d %s.|
|19888|VTI SCAN|
|19889|VII Index Keys:|
|19890|VTI Filters:|
|19891|VII Index Filter:|
|19892|(sampcnt)|
|19893|(medcnt)|
|19894|(Key-First)|
|19895|(Semi Join)|
|19896|(Skip Duplicate)|
|19897|(First Row)|
|19898|NESTED LOOP JOIN|
|19899|Index Key Filters:|
|19900|INDEX|
|19901|AVOID_INDEX|
|19902|FULL|
|19903|AVOID_FULL|
|19904|ORDERED|
|19905|USE_NL|
|19906|AVOID_NL|
|19907|USE_HASH|
|19908|AVOID_HASH|
|19909|FIRST_ROWS|
|19910|ALL_ROWS|
|19911|EXPLAIN|
|19912|UNKNOWN|
|19913|Error|
|19914|DIRECTIVES OFF|
|19915|DIRECTIVES DISABLED|
|19916|DIRECTIVES FOLLOWED|
|19917|DIRECTIVES NOT FOLLOWED|
|19918|Multiple directives of same type on same table.|
|19919|Invalid Table Name Specified.|
|19920|Invalid Index Name Specified.|
|19921|This directive cannot be specified in query with remote table.|
|19922|Directives rule out all access paths for table.|
|19923|Cannot Obey Access Method directives for given table.|
|19924|Cannot use USE_NL for *all* tables.|
|19925|Cannot use USE_NL for first table with ORDERED.|
|19926|Outerjoin nesting not compatible with ORDERED.|
|19927|Hash-Join cannot be forced w/o equality predicate or with Complex Outerjoins.|
|19928|Probe option disallowed for OUTER table of Outerjoin.|
|19929|Multiple optimization goal directives not allowed.|
|19930|Optimization goal directive only allowed in top-level query.|
|19931|Optimization goal directive allowed in first query of UNION.|
|19932|Optimization goal directive not allowed inside Views.|
|19933|Explain directive only allowed in top-level query.|
|19934|Explain directive only allowed in first query of UNION.|
|19935|Explain directive not allowed inside Views.|
|19936|Directives not allowed with WHERE CURRENT OF statement.|
|19937|ORDERED both inside and outside View not allowed.|
|19938|Join Method directive cannot be obeyed (Unspecified Reason).|
|19939|Multiple directives of same type.|
|19940|Join directives not compatible with Outerjoin nesting.|
|19941|Access Method directives not allowed on View or Derived Table.|
|19942|Join Method directives not allowed on View or Derived Table.|
|19943|Join Method and Ordered directives conflict or hash join cannot be enforced.|
|19944|ORDERED in/with View or Subquery|
|19945|BUILD|
|19946|PROBE|
|19947|Same index specified multiple times on same table.|
|19948|Opt Goal directive not allowed in UPDATE/DELETE.|
|19949|Directive already followed by ORDERED in parent query.|
|19950|Directive overridden by sub-query flattening.|
|19951|COLLECTION SCAN|
|19952|(Temp Table For Group By)|
|19953|Directive is not compatible with SLV usage.|
|19954|Site Directive not compatible with other directives.|
|19955|SITE|
|19956|AVOID_SITE|
|19957|SITE directive cannot be satisfied on Remote outer table.|
|19958|Site directive not compatible with other Site directive or Local table.|
|19959|Site directive not compatible with Join Method directive(s).|
|19960|USE_SUBQF|
|19961|AVOID_SUBQF|
|19962|Conflicting multiple subquery flattening directives specified|
|19963|Subuery flattening directives can be specified only for subqueries|
|19964|(Unique)|
|19965|AVOID_EXECUTE|
|19966|EXPLAIN_ALL|
|19967|This directive cannot be specified in query with ansi join.|
|19968|(All fragments may be re-considered for further execution of same query,   based on values of host variables.)|
|19969|(Temp Table For Collection Subquery)|
|19970|External Directives in effect.|
|19971|REMOVE DUPLICATES|
|19972|Remove Duplicates Keys:|
|19973|Index Self Join Keys|
|19974|Lower bound:|
|19975|Upper bound:|
|19976|INDEX_SJ|
|19977|AVOID_INDEX_SJ|
|19978|Invalid index specified in INDEX_SJ or AVOID_INDEX_SJ directive.|
|19979|(FULL OUTER JOIN PHASE 1)|
|19980|(FULL OUTER JOIN PHASE 2)|
|19981|(fragments might be eliminated at runtime because filter contains   runtime constants)|
|19982|ON-Filters:|
|19983|PostJoin-Filters:|
|19984|(LEFT OUTER JOIN)|
|19985|(Key-Start)|
|19986|Server received an invalid id number for locating a remote server endpoint.|
|19987|ITERATOR SCAN|
|19988|(FULL OUTER JOIN)|
|19989|STATISTICS|
|-19989|Enterprise Replication is not in active state|
|-19991|Table is not in Enterprise Replication alter mode|
|-19992|Cannot perform insert/delete/update operations on a replicated table while the table is in alter mode|
|-19993|Cannot modify a replicated column|
|-19994|Cannot drop a replicated column while the column is part of replicate definition|
|-19995|Enterprise Replication error encountered while setting alter mode. See message log file to get the Enterprise Replication error code|
|-19996|Enterprise Replication error encountered while unsetting alter mode. See message log file to get the Enterprise Replication error code|
|-19997|Cannot alter table type to STANDARD, failed to write a log record.|
|19998|Warning:Privilege not revoked.|
|19999|Warning:Data Commit is a result of an unhandled exception in TXN PROC/FUNC/TRI|


## sql7  

|ErrCode|Description|
|:---|:---|
|600|Script saved in '%s'|
|601|Query interrupted before it completed|
|602|No where clause on Delete or Update, every row in table will be affected|
|603|< Additional lines not displayed >|
|604|Error in line %d|
|605|Near character position %d|
|611|Column name	    Type|
|612|User	     select              update              insert   delete   index|
|613|Table Name          Owner  Row Size  Columns    Created      Audit File|
|614|Index name	    Owner       Type      Columns|
|615|Table name|
|700|No forms are available - Use create to create one|
|701|No reports are available - Use create to create one|
|702|No databases are available - Use create to create one|
|703|Form with the same name already exists|
|704|Report with the same name already exists|
|705|Database with the same name already exists|
|706|Form was successfully compiled|
|707|Report was successfully compiled|
|793|%lld row(s) loaded.|
|794|%.0lf row(s) loaded.|
|795|%lld row(s) unloaded.|
|796|%.0lf row(s) unloaded.|
|797|%u row(s) unloaded.|
|798|%u row(s) loaded.|
|799|No rows found.|
|801|Database selected.|
|802|%u row(s) retrieved.|
|803|%u row(s) retrieved into temp table.|
|804|%d row(s) updated.|
|805|%u row(s) deleted.|
|806|%u row(s) inserted.|
|809|%u row(s) inserted.|
|810|Table locked.|
|811|Table unlocked.|
|812|Database created.|
|813|Database dropped.|
|814|Table created.|
|815|Table dropped.|
|816|Index created.|
|817|Index dropped.|
|818|Permission granted.|
|819|Permission revoked.|
|820|Table renamed.|
|821|Column renamed.|
|822|Audit created.|
|825|Audit dropped.|
|826|Table recovered.|
|827|Table checked.|
|828|Table repaired.|
|829|Table altered.|
|830|Statistics updated.|
|831|Database closed.|
|832|%u row(s) deleted.|
|833|%d row(s) updated.|
|834|Started transaction.|
|835|Data committed.|
|836|Transaction rolled back.|
|837|Savepoint %d.|
|838|Database started.|
|839|Database rolled forward.|
|840|View created.|
|841|View dropped.|
|842|Debug.|
|843|Synonym created.|
|844|Synonym dropped.|
|845|Temporary table created.|
|846|Lockmode set.|
|847|Index altered.|
|848|Isolation level set.|
|849|Log set.|
|850|Explain set.|
|851|Schema created.|
|852|Optimization option set.|
|853|Routine created.|
|854|Routine dropped.|
|855|Constraint mode set.|
|856|Routine executed.|
|857|Debug file for trace opened.|
|858|Optical cluster created.|
|859|Optical cluster altered.|
|860|Optical cluster dropped.|
|861|Reserved optical volume.|
|862|Released optical volume.|
|863|Mounting timeout set for optical media.|
|864|Routine Statistics updated.|
|867|Smart Disk Inhibit set.|
|868|Smart Disk Show set.|
|869|Smart Disk All set.|
|870|Trigger created.|
|871|Trigger dropped.|
|872|Statement with foreign SQL syntax executed.|
|873|Dataskip set.|
|874|PDQ Priority set.|
|875|Alter fragment completed.|
|876|Mode set.|
|877|Table started.|
|878|Table stopped.|
|879|Session level set.|
|880|Session authorization set.|
|881|Table high set.|
|882|Extent size set.|
|883|Role created.|
|884|Role dropped.|
|885|Role set.|
|886|DBpassword set.|
|887|Database renamed.|
|888|Domain created.|
|889|Domain dropped.|
|890|Row type created.|
|891|Row type dropped.|
|892|Distinct type created.|
|893|Cast created.|
|894|Cast dropped.|
|895|Opaque type created.|
|896|Type dropped.|
|897|Routine altered.|
|898|Access_method created.|
|899|Access_method dropped.|
|900|Access_method altered.|
|901|Opclass created.|
|902|Opclass dropped.|
|903|Constructor created.|
|904|Memory resident status changed.|
|905|Aggregate created.|
|906|Aggregate dropped.|
|907|PLOAD file opened.|
|908|Index checked.|
|909|SCHEDULE level set.|
|910|Environment set.|
|911|Statement executed.|
|912|Statement executed.|
|913|Statement executed.|
|914|Statement executed.|
|915|Statement cache set.|
|916|Index renamed.|
|917|ServerUuid created.|
|918|SerrverUuid dropped.|
|919|ServerUuid altered.|
|920|Opaque type altered.|
|921|Constructor type altered.|
|922|Table truncated.|
|923|Implicit transaction set.|
|924|Sequence created.|
|925|Sequence dropped.|
|926|Sequence altered.|
|927|Sequence renamed.|
|928|Table truncated.|
|929|Collation set.|
|930|Default collation set.|
|931|Role set.|
|932|Encryption password set.|
|933|External directives saved.|
|934|Xadatasource type created.|
|935|Xadatasource created.|
|936|Xadatasource type dropped.|
|937|Xadatasource dropped.|
|938|Table truncated.|
|939|Security label component created.|
|940|Security label component altered.|
|941|Security label component dropped.|
|942|Security label component renamed.|
|943|Security policy created.|
|944|Security policy dropped.|
|945|Security policy renamed.|
|946|Security label created.|
|947|Security label dropped.|
|948|Security label renamed.|
|949|DBSECADM granted.|
|950|DBSECADM revoked.|
|951|Security exemption granted.|
|952|Security exemption revoked.|
|953|Security label granted.|
|954|Security label revoked.|
|955|SETSESSIONAUTH privilege granted.|
|956|SETSESSIONAUTH privilege revoked.|
|957|Session import set.|
|959|Savepoint set.|
|960|Savepoint released.|
|961|Transaction rolled back to savepoint.|
|962|%d row(s) merged.|
|963|%u row(s) retrieved into table.|
|964|Access granted.|
|965|Access revoked.|
|967|Trusted context created.|
|968|Trusted context altered.|
|969|Trusted context dropped.|
|970|Trusted context renamed.|
|971|User created.|
|972|User altered.|
|973|User dropped.|
|974|User renamed.|
|975|User password changed.|
|976|Comments changed.|
|977|Comments on column changed.|
|978|Package created.|
|979|Package body created.|
|980|Package has already been dropped.|
|981|PL/SQL procedure successfully completed.|
|982|Global temporary table successfully created.|
|983|Materialized view refreshed.|
|984|WITH FUNCTION execute successfully.|
|985|Oracle Type created.|
|986|Oracle Type dropped.|
|987|DBLINK object successfully created.|
|988|DBLINK object has already been dropped.|
|989|DBLINK object successfully altered.|
|990|Materialized view log created.|
|991|Materialized view log dropped.|
|992|Materialized view log refresh.|
|993|Materialized view alter success;|
|994|Exec collection method success;|
|995|Comments on materialized view changed.|
|996|Oracle Type body created.|
|997|Oracle Type body dropped.|
|998|Oracle Type alter.|
|999|Oracle Type body alter.|
|-25700|UUID Cache corrupted/not initialized.|
|-25701|The specified servername (%s) is not in SYSSERVERS.|
|-25702|Error receiving the UUID from remote server (%s).|
|-25703|UUID cache not initialized.|
|-25704|Attempt to increment/decrement the reference count on a remote smartblob.|
|-25705|Invalid UUID. Server name corresponding to the UUID cannot be located.|
|-25706|Attempt to delete ServerUuid entry for the local server.|
|-25707|Attempt to alter ServerUuid entry for local server.|
|-25708|Unable to find servername from UUID.|
|-25709|Server received an invalid id number for locating a remote server endpoint.|
|-25710|Invalid routine structure in server to server fastpath call.|
|-25711|No more than 3 connections can be involved in a single fastpath call.|
|-25712|Routine (%s) cannot be called from a remote server.|
|-25713|Attempting to run a cross server routine (%s) in parallel.|
|-25718|Cannot insert or update from a non logging database to a logging database.|
|-25720|Invalid combination of modifiers DISTRIBUTEBINARY and (%s).|
|-25721|Invalid combination of modifiers ISCANONICAL and DONOTDISTRIBUTE.|
|-25722|Invalid combination of modifiers DONOTDISTRIBUTE and DISTRIBUTESREFERENCES.|
|-25723|A modifier may not appear more than once in an ALTER statement.|
|-25724|May not modify built in type (%s).|
|-25725|Attempt to add duplicate modifier (%s).|
|-25726|Attempt to drop non-existent modifier (%s).|
|-25727|Modifier (%s) is incompatible with SRVSENDRECV/DBSENDRECV cast.|
|-25728|Type (%s) is not the same in the local and remote database.|
|-25729|Type (%s) may not be used in a distributed query (DONOTDISTRIBUTE).|
|-25731|Error opening the remote file: %s.|
|-25732|Error closing the remote file.|
|-25733|Error reading from the remote file.|
|-25734|File descriptor is invalid.|
|-25735|Error writing to the remote file.|
|-25736|The extended type (%s) has not been defined in the local database.|
|-25739|The column definition for (%s) does not match the local definition.|
|-25740|Access to remote User Defined Types in this version is not allowed.|
|-25741|The column type for (%s) does not match with the local definition.|
|-25745|UUID already exists for (%s).|
|-25746|UUID does not exist for (%s).|
|-25747|Do not have permissions to execute the drop serveruuid statement.|
|-25748|Incorrect server or cursor name format.|
|-25737|Cluster Indexes cannot be created in an online environment.|
|-25738|Index can be created online only for btree secondary access method.|
|-25785|Cannot create external routine (%s) without the EXTEND role.|
|-25786|Only DBSA can grant/revoke permissions for the EXTEND role.|
|-25787|Drop EXTEND role while converting to 10.00.|
|-25788|Cannot unload or reload module without the EXTEND role.|
|-25789|The file name in SET EXPLAIN FILE or SET DEBUG FILE must be a non-null string.|
|-25790|File name in SET EXPLAIN FILE or SET DEBUG FILE statement is too long.|
|-25791|Cannot execute privileged built-in Java routine (%s) without the EXTEND role or DBSA authority.|
|-25800|Cannot specify overlapping fragment expressions for interval or list fragmentation.|
|-25801|Cannot specify a dbspace more than once in the STORE IN clause.|
|-25802|The PARTITION clause is mandatory for interval and list fragmentation.|
|-25803|Interval or list fragmentation must have at least one non-null, non-remainder fragment.|
|-25804|The interval value must be a non-zero positive constant.|
|-25805|The interval value must be a numeric or INTERVAL data type.|
|-25806|The fragment key for interval fragmentation must be a numeric, DATE, or DATETIME type.|
|-25807|The fragment key for interval fragmentation must be a single column expression.|
|-25808|The expression defining the upper limit of each fragment must be a constant.|
|-25809|One or more dbspaces specified in the STORE IN clause does not exist.|
|-25810|The fragment key, interval value, and upper limit of the fragments are not compatible.|
|-25811|The transition value for interval fragments must be aligned to the boundary of the interval value type.|
|-25812|The difference between the old and new transition values must be a multiple of the interval value.|
|-25813|The partition name used in the fragmentation scheme is not allowed.|
|-25814|Incorrect argument passed to function NUMTOYMINTERVAL(), NUMTODSINTERVAL(), TO_YMINTERVAL(), or TO_DSINTERVAL().|
|-25815|The expression defining the list of values for a fragment in list fragmentation must be a constant.|
|-25816|The dbspace (%s) does not exist in list of dbspaces for interval fragments.|
|-25817|Cannot drop or detach the only remaining non-null, non-remainder fragment.|
|-25818|The specified operation or syntax is not supported.|
|-25819|The INTERVAL clause is allowed with interval fragmentation scheme only.|
|-25820|Cannot attach two non-fragmented tables to create an interval or list fragmented table.|
|-25821|Internal error: The interval or list fragmented table/index has zero fragments.|
|-25822|Unable to determine fragment position for fragments while moving to new fragmentation scheme.|
|-25823|Cannot specify BEFORE or AFTER clause while adding or attaching a fragment.|
|-25824|The upper limit of the fragment must be aligned to an interval fragment boundary.|
|-25825|Cannot specify remainder fragment for interval fragmentation.|
|-25826|Cannot specify more than one null fragment for interval or list fragmentation.|
|-25827|Cannot add or attach a fragment expressions that matches an exisitng fragment expression.|
|-25828|An error occurred while adding or attaching a fragment to the initial range fragments.|
|-25829|Cannot modify the fragment expression for an interval fragment.|
|-25830|The new fragment expression cannot cross adjacent fragment boundaries.|
|-25831|Cannot modify fragment expression for transition fragment.|
|-25832|Internal error: Could not modify the transition value.|
|-25833|Internal error: The compact representation of fragment partitioning could not be constructed.|
|-25834|The specified alter fragment operation cannot be performed online.|
|-25835|The transition value specified is not valid.|
|-25836|The transition value must be a non-null constant.|
|-25837|Cannot truncate an index fragment.|
|-25838|Duplicate partition name in the list of fragments for truncation.|
|-25839|Internal error: Could not find the transition fragment.|
|-25840|An error occurred during online attach of fragment.|
|-25841|An error occurred during online detach of fragment.|
|-25842|An online alter fragment operation cannot be performed in a transaction that has modified objects in a database.|
|-25843|An online alter fragment operation cannot be performed in a transaction that has explicitly locked the table that is being altered.|
|-25844|Cannot create an interval fragmented temporary table or index.|
|-25845|An online operation is already in progress on this table.|
|-25846|Cannot alter the fragmentation scheme online if replication is defined on the table.|
|-25847|The fragments of the table or index have changed.|
|-25848|The functional key argument is invalid.|
|-25849|The indexkey size exceeds the catalog column size.|
|-25850|The window frame extent specification requires window order clause.|
|-25851|The window frame extent value specification are not correct.|
|-25852|The window frame extent BETWEEN options are not valid.|
|-25853|The ntile, lead, lag and ranking window functions require window order.|
|-25854|The ntile, lead, lag, ranking and row_number window functions can not have window frame extent.|
|-25855|The option specified is not supported with window aggregates.|
|-25856|Invalid usage of window aggregate in this context.|
|-25857|Invalid usage of DISTINCT aggregate in this context.|
|-25858|DISTINCT aggregate can not have ORDER BY clause or window frame extent.|
|-25859|The argument to NTILE window function is invalid.|
|-25860|The offset of the LEAD, LAG window function is invalid.|
|-25861|The types of default expression and expression of LEAD, LAG are not compatible.|
|-25862|The argument to RATIO_TO_REPORT window function is invalid.|
|-26000|%s cannot be limited for a user who has administrative privileges.|
|-26001|The encryption/decryption password is not set.|
|-26002|The encryption password is invalid because the specified password data type   is not supported.|
|-26003|The encryption password is invalid because the length of the specified   password was less than 6 bytes or greater than 128 bytes.|
|-26004|The encryption hint is invalid because the specified hint data type is   not supported.|
|-26005|The encrypted data is wrong or corrupted.|
|-26006|The data type is not supported for encryption functions.|
|-26007|The internal encryption function failed.|
|-26008|The internal decryption function failed.|
|-26009|Key generation failed.|
|-26010|Random IV generation failed.|
|-26011|The internal base64 encoding function failed.|
|-26012|The internal base64 decoding function failed.|
|-26013|Encrypt VP mailbox operation failed.|
|-26014|Alter fragment on typed table is not allowed.|
|-26015|All fragments of the table or index need to be of same pagesize.|
|-26016|Illegal leading byte 0x20 in Index name (%s).|
|-26017|External indices are not supported with non-default pagesizes.|
|-26018|Table %s has a referential key constraint and is not empty.|
|-26019|Purpose function am_truncate not defined for table or index.|
|-26020|Truncating a table with delete trigger requires ALTER privilege.|
|-26021|No operations allowed after truncate or online alter fragment in a transaction.|
|-26022|EXTERNAL NAME too long.|
|-26023|Cannot perform rename operation while non-mastered or strict mastered -- column and table names must match along with data types across all replicate participants -- replicates are defined for it|
|-26024|The sysdbopen and sysdbclose routines cannot have arguments or return values.|
|-26025|SELECT FROM INSERT syntax is disallowed in this context.|
|-26026|Remote table reference in INSERT statement disallowed in SELECT FROM INSERT syntax.|
|-26027|Label (%s) specified on a GOTO statement is not valid.|
|-26028|Label (%s) must be unique within an SPL procedure.|
|-26029|GOTO cannot be used and labels cannot be defined within an exception handler.|
|-26030|Invalid usage of EXIT or CONTINUE statement, which should be within a LOOP statement.|
|-26031|END LOOP label (%s) does not match the LOOP label label-name.|
|-26032|Invalid label (%s) used with EXIT WHEN clause.|
|-26033|Cannot create temp table with VERCOLS|
|-26034|Cannot create temp table with VERCOLS|
|-26035|Illegal usage of version columns.|
|-26036|Cannot add VERCOLS when table already has version columns.|
|-26037|Cannot drop VERCOLS when table does not have version columns.|
|-26038|Cannot perform this operation on a table with version columns.|
|-26039|Use of VERCOLS must be consistent across the table hierarchy.|
|-26040|Encrypt VP initialization failed.|
|-26041|Invalid values specified for the %s environment variable.|
|-26042|Function (explain_sql) failed in %s.|
|-26043|Function (explain_sql): The required parameter %s is NULL.|
|-26044|Function (explain_sql): An error occurred during the reading of parameter %s.|
|-26047|Function (explain_sql) does not support the query provided in (%s). Only a single select statement is supported.|
|-26048|Function (explain_sql) has an invalid %s parameter.|
|-26049|Function (explain_sql) has invalid encoding (%s) for xml_input.|
|-26050|Function (explain_sql) does not support query with host variables.|
|-26051|EXECUTE IMMEDIATE and PREPARE cannot take NULL statement|
|-26052|OPEN attempted on already opened cursor (%s)|
|-26053|FETCH or CLOSE cannot reference cursor (%s) that is not opened|
|-26054|Cannot FREE a cursor (%s) that is in use|
|-26055|Either statement-id or cursor name (%s) is not defined|
|-26056|Function cursor (%s) in SPL cannot have WITH HOLD option|
|-26057|Either statement-id or cursor (%s) is already in use|
|-26058|EXECUTE IMMEDIATE and PREPARE in SPL cannot allow multiple SQL statements|
|-26059|Unsupported data type in EXECUTE IMMEDIATE or PREPARE statement|
|-26060|Procedure was created with an older version of the engine and must   be dropped and created again in order to work properly|
|-26061|Procedure (%s) was created with an older version of the server and must   be dropped and recreated again in order to work properly|
|-26062|The specified case is not defined in the CASE statement|
|-26063|Data type not supported with CASE statement of SPL|
|-26064|The stored procedure execution failed because a statement cannot be prepared (%s).|
|-26071|Update statistics is not allowed on cross database or cross server objects.|
|-26072|The (%s) operator cannot be used in this context.|
|-26073|Savepoint name is unspecified.|
|-26074|Unable to set savepoint %s.|
|-26075|Unable to release savepoint %s.|
|-26076|Unable to rollback to savepoint %s.|
|-26077|Savepoint statements are disallowed inside triggers.|
|-26078|Rollback to savepoint disallowed on updating an old server in same transaction|
|-26079|CONNECT BY query resulted in a loop/cycle.|
|-26080|Generic error in CONNECT BY query processing.|
|-26081|Incorrect use of the CONNECT BY keywords in this context.|
|-26082|CONNECT_BY_ISCYCLE is used without the NOCYCLE keyword.|
|-26084|Cross server objects cannot be referenced in CONNECT BY queries.|
|-26085|You cannot have a CONNECT BY query on a join of two or more tables.|
|-26086|The value of this session environment variable must be between 0 and 32.|
|-26087|Incorrect use of the bson unwind in this context.|
|-26088|Prior specified rownum not allowed here.|
|-26090|Column (%s) not found in the target table.|
|-26091|Table (%s) is not the target table.|
|-26092|Column (%s) is not found in the source table.|
|-26093|Table (%s) is not the source table.|
|-26094|A MERGE operation is not allowed on this target table (%s).|
|-26095|Cannot update or delete a row twice in a MERGE statement.|
|-26096|Cannot define an INSTEAD OF trigger on a view when the view is specified as the   target in the MERGE statement.|
|-26097|Operation is not valid on a secondary server.|
|-26098|In a MERGE statement, the security policies of the target table and source   table (%s) do not match.|
|-26099|The optimizer cannot choose a viable plan based on the ON clause filter   specified in the MERGE statement.|
|-26100|You cannot set the GRANT ACCESS or REVOKE ACCESS properties when the   USERMAPPING onconfig parameter is OFF|
|-26101|The specified group name (%s) does not exist.|
|-26102|The specified user name (%s) does not exist.|
|-26103|You cannot modify existing access for user %s now. You must revoke access   first then grant access.|
|-26105|You should specify a group for the user.|
|-26106|You specified more than %d group numbers or names.|
|-26107|User name (%s) has already been granted access.|
|-26108|You cannot grant root or gbasedbt user privilege to the user.|
|-26109|You cannot grant access to user gbasedbt or root.|
|-26110|The specified group has administrative privileges. You must either specify   userauth properties or not include the group in the GRANT ACCESS statement.|
|-26111|The specified userauth (%s) property does not exist.  The valid values are   dbsa, dbsso, dbaao or bargroup.|
|-26112|The home directory is already specified.|
|-26113|The group name is already specified.|
|-26114|The userauth property is already specified.|
|-26115|The names assigned to resulting partitions must be distinct|
|-26151|Could not write to external table file: %s.|
|-26152|Could not exclusively lock external table.|
|-26153|Could not close external table.|
|-26154|Could not open file: (file, errno)=(%s).|
|-26155|Could not close external table file: %s.|
|-26156|Failed to read from file: (file, errno)=(%s).|
|-26157|File is incorrectly specified as a DISK type: (file)=(%s).|
|-26158|File is incorrectly specified as a PIPE type: (file)=(%s).|
|-26159|Error accessing AIO buffer (FILE,LINE,bufid,status)=(%s).|
|-26160|Could not remove the external table file: %s.|
|-26161|External table internal error: %s.|
|-26162|Failed to start an AIO operation errno=%s.|
|-26163|Target table cannot have BLOB columns.|
|-26164|External table data conversion failure (unload).|
|-26165|Datafile full (unload).|
|-26166|Datafile AIO write error (unload): %s.|
|-26167|All data files are either full or corrupted (unload).|
|-26168|Conversion err:(file,offset,reason,col)=(%s).|
|-26169|Failed to access file:(file, errno)=(%s).|
|-26170|Could not find record end: must stop loading.|
|-26171|Cannot undo partial write to %s when detecting a full disk.|
|-26172|There are too many %s keywords in the USING clause.|
|-26173|Incorrect value for a keyword %s.|
|-26174|Incorrect DATAFILE entry %s.|
|-26175|DATAFILE entries are missing.|
|-26176|Cannot use SAMEAS for FIXED format tables.|
|-26178|Incorrect external column type %s.|
|-26179|FIXED or DELIMITED columns must be external CHAR type %s.|
|-26180|Missing external column type %s.|
|-26181|Only FIXED format columns can declare a NULL %s.|
|-26182|Incorrect file type in DATAFILES string %s.|
|-26183|Could not replace r macro in filename %s.|
|-26184|Could not parse r macro in filename %s.|
|-26185|None of the DATAFILES strings name valid data files.|
|-26186|File name is too long: %s.|
|-26187|Cannot select from multiple external tables.|
|-26188|Null string is too long or has an incorrect format %s.|
|-26189|Cannot use a %s clause with a SELECT statement into an external table.|
|-26190|Insert into an external table must provide values for all columns in the table.|
|-26191|Incorrect use of an external table %s in query.|
|-26192|Column too long for fixed field %s.|
|-26193|An external table must be a fixed format file if it has an external column type %s.|
|-26194|Unknown external column type %s.|
|-26195|No constraints can be defined for external tables.|
|-26196|Internal type must be a numeric type %s.|
|-26197|Reached maximum error limit during load: (%s).|
|-26198|Cannot modify an external table that is also used in the subquery.|
|-26199|The RETAINUPDATELOCKS session environment cannot be set in a nonlogging database.|
|-26200|The RETAINUPDATELOCKS session environment cannot be set on secondary server in a high-availability cluster.|
|-26360|Invalid bucket size specified for FOT index.|
|-26361|Invalid 'hash on' list specified for FOT index.|
|-26362|Invalid data type for 'hash on' columns specified for FOT index.|
|-26363|FOT indexes cannot be functional indexes.|
|-26364|FOT indexes cannot be attached indexes.|
|-26365|FOT indexes cannot be clustered indexes.|
|-26371|Only the DBSSO can drop the audit property of the table.|
|-26213|The DELIMITER keyword is not valid for FIXED format tables.|
|-26214|Cannot perform this operation on an external table.|
|-26216|The RECORDEND keyword is not valid for FIXED format tables.|
|-26381|BLOBDIR directory (%s) does not exist or is not accessible.|
|-26382|CLOBDIR directory (%s) does not exist or is not accessible.|
|-26383|DATAFILES string (%s) with file type PIPE is not supported with BLOB/CLOB types|
|-26384|FORMAT (%s) is not supported with BLOB, CLOB, BYTE or TEXT types|
|-26385|Could not parse r macro in BLOBDIR %s.|
|-26386|Could not parse r macro in CLOBDIR %s.|
|-26387|Cannot use r macro in BLOBDIR %s without having a matching macro in filename %s.|
|-26388|Cannot use r macro in CLOBDIR %s without having a matching macro in filename %s.|
|-26389|Range for r macro in BLOBDIR %s does not match range in filename %s.|
|-26390|Range for r macro in CLOBDIR %s does not match range in filename %s.|
|-26391|FORMAT (%s) is not supported with collection types.|
|-26392|The INSERT operation into an external table failed because a row size exceeds the maximum limit of %s.|
|-26401|cannot connect to accelerator server: %s|
|-26402|accelerator server operation failed: %s|
|-26403|SQDWA internal error|
|-26404|query cannot be accelerated, fallback to local execution is not allowed|
|-26406|Multiple cursors to a single accelerator server unsupported in a session|
|-26407|Host variables type change rebind is unsupported for accelerated query|
|-26408|Arithmetic operation resulted in an overflow|
|-26431|[Internal] Extended type is not valid.|
|-26451|STATCHANGE can take values in the range of 0 to 100.|
|-26452|You cannot specify the STATLEVEL as FRAGMENT for non-fragmented tables.|
|-26453|%s is not supported in this edition of IDS.|
|-26454|Cannot specify both a PRIMARY KEY constraint and a NULL constraint on the same column.|
|-26455|Cannot specify both a NOT NULL constraint and a NULL constraint on the same column.|
|-26456|The authorization ID <%s> is not defined for the trusted context.|
|-26457|The trusted context <%s> already exists.|
|-26458|The trusted context specifies an authorization ID (<%s>) that is used by   another trusted context.|
|-26459|The trusted context <%s> does not exist.|
|-26460|Attribute with value <%s> cannot be dropped or altered because it is not   part of the definition of trusted context.|
|-26461|Attribute with value <%s> is not unique for trusted context.|
|-26462|User <%s> cannot be dropped or altered because it is not part of the definition   of trusted context.|
|-26463|User <%s> is not unique for trusted context.|
|-26464|The CREATE TRUSTED CONTEXT or ALTER TRUSTED CONTEXT statement was not processed   because the system authorization ID <%s> is already defined to be used by this   authorization ID or PUBLIC.|
|-26465|The ALTER TRUSTED CONTEXT statement was not processed for trusted context   because it is not currently defined to be used by this authorization   ID <%s> or PUBLIC.|
|-26466|The ENCRYPTION attribute cannot be specified more than once.|
|-26467|The CREATE TRUSTED CONTEXT statement cannot be processed. You must specify   at least one ATTRIBUTE address with value.|
|-26468|DBSECADM users cannot create a trusted context for themselves.|
|-26469|A trusted connection was not established because a trusted context is not   defined or enabled for the specified authorization ID.|
|-26470|The database specified (%s) is not associated with a trusted context definition.|
|-26471|Internal Function (%s): Unable to send or receive from the Session Manager.|
|-26472|Internal Error occurred during a BLOB operation in function %s.|
|-26473|Internal Error occurred. The required parameter %s is NULL.|
|-26474|[Internal] Error occurred during codeset conversion in function %s.|
|-26475|Function (%s): Unable to connect to the Session Manager.|
|-26476|Can not create temp table with ERKEY|
|-26477|Illegal usage of ERKEY|
|-26478|Can not add ERKEY when table already has ERKEY|
|-26479|Can not drop ERKEY when table does not have ERKEY|
|-26480|Illegal usage of ifx_replcheck|
|-26481|Cannot perform this operation through a grid|
|-26482|Cannot alter a replicated table in a grid outside of the same grid context|
|-26483|Grid or Region is not defined|
|-26484|SQL error encountered from SET ENVIRONMENT GRID_SELECT command|
|-26491|JDBC method (%s) not supported with this server.|
|-26500|query offloading is turned OFF|
|-26501|subquery matching is unsupported for offloading|
|-26502|Contradictory filters in where clause will not produce any rows|
|-26503|statement is unsupported for offloading|
|-26504|query containing FOR UPDATE is unsupported for offloading|
|-26505|query contains a pseudo table|
|-26506|query contains a temporary table|
|-26507|query contains a table which is not a real table|
|-26508|query contains a system catalog table|
|-26509|query references a table in remote database|
|-26510|cannot identify fact table|
|-26512|no marts are defined on this database|
|-26513|mart is virtual, and AVOID_EXECUTE is not set (explain setting or optimizer directive)|
|-26514|query contains more tables than AQT reference definitions|
|-26515|query does not contain a fact table of any data mart|
|-26516|query contains combination of tables not contained in any data mart|
|-26520|ON clause contains a non-equality join between columns|
|-26525|OUTER join with in-join filter (extends NULLs)|
|-26528|OR clause contains joins between different tables|
|-26529|OR clause contains joins between different columns|
|-26530|query contains a full join|
|-26532|ON clause of LEFT OUTER refers to more than two tables|
|-26534|INNER join must be on first level of joins|
|-26536|INNER join contains a non-equality join between columns|
|-26537|INNER join refers to more than two tables|
|-26538|joins do not form a star or snowflake scheme|
|-26540|table cannot be fact table, it is used by query with different aliases|
|-26543|query does not contain an equality join that is present in the mart definition,   and non of the columns in the equality join has a unique index|
|-26544|query does not contain a table that is present in the mart definition,   and there is no unique index on that table|
|-26546|query contains equality joins that are not present in the mart definition|
|-26547|query does not contain equality join that is present in the mart definition,   and none of the columns in the equality join of the mart definition have a   unique index|
|-26552|column is not contained in mart definition|
|-26555|expression is not supported|
|-26557|data type is not supported|
|-26558|query contains implicit column|
|-26559|query does not explicitly contain columns|
|-26560|no synonym is defined on this table|
|-26561|cannot map to GBasedbt sqlcode: %s|
|-26563|The query cannot be accelerated because the unary function with expression   is not supported on the accelerator.|
|-26564|The query containing Windowed aggregates is unsupported for offloading|
|-26565|Row type is not supported as an OUT/INOUT parameter in C UDR when invoking from SPL routine.|
|-26700|User (%s) was not found.|
|-26701|User (%s) was not created because it already exists.|
|-26702|User (%s) cannot connect to the database server because the user account is locked.|
|-26703|User (%s) is not authorized to create, alter, drop, or rename users.|
|-26704|User name (%s) exceeds the maximum length. Specify a user name that is not longer than 32 characters.|
|-26705|The password specified for user (%s) is not valid. Specify a password that contains 6 - 32 characters.|
|-26706|Cannot add a password to the user (%s) because a password already exists. Use the MODIFY option instead of the ADD option.|
|-26707|User (%s) cannot be created because the user is not mapped to any properties.|
|-26708|The existing password specified for user (%s) is not valid. You must specify the valid, existing password before you can change it.|
|-26709|The new password specified for user (%s) is not valid. Specify a password that contains 6 - 32 characters.|
|-26710|PUBLIC is a reserved word. You cannot create, drop, alter, or rename a user with the name PUBLIC.|
|-26711|The default user was not found.|
|-26712|Default user was not created as it already exists.|
|-26713|Do not specify a password while creating the default user.|
|-26714|An internal error occurred while hashing the password. Record all circumstances prior to the error and contact GBase Software Support.|
|-26715|Cannot alter the user (%s) because only one USER or UID property is allowed.|
|-26716|Cannot alter the user to add groups because the number of groups would exceed the maximum limit (%s).|
|-26717|An internal error occurred while performing an ALTER operation. Note all   circumstances and contact GBase Software Support.|
|-26718|Cannot alter the user (%s) to add a home directory because the property value already exists. Use the MODIFY option instead of the ADD option.|
|-26719|The ALTER statement specified an incorrect authorization value (%s).|
|-26720|Cannot change a property value more than once in the same ALTER statement.|
|-26721|Cannot drop the password for the user (%s) because the password is specified. Do not include a value for the PASSWORD property with the DROP option.|
|-26722|The surrogate user name (%s) exceeds the maximum length of 32 characters. Specify a user name that has 32 characters or fewer.|
|-26723|The value of the surrogate property HOMEDIR exceeds the maximum length. Specify a value that is less that 255 bytes.|
|-26724|Cannot drop the HOMEDIR property for the user (%s) because a value is specified. Do not include a value for the HOMEDIR property with the DROP option.|
|-26725|Cannot drop the UID property for the user (%s) because a value is specified. Do not include a value for the UID property with the DROP option.|
|-26726|Cannot drop the USER property for the user (%s) because a value is specified. Do not include a value for the USER property with the DROP option.|
|-26727|The SQL statement cannot assign operating system properties to the user (%s).|
|-26728|The uid %s is not in the /etc/gbasedbt/allowed.surrogates file or in the cache.|
|-26729|The user %s is not in the /etc/gbasedbt/allowed.surrogates file or in the cache.|
|-26730|The gid %s is not in the /etc/gbasedbt/allowed.surrogates file or in the cache.|
|-26731|The group %s is not in the /etc/gbasedbt/allowed.surrogates file or in the cache.|
|-26732|The USERMAPPING feature is disabled.  The USERMAPPING configuration parameter must be set to BASIC or ADMIN.|
|-26733|A grid object can only be altered, dropped, or renamed within the grid context.|
|-26734|You cannot drop a database containing grid tables except within the grid context.|
|-26600|Exceeded limit on maximum number of concurrent open databases.|
|-26601|Cannot define a partial-column index on the non-character column, (%s).|
|-26735|Invalid value for %s|
|-26750|The fragment key in hash startegy should be column name, not expr.|
|-26751|Could not create table - duplicate column names in fragment key.|
|-26752|Could not alter table column's type or len which is in fragment key.|
|-26753|Could not create table - fragment key could not be TEXT/BYTE/BLOB/CLOB.|
|-26801|Cannot reference an external database that is not case sensitive.|
|-26802|Cannot reference an external database that is case sensitive.|
|-26736|The statement failed because the escape character is not a constant of type CHARACTER.|
|32766|Unknown error number %d.|
|-26811|Can not create temp table with REPLCHECK|
|-26812|Illegal usage of REPLCHECK columns.|
|-26813|Can not add REPLCHECK when table already has REPLCHECK columns.|
|-26814|Can not drop REPLCHECK when table does not have REPLCHECK columns.|
|-26815|Can not perform this operation on a table with REPLCHECK columns.|
|-26816|Use of REPLCHECK must be consistent across the table hierarchy.|
|-26901|An alias cannot represent another alias.|
|-26902|[Internal] Client decimal buffer size mismatch.|
|-26903|Multiple execution of a CREATE TABLE statement that was prepared once is not allowed.|
|-26904|Compressed indexes cannot be attached indexes, non-vanilla  or interval fragmented.|
|-26905|The procedure was not created because its definition has more than 341 parameters.|
|-26907|Routine creation failed because a collection variable was defined as a global variable.|
|-26910|The statement failed because it referenced a rolling window table.|
|-26911|The statement failed because each constraint on a rolling window table  requires a supporting index.|
|-26912|The statement failed because rowids are not allowed in rolling window tables.|
|-26913|Cannot enable a purge policy because the table is referenced by other tables.|
|-26914|The index was not created, because its storage differs from that of its rolling window table.|
|-26915|The statement failed because the ROLLING FRAGMENTS and LIMIT TO clauses require positive integers.|
|-26916|The statement failed because the new table size would exceed the threshold set by the LIMIT TO clause.|
|-26917|The statement failed because a UDR specifies the dbspace for the next interval fragment of this table or index.|
|-26930|OTHERS handler must be last among the exception handlers of a block.|
|-26931|Exception '%s'  may appear in at most one handler in this block.|
|-26932|RAISE statement with no exception name must be inside an exception handler.|
|-26933|Invalid using EXCEPTION type of '%s'.|
|-26934|No choices may appear with choice OTHERS in an exception handler.|
|-26935|In exception handler, '%s' must be an exception name.|
|-26936|Illegal error number '%s' for PRAGMA EXCEPTION_INIT.|
|-26937|'%s' must be declared as an exception.|
|-26938|Constant variable(%s) cannot be modified.|
|-26939|Alias required in SELECT list of cursor to avoid duplicate column names.|
|-26940|Unhandled user-defined exception.|
|-26941|A variable declared NOT NULL must have an initialization assignment.|
|-26942|Can not do assign from a record type to another record type.|
|-26943|The declaration of the type is incomplete or malformed.|
|-26950|Clustered compressed indexes are not supported.|
|-26951|The grid query failed to run.  Contact GBase Software Support.|
|-26952|The grid query statement can not contain a server name (%s).|
|-26953|The grid or region (%s) does not exist.|
|-26954|Grid Queries can not contain a UNION or UNION ALL statement.|
|-26955|Invalid value for the SET ENVIRONMENT GRID_NODE_SKIP statement.|
|-26956|Cannot run SET ENFIRONMENT SELECT_GRID or SET ENFIRONMENT SELECT_GRID_ALL statement.|
|-26957|The grid query can not connect to server %s.|
|-26958|Grid queries can not have subqueries.|
|-26959|Invalid syntax for a grid query.|
|-26960|Table (%s) is not a grid table and cannot be used in a grid query.|
|-26961|Table (%s) is in the process of being altered.|
|-26962|Grid queries can not contain correlated joins.|
|-26963|The grid or region (%s) has no members.|
|-26991|The query failed because the FROM clause includes more than one sharded table.|
|-26992|The sharded query failed because of an internal error.|
|-26993|Cannot alter the table to shard collection table.|
|-26981|Invalid label (%s) used with CONTINUE/EXIT WHEN clause.|


## sql8  

|ErrCode|Description|
|:---|:---|
|-8200|User (%s) does not have DBSECADM authority.|
|-8201|The security label component (%s) already exists.|
|-8202|The security label component element (%s) is already defined.|
|-8203|The security label component element (%s) exceeds 32 bytes.|
|-8204|The security label component (%s) has too many elements.|
|-8205|The security label component element (%s) is not yet defined.|
|-8206|The security policy (%s) already exists.|
|-8207|The security label component (%s) was specified more than once.|
|-8208|The security label component (%s) does not exist.|
|-8209|The maximum number of components in security policy (%s) has been exceeded.|
|-8210|The security policy (%s) does not exist.|
|-8211|The security label (%s) already exists.|
|-8212|The security label component (%s) is not defined in the security policy.|
|-8213|The element (%s) is not defined in the security label component.|
|-8214|Two or more elements are specified for the security label component (%s).|
|-8215|The security label component element (%s) was specified more than once.|
|-8216|The access rule (%s) does not exist in the rule set used by the security policy.|
|-8217|Cannot specify PUBLIC or a role name.|
|-8218|A DBSECADM cannot grant a privilege, security label or exemption to self.|
|-8219|A DBSECADM cannot revoke a privilege, security label or exemptions from self.|
|-8220|User (%s) does not hold this privilege, security label, or exemption.|
|-8221|The security label (%s) does not exist for the security policy.|
|-8222|User already has a security label (%s) for READ access.|
|-8223|User already has a security label (%s) for WRITE access.|
|-8224|The security label (%s) conflicts with the existing granted security label.|
|-8225|The security label component (%s) is still in use by a security policy.|
|-8226|The security label (%s) is currently in use.|
|-8227|The security policy (%s) is currently in use.|
|-8228|Cannot GRANT or REVOKE SETSESSIONAUTH privilege to or from PUBLIC.|
|-8229|User (%s) does not have SETSESSIONAUTH privilege.|
|-8230|User (%s) does not have the authority to grant or revoke DBSECADM.|
|-8231|DBSECADM cannot be granted to user (%s).|
|-8232|The element (%s) already exists in the security label component.|
|-8233|Cannot secure columns or rows in a table without a security policy.|
|-8234|Invalid specification of a column (%s) of type IDSSECURITYLABEL.|
|-8235|A security policy cannot be added to a temporary, typed or external table.|
|-8236|Only one security label column is allowed in a table.|
|-8237|Cannot modify column (%s) to type IDSSECURITYLABEL.|
|-8238|Source table must have the same security protection as target table.|
|-8239|The table (%s) already has a security policy.|
|-8240|The table (%s) is not protected with a security policy.|
|-8241|The column (%s) has already been protected by a security label.|
|-8242|The column (%s) is not protected by a security label.|
|-8243|User (%s) does not hold a security label for READ access.|
|-8244|The value (%s) provided for row security label column is invalid.|
|-8245|User cannot perform READ access to the protected column (%s).|
|-8246|User cannot perform WRITE access to the protected column (%s).|
|-8247|User does not have the LBAC credentials to perform INSERT on table (%s).|
|-8248|User does not have the LBAC credentials to perform SELECT on table (%s).|
|-8249|User does not have the LBAC credentials to perform UPDATE on table (%s).|
|-8250|User does not have the LBAC credentials to perform DELETE on table (%s).|
|-8251|Update, delete, or insert into a UNION ALL view is not allowed.|
|-8252|Cannot set role to DBSECADM.|
|-8253|Cannot open database (%s).|
|-8254|Database (%s) is currently opened by another user.|
|-8255|User (%s) does not have DBSA authority.|
|-8256|Invalid character in element (%s).|
|-8257|The security label component element (%s) cannot be null.|
|-8258|The rule specified is not consistent with the security policy (%s).|
|-8259|Cannot GRANT or REVOKE SETSESSIONAUTH privilege for role.|
|-8260|Multiple security policy clauses.|
|-8261|Cannot secure rows in a table without a default value for IDSSECURITYLABEL column.|
|-8262|Cannot update partition flags.|
|-8263|The component type specified (%s) does not match the type in the system catalog.|
|-8264|Cannot alter ARRAY security label component to add elements before (%s).|
|-8265|Cannot alter ARRAY security label component to add elements after (%s).|
|-8266|Operation not permitted.|
|-8267|Cannot add LBAC protection to a table defined for replication.|
|-8268|Cannot create a distinct type (%s) of type IDSSECURITYLABEL.|
|-8269|LBAC internal error: %s|
|-8270|Row security label for a protected table cannot be null.|


## sql9  

|ErrCode|Description|
|:---|:---|
|-10112|The syntax is ora style.|
|10112|The syntax is ora style.|
|-10000|Argument must be a variable to be an OUT or INOUT parameter.|
|25751|REMOTE SESSION ID FOR %s|
|25752|QUERY: (OPTIMIZATION TIMESTAMP: %s)|
|25753|(Temp Table For Subquery)|
|25754|Connect by Query Rewrite:|
|25755|Index Name:|
|25756|Fragments Scanned:|
|25757|MULTI INDEX PATH (SKIP SCAN)|
|25758|INDEX PATH (SKIP SCAN)|
|25759|INDEX_ALL|
|25760|MULTI_INDEX|
|25761|AVOID_MULTI_INDEX|
|25762|Invalid index specified in INDEX_ALL or MULTI_INDEX or AVOID_MULTI_INDEX directive.|
|25763|In a MERGE statement, the target table cannot be the inner table of a nested loop join.|
|25764|Index Keys (Detached):|
|25765|PRED_ORDERED|
|25766|Index Push Down Key:|
|25767|Bit Vector Push Down Key:|
|25768|Bit Vector Filter:|
|25769|stream from|
|25770|STAR_JOIN|
|25771|AVOID_STAR_JOIN|
|25772|Multiple star join directives defined.|
|25773|Join method or join order directive conflicts with star join directive.|
|25774|FACT|
|25775|AVOID_FACT|
|25776|The final cost of the plan is reduced because of the FIRST n specification in the query.|
|25777|USE_PARTITION|
|25778|AVOID_PARTITION|
|25779|Invalid Table Partnum Specified.|
|25780|(Anti Semi Join)|
|25781|RESULT_CACHE|
|25782|STARTWITH_BIGHASH|
|25783|MVTONRL_VIEW|
|26045|Warning: Function (explain_sql) %s and the current support version do not match.|
|26046|Warning: Function (explain_sql): The requested locale was not provided. The default locale %s will be used.|
|26083|You cannot use a join-method directive or the ORDERED directive in a CONNECT BY Query.|
|26251|Star Join directive cannot be obeyed|
|26252|Star Join requires PDQ priority set|
|26253|Star Join requires UPDATE STATISTICS for all tables in query|
|26254|(Reverse)|
|26255|(Temp Table For Window Functions)|
|26415|DWA attempted:|
|26416|DWA avoid_execute:|
|26418|DWA executed:|
|26419|IDS executed:|
|26420|IDS avoid_execute:|
|26421|IDS FYI:|
|26422|(OPTIMIZATION TIMESTAMP: %s)|
|26423|GRID:%s|
