# GBase 8s数据库错误代码  
第二部分  

## itoxmsg  

|ErrCode|ODBC ErrCode|
|:---|:---|
|100|02000|
|0|00000|
|-201|42000|
|-206|42000|
|-208|S1001|
|-236|21S01|
|-239|23000|
|-254|07001|
|-259|24000|
|-260|07005|
|-262|24000|
|-266|24000|
|-268|23000|
|-272|42000|
|-273|42000|
|-274|42000|
|-275|42000|
|-276|24000|
|-284|21000|
|-285|24000|
|-306|22003|
|-310|S0001|
|-316|S0011|
|-319|S0012|
|-328|S0021|
|-350|S0011|
|-352|S0002|
|-371|23000|
|-385|44000|
|-391|23000|
|-400|24000|
|-404|07003|
|-406|S1001|
|-410|37000|
|-467|22002|
|-471|33000|
|-472|22003|
|-481|37000|
|-483|37000|
|-525|23000|
|-530|23000|
|-536|23000|
|-543|22019|
|-551|23000|
|-586|24000|
|-598|34000|
|-676|23000|
|-691|23000|
|-692|23000|
|-699|40000|
|-766|22024|
|-839|S0002|
|-840|S0000|
|-841|S0000|
|-879|22027|
|-886|42000|
|-887|2B000|
|-901|28000|
|-902|28000|
|-908|08004|
|-930|08004|
|-934|08006|
|-942|42000|
|-1202|22012|
|-1214|22003|
|-1215|22003|
|-1222|22003|
|-1226|22003|
|-1278|22025|
|-1279|22001|
|-1800|25000|
|-1801|0A001|
|-1802|08002|
|-1803|08003|
|-1806|08006|
|-1805|2E000|
|-1809|08004|
|-1810|01002|
|-9442|46103|
|-9443|46103|
|-9447|46007|
|-9448|46007|
|-9449|46007|
|-9452|39004|
|-9479|38000|
|-9484|46002|
|-9485|46002|
|-9486|46001|
|-9487|46002|
|-9488|46003|
|-9489|46003|
|-22283|22003|


## jdbc  

