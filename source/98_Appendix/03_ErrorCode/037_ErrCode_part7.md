# GBase 8s数据库错误代码  
第七部分  

## sqli  

|ErrCode|Description|
|:---|:---|
|-1800|Invalid transaction state.|
|-1801|Multiple-server transaction not supported.|
|-1802|Connection name in use.|
|-1803|Connection does not exist.|
|-1804|Invalid database environment.|
|-1805|Invalid connection name.|
|-1806|Connection failure.|
|-1807|No connection to disconnect.|
|-1808|Reconnect to '%s' server to perform the database operation.|
|-1809|Server rejected the connection.|
|-1810|Disconnect error.|
|-1811|Implicit connection not allowed after an explicit connection.|
|-1812|Internal error.|
|-1813|Only the current connection can be made dormant.|
|-1814|Need to allocate collection or row variable before using it.|
|-1815|No type information for collection or row is available.|
|-1816|No such column exists in the collection or row.|
|-1817|No collection or row variable provided.|
|-1818|Input variable type does not match collection or row definition.|
|-1819|Only one row allowed into a collection at a time.|
|-1820|Host variable type has been changed between fetches or puts.|
|-1821|Host variable is not large enough to hold the data returned from the server.|
|-1822|Invalid argument.|
|-1823|Need more memory to store the data.|
|-1824|Message cannot be found.|
|-1825|INSERT and DELETE cannot be performed on ROW host variables.|
|-1826|DESCRIBE information for this statement is not available at this time.|
|-1827|Can not execute an EXECUTE statement when DEFERRED_PREPARE feature is enabled.|
|-1828|Cannot use scroll or hold cursor with client collections.|
|-1829|Cannot open file citoxmsg.pam.|
|-1830|Method not supported in this version.|
|-1831|Combination of FetArrSize, Deferred-PREPARE, and OPTOFC is not supported.|
|-1832|Environment block is greater than 32 K.|
|-1833|Cannot open file itoxmsg.pam.|


## util  

|ErrCode|Description|
|:---|:---|
|-33500|Bad environment variable on line %d.|
|-33501|Mapping file for DBAPICODE is not found.|
|-33502|Mapping file does not have the correct format.|
|33510|Usage: finderr msgnum [msgnum2 ...]   finderr searches the file of error message explanations   distributed with GBase products and copies the text of one   or more error messages to the standard output.   If an unsigned number is given, a negative sign is assumed.   Examples:   finderr  327    (looks for message number -327)   finderr -327    (looks for message number -327)   finderr +1234   (looks for message number 1234)   finderr -233 107 113 134 143 144 +1541 &#124; more   See the rofferr script for more formatting capabilities.|
|-33512|Cannot read the message text file (%s).   Please verify that your GBASEDBTDIR variable is set correctly.   Please also check your DBLANG variable, if necessary.|
|-33513|%s is outside the range of documented messages.|
|-33514|argument (%s) is not numeric.|
|-33515|Message number %s not found.|
|-33516|No messages found between %s and %s.|
|-33517|Both ends of message range must be of same sign (positive or negative).|
|-33518|Checking shared environment configuration file: %s|
|-33519|Checking private environment configuration file: %s|
|-33520|Checking user provided environment configuration file: %s|
|-33521|Usage: chkenv[<environment-configuration-file-path>]|
|-33522|File does not exist|
|-33523|%s: Bad environment variable on line %d.|


## xopen  