|ErrCode|Description|
|:---|:---|
|-79700|Method not supported|
|-79701|Blob not found|
|-79702|Can't create new object|
|-79703|Row/column index out of range|
|-79704|Can't load driver|
|-79705|Incorrect URL format|
|-79706|Incomplete input|
|-79707|Invalid qualifier|
|-79708|Can't take null input|
|-79709|Error in date format|
|-79710|Syntax error in SQL escape clause:|
|-79711|Error in time format|
|-79712|Error in timestamp format|
|-79713|Incorrect number of arguments|
|-79714|Type not supported|
|-79715|Syntax error|
|-79716|System or internal error|
|-79717|Invalid qualifier length|
|-79718|Invalid qualifier start code|
|-79719|Invalid qualifier end code|
|-79720|Invalid qualifier start or end code|
|-79721|Invalid interval string|
|-79722|Numeric character(s) expected|
|-79723|Delimiter character(s) expected|
|-79724|Character(s) expected|
|-79725|Extra character(s) found|
|-79726|Null SQL statement|
|-79727|Statement was not prepared|
|-79728|Unknown object type|
|-79729|Method can not take argument|
|-79730|Connection not established|
|-79731|MaxRows out of range|
|-79732|Illegal cursor name|
|-79733|No active result|
|-79734|GBASEDBTSERVER has to be specified|
|-79735|Can't instantiate protocol|
|-79736|No connection/statement established yet|
|-79737|No meta data|
|-79738|No such column name|
|-79739|No current row|
|-79740|No statement create|
|-79741|Can't convert to|
|-79742|Can't convert from|
|-79743|Cannot load the specified IfxProtocol class|
|-79744|Transactions not supported|
|-79745|Read only mode not supported|
|-79746|No Transaction Isolation on non-logging db's|
|-79747|Invalid transaction isolation level|
|-79748|Can't lock the connection|
|-79749|Number of input values does not match number of question marks|
|-79750|Method only for queries|
|-79751|Forward fetch only. (in JDBC 1.2)|
|-79752|Insufficient Blob data|
|-79753|Out of Blob memory|
|-79754|Write Fault|
|-79755|Object is null|
|-79756|must start with 'jdbc'|
|-79757|Invalid sub-protocol|
|-79758|Invalid ip address|
|-79759|Invalid port number|
|-79760|Invalid database name|
|-79761|Invalid Property format|
|-79762|Attempt to connect to a non 5.x server.|
|-79763|Updates are not allowed on READ_ONLY cursor.|
|-79764|Invalid Fetch Direction value.|
|-79765|ResultSet Type is TYPE_FETCH_FORWARD, direction can only be FETCH_FORWARD.|
|-79766|Incorrect Fetch Size value.|
|-79767|ResultSet Type is TYPE_FORWARD_ONLY.|
|-79768|Incorrect row value.|
|-79769|A customized type map is required for this data type.|
|-79770|Cannot find the SQLTypeName specified in the SQLData or Struct class.|
|-79771|Input value is not valid.|
|-79772|No more data to read or write. Verify your SQLData class or getSQLTypeName() string.|
|-79773|Invalid arguments.|
|-79774|Unable to create local file.|
|-79775|Only TYPE_SCROLL_INSENSITIVE and TYPE_FORWARD_ONLY are supported.|
|-79776|Type requested (%s) doesn't match row type information (%s) type.|
|-79777|readObject/writeObject() only supports UDT's, Distincts and complex types.|
|-79778|Type mapping class must be a java.util.Collection implementation.|
|-79779|To insert null data into a row use java null representation.|
|-79780|Data within a collection must all be the same java class and length.|
|-79781|Index/Count out of range.|
|-79782|Method can be called only once.|
|-79783|Encoding or code set not supported.|
|-79784|Locale not supported.|
|-79785|Unable to convert JDBC escape format date string to localized date string.|
|-79786|Unable to build a Date object based on localized date string representation.|
|-79787|Blob/Clob object has not been created from a BLOB/CLOB column.|
|-79788|User name must be specified.|
|-79789|Server does not support GLS variables DB_LOCALE, CLIENT_LOCALE or GL_DATE.|
|-79790|Invalid complex type definition string.|
|-79791|Invalid object. Cannot be inserted into clob/blob column.|
|-79792|Row must contain data.|
|-79793|Data in array doesn't match getBaseType() value.|
|-79794|Row length provided (%s) doesn't match row type information (%s).|
|-79795|Row extended id provided (%s) doesn't match row type information (%s).|
|-79796|Cannot find UDT, distinct or named row (%s) in database.|
|-79797|DBDATE setting must be at least 4 characters and no longer than 6 characters.|
|-79798|A numerical year expansion is required after 'Y' character in DBDATE string.|
|-79799|An invalid character is found in DBDATE string after the 'Y' character.|
|-79800|No 'Y' character is specified before the numerical year expansion value.|
|-79801|An invalid character is found in DBDATE format string.|
|-79802|Not enough tokens are specified in the string representation of a date value.|
|-79803|Date string index out of bounds during date format parsing to build Date object.|
|-79804|No more tokens are found in DBDATE string representation of a date value.|
|-79805|No era designation found in DBDATE/GL_DATE string representation of date value.|
|-79806|Numerical day value can not be determined from date string based on DBDATE.|
|-79807|Numerical month value can not be determined from date string based on DBDATE.|
|-79808|Not enough tokens specified in %D directive representation of date string.|
|-79809|Not enough tokens specified in %x directive representation of date string.|
|-79810|This release of JDBC requires to be run with JDK 1.2+.|
|-79811|Connection without user/password not supported.|
|-79812|user/Password does not match with datasource.|
|-79813|Cannot call setBindColType() after executeQuery().|
|-79814|Blob/Clob object is either closed or invalid.|
|-79815|Not in Insert mode. Need to call moveToInsertRow() first.|
|-79816|Cannot determine the table name.|
|-79817|No serial, rowid, or primary key specified in the statement.|
|-79818|Statement concurrency type is not set to CONCUR_UPDATABLE.|
|-79819|Still in Insert mode. Call moveToCurrentRow() first.|
|-79820|Function contains an output parameter.|
|-79821|Name unneccessary for this data type.|
|-79822|OUT parameter has not been registered.|
|-79823|IN parameter has not been set.|
|-79824|OUT parameter has not been set.|
|-79825|Type name is required for this data type.|
|-79826|Ambiguous java.sql.Type, use IfxRegisterOutParameter().|
|-79827|Function doesn't have an output parameter or the out parameter isn't returned.|
|-79828|Function parameter specified isn't an OUT parameter.|
|-79829|Invalid directive used for the GL_DATE environment variable.|
|-79830|Insufficient information given for building a Time or Timestamp Java object.|
|-79831|Exceeded maximum no. of connections configured for Connection Pool Manager.|
|-79832|Netscape Exception! Permission to connect denied by user.|
|-79833|Netscape Exception! Unknown exception while enabling privilege.|
|-79834|Distributed transactions (XA) not supported by this server.|
|-79835|RowSet is set to ReadOnly.|
|-79836|Proxy Error: No database connection.|
|-79837|Proxy Error: Input/output error while communicating with database.|
|-79838|Cannot execute change permission command (chmod/attrib).|
|-79839|Same Jar SQL name already exists in the system catalog.|
|-79840|Unable to copy jar file from client to server.|
|-79841|Invalid or Inconsistent Tuning Parameters for Connection Pool Datasource.|
|-79842|No UDR information was set in UDRMetaData.|
|-79843|SQL name of the jar file was not set in UDR/UDT metadata.|
|-79844|Can't create/remove UDT/UDR as no database is specified in the connection.|
|-79845|Jar file on the client does not exist or can't be read.|
|-79846|Invalid Jar file name.|
|-79847|The 'javac' or 'jar' command failed.|
|-79848|Same UDT SQL name already exists in the system catalog.|
|-79849|UDT SQL name was not set in UDTMetaData.|
|-79850|UDT field count was not set in UDTMetaData.|
|-79851|UDT length was not set in UDTMetaData.|
|-79852|UDT field name or field type was not set in UDTMetaData.|
|-79853|No class file to be put into the jar, or one of the class files does not exist.|
|-79854|UDT java class must implement java.sql.SQLData interface.|
|-79855|Specified UDT java class is not found.|
|-79856|Specified UDT does not exist in the database.|
|-79857|Invalid support function type.|
|-79858|The command to remove file on the client failed.|
|-79859|Invalid UDT field number.|
|-79860|Ambiguous java type(s) - can't use Object/SQLData as method argument(s).|
|-79861|Specified UDT field type has no Java type match.|
|-79862|Invalid UDT field type.|
|-79863|UDT field length was not set in UDTMetaData.|
|-79864|Statement length exceeds maximum.|
|-79865|'Statement' already closed.|
|-79868|ResultSet not open, operation not permitted.|
|-79869|Negative timeout value given.|
|-79877|Invalid parameter value for setting maximum field size.|
|-79878|ResultSet not open, operation 'next' not permitted. Verify that autocommit is OFF|
|-79879|An unexpected exception was thrown.  See next exception for details.|
|-79880|Unable to set JDK Version for the Driver.|
|-79881|Already in local transaction, so cannot start XA transaction.|
|-79882|Method not supported with this server.|
|-79883|Class that implements IfmxPAM interface could not be located or loaded.|
|-79884|Class must implement com.gbasedbt.jdbc.IfmxPAM interface for PAM functionality.|
|-79885|PAM authorization has failed.|
|-79886|PAM Response Message Size exceeds maximum size allowed.|
|-79887|Parameter name not found.|
|-79888|Parameters indicated by both name and index for CallableStatement object.|
|-79889|Cannot set savepoint, rollback to a savepoint, or release a savepoint when auto-commit mode is on.|
|-79890|Cannot set savepoint, rollback to a savepoint, or release a savepoint within XA transaction.|
|-79891|Savepoint name for the Named savepoint cannot be null.|
|-79892|Savepoint cannot be null for rollback to a savepoint or release a savepoint.|
|-79893|Savepoint not valid in current connection.|
|-79894|Can not get savepoint id for named savepoint.|
|-79895|Can not get savepoint name for un-named savepoint.|
|-79896|Incorrect connection array index in the connection pool.|
|-79897|Insufficient Clob data|
|-79999|Message text will be provided in later releases|


## jdbcminor  

|ErrCode|Description|
|:---|:---|
|-80000|: Fraction should start with 0 or .|
|-80001|: First field should have digits|
|-80002|: First field has too many digits|
|-80003|: At position|
|-80004|: Missing|
|-80005|: In outer join|
|-80006|: Invalid SQL escape syntax|
|-80007|: Can't be < 0|
|-80008|: int|
|-80009|: Integer|
|-80010|: long|
|-80011|: Long|
|-80012|: short|
|-80013|: Short|
|-80014|: BigDecimal|
|-80015|: byte|
|-80016|: byte array|
|-80017|: Byte|
|-80018|: boolean|
|-80019|: Boolean|
|-80020|: float|
|-80021|: Float|
|-80022|: double|
|-80023|: Double|
|-80024|: Date|
|-80025|: Time|
|-80026|: Timestmp|
|-80027|: String|
|-80028|: input stream|
|-80029|: ASCII stream|
|-80030|: binary stream|
|-80031|: Object|
|-80032|: GBasedbt internal format|
|-80033|for critical message transfer|
|-80034|GBasedbt error code|
|-80035|URL|
|-80036|IntervalYM|
|-80037|IntervalDF|
|-80038|Interval|
|-80039|Character stream|
|-80040|IfxBSONObject|
|-80251|Adding Ldap entry:-->\n|
|-80252|Deleting Ldap entry:-->\n|
|-80253|<--- Entry Exists in the Server, not added.|
|-80254|Usage --->\nSqlhUpload sqlhosts_file ldap_host:port [sqlhostsRdn]|
|-80255|\n*-------------------------------------------------------->\n   This utility uploads the Sqlhosts data in flat ascii file \n   onto the Sqlhosts subtree in LDAP in the prescribed format:\n   \n Note: The Service field (4th field in the sqlhosts field)\n   should specify an Integer port number.\n   <----------------------------------------------------------*\n|
|-80256|Usage --->\nSqlhDelete ldap_host:port [sqlhostsRdn]|
|-80257|\n*-------------------------------------------------------->\n   This utility deletes the Sqlhosts data from the LDAP server.\n   <----------------------------------------------------------*\n|
|-80258|\nEnter the DN for GBasedbt in your LDAP tree ==>|
|-80259|\nEnter the uname for Ldap login (eg: cn=root, o=acme, c=us) ==>|
|-80260|\nEnter the password for Ldap login ==>|
|-80261|\n The input arguments --->;|
|-80262|\t The file name -->|
|-80263|\t The LDAP URL -->|
|-80264|\t The GBasedbt base -->|
|-80265|\t The Sqlhosts base -->|
|-80266|\t The User Name -->|
|-80267|\n If the argumets are not ok, please start over !!!!\n   \n Enter [q] to quit or [c] to continue ==>|
|-80268|\n Error while reading the Terminal Input|
|-80269|\n Uploading Sqlhosts file data to LDAP Server --->|
|-80270|\n Deleting Sqlhosts data from from LDAP Server --->|
|-80281|JNS Internal Error.|
|-80282|JNS: Error while initializing Ldap Context.|
|-80283|JNS: Error while searching Ldap Server.|
|-80284|JNS: Error while updating Ldap Server.|
|-80290|InitDirCtx for SqlHosts in SqlHosts() Failed|
|-80291|Search or Results operation in getServer()::|
|-80292|Empty set in Search operation in getServer()::|
|-80293|Check credentials for LDAP|
|-80294|Search or Results operation in getServerGroup()::|
|-80295|Update operation in addServer()::|
|-80296|Update operation in addEntry()::|
|-80297|Update operation in delServer()::|
|-80298|Update operation in destroySqlhosts()::|
|-80299|Update operation in uploadToLdap()::|
|-80300|Update operation in updateSqlhosts()::|
|-80301|Error in FileSqlhosts()::|
|-80302|Search operation in getServer() [file]::|
|-80303|Update operation in uploadToLdap()::|