|ErrCode|Description|
|:---|:---|
|36000|Success|
|36001|Success with warning|
|36002|Disconnect error.|
|36003|Null value eliminated in set function|
|36004|String data, right truncation|
|36005|Insufficient item descriptor areas|
|36006|Privilege not revoked|
|36007|No data|
|36008|Dynamic SQL error|
|36009|Using-clause does not match dynamic parameters|
|36010|Using-clause does not match target specifications|
|36011|Cursor specification cannot be executed|
|36012|Using-clause is required for dynamic parameters|
|36013|Prepared statement is not a cursor specification|
|36014|Restricted data type attribute violation|
|36015|Invalid descriptor count|
|36016|Invalid descriptor index|
|36017|Connection exception|
|36018|Server rejected the connection|
|36019|Connection name in use|
|36020|Connection does not exist|
|36021|Client unable to establish connection|
|36022|Connection failure|
|36023|Transaction resolution unknown|
|36024|Communication failure|
|36025|Cardinality violation|
|36026|Data exception|
|36028|Null value, no indicator parameter|
|36029|Numeric value out of range|
|36030|Error in assignment|
|36031|Division by zero|
|36032|Unterminated string|
|36033|Integrity constraint violation|
|36034|Invalid cursor state|
|36035|Invalid transaction state|
|36036|Transaction was begun globally|
|36037|Invalid SQL statement identifier|
|36038|Invalid user authorization specification|
|36039|Invalid SQL descriptor name|
|36040|Invalid exception number|
|36041|Syntax error or access violation in PREPARE or EXECUTE IMMEDIATE|
|36042|Serialization failure|
|36043|Syntax error or access violation|
|36044|Invalid transaction terminated|
|36045|Memory allocation failure|
|36046|SQLCLI function sequence error|
|36047|Memory management error|
|36048|RDA error|
|36049|Access Control Violation|
|36050|Bad Repetition Count|
|36051|Command Handle Unknown|
|36052|Control Authentication Failure|
|36053|Data Resource Handle Not Specified|
|36054|Data Resource Handle Unknown|
|36055|Data Resource Name Not Specified|
|36056|Data Resource Not Available|
|36057|Data Resource Open|
|36058|Data Resource Unknown|
|36059|Diaglog ID Unknown|
|36060|Duplicate Command Handle|
|36061|Duplicate Data Resource Handle|
|36062|Duplicate Dialogue ID|
|36063|Duplicate Operation ID|
|36064|Invalid Sequence|
|36065|No Data Resource Available|
|36066|Operation Aborted|
|36067|Operation Cancelled|
|36068|Service Not Negotiated|
|36069|Transaction Rolled Back|
|36070|User Authentication Failure|
|36071|Host Identifier Error|
|36072|Invalid SQL Conformance Level|
|36073|RDA Transaction Rolled Back|
|36074|SQL Access Control Violation|
|36075|SQL Database Resource Already Open Error|
|36076|SQL DBL Argument Count Mismatch|
|36077|SQL DBL Argument Type Mismatch|
|36078|SQL DBL Transaction Statement Not Allowed|
|36079|SQL Usage Mode Violation|
|36080|Connection Establishment Error|
|36081|Connection Release Error|
|36082|Connection Failure|
|36083|Insert value list does not match column list|
|36084|Degree of derived table does not match column list|
|36085|Invalid name|
|36086|Base table or viewed table already exists|
|36087|Base table not found|
|36088|Index already exists|
|36089|Column already exists|
|36090|Invalid cursor name|
|36091|Index not found|
|36092|Feature not supported|
|36093|Multiple server transaction|
|36094|Duplicate cursor name|
|36095|Statement completion unknown|
|36096|Connection does not exist|
|36097|Invalid connection name|
|36098|Invalid escape character|
|36099|Invalid escape sequence|
|36100|Trim error|
|36101|Dependent privilege descriptors still exist|
|36105|GBasedbt reserved error message|
|36106|Database has transactions|
|36107|Aggregate function (SUM,AVG,MIN,MAX) encountered null value in evaluation|
|36108|ANSI-compliant database selected|
|36109|Database selected|
|36110|Float to decimal conversion has been used|
|36111|UPDATE/DELETE statement does not have a WHERE clause|
|36112|GBasedbt extension to an ANSI-compliant standard syntax|
|36113|An ANSI keyword has been used as a cursor name|
|36114|No. of items in the select-list is not equal to the no. in into-list.|
|36115|Database server running in secondary mode.|
|36116|Dataskip is turned on.|
|36117|Privilege not granted|
|36118|A site that does not support savepoints is updated when a savepoint is set.|
|36200|Invalid column number|
|36201|Program type out of range|
|36202|SQL data type out of range|
|36203|Invalid argument value|
|36204|Invalid transaction operation code|
|36205|No cursor name available|
|36206|Warning! avoid_execute has been set|


## xps  