## miapi  

|ErrCode|Description|
|:---|:---|
|-7400|Invalid API argument (%s).|
|-7401|Invalid API usage (%s).|
|-7402|Internal error (%s).|
|-7403|File protocol error.  Expected (%s).|
|-7404|File protocol error.  Reported by client.|
|-7405|Cannot do set operation on GBASEDBTSERVER|
|-7406|Operation (%s) not supported outside execution.|
|-7411|Error loading locale object for client locale.|
|-7412|Error loading codeset conversion object for converting to client codeset.|
|-7413|Error loading locale object for server processing locale.|
|-7420|Argument (%s) is invalid.|
|-7421|The specified column position is invalid.|
|-7422|Cannot issue SAPI function %s in a secondary PDQ thread.   You need to define the user-defined routine as non-parallelizable.|
|-7423|An invalid argument is specified. Either the return type   buffer is empty or the buffer's length is not valid.|
|-7424|A Cursor can only be defined for a prepared SELECT statement.|
|-7425|Invalid statement handle.|
|-7426|There is no active query on this connection.|
|-7427|Argument is not a valid %s.|
|-7428|Saveset is corrupted.|
|-7429|Out of memory allocating save set.|
|-7430|Out of memory allocating save set element.|
|-7431|Invalid save set type %s.|
|-7432|Command is not yet complete.|
|-7433|Command not a DML.|
|-7435|This statement references a table that is used in the parent queries.|
|-7436|Inappropriate statement type for parameter information.|
|-7437|Null MI_ROW from mi_fp_getrow.|
|-7438|Unsupported data type.|
|-7439|Cannot use the same cursor name more than once.|
|-7440|Type must be specified for all parameters in where clause.|
|-7441|%s: Type must be complex type (SET, LIST, MULTISET, ROW).|
|-7442|The statement must be opened before this operation can be performed.|
|-7443|The statement must be closed before it can be reopened or executed.|
|-7469|Calling %s is not supported from compare function|
|-7470|Invalid connection (%s).|
|-7471|Internal error: Invalid user-defined routine context/state (%s).|
|-7472|Out of memory allocating internal user-defined routine connection state.|
|-7473|Internal error: Bad install of user-defined routine-language manager callback.|
|-7474|Out of memory allocating server user-defined routine connection.|
|-7475|Can't close a connection from outside of its own parent statement.|
|-7476|Can't close a session duration connection within an UDR.|
|-7490|Cannot open trace output file (%s).|
|-7491|Cannot read trace system table (%s).|
|-7492|Write to trace output file failed.|
|-7493|Cannot create internal map to trace classes.|
|-7494|Cannot create internal trace message list.|
|-7500|Invalid multi-byte character in syserrors catalog table for sqlstate '%s'.|
|-7501|Message not found in syserrors catalog table for sqlstate '%s'.|
|-7502|Illegal SQL statement in user-defined routine: '%s'.|
|-7503|The BLOB or CLOB data size provided differs from the client file size.|
|-7510|API use not valid in callback (%s).|
|-7511|Callback not found for the specified event type (%s).|
|-7512|Invalid return value from registered callback function.|
|-7513|Exception during callback %s.|
|-7514|MI_EVENT_END_XACT callback can only be registered inside a transaction.|
|-7515|Last callback already registered.|
|-7520|Argument (%s) is NULL.|
|-7521|GLS internal error within API: (%s).|
|-7522|Incomplete locale information for conversion between client and server formats|
|-7523|ASF layer call failed: insufficient data for client-server format conversion|
|-7524|Client format unknown: cannot convert between client and server formats|
|-7530|Missing parenthesis in the signature specified for user-defined routine lookup|
|-7531|Invalid user-defined routine type: must be function or procedure|
|-7532|Error converting type in string format to id format|
|-7535|Invalid MI_FPARAM pointer returned|
|-7536|Error unlinking function descriptor from connection, not previously linked|
|-7538|Error converting default arguments to C style values|
|-7540|Routine's return value ID is out of range|
|-7541|Validation for current connection failed|
|-7543|Internal error while performing system cast|
|-7544|Attempt to free MI_FPARAM structure allocated internally, not on behalf of UDR|
|-7545|Index out of range for UDR argument or return array in MI_FPARAM|
|-7546|Unknown routine type %s, routine type must be one of 'f' or 'p'.|
|-7547|Routine name is missing in call to mi_create_signature|
|-7548|Cannot create capsules for remote routines.|
|-7549|Cannot use mi_funcmap_get on remote routines.|
|-7560|Can not determine user name|
|-7561|A Password must be provided if other than default username is given|
|-7562|Error finishing the last query|
|-7563|Attempt to open a cursor which is already open|
|-7564|Can not open a cursor on a non-select statement|
|-7565|Bad Cursor Action|
|-7566|Can not position on a non-list collection|
|-7567|Invalid Collection Position|
|-7568|Not supported from Client API|
|-7570|Environmental variable GBasedbtdir is not set.|
|-7571|Sqlhosts file (%s) could not be opened.|
|-7572|Sqlhosts file (%s) read error.|
|-7573|Out of memory trying to allocate hostslist entry.|
|-7574|Sqlhosts registry key cannot be opened.|
|-7575|Sqlhosts registry key cannot be enumerated.|
|-7580|Invalid attempt to call %s: this routine may only be called from an am_check routine.|
|-7581|Invalid attempt to call %s: this routine may only be called from an am_open or am_beginscan routine.|
|-7582|Invalid attempt to call %s: this routine may only be called from an am_insert routine.|
|-7583|Invalid attempt to call %s: this routine may only be called from an am_getnext routine.|
|-7584|Cannot insert more than maximum number of rows in Set Read/Write cache.|
|-7585|Cannot read past actual number of rows in Set Read/Write cache.|
|-7586|Maximum number of rows in Set Read/Write cache already set.|
|-7590|Cannot read past the end of stream marker|
|-7591|A generic mistream failure|
|-7592|Stream function capability is not implemented|
|-7593|Send side failure for stream|
|-7594|Receive side failure for stream|
|-7595|Error in int8 operation|
|-7596|A bad whence value was used for seek a operation|
|-7597|SAPI function attempting to determine shared library module ID failure|
|-7598|Function symbol lookup in shared libray failed|
|-7599|Function pointer lookup in shared libray failed|
|-7600|Collection jump position non-zero on non-LIST collection.|
|-7601|Bad cursor action (%s).|
|-7602|Invalid field count for a row (%s).|
|-7603|Create collection failed: No such type (%s).|
|-7604|Collection comparison not allowed.|
|-7605|Invalid (NULL) mi_sendrecv struct from mi_routine_exec.|
|-7606|Invalid builtin type (%s);|
|-7607|Invalid row literal value.|
|-7608|Bad ABSOLUTE jump value: %s.  Must be greater than 0.|
|-7609|Cursor does not exist.|
|-7610|Invalid collection literal value.|
|-7620|Invalid JVP sapi callback request.|
|-7621|Out of memory allocation sapi callback arguments|
|-7622|Internal error: Bad install of Java-language manager callback.|


## mls2  

|ErrCode|Description|
|:---|:---|
|32500|User does not have Discrete privilege to change session levels.|
|-32500|User does not have Discrete privilege to change session levels.|
|32501|Login session level not dominating the new session level.|
|-32501|Login session level not dominating the new session level.|
|32502|New session level not dominating the database level.|
|-32502|New session level not dominating the database level.|
|32503|User tables should be closed to change session attribute.|
|-32503|User tables should be closed to change session attribute.|
|32504|Remote operation not allowed.|
|-32504|Remote operation not allowed.|
|32505|Cannot set session level.|
|-32505|Cannot set session level.|
|32506|Bad session label format|
|-32506|Bad session label format|
|32507|Cannot set session authorization.|
|-32507|Cannot set session authorization.|
|32508|Statement is invalid within a transaction.|
|-32508|Statement is invalid within a transaction.|
|32509|Bad session authorization format|
|-32509|Bad session authorization format|
|32510|User does not have Discrete privilege to change session authorization.|
|-32510|User does not have Discrete privilege to change session authorization.|
|32511|User does not have Discrete privilege for set table high.|
|-32511|User does not have Discrete privilege for set table high.|
|32512|Cannot set the specified table high.|
|-32512|Cannot set the specified table high.|
|32513|Cannot rename a table or column.|
|-32513|Cannot rename a table or column.|
|-32514|Session level is different from the level of the database object.|
|32514|Session level is different from the level of the database object.|
|-32515|Cannot update the referential constraints on the table.|
|32515|Cannot update the referential constraints on the table.|
|32516|Cannot create referential constraint on the table.|
|-32516|Cannot create referential constraint on the table.|
|32517|Statement not valid on a remote server.|
|-32517|Statement not valid on a remote server.|
|32518|Session and login attributes are different.|
|-32518|Session and login attributes are different.|
|32519|The USING password clause in the SET SESSION AUTHORIZATION statement is used only for trusted connections.|
|-32519|The USING password clause in the SET SESSION AUTHORIZATION statement is used only for trusted connections.|
|32520|Cannot create SL map tblspace.|
|-32520|Cannot create SL map tblspace.|
|32521|Cannot create IL map tblspace.|
|-32521|Cannot create IL map tblspace.|
|32522|Cannot create Datalo translation.|
|-32522|Cannot create Datalo translation.|
|32523|Cannot create Datahi translation.|
|-32523|Cannot create Datahi translation.|
|32524|Cannot create ixdataH translation.|
|-32524|Cannot create ixdataH translation.|
|32525|Cannot create saved translations.|
|-32525|Cannot create saved translations.|
|32526|Saved and stored tags disagree.|
|-32526|Saved and stored tags disagree.|
|32527|Out of memory.|
|-32527|Out of memory.|
|32528|Tag not found.|
|-32528|Tag not found.|
|32529|Cannot create ixdbsaL translation.|
|-32529|Cannot create ixdbsaL translation.|
|-32530|Need to attach to share memory to get tag.|
|32531|-C     print security session configuration.|
|32532|Illegal data type for aggregation function.|
|-32532|Illegal data type for aggregation function.|
|-32540|Illegal GBase tag supplied.|
|-32550|Commercial error : Syntax error in security files.|
|-32551|Commercial error : Illegal characters detected in security files.|
|-32552|Commercial error : Class id is out of range.|
|-32553|Commercial error : Duplicated names used in security files.|
|-32554|Commercial error : Duplicated ids used in security files.|
|-32555|Commercial error : Undefined category name supplied.|
|-32556|Commercial error : Undefined class name supplied.|
|-32557|Commercial error : Undefined class id.|
|-32558|Commercial error : Undefined category id.|
|-32559|Commercial error : Cannot open file.|
|-32560|Commercial error : Size of label is too small.|
|-32561|Commercial error : User not found.|
|-32562|Commercial error : Host not found.|
|-32563|Commercial error : Illegal parameter.|
|-32564|Commercial error : Error opening secconfig file.|
|-32565|Commercial error : Syntax error in secconfig file.|
|-32566|Commercial error : No such synonym in secconfig file.|
|-32600|Current session level dominates user's clearance on remote server.|
|32600|Current session level dominates user's clearance on remote server.|
|-32601|Server unable to get/set sensitivity level of connection/process.|
|32601|Server unable to get/set sensitivity level of connection/process.|
|-32602|Server unable to get/set effective privileges for user.|
|32602|Server unable to get/set effective privileges for user.|
|-32603|Server unable to get/set DAC parameters for user.|
|32603|Server unable to get/set DAC parameters for user.|
|-32604|Permission denied, Session DAC/MAC check failed.|
|32604|Permission denied, Session DAC/MAC check failed.|
|-32605|Unable to change process label to ixdataH.|
|32605|Unable to change process label to ixdataH.|
|32606|Invalid system catalog data in vanilla unload tape.|
|32607|Loading of vanilla tables is not supported.|
|32608|Starting load of vanilla database.|
|32609|Cannot write to audit log...system shutting down.|
|-32609|Cannot write to audit log...system shutting down.|
|32610|Audit records are temporarily written to OnLine log.|
|-32610|Audit records are temporarily written to OnLine log.|
|32611|Cannot write to audit log...STAR/Secure daemon aborting.|
|-32611|Cannot write to audit log...STAR/Secure daemon aborting.|
|32612|Cannot write to remote audit log...connection refused.|
|-32612|Cannot write to remote audit log...connection refused.|