|ErrCode|Description|
|:---|:---|
|-23501|CM error: Operation not supported on secondary coservers.|
|-23502|CM error: Can not allocate memory.|
|-23503|CM error: No such DBspace.|
|-23504|CM error: DBspace already exists.|
|-23505|CM error: DBspace table overflow.|
|-23506|CM error: No such chunk.|
|-23507|CM error: Chunk already exists.|
|-23508|CM error: Chunk table overflow.|
|-23509|CM error: Chunk not empty.|
|-23510|CM error: Can not drop first chunk.|
|-23511|CM error: No such DBslice.|
|-23512|CM error: DBslice already exists.|
|-23513|CM error: DBslice table overflow.|
|-23514|CM error: No such cogroup.|
|-23515|CM error: Cogroup already exists.|
|-23516|CM error: Cogroup table overflow.|
|-23517|CM error: Can not drop or alter a system defined cogroup.|
|-23518|CM error: No such coserver.|
|-23519|CM error: Coserver already exists.|
|-23520|CM error: Coserver table overflow.|
|-23521|CM error: An illegal identifier was specified.|
|-23522|CM error: An illegal range identifier was specified.|
|-23523|CM error: An uneven number of cogroup members were specified.|
|-23524|CM error: Nested cogroups not supported in this release.|
|-23525|CM error: All available ids for Fragmented Tables are in use.|
|-23526|CM error: Unable to create a mutex.|
|-23527|CM error: No such logslice.|
|-23528|CM error: Logslice already exists.|
|-23529|CM error: Logslice table overflow.|
|-23530|CM error: No such DBspace or DBslice.|
|-23531|SVC Error: Feature not implemented.|
|-23532|SVC error: Cannot allocate memory.|
|-23533|SVC Error: Service tag is not valid.|
|-23534|SVC Error: Service instance id is not valid.|
|-23535|SVC Error: Specified option is invalid.|
|-23536|SVC Error: No such service is registered.|
|-23537|SVC Error: No such instance of the service is registered.|
|-23538|SVC Error: No instance candidate exists.|
|-23539|SVC Error: The instance has not set its data value.|
|-23540|SVC Error: The requested instance would not be unique if registered.|
|-23541|SVC Error: The request timed out before completing.|
|-23542|SVC Error: The buffer is too small for the instance data requested.|
|-23543|SVC Error: The coserver cannot be restarted.|
|-23544|SVC Error: The SVC thread cannot be started.|
|-23545|SVC Error: The SVC mutex cannot be allocated.|
|-23546|SVC Error: The SVC subsystem has not been properly initialized.|
|-23547|CM error: This would create two chunks that would overlap each other.|
|-23548|CM error: This would create two chunks with the same name and offset   on one node.|
|-23549|CM error: This would create a chunk that would overlap its own mirror.|
|-23550|CM error: This would create a chunk that would overlap an existing chunk.|
|-23551|CM error: Cannot alter a Logslice whose Dbslice has not been altered.|
|-23552|The specified dbspace (%s) does not exist.|
|-23553|CM error: Number of read-locks held is less than zero.|
|-23554|CM error: Number of write-locks held is less than zero.|
|-23555|CM error: Number of write-options held is less than zero.|
|-23556|CM error: Attempt to get write-lock without write option.|
|-23557|CM error: Attempt to drop write-lock without write option.|
|-23558|CM error: Attempt to drop write option without having it.|
|-23559|CM error: CM activity detected during reversion.|
|-23560|CM error: Can't add a dbspace to the root slice.|
|-23561|CM error: Cannot delete a coserver ID that is not the highest ID.|
|-23562|CM error: Cannot delete a coserver ID that exists in the $ONCONFIG file.|
|-23563|CM error: Cannot enable a capability on a coserver configured as fully capable.|
|-23564|CM error: Cannot disable a capability on a coserver configured as fully capable.|
|-23565|CM error: Capability is not configured on the coserver.|
|-23566|CM error: Coserver counts are inconsistent, only the delete coserver command is allowed.|
|-23567|CM error: Dynamic Coserver Management is not currently supported.|
|-23568|CM error: Deleting fully-capable coserver is not supported.|
|-23569|CM error: Permanent dbspaces are not supported on a target coserver.|
|-23570|CM error: coserver is still participating in at least one global transaction.|
|-23571|CM error: Coserver 1 must be a fully-capable coserver.|
|-23572|CM error: The capabilities for coserver %d have changed.|
|-23573|CM error: The coserver type specified is invalid.|
|-23574|CM warning: CM/RSAM inconsistency detected.  %s will drop %s %s|
|-23575|CM warning: CM/RSAM inconsistency detected.  %s will drop chunk %d|
|-23576|CM warning: %s operation failed with ISAM error %d.|
|-23577|CM warning: XMF send failed in %s with XMF error %d.|
|-23578|CM error:  deliberate debug crash: %s|
|-23579|CM error:  operation cannot be performed on root space or chunk.|
|-23580|CM error: server must be started in quiescent mode when deleting coservers.|
|-23600|Backup Manager Error: Out of memory.|
|-23601|Backup Manager Error: A coserver can support at most one storage manager.|
|-23602|Backup Manager Error: A dbspace backup/restore is already active   for this dbspace.|
|-23603|Backup Manager Error: An unrecognised session id was supplied.|
|-23604|Backup Manager Error: This coserver does not support a storage manager.|
|-23605|Backup Manager Error: An unrecognised worker id was supplied   - contact product support.|
|-23606|Backup Manager Error: This worker is already waiting or busy   - contact product support.|
|-23607|Backup Manager Error: Wait on a session which is already waiting   - contact product support.|
|-23608|Backup Manager Error: No object allocated to worker   - contact product support.|
|-23609|Backup Manager Error: Type different to that allocated to worker   - contact product support.|
|-23610|Backup Manager Error: Internal error - No workers ready to run.|
|-23611|Backup Manager Error: Internal error - Object not allocated.|
|-23612|Backup Manager Error: Internal coding error - contact product support.|
|-23613|Backup Manager Error: The session id is already in use by another session.|
|-23614|Backup Manager Error: Priority must be between 0 and 100.|
|-23615|Backup Manager Error: Unrecognised event type - contact product support.|
|-23616|Backup Manager Error: The set placement failed for this object.|
|-23617|Backup Manager Error: That session is already suspended.|
|-23618|Backup Manager Error: That session is not suspended.|
|-23619|Backup Manager Error: The supplied placement does not match a   configured storage manager.|
|-23620|Backup Manager Error: The supplied timestamp value disagrees with   another existing value.|
|-23621|Backup Manager Error: The session has been aborted.|
|-23622|Backup Manager Error: Internal error: mt_create_mutex failed   - contact product support.|
|-23623|Backup Manager Error: Internal error: mt_create_thread failed   - contact product support.|
|-23624|Backup Manager Error: Internal error: xmf_bf_alloc failed   - contact product support.|
|-23625|Backup Manager Error: Internal error: xmf_reqt failed   - contact product support.|
|-23626|Backup Manager Error: Internal error: xmf_resp failed   - contact product support.|
|-23627|Backup Manager Error: The Dbspace is unknown to the system   (it may be a dbslice ?).|
|-23628|Backup Manager Error: Internal error: cm_dbs_info failed   - contact product support.|
|-23629|Backup Manager Warning: There are no storage managers configured.   All operations will be queued.|
|-23630|Backup Manager Error: Internal error: xmf_send failed   - contact product support.|
|-23631|Backup Manager Error: A worker onbar died while processing this object   - see onbar logs for more information.|
|-23632|The backup manager cannot do any backups or restores while LOG_BACKUP_MODE is   set to NONE. Change this setting in your onconfig file to MANUAL or CONT and   retry the request.|
|-23633|The specified logfile does not exist.|
|-23634|Multiple storage managers backing up a single logstream is currently not   supported.|
|-23635|BACKUP Manager Error (23635)   The start_worker.sh shell script file in the etc sub-directory is   missing or its execute permission is revoked.|
|-23636|Backup Manager Error: Invalid coserver id.|
|-23637|Backup Manager Error: There are running backups/restores on a specified coserver - all coservers can't be blocked.|
|-23638|Backup Manager Error: Invalid dbspace.|
|-23639|Backup Manager Error: The Backup Manager has not been properly initialized.|
|-23640|Backup Manager Error: DUPLICATE ROOT DBSPACE.|
|-23641|Backup Manager Error (23641)   The start_merger.sh shell script file in the etc sub-directory is   missing or its execute permission is revoked.|
|-23642|Backup Manager Error (23642): A restore is already in progress.|
|-23700|Could not write to file: (cosvr, file)=(%s).|
|-23701|PLOAD: could not exclusively lock external table.|
|-23702|PLOAD: could not close external table.|
|-23705|Could not open file: (cosvr, file, errno)=(%s).|
|-23706|Could not close file: (cosvr, file)=(%s).|
|-23707|Failed to read from file: (cosvr, file, errno)=(%s).|
|-23709|File specified as FILE type but is not: (cosvr, file)=(%s).|
|-23710|File specified as PIPE type but is not: (cosvr, file)=(%s).|
|-23712|Illegal AIO buffer status (FILE,LINE,bufid,status)=(%s).|
|-23713|Could not open info file '%s'.|
|-23714|Syntax error in info file at line %s.|
|-23715|Syntax error in info file: bad TYPE section token <%s>.|
|-23716|Syntax error in info file: bad DEVICE section token <%s>.|
|-23717|Syntax error in info file: bad coserver id at line %s.|
|-23718|Syntax error in info file: bad keyword at line %s.|
|-23719|Error in info file: missing or invalid TYPE section.|
|-23720|Error in info file: missing or invalid DATA-FILES section.|
|-23721|Internal error: iff_op() look-ahead buffer overflow.|
|-23723|Invalid field delimiter '%s'; Don't use '\', SPACE or HEX chars.|
|-23724|Could not remove file: (cosvr, file)=(%s).|
|-23725|PLOAD internal error in (FILE, LINE#)=(%s).|
|-23726|PLOAD (load or unload) failed to start an AIO operation errno=%s.|
|-23730|PLOAD (unload): conversion failure.|
|-23731|PLOAD (unload): datafile full.|
|-23732|PLOAD (unload): datafile AIO write error (%s).|
|-23733|PLOAD (unload): all data files are either full or bad.|
|-23734|PLOAD: row size of target table is too large (size, max)=(%s).|
|-23735|PLOAD conversion err:(cosvr,file,offset,reason,col)=(%s).|
|-23736|PLOAD failed to access file:(cosvr, file, errno)=(%s).|
|-23737|PLOAD could not find record end: must abort.|
|-23738|PLOAD (unload) cannot undo partial write to %s when detecting disk full.|
|-23739|Cannot open PLOAD log file.|
|-23740|CREATE EXTERNAL TABLE: Too many %s keywords in USING clause.|
|-23741|CREATE EXTERNAL TABLE: Invalid value for %s.|
|-23742|CREATE EXTERNAL TABLE: Invalid DATAFILE entry '%s'.|
|-23743|CREATE EXTERNAL TABLE: Missing DATAFILE entries.|
|-23744|CREATE EXTERNAL TABLE: Cannot use SAMEAS for FIXED format tables.|
|-23745|CREATE EXTERNAL TABLE: Internal column types must be defined (%s).|
|-23746|CREATE EXTERNAL TABLE: Invalid external column type (%s).|
|-23747|CREATE EXTERNAL TABLE: FIXED or DELIMITED columns must be external chars (%s).|
|-23748|CREATE EXTERNAL TABLE: Missing external column type (%s).|
|-23749|CREATE EXTERNAL TABLE: Only FIXED format columns can declare nulls (%s).|
|-23750|Invalid file type in DATAFILES string (%s).|
|-23751|Could not replace n macro in filename (%s).|
|-23752|Could not find coserver name for coserver (cid,errno) (%s).|
|-23753|Could not replace r macro in filename (%s).|
|-23754|Could not replace c macro in filename (%s).|
|-23755|Missing delimiter at end of coserver item (%s).|
|-23756|Unknown coserver (%s).|
|-23757|Unknown cogroup (%s).|
|-23758|Could not parse r macro in filename (%s).|
|-23759|None of the DATAFILES strings name valid data files.|
|-23760|File name is too long (%s).|
|-23761|Cannot select from multiple external tables.|
|-23762|Null string longer than external column length or of bad format (%s).|
|-23763|Cannot use a %s clause with a select into an external table.|
|-23764|Insert into an external table must provide values for all columns in the table.|
|-23765|Cannot use a %s clause with a select from external table.|
|-23766|Illegal use of an external table (%s) in query.|
|-23767|Column too long for fixed field (%s).|
|-23768|External table must be fixed format for external column type (%s).|
|-23769|Unknown external column type (%s).|
|-23770|Only check constraints can be defined for external tables.|
|-23771|Internal type must be a numeric type (%s).|
|-23772|Internal type must be a small integer or integer (%s).|
|-23773|Reached max error during load (maxerr,csvrid)=(%s).|
|-23774|Create external table for %s failed.|
|-23800|An internal error has occurred in the XTM facility.|
|-23801|A memory allocation error has occurred in the XTM facility.|
|-23802|A request to idle an XTM participant has failed.  Transactions are in an   inconsistent state.|
|-23803|An XMF send has failed within the XTM facility.|
|-23804|An XMF receive has failed within the XTM facility.|
|-23805|An unknown transaction ID was encountered in the XTM transaction management   system.|
|-23806|A corrupted message has been received within the XTM facility.|
|-23807|The backup information for the XTM coordinator is corrupted.|
|-23808|The creation of the XMF port for the XTM facility failed.|
|-23850|Table type specified twice.|
|-23851|This operation is not allowed on a table where the type is raw or scratch.|
|-23852|This operation is not allowed on a table where the type is static.|
|-23853|Unable to change the type of table %s.|
|-23854|Raw and scratch tables cannot have referential or unique constraints.|
|-23855|Express mode loads are not permitted for this type of table.|
|-23856|This operation is not allowed on an SMI pseudo table.|
|-23857|This operation is not allowed on tables where the type is raw or static.|
|-23858|This operation is not allowed on a temporary table (%s).|
|-23859|This operation is not allowed on a violations/diagnostics table (%s).|
|-23860|This operation is not allowed on a duplicated table (%s).|
|-23861|Triggers are not allowed on raw, scratch, or static tables.|
|-23900|freeshdic FAILED: non-exclusive access   dic %s ref %d lk %d   possible memory loss|
|-23901|Index name (%s) with leading byte 0x20 not allowed.|
|-23902|Operation is not supported in SMI database (%s).|
|-23903|The EXPLAIN output file name must be a NON-NULL CHAR, VARCHAR, VARCHAR2.|
|-23904|Attached table (%s) has an incompatible hash column specification.|
|-23905|Attached table (%s) has an incompatible table type.|
|-23906|Dbslice lookup failed.|
|-23907|Column %s for hash fragmentation doesn't exist.|
|-23908|Alter Fragment option not supported for hash fragmentation.|
|-23909|Blob or Text field (%s) cannot be used in hash fragmentation.|
|-23910|Result types from case expression must be compatible.|
|-23911|Cannot update a row twice in a joined-row update.|
|-23912|Cannot use 'first' or 'middle' in this context.|
|-23913|SAMPLE/LOCAL specifiers apply to tables. %s is not a table.|
|-23915|Alter Fragment option not supported for hybrid fragmentation.|
|-23916|Attached table (%s) has an incompatible fragmentation scheme.|
|-23917|Unable to lock row for hold cursor.|
|-23918|Cannot create detached cluster index.|
|-23919|Cannot create index with IN dbslice clause.|
|-23920|Could not create bitmap index due to outstanding in-place alter.|
|-23921|Cannot alter table type in combination with other alter table options.|
|-23922|Serial column usage incompatible with fragmentation scheme.|
|-23923|HAVING clause should be accompanied by a GROUP clause or with aggregates on all   columns in the SELECT clause.|
|-23924|Unique/referential/primary key constraints are not allowed on blob columns.|
|-23925|Second arg of dbinfo(dbspace/coserverid) cannot specify a view.|
|-23926|Second arg of dbinfo(dbspace/coserverid) must specify a column.|
|-23927|Third arg of dbinfo(dbspace/coserverid) must be string 'currentrow'.|
|-23928|Unable to determine if there are outstanding In-place alters.|
|-23929|Cannot set memory resident status for a view.|
|-23930|GK-index creation syntax error: (%s).|
|-23931|GK-index creation: FROM clause must contain LOCAL, STATIC BASE tables only.|
|-23932|GK-index creation: indexed table missing in the SELECT statement.|
|-23933|GAM sanity error (%s).|
|-23934|GAM internal error (%s).|
|-23935|GAM: HCNF not supported yet.|
|-23936|There are GK-indexes depending on a table in the statement.|
|-23937|GK-index creation: table %s isn't join on key to the indexed table.|
|-23950|XBAR error: Error during dbspace backup.|
|-23951|XBAR error: Error during logical log backup.|
|-23952|XBAR error: Error during physical restore.|
|-23953|XBAR error: Error during logical log restore.|
|-23954|XBAR error: No such dbspace.|
|-23958|XBAR error: Invalid argument.|
|-23959|XBAR error: Internal error - Error %d from DFM %s at file %s line %d|
|-23960|XBAR error: Internal error - Unexpected message type %d received at file %s line %d|
|-23961|XBAR error: Not all buffers have been backed up|
|-23962|XBAR error: Detected error on local xplan thread. Remote thread aborting.|
|-23963|XBAR error: Memory allocation failed.|
|-23964|XBAR error: Internal error - Error %d from SCH %s at file %s line %d|
|-23965|XBAR error: Internal error - Error %d from XPL %s at file %s line %d|
|-23966|XBAR error: Interrupt received.|
|-23967|XBAR error: XPLAN has been aborted.|
|-23968|XBAR error: Internal error - Error %d from RSAM %s at file %s line %d|
|-23969|XBAR error: Invalid argument to %s: %s|
|-23970|XBAR error: Internal error - session control block is NULL.|
|-23971|XBAR error: Internal error - operation control block is NULL.|
|-23972|XBAR error: Fatal error detected on xplan.|
|-23973|XBAR error: Internal error - Error %d from CM %s at file %s line %d|
|-23974|XBAR error: Invalid transport buffer.|
|-23975|XBAR error: Internal error - Error %d from MT %s at file %s line %d|
|-23976|XBAR error: At least one dbspace must be specified for this operation|
|-23977|XBAR error: Internal error - Fatal error executing external restore.  Not all dbspaces are complete|
|-23979|XBAR error: Invalid coserver id.|
|-23980|XBAR error: Duplicate coserver id.|
|-23981|XBAR error: Allocate transport buffer failed.|
|-23982|XBAR error: Free transport buffer failed.|
|-23983|XBAR error: At least one index fragment must be specified for this operation.|
|-23984|XBAR error: Partition holding index fragment could not be opened for rebuild.|
|-23985|XBAR error: Index fragment in unexpected state, not being rebuilt.|
|-23986|XBAR error: Could not start thread for index rebuild.|
|-23987|XBAR error: Could not lock table for index rebuild.|
|-23988|XBAR error: Could not locate index rebuild thread.|
|-23989|XBAR error: Index rebuild thread is in an unexpected state.|
|-23990|XBAR error: Index fragment is already being rebuilt.|
|-24000|Check executor internal error: %d   Query: %s|
|-24001|Check object does not exist|
|-24002|Query doesn't exist.|
|-24003|Query is on the RGM wait queue.|
|-24004|Onutil Error: Server must be in quiescent or on-line mode.|
|-24005|Query type is not supported.|
|-24006|Session has additional 0x%06x information.|
|-24100|Cannot alter index lock mode.|
|-24101|Cannot specify lock mode for an index on a temporary table.|
|-24102|Index columns are not same as RANGE columns|
|-24103|RANGE column(%s) must specify a MIN/MAX range.|
|-24104|Fragmentation column(%s) must not specify MIN/MAX range.|
|-24105|Table(%s) is not FRAGMENT BY RANGE.|
|-24106|Index column list must include fragmentation column(%s).|
|-24107|RANGE Column(%s) must be of type INTEGER or SMALLINT.|
|-24108|RANGE dbslices must contain equal number of dbspaces.|
|-24109|Specified RANGE is smaller than the number of dbspaces.|
|-24110|Total number of index keys specified by the ranges   already exceeds the limit of 2147483647.|
|-24111|Rowsize (%s) is too large for Range Cluster Index.|
|-24112|Cannot update column (%s).|
|-24113|Table (%s) is not a duplicated table.|
|-24114|Number of dbspace lists does not match number of fragments in table.|
|-24115|Number of dbspaces per dbspace list must be identical.|
|-24116|Duplicate dbspace (%s) detected in CREATE DUPLICATE specification.|
|-24117|Dbspace (%s) in CREATE DUPLICATE specification already exists in table.|
|-24118|This ddl operation is not allowed due to deferred constraints   pending on this table and dependent tables.|
|-24119|Cannot specify/change locking mode for RCI.|
|-24120|Cannot use dbinfo function in HAVING clause.|
|-24121|Data Dictionary locking error (%s).|
|-24122|Column not specified for hash/hybrid fragmentation and there is no   primary key for the table.|
|-24123|Blobs are not allowed in the 'Union' clause.|
|-24124|Truncate Table statement cannot be executed if already inside a transaction.|
|-24125|The table cannot be truncated, it has at least one non-empty   child table with referential constraint.|
|-24126|Update or delete not allowed on inner tables in UPDATE/DELETE outer joins.|
|-24127|Target table cannot appear more than once in UPDATE/DELETE joins table list.|
|-24128|One or more coservers are not capable of holding data of this type.|
|-24129|Logged temporary tables cannot be created in an unlogged temporary dbspace.|
|-24130|Hybrid fragmentation must have more than one expression specification.|
|-24131|Session cache overflow: too many concurrent database accesses.|
|-24132|Tmpspace allocation exceeded.|
|-24133|You can run onaudit only on the primary coserver.|
|-24134|XA transaction aborted.|
|-24135|Cannot prepare XA transaction.|
|-24136|CREATE DATABASE: dbspace '%s' not found on coserver one.|
|-24137|Table expressions are not allowed in triggers and gk-indexes.|
|-24138|All column references in a table expression must refer to tables in the   FROM clause of the table expression.|
|-24139|Found a temporary dbspace '%s' in the SET (TEMP) TABLE_SPACE clause.|
|-24140|Invalid PDQ priority value specified|
|-24141|Serial foreign key cannot refer to another serial column.|
|-24142|Permission denied: User cannot set mutability for environment variables.|
|-24143|Session environment variable %s is immutable. Contact DBA.|
|-24144|Session is already connected to coserver (%s).|
|-24145|Only permanent(base) tables can be moved.|
|-24146|Username and rolename have conflicting permissions.|
|-24147|Source and destination database must be different.|
|-24148|Cannot move a table from the sysmaster and sysutils databases.|
|-24149|Owner name conflicts with role name in the destination database.|
|-24150|Only users with DBA privileges can move the table.|
|-24151|Globally detached indexes are not supported on raw or scratch tables.|
|-24161|CLIENT_TZ has an invalid setting for the current operation.|
|-24162|CLIENT_TZ has not been set.|
|-24163|Column alias is necessary in the specified table expression.|
|-24164|DBslice or DBspace (%s) is not usable.|
|-24165|%s is currently not a defined class.|
|-24166|Resource class memory quota insufficient to execute query.|
|-24200|RQM Error: Can not find the session.|
|-24201|RQM Error: Can not find statement sdb.|
|-24250|Dataflow Manager: System error in routine %s|
|-24251|Dataflow Manager: Insufficient memory for request (%d bytes required)|
|-24252|Dataflow Manager: Invalid parameter (%d, %s)|
|-24253|Dataflow Manager: Internal error (%d, %s) contact product support.|
|-24254|Dataflow Manager: Caller defined error (%d, %s).|
|-24255|Dataflow Manager: Channel not found.|
|-24256|Dataflow Manager: Caller must wait (%s).|
|-24257|Dataflow Manager: No such flow control algorithm (%d).|
|-24258|Dataflow Manager: Internal error unblock possible.|
|-24259|Dataflow Manager: Operation interrupted by user.|
|-24260|Dataflow Manager: Channel already open.|
|-24261|Dataflow Manager: Internal error want idle processing.|
|-24262|Dataflow Manager: Internal error enqueue packet.|
|-24300|Column (%s) not found in the target table.|
|-24301|Table (%s) is not the target table.|
|-24302|Column (%s) not found in the source table.|
|-24303|Table (%s) is not the source table.|
|-24304|A query using an outer join that references remote objects in its   current form is unsupported.|
|-24305|Invalid value for environment variable %s.|
|-24306|Aborting concurrent attempt by threads to use the same connection to a remote server.|
|-24307|Internal SQL Error. (%s)|
|-24308|Data Dictionary cache has been modified.|