## mls  

|ErrCode|Description|
|:---|:---|
|32100|MAC check failed.|
|-32100|MAC check failed.|
|32101|DAC check failed.|
|-32101|DAC check failed.|
|32102|Bad label range.|
|-32102|Bad label range.|
|32103|Label comparison operation failed.|
|-32103|Label comparison operation failed.|
|32104|Internal error; no table descriptor.|
|-32104|Internal error; no table descriptor.|
|32110|Illegal session level for dropping a database.|
|-32110|Illegal session level for dropping a database.|
|32111|ISAM error: Illegal session level for changing database logging.|
|-32111|ISAM error: Illegal session level for changing database logging.|
|32112|No DBA privilege for creating a view schema.|
|-32112|No DBA privilege for creating a view schema.|
|32113|No DBA privilege for creating a table schema.|
|-32113|No DBA privilege for creating a table schema.|
|32114|Cannot drop system catalog tables.|
|-32114|Cannot drop system catalog tables.|
|32115|Cannot change the ownership of a table.|
|-32115|Cannot change the ownership of a table.|
|32116|Illegal session level for altering a table.|
|-32116|Illegal session level for altering a table.|
|32117|Illegal session level for creating an index.|
|-32117|Illegal session level for creating an index.|
|32118|No Index privilege for creating an index.|
|-32118|No Index privilege for creating an index.|
|32119|Illegal session level for altering an index.|
|-32119|Illegal session level for altering an index.|
|32120|No Resource privilege.|
|-32120|No Resource privilege.|
|32121|Illegal session level for dropping an index.|
|-32121|Illegal session level for dropping an index.|
|32122|Cannot modify system catalog tables.|
|-32122|Cannot modify system catalog tables.|
|32123|Not the owner of the index.|
|-32123|Not the owner of the index.|
|32124|Cannot modify an index on a temporary table.|
|-32124|Cannot modify an index on a temporary table.|
|32125|Current database number out of range.|
|-32125|Current database number out of range.|
|32126|Illegal label tag.|
|-32126|Illegal label tag.|
|32127|Illegal session level for dropping a table.|
|-32127|Illegal session level for dropping a table.|
|32128|No privilege for changing a SERIAL column.|
|-32128|No privilege for changing a SERIAL column.|
|32129|Table was not opened at required level.|
|-32129|Table was not opened at required level.|
|32130|There is no record at the specified level.|
|-32130|There is no record at the specified level.|
|32131|Internal heap error.|
|-32131|Internal heap error.|
|32132|Cannot order by label.|
|-32132|Cannot order by label.|
|32133|Illegal session level for granting table-level privileges.|
|-32133|Illegal session level for granting table-level privileges.|
|32134|Illegal session level for granting database-level privileges.|
|-32134|Illegal session level for granting database-level privileges.|
|32135|Illegal session level for revoking table-level privileges.|
|-32135|Illegal session level for revoking table-level privileges.|
|32136|Illegal session level for revoking database-level privileges.|
|-32136|Illegal session level for revoking database-level privileges.|
|32137|No Alter privilege to modify a constraint.|
|-32137|No Alter privilege to modify a constraint.|
|32138|Cannot set the initial SERIAL value.|
|-32138|Cannot set the initial SERIAL value.|
|32139|No initial value has been set for the SERIAL column.|
|-32139|No initial value has been set for the SERIAL column.|
|32140|Internal error: file handle and tabid are not consistent.|
|-32140|Internal error: file handle and tabid are not consistent.|
|32141|Internal error: unknown column found in SYSCOLUMNS.|
|-32141|Internal error: unknown column found in SYSCOLUMNS.|
|32142|Internal error: unknown index found in SYSINDEXES.|
|-32142|Internal error: unknown index found in SYSINDEXES.|
|32143|Cannot make index.|
|32145|Cannot change label of row.|
|-32145|Cannot change label of row.|
|32146|Cannot change label of table.|
|-32146|Cannot change label of table.|
|32147|Cannot change label of database.|
|-32147|Cannot change label of database.|
|32148|Cannot change DAC permission for column.|
|-32148|Cannot change DAC permission for column.|
|32149|Cannot change DAC permission for table.|
|-32149|Cannot change DAC permission for table.|
|32150|cannot change DAC permission for database.|
|-32150|cannot change DAC permission for database.|
|32151|Not owner of the view.|
|-32151|Not owner of the view.|
|32152|Illegal partition number for lock request.|
|-32152|Illegal partition number for lock request.|
|32164|Error creating session shared memory.|
|-32164|Error creating session shared memory.|
|32165|Error attaching to session shared memory.|
|-32165|Error attaching to session shared memory.|
|32167|Internal Error: Table label inconsistent.|
|-32167|Internal Error: Table label inconsistent.|
|32168|Internal Error: Database label inconsistent.|
|-32168|Internal Error: Database label inconsistent.|
|32169|Cannot convert label between internal and external forms.|
|-32169|Cannot convert label between internal and external forms.|
|32170|SAFE: cannot change object to non-comparable label.|
|-32170|SAFE: cannot change object to non-comparable label.|
|32171|SAFE: new database label not dominated by all tables.|
|-32171|SAFE: new database label not dominated by all tables.|
|32172|SAFE: fail to upgrade system catalogs.|
|-32172|SAFE: fail to upgrade system catalogs.|
|32173|SAFE: fail to downgrade system catalogs.|
|-32173|SAFE: fail to downgrade system catalogs.|
|32174|SAFE: new table label not dominating database.|
|-32174|SAFE: new table label not dominating database.|
|32175|SAFE: cannot modify label for system catalogs.|
|-32175|SAFE: cannot modify label for system catalogs.|
|32176|SAFE: cannot modify label for temp table.|
|-32176|SAFE: cannot modify label for temp table.|
|32177|SAFE: new table label not dominated by all rows.|
|-32177|SAFE: new table label not dominated by all rows.|
|32178|SAFE: new view label not dominating base table.|
|-32178|SAFE: new view label not dominating base table.|
|32179|SAFE: new synonym label not dominating base table.|
|-32179|SAFE: new synonym label not dominating base table.|
|32180|Enter the estimated # of security labels per table.|
|-32180|Enter the estimated # of security labels per table.|
|32181|The number of estimated security labels must be > 0.|
|-32181|The number of estimated security labels must be > 0.|
|32182|Invalid number of estimated security labels %d.|
|-32182|Invalid number of estimated security labels %d.|
|32183|LUB computation failed.|
|-32183|LUB computation failed.|
|32184|GLB computation failed.|
|-32184|GLB computation failed.|
|32185|Illegal session level for setting dbpassword.|
|-32185|Illegal session level for setting dbpassword.|
|32190|Can not aggregate label column.|
|-32190|Can not aggregate label column.|
|32191|Can not alter table.|
|-32191|Can not alter table.|
|32192|Illegal number of security labels %d|
|-32192|Illegal number of security labels %d|
|32193|oninit: Cannot create audit tblspace.|
|-32193|oninit: Cannot create audit tblspace.|
|32194|oninit: Cannot create reserved tblspace.|
|-32194|oninit: Cannot create reserved tblspace.|
|32195|oninit: Cannot create SL map tablespace.|
|32196|oninit: Cannot create IL map tablespace.|
|32197|Not an OnLine/Secure tape.|
|32198|Not an OnLine/Secure root chunk.|
