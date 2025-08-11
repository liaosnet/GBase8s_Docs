# GBase 8s数据库错误代码  

## cals  

|ErrCode|Description|
|:---|:---|
|-23101|Unable to load locale categories.|
|-23102|Memory allocation failed during locale processing.|
|-23103|Code-set conversion function failed due to illegal sequence or invalid value.|
|-23104|Error opening required code-set conversion object file.|
|-23105|The current database engine does not support code-set conversion.|
|-23106|Invalid argument for the code-set conversion initializing function.|
|-23107|DBLANG and CLIENT_LOCALE environment variables are incompatible.|
|-23108|An error occurred during locale structure creation.|
|-23109|Invalid locale specification.|
|-23110|An error occurred during environment variable processing.|
|-23111|Internal error.  Illegal argument for locale initialization.|
|-23112|Place holder for invalid GCV argument.|
|-23113|Place holder for unknown GCV error.|
|-23114|Place holder for GCV truncation.|
|-23115|Code sets of the locale categories are not the same.|
|-23190|Multibyte database name is not allowed in this system.|
|-23194|Code-set conversion restore failed.|
|-23195|Reset locale failed. Connection refused.|
|-23196|Unknown locale in selected database.|
|-23197|Database locale information mismatch.|
|-23198|GL_COLLATE information is missing from the system catalogs.|
|-23199|GL_CTYPE information is missing from the system catalogs.|
|-23100|An Error has occurred during locale structure creation.|


## csm  

|ErrCode|Description|
|:---|:---|
|-5000|CSM error: %s|
|-5001|CSM: memory allocation error.|
|-5002|CSM: memory de-allocation error.|
|-5003|CSM: file I/O error.|
|-5004|CSM: invalid context.|
|-5005|CSM: unsupported feature.|
|-5006|CSM: invalid global options.|
|-5007|CSM: invalid context options: %s|
|-5008|CSM: peer disconnected.|
|-5009|CSM: authentication error.|
|-5010|CSM: internal processing error.|
|-5011|CSM: protocol error.|
|-5012|CSM: received message of unexpected type.|
|-5013|CSM: cannot obtain credential: authentication error.|
|-5020|CSM: database server principal name not provided.|
|-5021|CSM: GBASEDBTKEYTAB environment variable not set.|
|-5022|CSM: received message of unexpected type.|
|-5030|CSM: crypto library error: %s|


## css  

|ErrCode|Description|
|:---|:---|
|-14500|CSS: error %s.|
|-14501|CSS: out of memory.|
|-14502|CSS: CSM %s not found.|
|-14503|CSS: error loading %s.|
|-14504|CSS: unsupported CSM version %s.|
|-14506|CSS: CSM %s: unexpected return code.|
|-14507|CSS: cascade disconnected.|
|-14508|CSS: error getting flags from CSM %s.|
|-14509|CSS: CSM disconnected inside cascade.|
|-14510|CSS: null buffer owner.|
|-14511|CSS: init function is not found in library %s.|
|-14512|CSS: shared library name is not specified.|
|-14513|CSS: CSM cannot finish a service operation.|
|-14551|CSS: CSM negotiation is not implemented.|
|-14562|CSS: no buffer management function provided.|
|-14563|CSS: error writing data.|
|-14564|CSS: no output function provided.|
|-14565|CSS: error reading data.|
|-14566|CSS: no input function provided.|
|-14567|CSS: buffer management function return code %s.|
|-14571|CSS: null CSS library context.|
|-14572|CSS: null I/O reference context.|
|-14573|CSS: bogus iterator direction.|
|-14574|CSS: error processing initialization string: %s.|
|-14575|CSS: invalid run-time parameters.|
|-14576|CSS: null CSS context.|
|-14577|CSS: no registered output buffer owner.|
|-14578|CSS: null output buffer owner.|
|-14579|CSS: unspecified buffer type.|
|-14581|CSS: CSM descriptor: syntax error.|
|-14582|CSS: CSM descriptor: CSM redefinition.|
|-14583|CSS: CSM descriptor: CSM not defined.|
|-14584|CSS: CSM descriptor: link method undefined.|
|-14585|CSS: CSM descriptor: unknown error %s.|
|-14586|CSS: CSM descriptor: nameless CSM!|
|-14587|CSS: CSM descriptor %s: self reference.|
|-14588|CSS: CSM descriptor %s: CSM link type undefined.|
|-14589|CSS: cannot open %s file.|
|-14590|CSS: failed to aquire sync object.|
|-14591|CSS: failed to release sync object.|


## eami  

|ErrCode|Description|
|:---|:---|
|-12800|Unsuspected internal error.|
|12800|Unsuspected internal error.|
|-12801|An attempt was made to invoke an access_method routine that does not exist.|
|12801|An attempt was made to invoke an access_method routine that does not exist.|
|-12802|Error in initializing an access_method routine execution sequence.|
|12802|Error in initializing an access_method routine execution sequence.|
|-12803|Error in executing an access_method routine execution sequence.|
|12803|Error in executing an access_method routine execution sequence.|
|-12804|Error indicated by an access_method routine.|
|12804|Error indicated by an access_method routine.|
|-12805|Improper return value from access_method routine.|
|12805|Improper return value from access_method routine.|
|-12806|Unable to build row descriptor.|
|12806|Unable to build row descriptor.|


## isam  

|ErrCode|Description|
|:---|:---|
|-100|ISAM error:  duplicate value for a record with unique key.|
|100|One of the following applies to your situation:   ISAM error:  duplicate value for a record with unique key.   No matching records found.|
|-101|ISAM error:  file is not open.|
|101|ISAM error:  file is not open.|
|-102|ISAM error:  illegal argument to ISAM function.|
|102|ISAM error:  illegal argument to ISAM function.|
|-103|ISAM error:  illegal key descriptor (too many parts or too long).|
|103|ISAM error:  illegal key descriptor (too many parts or too long).|
|-104|ISAM error:  too many files open.|
|104|ISAM error:  too many files open.|
|-105|ISAM error:  bad isam file format.|
|105|ISAM error:  bad isam file format.|
|-106|ISAM error:  non-exclusive access.|
|106|ISAM error:  non-exclusive access.|
|-107|ISAM error:  record is locked.|
|107|ISAM error:  record is locked.|
|-108|ISAM error:  key already exists.|
|108|ISAM error:  key already exists.|
|-109|ISAM error:  the key is the file's primary key.|
|109|ISAM error:  the key is the file's primary key.|
|-110|ISAM error:  end or beginning of the file.|
|110|ISAM error:  end or beginning of the file.|
|-111|ISAM error:  no record found.|
|111|ISAM error:  no record found.|
|-112|ISAM error:  there is no current record.|
|112|ISAM error:  there is no current record.|
|-113|ISAM error:  the file is locked.|
|113|ISAM error:  the file is locked.|
|-114|ISAM error:  the file name is too long.|
|114|ISAM error:  the file name is too long.|
|-115|ISAM error:  cannot create lock file.|
|115|ISAM error:  cannot create lock file.|
|-116|ISAM error:  cannot allocate memory.|
|116|ISAM error:  cannot allocate memory.|
|-117|ISAM error:  bad custom collating sequence.|
|117|ISAM error:  bad custom collating sequence.|
|-118|ISAM error:  cannot read log record.|
|118|ISAM error:  cannot read log record.|
|-119|ISAM error:  bad log record|
|119|ISAM error:  bad log record|
|-120|ISAM error:  cannot open log file.|
|120|ISAM error:  cannot open log file.|
|-121|ISAM error: cannot write log record|
|121|ISAM error: cannot write log record|
|-122|ISAM error: transaction not available|
|122|ISAM error: transaction not available|
|-123|ISAM error: no shared memory|
|123|ISAM error: no shared memory|
|-124|ISAM error: no begin work yet|
|124|ISAM error: no begin work yet|
|-125|ISAM error: can't use nfs|
|125|ISAM error: can't use nfs|
|-126|ISAM error: bad row id|
|126|ISAM error: bad row id|
|-127|ISAM error: no primary key|
|127|ISAM error: no primary key|
|-128|ISAM error: no logging|
|128|ISAM error: no logging|
|-129|ISAM error: too many users|
|129|ISAM error: too many users|
|-130|ISAM error: no such DBspace|
|130|ISAM error: no such DBspace|
|-131|ISAM error: no free disk space|
|131|ISAM error: no free disk space|
|-132|ISAM error: rowsize too big|
|132|ISAM error: rowsize too big|
|-133|ISAM error: audit trail exists|
|133|ISAM error: audit trail exists|
|-134|ISAM error: no more locks|
|134|ISAM error: no more locks|
|-135|ISAM error: TBLspace does not exist|
|135|ISAM error: TBLspace does not exist|
|-136|ISAM error: no more extents|
|136|ISAM error: no more extents|
|-137|ISAM error: chunk table overflow|
|137|ISAM error: chunk table overflow|
|-138|ISAM error: DBspace table overflow|
|138|ISAM error: DBspace table overflow|
|-139|ISAM error: logfile table overflow|
|139|ISAM error: logfile table overflow|
|-140|ISAM error: operation illegal on a DR Secondary|
|140|ISAM error: operation illegal on a DR Secondary|
|-141|ISAM error: TBLspace table overflow|
|141|ISAM error: TBLspace table overflow|
|-142|ISAM error: overflow of TBLspace page|
|142|ISAM error: overflow of TBLspace page|
|-143|ISAM error: deadlock detected|
|143|ISAM error: deadlock detected|
|-144|ISAM error: key value locked|
|144|ISAM error: key value locked|
|-145|ISAM error: system does not have disk mirroring|
|145|ISAM error: system does not have disk mirroring|
|-146|ISAM error: the other copy of this disk is currently disabled or non-existent|
|146|ISAM error: the other copy of this disk is currently disabled or non-existent|
|-147|ISAM error: archive in progress|
|147|ISAM error: archive in progress|
|-148|ISAM error: DBspace is not empty|
|148|ISAM error: DBspace is not empty|
|-149|ISAM error: GBase Database Server daemon is no longer running|
|149|ISAM error: GBase Database Server daemon is no longer running|
|-150|The limits of the GBase Demo Version have been exceeded.|
|150|The limits of the GBase Demo Version have been exceeded.|
|-151|ISAM error: Illegal value in varchar or varchar2 length field|
|151|ISAM error: Illegal value in varchar or varchar2 length field|
|-152|ISAM error: Illegal message type received from remote process.|
|152|ISAM error: Illegal message type received from remote process.|
|-153|ISAM error: not in ISMANULOCK mode.|
|153|ISAM error: not in ISMANULOCK mode.|
|-154|ISAM error: Lock Timeout Expired|
|154|ISAM error: Lock Timeout Expired|
|-155|ISAM error: Primary and Mirror chunks are bad|
|155|ISAM error: Primary and Mirror chunks are bad|
|-156|ISAM error: Cannot attach to shared memory|
|156|ISAM error: Cannot attach to shared memory|
|-157|ISAM error: Interrupted ISAM call|
|157|ISAM error: Interrupted ISAM call|
|-158|ISAM error: Operation disallowed on SMI pseudo table|
|158|ISAM error: Operation disallowed on SMI pseudo table|
|-159|ISAM error: Collation sequence invalid|
|159|ISAM error: Collation sequence invalid|
|-160|ISAM error: only one blob may be open at any time.|
|160|ISAM error: only one blob may be open at any time.|
|-161|ISAM error: no blob is open.|
|161|ISAM error: no blob is open.|
|-162|ISAM error: BLOBspace does not exist.|
|162|ISAM error: BLOBspace does not exist.|
|-163|ISAM error: begin and end page stamps are different.|
|163|ISAM error: begin and end page stamps are different.|
|-164|ISAM error: Blob stamp is incorrect|
|164|ISAM error: Blob stamp is incorrect|
|-165|ISAM error: Blob Column does not exist.|
|165|ISAM error: Blob Column does not exist.|
|-166|ISAM error: BLOBspace is full|
|166|ISAM error: BLOBspace is full|
|-167|ISAM error: page size is not multiple of system default page size.|
|167|ISAM error: page size is not multiple of system default page size.|
|-168|ISAM error: archive is blocking BLOBpage allocation.|
|168|ISAM error: archive is blocking BLOBpage allocation.|
|-169|ISAM error: BLOB pages can't be allocated from a chunk until chunk add is logged.|
|169|ISAM error: BLOB pages can't be allocated from a chunk until chunk add is logged.|
|-170|ISAM error: Illegal use of a BLOBspace|
|170|ISAM error: Illegal use of a BLOBspace|
|-171|ISAM error:  isam file format change detected|
|171|ISAM error:  isam file format change detected|
|-172|ISAM error:  Unexpected internal error|
|172|ISAM error:  Unexpected internal error|
|-173|ISAM error:  An error has occurred during logical log back up.|
|173|ISAM error:  An error has occurred during logical log back up.|
|-174|ISAM error:  An error has occurred during archive back up.|
|174|ISAM error:  An error has occurred during archive back up.|
|-175|ISAM error:  Cannot get lock while holding a buffer.|
|175|ISAM error:  Cannot get lock while holding a buffer.|
|-176|ISAM error:  An error has occurred during physical restore.|
|176|ISAM error:  An error has occurred during physical restore.|
|-177|ISAM error:  An error has occurred during logical restore.|
|177|ISAM error:  An error has occurred during logical restore.|
|-178|ISAM error:  Database is locked; pending change to logging mode.|
|178|ISAM error:  Database is locked; pending change to logging mode.|
|-179|ISAM error: no free disk space for sort|
|179|ISAM error: no free disk space for sort|
|-180|ISAM error: Shared open blob table is full|
|180|ISAM error: Shared open blob table is full|
|-181|ISAM error: No Optical Subsystem connection|
|181|ISAM error: No Optical Subsystem connection|
|-182|ISAM error: Duplicate optical BLOBspace name|
|182|ISAM error: Duplicate optical BLOBspace name|
|-183|ISAM error:  DDR log post processing is already active|
|183|ISAM error:  DDR log post processing is already active|
|-184|ISAM error: Archive required before altering to a standard table|
|184|ISAM error: Archive required before altering to a standard table|
|-185|ISAM error:  DDR log post processing is not active|
|185|ISAM error:  DDR log post processing is not active|
|-186|ISAM error: Cannot open partition. Online create/drop index in progress.|
|186|ISAM error: Cannot open partition. Online create/drop index in progress.|
|-187|ISAM error: User Defined Routine execution failed|
|187|ISAM error: User Defined Routine execution failed|
|-188|ISAM error:  Cannot add transaction logging on a DR primary with DR on.|
|188|ISAM error:  Cannot add transaction logging on a DR primary with DR on.|
|-190|ISAM error: Transaction table overflow|
|190|ISAM error: Transaction table overflow|
|-191|ISAM error:  No such chunk|
|191|ISAM error:  No such chunk|
|-192|ISAM error:  Cannot drop first chunk|
|192|ISAM error:  Cannot drop first chunk|
|-193|ISAM error:  Chunk is busy|
|193|ISAM error:  Chunk is busy|
|-194|ISAM error:  Chunk not empty|
|194|ISAM error:  Chunk not empty|
|-195|ISAM error:  No miscellaneous vp|
|195|ISAM error:  No miscellaneous vp|
|-196|ISAM error:  Operation not allowed in temporary DBspace.|
|196|ISAM error:  Operation not allowed in temporary DBspace.|
|-197|ISAM error:  Cannot open a recently appended logged partition for writing.|
|197|ISAM error:  Cannot open a recently appended logged partition for writing.|
|-198|ISAM error: Cannot alter table. Too many in-place alters of the table in progress.|
|198|ISAM error: Cannot alter table. Too many in-place alters of the table in progress.|
|-199|ISAM error:  DBSpace is full.|
|199|ISAM error:  DBSpace is full.|
|-7350|Attempt to update a stale version of a row|
|7350|Attempt to update a stale version of a row|
|-7351|Connection between secondary and primary has been lost|
|7351|Connection between secondary and primary has been lost|
|-7352|Operation (%s) can not be run on secondary node|
|7352|Operation (%s) can not be run on secondary node|
|-7353|The transaction cannot continue on the new primary server.|
|7353|The transaction cannot continue on the new primary server.|
|-12215|ISAM error: an invalid address for a text/byte type was intercepted.|
|12215|ISAM error: an invalid address for a text/byte type was intercepted.|
|-12216|ISAM error: attempt to add extended index into a partition whose key descriptors are in 7.x Server format|
|12216|ISAM error: attempt to add extended index into a partition whose key descriptors are in 7.x Server format|
|-12217|Could not add new log. root chunk is almost full|
|12217|Could not add new log. root chunk is almost full|
|-12218|No more new log numbers to allocate|
|12218|No more new log numbers to allocate|
|-12219|Another thread requested READ/WRITE access|
|12219|Another thread requested READ/WRITE access|
|-12220|The request was cancelled while waiting|
|12220|The request was cancelled while waiting|
|-12221|WARNING: Addition of new log appears to be stalled and is not complete.|
|12221|WARNING: Addition of new log appears to be stalled and is not complete.|
|-12222|Cannot Rename a Dbspace while checkpoint is in progress.|
|12222|Cannot Rename a Dbspace while checkpoint is in progress.|
|-12223|Can not Rename dbspace on HDR secondary.|
|12223|Can not Rename dbspace on HDR secondary.|
|-12224|ISAM error: The partition needs to be archived.|
|12224|ISAM error: The partition needs to be archived.|
|-12225|ISAM error: The partition is altered.|
|12225|ISAM error: The partition is altered.|
|-12226|ISAM error: Cannot add dbspace of big page when Large Chunk support is disabled.|
|12226|ISAM error: Cannot add dbspace of big page when Large Chunk support is disabled.|
|-12227|ISAM error: Tape might contain a corrupt page (or) if you are executing onload   command specify the correct DBspace name using the -d argument.|
|12227|ISAM error: Tape might contain a corrupt page (or) if you are executing onload   command specify the correct DBspace name using the -d argument.|
|-12233|ISAM error: Alter in progress on partition.|
|12233|ISAM error: Alter in progress on partition.|
|-12234|ISAM error: Partition has been altered.|
|12234|ISAM error: Partition has been altered.|
|-12235|ISAM error: An online fragment operation is in progress on this table.|
|12235|ISAM error: An online fragment operation is in progress on this table.|
|-21500|RSAM error: Invalid column default value size.|
|21500|RSAM error: Invalid column default value size.|
|-21511|Cannot request more than 1 page for online index build|
|21511|Cannot request more than 1 page for online index build|
|-21512|Exclusive access required to pre-image buffer|
|21512|Exclusive access required to pre-image buffer|
|-21513|Error in online index operation|
|21513|Error in online index operation|
|-21514|Error saving keyp after online index build|
|21514|Error saving keyp after online index build|
|-21515|Cannot perform online index build for attached indices|
|21515|Cannot perform online index build for attached indices|
|-21516|Partially read row|
|21516|Partially read row|
|-21517|Error allocating bufQ for preimage or updator log|
|21517|Error allocating bufQ for preimage or updator log|
|-21518|Error occurred while starting a thread for processing preimage or updator log|
|21518|Error occurred while starting a thread for processing preimage or updator log|
|-21519|No preimage exists|
|21519|No preimage exists|
|-21520|Bad temp partition physaddr|
|21520|Bad temp partition physaddr|
|-21521|More than 1 online index operation is not allowed on the same table|
|21521|More than 1 online index operation is not allowed on the same table|
|-21522|No online index build possible|
|21522|No online index build possible|
|-21523|Cannot proceed with a dirty/modified table data dictionary entry.|
|21523|Cannot proceed with a dirty/modified table data dictionary entry.|
|-21524|Cannot create a temporary operating system file to use in a sort.|
|21524|Cannot create a temporary operating system file to use in a sort.|
|-21525|Cannot write to a temporary operating system file during a sort.|
|21525|Cannot write to a temporary operating system file during a sort.|
|-21526|This log cannot be dropped, because the next log has an open transaction.|
|21526|This log cannot be dropped, because the next log has an open transaction.|
|-21527|ISAM error: The partition could not be created because the dbspace is currently unavailable.|
|21527|ISAM error: The partition could not be created because the dbspace is currently unavailable.|
|32000|XA error: The rollback was caused by an unspecified reason.|
|-32000|XA error: The rollback was caused by an unspecified reason.|
|32001|XA error: The rollback was caused by a communication failure.|
|-32001|XA error: The rollback was caused by a communication failure.|
|32002|XA error: The rollback was caused by a deadlock was detected.|
|-32002|XA error: The rollback was caused by a deadlock was detected.|
|32003|XA error: A condition that violates the integrity of the resources was detected.|
|-32003|XA error: A condition that violates the integrity of the resources was detected.|
|32004|XA error: The Resource Manager rolled back the transaction branch for a reason not on the XA rollback errors.|
|-32004|XA error: The Resource Manager rolled back the transaction branch for a reason not on the XA rollback errors.|
|32005|XA error: A protocol error occurred in the Resource Manager.|
|-32005|XA error: A protocol error occurred in the Resource Manager.|
|32006|XA error: The rollback was caused by a transaction branch took too long.|
|-32006|XA error: The rollback was caused by a transaction branch took too long.|
|32007|XA error: The Resource Manager detected transient error.|
|-32007|XA error: The Resource Manager detected transient error.|
|32009|XA error: Routine returned with no effect and may be re-issued.|
|-32009|XA error: Routine returned with no effect and may be re-issued.|
|32010|XA error: The transaction branch has been heuristically committed and rolled back.|
|-32010|XA error: The transaction branch has been heuristically committed and rolled back.|
|32011|XA error: The transaction branch has been heuristically rolled back.|
|-32011|XA error: The transaction branch has been heuristically rolled back.|
|32012|XA error: The transaction branch has been heuristically committed.|
|-32012|XA error: The transaction branch has been heuristically committed.|
|32013|XA error: The transaction branch may have been heuristically completed.|
|-32013|XA error: The transaction branch may have been heuristically completed.|
|32014|XA error: Resumption must occur where suspension occurred.|
|-32014|XA error: Resumption must occur where suspension occurred.|
|32015|XA error: Asynchronous operation already outstanding.|
|-32015|XA error: Asynchronous operation already outstanding.|
|32016|XA error: A Resource Manager error occurred in the transaction branch.|
|-32016|XA error: A Resource Manager error occurred in the transaction branch.|
|32017|XA error: The XID is not valid.|
|-32017|XA error: The XID is not valid.|
|32018|XA error: Invalid arguments were given.|
|-32018|XA error: Invalid arguments were given.|
|32019|XA error: Routine invoked in improper context.|
|-32019|XA error: Routine invoked in improper context.|
|32020|XA error: Resource Manager unavailable.|
|-32020|XA error: Resource Manager unavailable.|
|32021|XA error: The XID already exists.|
|-32021|XA error: The XID already exists.|
|32022|XA error: Resource Manager doing work outside global transaction.|
|-32022|XA error: Resource Manager doing work outside global transaction.|
|32023|XA error: Error in executing an xadatasource purpose routine execution sequence.|
|-32023|XA error: Error in executing an xadatasource purpose routine execution sequence.|
|32024|XA error: Error indicated by an xadatasource purpose routine.|
|-32024|XA error: Error indicated by an xadatasource purpose routine.|
|32025|XA error: Improper return value from xadatasource purpose routine.|
|-32025|XA error: Improper return value from xadatasource purpose routine.|
|-32026|Savepoint not found.|
|-32027|A savepoint with the same name exists and the UNIQUE option was specified.|
|-32028|Limit on savepoint levels reached.|
|-21528|Defragment: The partition does not require defragmentation|
|-21529|Defragment: Could not find a large enough extent to cover 2 or more extents.|
|-21530|Defragment: Defragmentation is not supported on secondary servers.|
|-21531|Defragment: A partition that contains a partition header page table cannot be defragmented.|
|-21532|Defragment: The partition is in the wrong state or is an incompatible type.|
|-21533|Defragment: Only one instance of the defragmenter may run on a single dbspace|
|-21534|Defragment: Internal error - can't map logical page number|
|-21535|Defragment: Internal error - can't chfree the old extent|
|-21536|Defragment: Internal error - can't have two destination extents|
|-21537|Defragment: You can't run this command while a defragmentation is in progress|
|-21539|Defragment: You can't run this command on catalog/pseudo/temp tables|
|-12246|Smart Large Objects:Can't put temp large object into a permanent table|


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


## nals  

|ErrCode|Description|
|:---|:---|
|-34380|Input stream contains an illegal multi-byte character|
|-34381|Input stream ends in the middle of a valid character|
|-34382|A system error occurred while reading the input stream|
|-34383|An unknown error '%d' occurred while reading the input stream|
|-34388|Invalid character has been found. Cannot continue the processing.|
|-34389|Illegal character has been found in the input string.|
|34521|Convert-All Character Mode|
|34522|Convert-All Character Mode (Even in a comment)|
|34523|Verbose Mode|
|34524|unknown option : %s|
|34525|Creating New File Name from %s|
|34526|Rename from %s to %s|
|34527|Opening renamed file %s|
|34528|In :%s|
|34529|Out:%s|
|34530|%s: Opening original file|
|34531|%s: Opening destination file|
|34532|%s: Pre-processing|
|34533|Unrecoverable error.|
|34534|Usage: %s [-all] [-v] file [file .. ]   %s converts multibyte characters found   in quoted literals into octal format string.   -all     convert all multibyte characters   -v       verbose mode   file     C source file name|
|34535|Wrong file name %s|
|34536|Cannot rename %s to %s|
|34537|An error occurred during preprocessing (errno = %d).|
|34538|Cannot open the file %s|
|34539|Pre-processing failed %s|
|34902|Usage : crctmap  <input-file>  <output-file>|
|34903|Error: Cannot open %s file|
|34904|Error: Syntax error on line %d|
|34905|Warning: Duplicate mapping entry on line %d|
|34906|Error: Error in fwrite()|
|34907|Error: Filename %s is too long (maximum length is %d characters).|
|-34396|Illegal wide character. Line# %d|
|-34395|Illegal multibyte character. Line# %d|
|-34394|Session Initialization failed on bad locale name: %s.|
|-34393|GLS codeset conversion initialization failed.|
|-34390|Invalid delimiter; Don't use '\\', SPACE, HEX or Multibyte chars.|
|34400|Cannot open '%s'; system error %d.|
|34401|Unknown product: %s|
|34402|Unexpected EOF on '%s'.|
|34403|makecr: can't open or create '%s'; system error %d|
|34404|Can't chown '%s'; system error %d|
|34405|Can't chmod '%s'; system error %d|
|34406|cannot set user id|
|34407|owner must be root or gbasedbt|
|34408|usage: rinstall owner mode dir file-list|
|34409|%s must be a directory|
|34410|getgrgid() failed|
|34411|%s must be owned by group rds or gbasedbt|
|34412|Unknown Error %d|
|34413|isam error %d|
|34414|Fork failed|
|34415|Program not found.|
|34416|Program over.|
|34417|Cannot run filename: %s|
|34418|Cannot save filename: %s|
|34419|%s saved successfully.|
|34420|RDSQL Structured Query Language|
|34421|Please retype the command.|
|34422|The execute file '%s' could not be opened. The file   probably does not exist.|
|34423|Please select a database using the database command.   usage: database dbname|
|34424|Command aborted|
|34426|INSERT|
|34427|------|
|34428|This C-ISAM has a bad serial number.|
|34429|This program has an invalid serial number.   Please consult your installation instructions.|
|34541|t_alloc failed|
|34542|t_optmgmt failed; TO_NODELAY.|
|34543|t_optmgmt failed; TO_NODELACK.|
|34544|t_optmgmt failed; TO_KEEPALIVE.|
|34566|Unable to start SQL engine|
|34567|Failed to stat chunk '%s', errno=%d|
|34568|Fcntl failed in Async Chunk Initialization '%s', fd=%d, errno=%d|
|34569|Memory Lock failed in Async Chunk Initialization '%s', errno=%d|
|34572|allocpage:warning pagenum (%d) > npused (%d)|
|34573|allocpage: partp (%lx), partnum (%lx)|
|34575|allocrow:warning pagenum (%d) > npused (%d)|
|34576|allocrow: partp (%lx), partnum (%lx)|
|34577|allocslot(no room) - partnum 0x%x tr_pagenum 0x%x|
|34578|allocslot(no room) - maxslots %d slotsize %d|
|34582|bitmap is wrong!|
|34583|allocvrow:warning pagenum (%d) > npused (%d)|
|34584|allocvrow: partp (%lx), partnum (%lx)|
|34585|newmode: Invalid page type of 0x%x|
|34586|Slot %d not free in page %x in partnum %x|
|34609|bfget(After wait) - bf_pagenum %x != pagenum %x|
|34610|userp %lx pid %d|
|34613|ERROR - bfput(BF_MODIFY) not in Critical Section!!!   us %x pid %d|
|34614|bad request|
|34615|I/O %s chunk %d, pagenum %ld, pagecnt %d|
|34616|GBASEDBT-OnLine Must ABORT   Root chunk and root mirror down.|
|34617|GBASEDBT-OnLine Must ABORT   Root chunk down.|
|34618|ERROR - Physical logging not in Critical Section!!!   us %x pid %d|
|34620|Physical log file overflow|
|34621|Overflow OK if restore completes successfully|
|34622|If restore fails, do a full restore from backup|
|34623|GBASEDBT-OnLine Must ABORT   Physical log flush write error   us 0x%x pid %d us_flags 0x%x   plog 0x%x pl_phybegin 0x%x pl_physize %d pl_phypos 0x%x|
|34627|I/O error 'lseek': expect %ld actual %ld addr 0x%lx errno %d retrys %d|
|34628|I/O error 'read': expect %d actual %d addr 0x%lx errno %d retrys %d|
|34629|I/O error 'write': expect %d actual %d addr 0x%lx errno %d retrys %d|
|34630|I/O - retry successful; addr 0x%lx retrys %d|
|34631|I/O error, %s Chunk '%s' -- Offline|
|34636|delrecord: bad rowid %lx partnum %lx pid %d|
|34637|Failed to stat chunk '%s' (%d), errno=%d|
|34638|Unchain chunk '%s'|
|34639|Unchained chunk '%s'|
|34640|Warning: Failed to unchain chunk '%s' (%d)|
|34641|Bad page address (%x) on chunk '%s' %d %x|
|34642|ERROR: page cleaner # %d has timed out|
|34643|Some dirty buffers not written! diskcnt=%d writes=%d notflsh=%d|
|34644|Not all writes to bufs are done! nwrite=%d ndone=%d|
|34645|Not all aio done! asyncwrite=%d asyncfin=%d|
|34646|Cannot execute gtrid_cmp -- No TP monitor available|
|34647|Cannot execute gtrid_fmt -- No TP monitor available|
|34648|Cannot execute gtrid_hash -- No TP monitor available|
|34649|Cannot execute gtrid_reg -- No TP monitor available|
|34650|Cannot execute gtrid_rmid -- No TP monitor available|
|34651|Cannot execute gtrid_unreg -- No TP monitor available|
|34652|Optical Subsystem STARTUP Error|
|34653|GBASEDBT-OnLine entering ABORT mode!!!|
|34654|GBASEDBT-OnLine automatically rebooting after abort|
|34655|Aborting Long Transaction: tx 0x%lx %lx|
|34656|Unable to abort transaction: tx 0x%lx %lx|
|34657|Continuing Long Transaction (for COMMIT):  tx 0x%lx %lx|
|34658|Optical Subsystem CLEANUP Error|
|34659|tbundo died pid=%d|
|34660|tbundo died pid=%ld|
|34661|Can't fork to create tbundo errno=%ld|
|34662|GBASEDBT-OnLine Copyright(C) 1986, 1987  GBasedbt Software, Inc.|
|34663|%s (critical section): pid=%d user=%d flags=%lx|
|34664|%s (latch): pid=%d user=%d flags=%lx|
|34665|%s (commit): tx=%lx flags=%lx|
|34666|%s (rollback): tx=%lx flags=%lx|
|34667|Insufficient resources for index change rollback (partnum = %ld, keynum = %d)|
|34668|Lock table overflow - user id %d, process id %d|
|34669|ERROR - NO 'waitfor' locks in Critical Section!!!|
|34670|logput() - not in critical section|
|34671|ERROR:  logput() - type %d len %d|
|34672|logput() - not in transaction|
|34673|logput() - logwrite() FAILED|
|34674|logput() - logsetup() FAILED|
|34675|logput() - Unknown|
|34676|logflush() - logwrite() FAILED|
|34677|Attempt to write %d pages from a %d page buffer!!|
|34678|Attempt to write pages %d - %d to a %d page logfile|
|34679|Attempt to write page %d to a %d page logfile|
|34680|error on log write, buf %8lx, physaddr %8ld, npages %4d|
|34681|logsetup() - Overwrite log|
|34682|Logical Log Files are Full -- Backup is Needed|
|34683|logread() - logsearch() FAILED|
|34684|logread() - Invalid page addr|
|34685|logread() - bfget() FAILED|
|34686|logread:bad log page|
|34687|ERROR:  logread() - loguniq %ld logpos 0x%lx|
|34688|GBASEDBT-OnLine Must ABORT   Log Error '%s'   us 0x%x pid %d us_flags 0x%x   tx 0x%x tx_flags 0x%x tx_loguniq %d tx_logpos 0x%x|
|34689|%s: log buffer overflow|
|34690|Dbspace '%s' now has mirror|
|34691|Dbspace '%s' now has no mirror|
|34692|Chunk number %d '%s' -- Offline|
|34693|Cannot Perform Checkpoint|
|34694|Can Not Open Primary Chunk %s|
|34695|Can Not Open Mirror Chunk %s|
|34696|DBSpace '%s' -- Recovery Failed - can't fork|
|34697|DBSpace '%s' -- Recovery Begins(%d)|
|34698|DBSpace '%s' -- Recovery Complete(%d)|
|34699|DBSpace '%s' -- Recovery Failed(%d)|
|34700|Chunk number %d '%s' -- Recovery Failed - can't fork|
|34701|Chunk number %d '%s' -- Recovery Complete(%d)|
|34702|Chunk number %d '%s' -- Recovery Failed(%d)|
|34703|Chunk Number %d - '%s' -- Recovery Begins(%d)|
|34704|Chunk Number %d - '%s' -- Online|
|34705|Chunk number %d '%s' -- Recovery Aborted Due to Signal|
|34706|Chunk number %d '%s' -- Recovery Failed|
|34707|The next Log file is USED and is NOT backed up.|
|34708|Forced Logical log buffer flush|
|34710|%s (endtx): tx=%lx flags=%lx   user %s tty %s|
|34711|Bombing out in btdelitem() - pid %d|
|34712|Bombing out in btadditem() - pid %d iserrno %d|
|34713|Bombing out in btsplit() - pid %d|
|34714|Item not found for delete|
|34715|Bombing out in btcompress() - pid %d|
|34717|Bombing out in btmerge() - pid %d|
|34718|Bombing out in btshuffle() - pid %d|
|34719|Empty B-tree node %x Unable to do CopyBack|
|34723|fatal pgcompress error: pid = %d, uid = %d|
|34726|Come get me %d|
|34729|Empty B-tree node %x; Unable to do CopyBack|
|34730|ERROR - ispsclose: failed PSU_TST() USERP 0x%x partp 0x%x|
|34731|ERROR - isenter: failed - PSU_TST userp 0x%x partp 0x%x|
|34737|ERROR IN DUMPOCT|
|34738|call to ptmap() from ptbld() failed|
|34740|tmap: bad pagenum = %ld -- only %ld pages|
|34741|ptmap: bad extent number %ld -- only %ld extents|
|34742|ptmap failure: userp = %lx, pid = %ld|
|34744|TBLSpace table overflow - user id %d, process id %d|
|34745|ERROR - ptifree: failed OPN_TST() USERP 0x%x partp 0x%x|
|34746|call to ptmap() from ptphysaddr() failed|
|34756|tblspace header error:|
|34758|Cannot Open Mirror Chunk '%s', errno = %d|
|34759|Cannot Open Primary Chunk '%s', errno = %d|
|34765|read_record: deleted rowid = %lx, partnum = %lx|
|34766|read_record: invalid rowid = %lx, partnum = %lx|
|34767|Checkpoint waiting on us %x pid %d us_flags %x|
|34768|recommit() - logread() FAILED|
|34769|cannot recreate index -- partnum = %lx, keynum = %d|
|34771|relock() - malloc failed|
|34772|relock() - logread failed|
|34773|relock() - isenter failed|
|34774|relock() - pntorsfd failed|
|34775|relock() - kysearch failed|
|34776|relock() - btsearch failed|
|34777|relock() - dotablocks failed|
|34778|find_gtrid() - malloc failed|
|34779|find_gtrid() - logread failed|
|34780|Called from %s|
|34781|Optical Subsystem SHUTDOWN Error|
|34782|User table overflow - user id %d, process id %d|
|34783|Transaction table overflow - user id %d, process id %d|
|34784|ioctl, get mappable size: unreasonable parameters|
|34785|ioctl, get mappable size: error|
|34786|ioctl, set mappable size: unreasonable parameter values|
|34787|ioctl, set mappable size: no permission|
|34788|ioctl, set mappable size: unit just mapped|
|34789|ioctl, set mappable size: EINVAL|
|34790|ioctl, set mappable size: error|
|34791|Not enough shared memory for TREELATCHs|
|34795|Initialization|
|34796|Quiescent|
|34797|Fast Recovery|
|34798|Archive Backup|
|34799|Shutting Down|
|34800|On-Line|
|34801|Abort|
|34802|Unknown|
|34803|(CKPT REQ)|
|34804|(CKPT INP)|
|34805|(LONGTX)|
|34806|-- Up %d days %02d:%02d:%02d -- %d Kbytes|
|34807|-- Up %02d:%02d:%02d -- %d Kbytes|
|34808|Message Log File: %s|
|34809|Configuration File: %s|
|34810|Latches with lock or user set|
|34811|Latches with lock or user set or average Q len > 0.1|
|34812|All top level Latches, plus locked/user set or Q len > 0.1|
|34814|Users|
|34815|address   flags       latch    lock    buff    ckpt   clean   lgbuf   other|
|34816|address  wtlist   owner    lklist   same     type     tblsnum  rowid    size|
|34817|total events|
|34818|total time (secs)|
|34819|%d active, %d total|
|34820|address  flags   pid     user     tty      wait     tout locks nreads   nwrites|
|34821|Locks|
|34822|address  wtlist   owner    lklist   type     tblsnum  rowid    size|
|34823|%d active, %d total, %d hash buckets|
|34824|Buffers|
|34825|address  user     flgs pagenum  memaddr  nslots pgflgs xflgs owner    waitlist|
|34826|address  flgs pagenum  pflgs puts     avqlen maxqlen  waits|
|34827|address  flgs pagenum  pflgs puts     avqlen maxqlen  waits    avwt     maxwt|
|34828|%d modified, %d total, %d hash buckets, %d buffer size|
|34829|%d buffer LRU queues|
|34830|LRU %2d: %4d (%4.1f%%) modified of %4d total|
|34831|%d dirty, %d queued, %d total, %d hash buckets, %d buffer size|
|34832|start clean at %d%% dirty, stop at %d%%|
|34833|Tblspaces|
|34834|n address  flgs ucnt tblnum   physaddr npages nused  npdata nrows  nextns|
|34835|Roving allocation pointers (top) and sizes (bottom) - lapagepn: %.x|
|34836|Dbspaces|
|34837|address  number   flags    fchunk   nchunks  flags    owner    name|
|34838|Chunks|
|34839|address  chk/dbs offset   page Rd  page Wr   pathname|
|34840|address  chk/dbs offset   size     free     bpages   flags pathname|
|34841|Physical Logging|
|34842|Buffer bufused  bufsize  numpages numwrits pages/io|
|34843|phybegin physize  phypos   phyused  %%used|
|34844|Logical Logging|
|34845|Buffer bufused  bufsize  numrecs  numpages numwrits recs/pages pages/io|
|34846|address  number   flags    uniqid   begin        size     used    %%used|
|34847|address  flusher  snooze   state    data|
|34848|states: Exit Idle Chunk Near Lru|
|34849|states: Exit Idle Chunk Lru|
|34850|Profile|
|34851|BIGreads|
|34852|dskreads pagreads bufreads %%cached dskwrits pagwrits bufwrits %%cached|
|34853|isamtot  open     start    read     write    rewrite  delete   commit   rollbk|
|34854|ovtbls   ovlock   ovuser   ovbuff   usercpu  syscpu   numckpts flushes|
|34855|bufwaits lokwaits lockreqs deadlks  dltouts  lchwaits ckpwaits compress|
|34856|Trace Info|
|34857|type stamp    time     userp    dat1     dat2     dat3     dat4 dat5|
|34858|Trace buffer size = %d, trace flags = 0x%lx|
|34859|Unable to create output file '%s'|
|34860|Error writing '%s' errno=%d|
|34861|Unable to open input file '%s'|
|34862|Error reading '%s' errno=%d|
|34863|malloc error (cnt %d) errno=%ld|
|34864|Index statistics|
|34865|search   additem  delitem  retry|
|34866|splits   page     slot     root     copyback|
|34867|compress merges   shuffles root|
|34868|Buffers (Access)|
|34869|address  owner    flags pagenum  memaddr   nslots pgflgs sharers  waiter|
|34870|NOTRANS|
|34871|DIRTY|
|34872|COMMIT|
|34873|CURSOR|
|34874|REPEAT|
|34875|UNKNOWN|
|34876|ERROR - flalloc: partnum (0x%x) != pt_partnum (0x%x)|
|34877|ERROR - flalloc: failed OPN_TST() userp 0x%x partp 0x%x|
|34878|ERROR - flalloc: failed PSU_TST() using USERP = 0x%x  partp = 0x%x|
|34879|ERROR - flfree: failed - fl_ocount <= 0, userp 0x%x partp 0x%x|
|34880|ERROR - flfree: failed - PSU_TST userp 0x%x partp 0x%x|
|34881|rollback() - logread() FAILED|
|34882|rollback() - logundo() FAILED|
|34883|ERROR: logundo(%d) iserrno %d us 0x%x pid %d   tx 0x%x loguniq %d logpos 0x%x|
|34884|ERROR - pntorsfd: failed - PSU_TST userp 0x%x partp 0x%x|
|34885|ERROR - pntorsfd: partp is NULL openp (0x%lx) op_filep (0x%lx)|
|34886|ERROR - pntorsfd: fl_partnum (0x%lx) != partnum (0x%lx)|
|34887|ERROR - pntorsfd: failed OPN_TST userp (0x%lx) op_partp (0x%lx)|
|34889|slotdelete: bad rowid = %lx, partnum = %lx|
|34890|sprback() - logread() FAILED|
|34891|sprback() - logundo() FAILED|
|34893|tx_offwtlist() - userp %x not on wait list - txp %x|
|34894|The -l flag has not been implemented. Sorry!|
|34895|%s: cannot create stream for %s|
|34896|%s: location %D is incorrect for %s|
|34897|%s: identify string not found in %s|
|34898|%s: identifier string multiply found in %s|
|34899|%s: cannot open %s|
|34900|Write to file failed.|
|34901|%s: usage: %s file1 file2 ...|
|34908|Invalid Type in value: %hd|
|34909|ERROR: in SQ_DBLIST.|
|34910|Index into string table.: %d|
|34911|Starting offset in tuple: %hd|
|34912|ERROR: Invalid msg type: %hd (0x%x).|
|34913|ERROR: Read too far.|
|34914|ERROR: Invalid file format.|
|34915|SQLIDBG Version %ld|
|34916|Usage: %s [ -tuple ] [ -o outfile ] [ inpfile ]|
|34917|Specify 'inpfile' OR set environment variable %s.|
|34918|Invalid syntax for %s environment variable.|
|34919|Init|
|34920|Recovery|
|34921|Backup|
|34922|Shutdown|
|34923|Off-Line|
|34924|I/O %s chunk %d, pagenum %ld, pagecnt %d|
|34925|slot %d (%d,%d) overlaps page header or slot table %d|
|34926|slot %d overlaps adjacent slot|
|34927|BLOBSpace Report for %s:%s.%s|
|34928|Total pages used by table	       %8d|
|34929|Page Size is %5d      %6d|
|34930|BLOBSpace usage:|
|34931|Space          Page                         Percent Full|
|34932|Name           Number      Pages   0-25%  26-50%  51-75%  76-100%|
|34933|WARNING: %s|
|34935|error code is %d|
|34936|Level %d Archive Started %s|
|34937|Level %d Archive Completed %s|
|34938|Level %d Archive Cancelled|
|34939|Logical Log %d Backed Up|
|34940|No legal checkpoint page|
|34941|No log pages on the archive tape|
|34942|OOPS, looks like the wrong tape|


## net  

|ErrCode|Description|
|:---|:---|
|-27000|Cannot support multiple connections over shared memory.|
|-27001|Read error occurred during connection attempt.|
|-27002|No connections are allowed in quiescent mode.|
|-27003|Internal Communications Error: internal inconsistency detected.|
|-27004|Illegal sqlhosts file option/parameter.|
|-27005|Illegal sqlexecd daemon option,%s.|
|-27006|Network driver cannot establish listen endpoint.|
|-27007|Invalid file descriptor openned for the user thread.|
|-27008|Invalid database server name.|
|-27009|None of the server in group is in primary or standard mode.|
|-27010|Only an administrative user can connect in administrative user mode.|
|-27100|Internal Communications Error: NSF subsystem error.|
|-27151|Internal error: No CSM specification string defined in sqlhosts.|
|-27152|Internal error: CSS context already exists; cannot create another context.|
|-27153|Internal error: CSS context is null.|
|-27154|Internal error: Invalid ASF_TIMEOUT semantics; same input buffer expected.|
|-27155|Internal error: CSS returned an undefined css_status.state code|
|-27156|Internal error: Invalid ASF-CSS state.|
|-27157|Internal error: No receive buffer available.|
|-27200|Invalid AM-API parameters.|
|-27201|There are no more serviceable connection handles.|
|-27202|Agent Messaging protocol error.|
|-27203|Event Handler is not registered on peer.|
|-27204|Event Handler is not registered locally.|
|-27205|Connect Event Handler is not registered locally for this service handle.|
|-27206|Disconnect Event Handler is not registered locally for this service handle.|
|-27207|Reply Event Handler is not registered locally for this service handle.|
|-27208|Exception Event Handler is not registered locally for this service handle.|
|-27209|Event Handler is not registered locally for this listen service handle.|
|-27210|Internal Agent Messaging versioning error.|
|-28001|Cannot become a multi-level server|
|-28002|Could not turn on extended security operations|
|-28003|Internal Error: Failed to create attribute buffer|
|-28004|m6last_attr failed|
|-28005|Failed to get sensitivity label from client|
|-28006|Internal Error:NON_M6_ATTRS_OK environment variable not found.|
|-28007|Attributes not received from MaxSix. Client could be non-m6|
|-28008|Users's session level is not dominated by its clearance.|
|-28009|Users session or clearance has an invalid label.|
|-28010|Error occured while reading users clearance file.|
|-28011|Access denied as session level does not have clearance for host.|
|-28012|Error occured while reading tnet file.|
|-28013|New users not allowed on secondary server.|
|-28014|Secure Sockets Layer error: %s.|
|-28015|Secure Sockets Layer configuration error.|
|-28016|GBASE Global Security Kit (GSKit) %s or higher is not installed.|
|-28021|Trusted context not defined or enabled for the specified authorization ID.|
|-28022|Trusted context encryption requirement was not satisfied.|
|-29000|Application Server error (%s).|
|+29001|Application Server warning (%s).|
|-29002|Supplied real-RDB-name does not match the real-RDB-name in sqlhosts.|
|-29003|RDB (%s) not found at DRDA server.|
|-29004|DRDA protocol error. ReplyMsg[,sub-code]: %s.|
|-29005|Hard DRDA protocol error. ReplyMsg[,sub-code]: %s.|
|-29006|DRDA connect protocol error. Manager,level: (%s) not supported.|
|-29007|RDB authorization failure. RDB-userID,RDB: %s.|
|-29008|DDM parameter (%s) not supported error. Disconnected from AS.|
|-29009|DDM parameter value (%s) not supported. Disconnected from AS.|
|-29010|AS reply message (codepoint=%s) not supported by the Gateway.|
|-29011|SNA communication error. GBase-SQLCODE,native-SNA-rc: %s.|
|-29012|One or more tables have been dropped, altered, or renamed.|
|-29013|AS resource not available. Reason,Type,Name,PrdID,RDB: %s.|
|-29014|Hard AS resource not available. Reason,Type,Name,PrdID,RDB: %s.|
|-29015|Non-bind related DDM command (codepoint=%s) attempted during bind.|
|-29016|Bind related command (codepoint=%s) encountered when bind not active.|
|-29017|Package owner authorization failure.|
|-29018|AS does not support the DDM command: %s.|
|-29019|AS does not support the DDM object type: %s.|
|-29028|Error parsing the parmlist string for procedure (%s).|
|-29029|Limit for maximum number of rows exceeded.|
|-29030|Feature (%s) not supported by the Gateway.|
|-29031|Table or view name (%s) has an invalid format.|
|-29032|Application Server CCSIDs could not be determined.|
|-29033|GBase GLS locale could not be loaded: %s.|
|-29034|Character codeset conversion error. Tokens: %s.|
|-29035|An incompatible data type was received by the Gateway.|
|-29036|Character codeset conversion file not found from,to,filename: %s.|
|-29037|There is no CCSID or GLS locale set for the FE OS locale (%s).|
|+29038|AS cannot support the mix/double-byte CCSIDs (%s).|
|-29039|Cannot have more than one SQL statement in PREPARE/EXECUTE IMMEDIATE.|
|-29040|Cannot translate the MATCHES pattern (%s) to a LIKE pattern.|
|-29041|Application Server does not support ESCAPE clause in the LIKE predicate.|
|-29042|Gateway cannot find package information for RDB (%s).|
|-29043|No more %s sections left. Rebind packages with more sections.|
|-29044|Gateway internal error (%s).|
|-29045|Gateway internal error (%s). Disconnected from AS.|
|-29046|SNA buffer size (%s) is not valid.|
|-29047|Error accessing catalog information for procedure (%s).|
|-29048|ISAM Error %s|
|-29049|Unable to locate/open Gateway setup file (%s).|
|-29050|Error accessing schema information (%s).|
|-29051|Only single-site updates allowed in a transaction.|
|-29052|Gateway cannot access the remote data source named %s.|
|-29053|Collection missing in the reference to object %s.|
|-29054|Gateway internal pseudo-error (%s).|
|-29055|DDL statements are not allowed on a remote object.|
|-29056|Gateway cannot rollback savepoint (%s).|
|-29057|Gateway does not support remote aliases (%s).|
|-29058|Incorrect number of arguments passed to procedure (%s).|
|-29059|Argument datatype incompatible for procedure (%s).|
|-29060|EDA error (%s).|
|+29061|EDA warning (%s).|
|-29062|An EDA Client or Server prompt was received.|
|-29063|Output data description changed between prepare and execute.|
|-29064|Unknown EDA datatype received.|
|-29065|Input host variables not allowed in EXECUTE PROCEDURE.|
|-29066|Password required in .netrc entry for '%s'.|
|-29067|Could not access EDALINK.CFG file (%s).|
|-29068|A field value received from the EDA Server could not be decoded.|
|-29069|Invalid argument specification for procedure (%s).|
|-29070|Package isolation level does not match for (%s).|
|-29071|Gateway cannot find package information for package (%s).|
|-29080|Target DBMS Error (%s).|
|-29081|ODBC Error (%s).|
|-29082|Could not decode field value for field number %s.|
|-29083|Compatible isolation level not supported by the data source.|
|-29084|Write access is not permitted to data source.|
|-29085|Cursor hold is not supported by the data source.|
|-29086|Operating System Error (%s).|
|-29087|Network protocol communication error. GBase-SQLCODE,native-protocol-rc: %s.|
|-29088|Communication buffer size (%s) is not valid.|
|-29089|RDB password required when client user('%s') is not authenticated by Gateway.|


## netsrv  

|ErrCode|Description|
|:---|:---|
|-25599|Network connection error - no listener.|
|-25598|Communications usage error: invalid state transition.|
|-25597|Error in system pipe processing.|
|-25596|The GBASEDBTSERVER value is not listed in the sqlhosts file or the Registry.|
|-25595|Invalid message received during connection attempt.|
|-25594|Shared Memory client failed to alert the database server for service.|
|-25593|Network listener failed to make an open I/O channel to be non-blocking.|
|-25592|Communications service not supported by network driver.|
|-25591|Transport control received an invalid connection address.|
|-25590|Authentication error.|
|-25589|Invalid database server mail-box message type.|
|-25588|The appl process cannot connect to the database server %s.|
|-25587|Network receive failed.|
|-25586|Network send failed.|
|-25585|Invalid buffer size.|
|-25584|Network driver cannot access the server program %s.|
|-25583|Unknown network error.|
|-25582|Network connection is broken.|
|-25581|Transport Layer memory free error.|
|-25580|System error occurred in network function.|
|-25579|Network function was issued in the wrong sequence.|
|-25578|Network driver cannot disconnect from the network.|
|-25577|Network driver cannot get a host structure.|
|-25576|Network driver cannot allocate the return structure.|
|-25575|Network driver cannot allocate the call structure.|
|-25574|Network driver cannot open the network device.|
|-25573|Network driver cannot accept a connection on the port.|
|-25572|Network driver cannot bind a name to the port.|
|-25571|Cannot create a user thread.|
|-25570|Network driver cannot execute the fork system call.|
|-25569|SQL protocol level negotiation error.|
|-25568|Debugging utility error.|
|-25567|Internal communications buffer management error detected.|
|-25566|System time error.|
|-25565|Cannot get process information.|
|-25564|Feature or function unsupported.|
|-25563|Invalid ASF API input parameters.|
|-25562|Could not construct Name Service registry.|
|-25561|Invalid authentication type.|
|-25560|Environment variable GBASEDBTSERVER must be set.|
|-25559|DBPATH server %s is not listed as a dbserver name in sqlhosts.|
|-25558|The NFS/RFS host %s is not listed as a dbserver name in sqlhosts.|
|-25557|Network internal error.|
|-25556|Invalid sqlhosts file format.|
|-25555|Server %s is not listed as a dbserver name in sqlhosts.|
|-25554|GBASEDBTSERVER environment variable too long.|
|-25553|Sqlhosts file not found or cannot be opened.|
|-25552|Service already in progress.|
|-25551|Invalid service ID.|
|-25550|ASF_INIT of RECOVER attempted with undefined state.|
|-25549|Invalid ASF API level.|
|-25548|Too many active connections.|
|-25547|ASF_INIT service not invoked.|
|-25546|Invalid ASF assoc_id.|
|-25545|Invalid operation mode.|
|-25539|Invalid connection-type.|
|-25540|The esqlauth.dll has refused your connection.|
|25500|The sqlexecd daemon is not licensed for remote use.|
|25501|The sqlexecd daemon must be started by root.|
|25502|The sqlexecd daemon cannot execute the fork system call.|
|25503|GBasedbt network support is not available in this version.|
|25504|The sqlexecd daemon cannot open a socket.|
|25505|The sqlexecd daemon cannot bind a name to the socket.|
|25506|The sqlexecd daemon cannot accept a connection on the socket.|
|25507|The specified service name or protocol is unknown.|
|25508|%s %s %s %s|
|25509|*?*|
|25510|The database engine %s could not be started by execv, system errno %d|
|25511|The sqlexecd daemon could not receive data from client.|
|25512|The database engine program cannot be accessed.|
|25513|sqlsrvlog|
|25514|The sqlexecd daemon cannot open the log file.|
|25515|Too many arguments were passed to the sqlexecd daemon.|
|25516|check_rights %s %s %s|
|25517|trusted host %s user %s|
|25518|Unknown network type specified in DBNETTYPE. Assuming STARLAN.|
|25519|The sqlexecd daemon cannot open the network device.|
|25520|The sqlexecd daemon cannot allocate the call structure.|
|25521|The sqlexecd daemon cannot allocate the return structure.|
|25522|The sqlexecd daemon cannot allocate the call structure.|
|25523|The sqlexecd daemon cannot bind the network structures.|
|25524|Listening for connections for %d. . .|
|25525|bind_ret->qlen = %d|
|25526|The sqlexecd daemon cannot listen on the network device.|
|25527|Call request received|
|25528|The sqlexecd daemon cannot accept a connection.|
|25529|The sqlexecd daemon cannot get a host structure.|
|25530|The sqlexecd daemon cannot bind to the required port address.|
|25531|The sqlexecd daemon cannot bind to the required address.|
|25532|The sqlexecd daemon cannot disconnect the network.|
|25533|The sqlexecd daemon cannot close the network.|
|25534|The sqlexecd daemon cannot allocate a structure.|
|25535|Address translation failed in sqlexecd daemon.|
|25536|connecting . . .|
|25537|The sqlexecd daemon cannot connect to network|
|25538|connected . . .|
|25539|tlook %d - %s|
|25540|listen|
|25541|unknown|
|25542|Binding the local name ...|
|25543|The specified service name or protocol is unknown.|
|25544|The sqlexecd daemon cannot get a host structure.|
|25545|The sqlexecd daemon cannot advertise the specified service name.|
|25546|client %s died, net address: %s|
|25547|not magic|
|25548|net abort called from file %s, line %d|
|25549|invalid comand %d|
|25550|bad net data structure found|
|25551|%s len:%d seq:%d session:%d kind:%s buf:|
|25552|...more...|
|25553|out of sync, t_sync required|
|25554|state fd %d: %s -  %d: %s|
|25555|uninitialized|
|25556|unbound|
|25557|idle|
|25558|outgoing connection pending|
|25559|incoming connection pending|
|25560|data transfer|
|25561|outgoing release pending|
|25562|incoming release pending|
|25563|unknown state|
|25564|max number of poll threads already running|
|25565|net_init failed|
|25566|out of memory|
|25567|parameter error|
|25568|no poll thread available|
|25569|max number of listen threads already running|
|25570|Host name not found in /etc/hosts|
|25571|Internal error - data structure|
|25572|Not in correct state for operation|
|25573|Message with zero length found|
|25574|service name not specified|
|25575|connection rejected - too many users|
|25576|REQUESTS in ONCONFIG greater than %d|
|25577|Listen thread terminating abnormally|
|25578|bad shm buffer id|
|25579|shm wait queue corrupted|
|25580|shm semaphore failure|
|25581|shm wrong buffer status|
|25582|shm creation of shmem segment failed|
|25583|shm bad address|
|25584|shm event on pipe failed|
|25585|shm thread wakeup failed|
|25586|failure, system out of semaphores|
|25587|could not create shm file '%s'|
|25588|could not open shm file|
|25589|application not linked with tli libs|
|25590|no communication system running system terminated|
|25591|could not get shm message buffer|
|25592|net_sm_write has failed|
|25593|sockets error - registering a file|
|25594|sockets error - updating nsf table|
|25595|Internal Error: Please contact and inform following messages to   Technical Support:|
|25596|Usage: %s dbservername [-s object] [-d object path] [-l log file]   [-f logfile_size] [-b [userid]]|
|25597|%s: ASF_Init(ASF_INIT) failed|
|25598|%s: defInitParms failed|


## optical  

|ErrCode|Description|
|:---|:---|
|-7000|Error 7000 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7000|Error 7000 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7001|Error 7001 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7001|Error 7001 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7002|Error 7002 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7002|Error 7002 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7003|Error 7003 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7003|Error 7003 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7004|Error 7004 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7004|Error 7004 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7005|Error 7005 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7005|Error 7005 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7006|Error 7006 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7006|Error 7006 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7007|Error 7007 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7007|Error 7007 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7008|Error 7008 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7008|Error 7008 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7009|Error 7009 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7009|Error 7009 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7010|Error 7010 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7010|Error 7010 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7011|Error 7011 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7011|Error 7011 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7012|Error 7012 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7012|Error 7012 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7013|Error 7013 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7013|Error 7013 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7014|Error 7014 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7014|Error 7014 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7015|Error 7015 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7015|Error 7015 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7016|Error 7016 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7016|Error 7016 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7017|Error 7017 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7017|Error 7017 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7018|Error 7018 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7018|Error 7018 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7019|Error 7019 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7019|Error 7019 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7020|Error 7020 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7020|Error 7020 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7021|Error 7021 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7021|Error 7021 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7022|Error 7022 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7022|Error 7022 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7023|Error 7023 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7023|Error 7023 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7024|Error 7024 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7024|Error 7024 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7025|Error 7025 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7025|Error 7025 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7026|Error 7026 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7026|Error 7026 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7027|Error 7027 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7027|Error 7027 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7028|Error 7028 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7028|Error 7028 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7029|Error 7029 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7029|Error 7029 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7030|Error 7030 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7030|Error 7030 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7031|Error 7031 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7031|Error 7031 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7032|Error 7032 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7032|Error 7032 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7033|Error 7033 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7033|Error 7033 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7034|Error 7034 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7034|Error 7034 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7035|Error 7035 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7035|Error 7035 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7036|Error 7036 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7036|Error 7036 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7037|Error 7037 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7037|Error 7037 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7038|Error 7038 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7038|Error 7038 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7039|Error 7039 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7039|Error 7039 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7040|Error 7040 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7040|Error 7040 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7041|Error 7041 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7041|Error 7041 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7042|Error 7042 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7042|Error 7042 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7043|Error 7043 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7043|Error 7043 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7044|Error 7044 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7044|Error 7044 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7045|Error 7045 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7045|Error 7045 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7046|Error 7046 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7046|Error 7046 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7047|Error 7047 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7047|Error 7047 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7048|Error 7048 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7048|Error 7048 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7049|Error 7049 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7049|Error 7049 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7050|Error 7050 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7050|Error 7050 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7051|Error 7051 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7051|Error 7051 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7052|Error 7052 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7052|Error 7052 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7053|Error 7053 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7053|Error 7053 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7054|Error 7054 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7054|Error 7054 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7055|Error 7055 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7055|Error 7055 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7056|Error 7056 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7056|Error 7056 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7057|Error 7057 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7057|Error 7057 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7058|Error 7058 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7058|Error 7058 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7059|Error 7059 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7059|Error 7059 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7060|Error 7060 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7060|Error 7060 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7061|Error 7061 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7061|Error 7061 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7062|Error 7062 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7062|Error 7062 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7063|Error 7063 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7063|Error 7063 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7064|Error 7064 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7064|Error 7064 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7065|Error 7065 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7065|Error 7065 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7066|Error 7066 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7066|Error 7066 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7067|Error 7067 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7067|Error 7067 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7068|Error 7068 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7068|Error 7068 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7069|Error 7069 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7069|Error 7069 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7070|Error 7070 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7070|Error 7070 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7071|Error 7071 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7071|Error 7071 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7072|Error 7072 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7072|Error 7072 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7073|Error 7073 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7073|Error 7073 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7074|Error 7074 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7074|Error 7074 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7075|Error 7075 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7075|Error 7075 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7076|Error 7076 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7076|Error 7076 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7077|Error 7077 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7077|Error 7077 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7078|Error 7078 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7078|Error 7078 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7079|Error 7079 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7079|Error 7079 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7080|Error 7080 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7080|Error 7080 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7081|Error 7081 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7081|Error 7081 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7082|Error 7082 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7082|Error 7082 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7083|Error 7083 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7083|Error 7083 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7084|Error 7084 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7084|Error 7084 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7085|Error 7085 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7085|Error 7085 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7086|Error 7086 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7086|Error 7086 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7087|Error 7087 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7087|Error 7087 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7088|Error 7088 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7088|Error 7088 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7089|Error 7089 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7089|Error 7089 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7090|Error 7090 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7090|Error 7090 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7091|Error 7091 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7091|Error 7091 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7092|Error 7092 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7092|Error 7092 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7093|Error 7093 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7093|Error 7093 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7094|Error 7094 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7094|Error 7094 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7095|Error 7095 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7095|Error 7095 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7096|Error 7096 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7096|Error 7096 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7097|Error 7097 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7097|Error 7097 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7098|Error 7098 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7098|Error 7098 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7099|Error 7099 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7099|Error 7099 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7100|Error 7100 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7100|Error 7100 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7101|Error 7101 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7101|Error 7101 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7102|Error 7102 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7102|Error 7102 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7103|Error 7103 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7103|Error 7103 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7104|Error 7104 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7104|Error 7104 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7105|Error 7105 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7105|Error 7105 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7106|Error 7106 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7106|Error 7106 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7107|Error 7107 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7107|Error 7107 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7108|Error 7108 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7108|Error 7108 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7109|Error 7109 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7109|Error 7109 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7110|Error 7110 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7110|Error 7110 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7111|Error 7111 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7111|Error 7111 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7112|Error 7112 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7112|Error 7112 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7113|Error 7113 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7113|Error 7113 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7114|Error 7114 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7114|Error 7114 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7115|Error 7115 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7115|Error 7115 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7116|Error 7116 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7116|Error 7116 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7117|Error 7117 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7117|Error 7117 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7118|Error 7118 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7118|Error 7118 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7119|Error 7119 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7119|Error 7119 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7120|Error 7120 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7120|Error 7120 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7121|Error 7121 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7121|Error 7121 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7122|Error 7122 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7122|Error 7122 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7123|Error 7123 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7123|Error 7123 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7124|Error 7124 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7124|Error 7124 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7125|Error 7125 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7125|Error 7125 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7126|Error 7126 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7126|Error 7126 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7127|Error 7127 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7127|Error 7127 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7128|Error 7128 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7128|Error 7128 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7129|Error 7129 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7129|Error 7129 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7130|Error 7130 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7130|Error 7130 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7131|Error 7131 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7131|Error 7131 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7132|Error 7132 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7132|Error 7132 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7133|Error 7133 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7133|Error 7133 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7134|Error 7134 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7134|Error 7134 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7135|Error 7135 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7135|Error 7135 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7136|Error 7136 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7136|Error 7136 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7137|Error 7137 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7137|Error 7137 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7138|Error 7138 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7138|Error 7138 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7139|Error 7139 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7139|Error 7139 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7140|Error 7140 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7140|Error 7140 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7141|Error 7141 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7141|Error 7141 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7142|Error 7142 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7142|Error 7142 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7143|Error 7143 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7143|Error 7143 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7144|Error 7144 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7144|Error 7144 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7145|Error 7145 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7145|Error 7145 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7146|Error 7146 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7146|Error 7146 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7147|Error 7147 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7147|Error 7147 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7148|Error 7148 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7148|Error 7148 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7149|Error 7149 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7149|Error 7149 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7150|Error 7150 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7150|Error 7150 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7151|Error 7151 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7151|Error 7151 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7152|Error 7152 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7152|Error 7152 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7153|Error 7153 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7153|Error 7153 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7154|Error 7154 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7154|Error 7154 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7155|Error 7155 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7155|Error 7155 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7156|Error 7156 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7156|Error 7156 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7157|Error 7157 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7157|Error 7157 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7158|Error 7158 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7158|Error 7158 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7159|Error 7159 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7159|Error 7159 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7160|Error 7160 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7160|Error 7160 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7161|Error 7161 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7161|Error 7161 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7162|Error 7162 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7162|Error 7162 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7163|Error 7163 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7163|Error 7163 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7164|Error 7164 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7164|Error 7164 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7165|Error 7165 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7165|Error 7165 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7166|Error 7166 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7166|Error 7166 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7167|Error 7167 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7167|Error 7167 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7168|Error 7168 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7168|Error 7168 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7169|Error 7169 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7169|Error 7169 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7170|Error 7170 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7170|Error 7170 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7171|Error 7171 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7171|Error 7171 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7172|Error 7172 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7172|Error 7172 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7173|Error 7173 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7173|Error 7173 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7174|Error 7174 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7174|Error 7174 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7175|Error 7175 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7175|Error 7175 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7176|Error 7176 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7176|Error 7176 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7177|Error 7177 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7177|Error 7177 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7178|Error 7178 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7178|Error 7178 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7179|Error 7179 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7179|Error 7179 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7180|Error 7180 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7180|Error 7180 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7181|Error 7181 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7181|Error 7181 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7182|Error 7182 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7182|Error 7182 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7183|Error 7183 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7183|Error 7183 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7184|Error 7184 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7184|Error 7184 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7185|Error 7185 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7185|Error 7185 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7186|Error 7186 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7186|Error 7186 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7187|Error 7187 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7187|Error 7187 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7188|Error 7188 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7188|Error 7188 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7189|Error 7189 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7189|Error 7189 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7190|Error 7190 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7190|Error 7190 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7191|Error 7191 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7191|Error 7191 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7192|Error 7192 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7192|Error 7192 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7193|Error 7193 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7193|Error 7193 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7194|Error 7194 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7194|Error 7194 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7195|Error 7195 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7195|Error 7195 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7196|Error 7196 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7196|Error 7196 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7197|Error 7197 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7197|Error 7197 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7198|Error 7198 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7198|Error 7198 from the optical subsystem.   Consult your appropriate subsystem manual.|
|-7199|Error 7199 from the optical subsystem.   Consult your appropriate subsystem manual.|
|7199|Error 7199 from the optical subsystem.   Consult your appropriate subsystem manual.|


## os  

|ErrCode|Description|
|:---|:---|
|1|Not owner|
|2|No such file or directory|
|3|No such process|
|4|Interrupted system call|
|5|I/O error|
|6|No such device or address|
|7|Arg list too long|
|8|Exec format error|
|9|Bad file number|
|10|No children|
|11|No more processes|
|12|Not enough core|
|13|Permission denied|
|14|Bad address|
|15|Block device required|
|16|Mount device busy|
|17|File exists|
|18|Cross-device link|
|19|No such device|
|20|Not a directory|
|21|Is a directory|
|22|Invalid argument|
|23|File table overflow|
|24|Too many open files|
|25|Not a typewriter|
|26|Text file busy|
|27|File too large|
|28|No space left on device|
|29|Illegal seek|
|30|Read-only file system|
|31|Too many links|
|32|Broken pipe|
|33|Argument too large|
|34|Result too large|
|35|Operation would block|
|36|Operation now in progress|
|37|Operation already in progress|
|38|Socket operation on non-socket|
|39|Destination address required|
|40|Message too long|
|41|Protocol wrong type for socket|
|42|Option not supported by protocol|
|43|Protocol not supported|
|44|Socket type not supported|
|45|Operation not supported on socket|
|46|Protocol family not supported|
|47|Address family not supported by protocol family|
|48|Address already in use|
|49|Can't assign requested address|
|50|Network is down|
|51|Network is unreachable|
|52|Network dropped connection on reset|
|53|Software caused connection abort|
|54|Connection reset by peer|
|55|No buffer space available|
|56|Socket is already connected|
|57|Socket is not connected|
|58|Can't send after socket shutdown|
|59|Too many references: can't splice|
|60|Connection timed out|
|61|Connection refused|
|62|Too many levels of symbolic links|
|63|File name too long|
|64|Host is down|
|65|Host is unreachable|
|66|Directory not empty|
|67|Too many processes|
|68|Too many users|
|69|Disc quota exceeded|
|70|Stale NFS file handle|
|71|Too many levels of remote in path|
|72|Not a stream device|
|73|Timer expired|
|74|Out of stream resources|
|75|No message of desired type|
|76|Not a data message|
|77|Identifier removed|
|78|Deadlock situation detected/avoided|
|79|No record locks available|
|-1|Not owner|
|-2|No such file or directory|
|-3|No such process|
|-4|Interrupted system call|
|-5|I/O error|
|-6|No such device or address|
|-7|Arg list too long|
|-8|Exec format error|
|-9|Bad file number|
|-10|No children|
|-11|No more processes|
|-12|Not enough core|
|-13|Permission denied|
|-14|Bad address|
|-15|Block device required|
|-16|Mount device busy|
|-17|File exists|
|-18|Cross-device link|
|-19|No such device|
|-20|Not a directory|
|-21|Is a directory|
|-22|Invalid argument|
|-23|File table overflow|
|-24|Too many open files|
|-25|Not a typewriter|
|-26|Text file busy|
|-27|File too large|
|-28|No space left on device|
|-29|Illegal seek|
|-30|Read-only file system|
|-31|Too many links|
|-32|Broken pipe|
|-33|Argument too large|
|-34|Result too large|
|-35|Operation would block|
|-36|Operation now in progress|
|-37|Operation already in progress|
|-38|Socket operation on non-socket|
|-39|Destination address required|
|-40|Message too long|
|-41|Protocol wrong type for socket|
|-42|Option not supported by protocol|
|-43|Protocol not supported|
|-44|Socket type not supported|
|-45|Operation not supported on socket|
|-46|Protocol family not supported|
|-47|Address family not supported by protocol family|
|-48|Address already in use|
|-49|Can't assign requested address|
|-50|Network is down|
|-51|Network is unreachable|
|-52|Network dropped connection on reset|
|-53|Software caused connection abort|
|-54|Connection reset by peer|
|-55|No buffer space available|
|-56|Socket is already connected|
|-57|Socket is not connected|
|-58|Can't send after socket shutdown|
|-59|Too many references: can't splice|
|-60|Connection timed out|
|-61|Connection refused|
|-62|Too many levels of symbolic links|
|-63|File name too long|
|-64|Host is down|
|-65|Host is unreachable|
|-66|Directory not empty|
|-67|Too many processes|
|-68|Too many users|
|-69|Disc quota exceeded|
|-70|Stale NFS file handle|
|-71|Too many levels of remote in path|
|-72|Not a stream device|
|-73|Timer expired|
|-74|Out of stream resources|
|-75|No message of desired type|
|-76|Not a data message|
|-77|Identifier removed|
|-78|Deadlock situation detected/avoided|
|-79|No record locks available|
|32765|Cannot open file '%s'.|
|32766|Unknown error message %d.|


## rds  

|ErrCode|Description|
|:---|:---|
|1200|Sun|Mon|Tue|Wed|Thu|Fri|Sat||
|1201|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec||
|1202|Press RETURN to continue.|
|1203|Cannot find message file.  Check GBASEDBTDIR and DBLANG.|
|1204|The type of your terminal is unknown to the system.|
|1205|128-173|
|1206|January|February|March|April|May|June||
|1207|July|August|September|October|November|December||
|1290|Environment variable %s is too long (maximum is %d characters).|
|1291|Command line argument %s is too long (maximum is %d characters).|
|-1200|Number is too large for a DECIMAL data type|
|-1201|Number is too small for a DECIMAL data type|
|-1202|An attempt was made to divide by zero.|
|-1203|Values used in a MATCH must both be type CHARACTER|
|-1204|Invalid year in date|
|-1205|Invalid month in date|
|-1206|Invalid day in date|
|-1207|Converted value does not fit into the allotted space|
|-1208|There is no conversion from non-character values to character values|
|-1209|Without any delimiters, this date must contain exactly 6 or 8 digits|
|-1210|Date could not be converted to month/day/year format|
|-1211|Out of memory|
|-1212|Date conversion format must contain a month, day, and year component|
|-1213|A character to numeric conversion process failed|
|-1214|Value exceeds limit of SMALLINT precision|
|-1215|Value exceeds limit of INTEGER precision|
|-1216|Illegal exponent|
|-1217|The format string is too large|
|-1218|String to date conversion error|
|-1219|Numeric value from database is too large for COBOL data item.|
|-1220|Numeric value from database is too small for COBOL data item.|
|-1221|Cannot convert null data types.|
|-1222|Value will not fit in a SMALLFLOAT.|
|-1223|Value will not fit in a FLOAT.|
|-1224|Invalid decimal number|
|-1225|Column does not admit a NULL value.|
|-1226|Decimal or money value exceeds maximum precision.|
|-1227|Message file not found|
|-1228|Message number not found in message file|
|-1229|Incompatible message file|
|-1230|Bad message file name formulation|
|-1231|Cannot seek within message file|
|-1232|Message buffer too small|
|-1233|Invalid hour, minute, or second|
|-1234|Function may be applied only to datetime data types|
|-1235|Character host variable is too short for the data.|
|-1236|Invalid era, could not assign era date|
|-1237|Specified era is not defined|
|-1238|Failed to initialize era information from locale|
|-1239|Specified era year overflows range of era|
|-1250|Unable to create pipes.|
|-1251|Unable to create shared memory. semget failed.|
|-1252|Unable to create shared memory. shmget failed.|
|-1254|Unable to connect to remote host.|
|-1257|Operating system cannot fork process for back end.|
|-1258|Cannot attach to shared memory used to communicate with back end.|
|-1260|It is not possible to convert between the specified types.|
|-1261|Too many digits in the first field of datetime or interval or timestamp with time zone.|
|-1262|Non-numeric character in datetime or interval or timestamp with time zone.|
|-1263|A field in a datetime or interval or timestamp with time zone value is incorrect or an illegal operation specified on datetime field.|
|-1264|Extra characters at the end of a datetime or interval or timestamp with time zone.|
|-1265|Overflow occurred on a datetime or interval or timestamp with time zone operation.|
|-1266|Intervals or datetimes or timestamp with time zone are incompatible for the operation.|
|-1267|The result of a datetime computation is out of range.|
|-1268|Invalid datetime or interval or timestamp with time zone qualifier.|
|-1269|Locator conversion error.|
|-1270|Interval literal may not have embedded minus sign|
|-1271|Missing decimal point in datetime or interval fraction.|
|-1272|No input buffer has been specified.|
|-1273|Output buffer is NULL or too small to hold the result.|
|-1274|No output buffer has been specified.|
|-1275|Invalid field width or precision in datetime or interval format string.|
|-1276|Format conversion character not supported.|
|-1277|Input does not match format specification.|
|-1278|Invalid escape sequence.|
|-1279|Value exceeds string column length.|
|-1280|Library API incompatibility found in libgen.so.|
|-1281|Library API incompatibility found in libos.so.|
|-1282|Library API incompatibility found in libsql.so.|
|-1283|Library API incompatibility found in libgls.so.|
|-1284|Value will not fit in a BIGINT or an INT8.|
|-1285|Internal error: data type unknown.|
|-1286|Invalid value for environment variable : %s.|
|-1290|Environment variable %s is too long.|
|1292|The error %d has been encountered %ld times since it was last printed to the log.|


## sblob  

|ErrCode|Description|
|:---|:---|
|-12000|Smart Large Objects: Cannot add entry to lofd table.|
|-12001|Smart Large Objects: Cannot add entry to lohd table.|
|-12002|Smart Large Objects: Cannot add entry to sbspace table.|
|-12003|Smart Large Objects: Cannot add entry to chunkadj table.|
|-12004|Smart Large Objects: Cannot add entry to arcreg table.|
|-12005|Smart Large Objects: Cannot add entry to arcspace table.|
|-12006|Smart Large Objects: Cannot add smart large object to truncation Q.|
|-12007|Smart Large Objects: Cannot add smart large object to delete Q.|
|-12008|Smart Large Objects: Cannot delete entry in lofd table.|
|-12009|Smart Large Objects: Cannot delete entry in lohd table.|
|-12010|Smart Large Objects: Cannot delete entry in sbspace table.|
|-12011|Smart Large Objects: Cannot delete entry in chunkadj table.|
|-12012|Smart Large Objects: Cannot delete entry in arcrec table.|
|-12013|Smart Large Objects: Cannot delete entry in arcspace table.|
|-12014|Smart Large Objects: Cannot find entry in lofd table.|
|-12015|Smart Large Objects: Cannot find entry in lohd table.|
|-12016|Smart Large Objects: Cannot find entry in sbspace table.|
|-12017|Smart Large Objects: Cannot find entry in chunkadj table.|
|-12018|Smart Large Objects: Cannot find entry in arcrec table.|
|-12019|Smart Large Objects: Cannot find entry in arcspace table.|
|-12020|Smart Large Objects: Cannot unlock table entry.|
|-12021|Smart Large Objects: Duplicate keys not allowed|
|-12022|Smart Large Objects: Duplicate entry in chunk adjtab|
|-12023|Smart Large Objects: chunk size is too small|
|-12024|Smart Large Objects: Chunked dropped from spspace.|
|-12025|Smart Large Objects: Chunk not empty.|
|-12026|Smart Large Objects: Cannot delete smart large object.|
|-12027|Smart Large Objects: Cannot delete SB_LOHD_SLOT.|
|-12028|Smart Large Objects: Cannot delete SB_LOMAP_SLOT.|
|-12029|Smart Large Objects: Cannot delete SB_USERDATA_SLOT.|
|-12030|Smart Large Objects: Cannot release memory buffer.|
|-12031|Smart Large Objects: Sbspace is full.|
|-12032|Smart Large Objects: Table is full.|
|-12033|Smart Large Objects: Cannot insert SB_LOHD_SLOT.|
|-12034|Smart Large Objects: Invalid buffer size.|
|-12035|Smart Large Objects: Invalid lock type.|
|-12036|Smart Large Objects: Invalid sbspace name.|
|-12037|Smart Large Objects: Invalid seek position.|
|-12038|Smart Large Objects: Invalid access time flag combination.|
|-12039|Smart Large Objects: Invalid whence value for seek.|
|-12040|Smart Large Objects: Invalid truncate value for size.|
|-12041|Smart Large Objects: Size of smart large object or buffer is too big.|
|-12042|Smart Large Objects: Size of page is too big.|
|-12043|Smart Large Objects: Invalid create flags.|
|-12044|Smart Large Objects: Invalid integrity type flag combination.|
|-12045|Smart Large Objects: Invalid logging mode combination.|
|-12046|Smart Large Objects: Cannot enter critical section.|
|-12047|Smart Large Objects: sb_lo_map_offs failed.|
|-12048|Smart Large Objects: unique ID does not match. Smart large object probably   deleted.|
|-12049|Smart Large Objects: No memory.|
|-12050|Smart Large Objects: dbm_bfget: Cannot get a memory buffer.|
|-12051|Smart Large Objects: Smart large object was not opened for read.|
|-12052|Smart Large Objects: Smart large object was not opened for write.|
|-12053|Smart Large Objects: No sbspace number specified.|
|-12054|Smart Large Objects: Cannot open chunk adj partition.|
|-12055|Smart Large Objects: Cannot open smart-large-object header partition.|
|-12056|Smart Large Objects: Cannot open sbspace.|
|-12057|Smart Large Objects: Cannot open sbspace description partition.|
|-12058|Smart Large Objects: Cannot read chunk adjunct entry.|
|-12059|Smart Large Objects: open failed at read of smart-large-object header.|
|-12060|Smart Large Objects: Cannot read SB_LOMAP_SLOT.|
|-12061|Smart Large Objects: Cannot read user data.|
|-12062|Smart Large Objects: Error in user data free list.|
|-12063|Smart Large Objects: Cannot update SB_LOHD_SLOT.|
|-12064|Smart Large Objects: Cannot update SB_LOMAP_SLOT.|
|-12065|Smart Large Objects: Cannot update optimization data.|
|-12066|Smart Large Objects Archive: Cannot build pre-image temporary partition.|
|-12067|Smart Large Objects Archive: Cannot extend pre-image temporary partition.|
|-12068|Smart Large Objects Archive: Cannot drop pre-image temporary partition during   archive.|
|-12069|Smart Large Objects Archive: Cannot write pre-image page to temporary   partition.|
|-12070|Smart Large Objects Archive: Cannot read pre-image page from temporary   partition.|
|-12071|Smart Large Objects Archive: During restore a page write failed.|
|-12072|Smart Large Objects: Not implemented.|
|-12073|Smart Large Objects Archive: Archive already active on sbspace.|
|-12074|Smart Large Objects: Free extension list overflow.|
|-12075|Smart Large Objects Archive: Cannot delete arch rec table.|
|-12076|Smart Large Objects Archive: Cannot create arch space table.|
|-12077|Smart Large Objects Archive: Unexpected exit condition.|
|-12078|Smart Large Objects Archive: Illegal level specified for archiving.|
|-12079|Smart Large Objects: Cannot decrement zero reference count.|
|-12080|Smart Large Objects Archive: Page is outside user data area.|
|-12081|Smart Large Objects Archive: illegal control page type in arc|
|-12082|Smart Large Objects Archive: invalid state encountered|
|-12083|Smart Large Objects: Restore: END_DESC record found before SB_ARC_CHUNK_RECS   record|
|-12084|Smart Large Objects: Restore: NULL control info block ptr; archive records out   of order|
|-12085|Smart Large Objects: Restore: SB_ARC_END_DESC record not found for this chunk.|
|-12086|Smart Large Objects: open: invalid open flags detected at smart-large-object   open time.|
|-12087|Smart Large Objects: alter: attempt to change physical characteristics of a   smart large object in sb_alter|
|-12088|Smart Large Objects: create: number of estimate bytes < -1|
|-12089|Smart Large Objects: create: size limit of smart large object < -1|
|-12090|Smart Large Objects: create: invalid column parameters|
|-12091|Smart Large Objects: the in-memory sbspace table doesn't exist|
|-12092|Smart Large Objects: sbspace exists but is currently down|
|-12093|Smart Large Objects: archive failed to create a mutex and aborted|
|-12094|Smart Large Objects: bad temporary partition page number|
|-12095|Smart Large Objects: create: Invalid Ext. size (kbytes) Ext. size < -1 or > MAXINT.|
|-12096|Smart Large Objects: alter: New size limit < number of bytes in the smart   large object.|
|-12097|Smart Large Objects: open: Bad smart-large-object address. Object might have   been deleted.|
|-12098|Smart Large Objects: Sbspace corrupted.|
|-12099|Smart Large Objects: Archiver found a smart large object with a corrupted   header.|
|-12100|Smart Large Objects: A bad value was entered for the sbpage unit.|
|-12101|Smart Large Objects: A bad value was entered for the average   smart-large-object size|
|-12102|Smart Large Objects: A bad Meta Data Area was entered for thesmart large   object.|
|-12103|Smart Large Objects: Attempt to open a non-sbspace as an sbspace.|
|-12104|Smart Large Objects: Inconsistent LO map was encountered.|
|-12105|Smart Large Objects: An attempt to change the sbspace name was made.|
|-12106|Smart Large Objects: An inconsistent LO extent map was encountered - see   system log.|
|-12108|Smart Large Objects: The requested database Server version conversion is not   available in smart large objects.|
|-12109|Smart Large Objects: The database Server version conversion failed to convert   the sbspace.|
|-12110|Smart Large Objects: This internal code indicates that we couldn't find an LO   extent of the requested length.|
|-12111|Smart Large Objects: Attempt to write to a smart large object without closing   light IO scan.|
|-12112|Smart Large Objects: Conversion from using buffers to light IO not allowed.|
|-12113|Smart Large Objects: Attempt to convert from using light IO to buffers while   LO is open|
|-12114|Smart Large Objects: Archive start is not called before building extent lists.|
|-12115|Smart Large Objects: The LO header page is a wrong length - probably corrupted.|
|-12116|Smart Large Objects: The smart-large-object header is corrupt or an invalid   LO handle was encountered.|
|-12117|Smart Large Objects: The smart-large-object header is corrupt - detected   during delete of LO.|
|-12118|Smart Large Objects: The smart large object's extent map is corrupt. It should   contain 'SBLM' in the first 4 bytes.|
|-12119|Smart Large Objects: The database Server reversion failed in the   smart-large-object subsystem.|
|-12120|Smart Large Objects: Duplicate key encountered in sbspace create.|
|-12121|Smart Large Objects: The sbspace is flagged as dropped.|
|-12122|Smart Large Objects: A drop of the sbspace chunk is already occurring.|
|-12123|Smart Large Objects: The metadata area in the sbspace is full.|
|-12124|Smart Large Objects: The archive preimage partition doesn't exist.|
|-12125|Smart Large Objects: End of smart-large-object headers.|
|-12126|Smart Large Objects: LO is not opened for byte range locking.|
|-12127|Smart Large Objects: Invalid range size in byte range lock / unlock call.|
|-12128|Smart Large Objects: Invalid offset in byte range lock / unlock call.|
|-12129|Smart Large Objects: Failed to create condition variable in smart-large-object   open call.|
|-12130|Smart Large Objects: Failed to create chunk because someone else is also   creating one.|
|-12131|Smart Large Objects: Metadata area in the chunk contains data.|
|-12132|Smart Large Objects: Invalid lock type for lock merge.|
|-12133|Smart Large Objects: During the creation of the sbspace, the desc partition   wasn't the first in the sbspace.|
|-12134|Smart Large Objects: During creation of the sbspace, the sbspace desc record   was not the first in the partition.|
|-12135|Smart Large Objects: Cannot initialize the smart-large-object subsystem.|
|-12136|Smart Large Objects: Informational warning - internal only - the entry is valid.|
|-12137|Smart Large Objects: The sbspace entry has been removed while we were using it.|
|-12138|Smart Large Objects: You can't specify write, light I/O and byte range locking.|
|-12141|Smart Large Objects: you cannot open sbspace when sbspace is not fully   recovered|
|-12142|Smart Large Objects: invalid sbspace number.|
|-12143|Smart Large Objects: invalid chunk number.|
|-12144|Smart Large Objects: warning - space is allocated in the chunk.|
|-12146|General Table Manager: No mvkey routine is defined for this table.|
|-12201|Smart Large Objects: The LO reference count is not zero|
|-12202|Smart Large Objects: The LO open count is not zero|
|-12203|Smart Large Objects: Cannot add LO to delete undo queue|
|-12204|RSAM error: Long transaction detected.|
|-12205|Smart Large Objects: No free disk space while extending the temp archive   preimage partition|
|-12206|Smart Large Objects: LO header table in memory is corrupt|
|-12207|Smart Large Objects: Invalid use of a temporary smart large object space|
|-12208|Smart Large Objects: Lofd is a remote object - this is a warning message only|
|-12209|Smart Large Objects: Internal error: can't find the SCB for the transaction|
|-12210|Smart Large Objects: the file descriptor table for smart large objects is full|
|-12211|Smart Large Objects: the file descriptor table in smart large objects corrupt|
|-12212|Smart Large Objects: parallel thread in same transaction changed file descriptor|
|-12213|Smart Large Objects: LO_LOGMETADATA flag set without LO_NOBUFFER|
|-12214|Smart Large Objects: smart large object space specified in onconfig is temporary|
|-12240|Changed Data Capture: Generic Read Error.|
|-12241|Changed Data Capture: The attempted operation is not supported.|
|-12242|Changed Data Capture: The CDC session must be closed.|
|-12243|Changed Data Capture: Read size smaller than minimum allowed.|
|-12244|Changed Data Capture: Object in incorrect state for attempted operation.|
|-12245|Changed Data Capture: Memory corruption detected.|
|-12246|Smart Large Objects:Can't put temp large object into a permanent table|
|-12247|Smart Large Objects: Processing failed because of an invalid buffer size from the client|


## security  

|ErrCode|Description|
|:---|:---|
|-21400|%s: Invalid serial number and/or key.|
|-21401|%s: Cannot open file -- %s probably not in current directory.|
|-21402|%s: Location %D is incorrect for %s|
|-21403|%s: %s already branded.|
|-21404|%s: Identifier string multiply found in %s|
|-21405|%s: Serial number is wrong length in %s|
|-21406|%s: Cannot open %s|
|-21407|Error Reading from File|
|-21408|Error Writing to File|
|-21409|infgen: Invalid SQL serial number|
|-21410|%s: Cannot create stream for %s|
|-21411|%s: Identify string not found in %s|
|-21412|%s: Warning: string found %d times in %s.|
|-21413|Cannot open '%s'; system error %d.|
|-21414|Unexpected EOF on '%s'.|
|-21415|subsuffix string was not fully processed '%s'.|
|21400|** Verify serial number and key values; restart installation procedure.|
|21401|** Please type carefully.|
|21402|%s: usage: %s [-p] [-s serialnum key] [-c cmeSN] file1 file2 ...|
|21403|%s: Identifier string found at %D in %s|
|21404|usage: %s serialnum key|
|21405|The -l flag has not been implemented. Sorry!|
|21406|%s: usage: %s file1 file2 ...|
|21407|usage: { %s [-p] [-s serialnum key] [-c cmeSN] file ... |   %s { -r DT_RPATH | -t } file }|
|21408|%s: The file %s is either not a Linux ELF file, or the ELF header is corrupt. Rerun the command and specify an ELF file.|
|21409|%s: The ELF file %s does not contain a DT_RPATH tag. You cannot add this tag.|
|21410|%s: Cannot change the DT_RPATH tag in %s to the specified value. Specify a new value that is shorter than the existing value.|


## shell  

|ErrCode|Description|
|:---|:---|
|-33400|Usage: %s <error/message number> arguments|
|-33401|The demo script would not run if GBASEDBTSERVER is not set.|
|33401|DBACCESS  Demonstration Database Installation Script|
|33402|Dropping existing %s database ....|
|33403|Creating %s database ....|
|33404|Loading data ...|
|33405|The creation of the demonstration database is now complete.  The remainder   of this script copies the examples into your current directory.   Press 'Y' to continue, or 'N' to abort.|
|33406|Now copying SQL command files ....|
|33407|End of DBACCESSDEMO script.|
|33408|Sorry, unrecognized option %s|
|33409|Sorry, database name must begin with a letter.|
|33410|Usage: %s  [dbname] [-log] [-dbspace] [DBspace] [-nots]|
|-33412|esql: file name required with -log|
|-33413|esql:   When using -thread, the THREADLIB environment variable   must be set to a supported thread library. Currently   supporting: DCE, POSIX(HP-UX 11.0, Solaris 2.5 and higher only) and   SOL (Solaris Kernel Threads).|
|-33414|esql:	Option -o requires an argument.|
|-33415|esql:   illegal output file suffix %s.|
|-33416|Usage: ifx_getversion [product_name | library_name]   where [product_name | library_name] is:   clientsdk   esql   dmi | libdmi   libcli[.a|.so]   libgls[.a|.so]   libos[.a|.so]   libasf[.a|.so]   libsql[.a|.so]   libgen[.a|.so]|
|-33417|Named product/library %s does not exist.|
|33421|GBASEDBT Embedded SQL/COBOL Demonstration Database Installation Script|
|33422|This script will create and populate a database named: %s .   If a database of that name exists, the script will drop and replace it.   If you do not own or have DBA privilege for an existing database %s,   the script will try to drop it and fail.  In that event, run the script   again specifying a different database name.|
|33423|This script will create and populate a database named: %s .   If a database of that name exists now in the current directory, the script   will drop and replace it.   If you do not own or have DBA privilege for an existing database %s,   the script will try to drop it and fail.  In that event, run the script   again either with a different current directory or specifying a different   database name.|
|33424|To continue, press return|
|33425|Dropping existing %s database ....|
|-33426|Unable to drop existing %s database.|
|33427|Creating %s database ...|
|-33428|Database setup incomplete.|
|33429|Based on the server information in sqlhosts, the database engine   does not support the data types varchar, varchar2, text and byte, so the   table 'catalog' has not been installed.|
|33430|Now installing indexes on loaded tables...|
|33431|The creation of the demonstration database is now complete.  The remainder   of this script copies the examples into your current directory.   Press 'Y' to continue, or 'N' to abort.|
|33432|Now copying GBase-ESQL/COBOL program source files ....|
|33433|End of GBase-ESQL/COBOL Demonstration Database Installation script.|
|-33441|Usage: esqlcobol [-n] [-e] [-esqlargs] [-otherargs]   [-native] [-o outfile] esqlfile.eco [otherobj.o...]   -n         Display preprocessor and compilation steps   -e         Preprocess only, no compilation or linking   -esqlargs  esqlcob arguments (-esqlout, -t type, -Ipathname, -bigB, -w,   -V, -ansi, -xopen, -local, -log file,   -EDname, -EUname, -icheck)   -native    Generate native code   -o         Next argument is program name (compiler-specific)|
|-33442|ERROR: Invalid COBOL compiler type|
|-33443|%s: Only one '*.cob' file allowed as input.|
|-33444|%s: Only one '*.cbl' file allowed as input.|
|-33445|%s: Only one '*.eco' file allowed as input.|
|-33446|esqlcobol: file name required with -log|
|-33447|You must set GBASEDBTCOBTYPE before running this script|
|-33448|ESQL/COBOL preprocessor error detected, skipping compile|
|-33449|You must set GBASEDBTCOB before running this script|
|33451|GBASEDBT Embedded SQL/C Demonstration Database Installation Script|
|33452|This script will create and populate a database named: %s .   If a database of that name exists, the script will drop and replace it.   If you do not own or have DBA privilege for an existing database %s,   the script will try to drop it and fail.  In that event, run the script   again specifying a different database name.|
|33453|This script will create and populate a database named: %s .   If a database of that name exists now in the current directory, the script   will drop and replace it.   If you do not own or have DBA privilege for an existing database %s,   the script will try to drop it and fail.  In that event, run the script   again either with a different current directory or specifying a different   database name.|
|33454|To continue, press return|
|33455|Dropping existing %s database ....|
|-33456|Unable to drop existing %s database.|
|33457|Creating %s database ...|
|-33458|Database setup incomplete.|
|33459|Based on the server information in sqlhosts, the database engine   does not support the data types varchar, varchar2, text and byte, so the   table 'catalog' has not been installed.|
|33460|Now installing indexes on loaded tables...|
|33461|The creation of the demonstration database is now complete.  The remainder   of this script copies the examples into your current directory.   Press 'Y' to continue, or 'N' to abort.|
|33462|Now copying GBase-ESQL/C program source files ....|
|33463|End of GBase-ESQL/C Demonstration Installation script.|
|-33471|Usage: infxserver [-bldsvrargs] [esqlfile.ec] [esqlfile.eco]   [othersrc.cob] [othersrc.cbl]   -bldsvrargs  buildserver arguments|
|-33481|You must first set GBASEDBTCOBDIR|
|-33482|You must first set GBASEDBTCOBTYPE|
|-33483|ERROR: Invalid COBOL compiler type|
|33484|Y|
|33485|y|
|-33487|Usage: esql [-e] [-thread] [-glu] [esqlcargs] [-cc] [otherargs] [-o outfile]   [-cp] [-onlycp] [-np] [-nup]   [-libs] esqlfile.ec [othersrc.c...] [otherobj.o...] [-lyourlib...]   -e         Preprocess only, no compilation or linking   -thread    Multithread support   -glu       Enable GLU (GLS for Unicode)   esqlcargs: esqlc arguments (-g, -G, -nln, -Ipathname, -nowarn, -V, -ansi   ,   -xopen, -local, -log, -EDname, -EUname,   -icheck)   -cc        Arguments after cc go to c compiler only   otherargs: Other arguments are passed to cc   -o         Next argument is program name   -libs      Display the list of libraries used by esql at link time.   -cp        Run C preprocessor before esqlc   -onlycp    Run only the C preprocessor, no esqlc, compilation or linking   -np        No protection of SQL keywords in SQL statements   -nup       No unprotection of SQL keywords, forces -onlycp|
|-33488|Error -33488: The options specified require a C++ compiler, but one could not   be found.|
|-33489|Error -33489: The GL_USEGLU environment variable setting requires a C++   compiler, but one could not be found.|
|33490|%s	   Preprocess only, no compilation or linking|
|33491|%s    Multithread support|
|33492|%s       Enable GLU (GLS for Unicode)|
|33493|%s       Enable SSL (Secure Sockets Layer)|
|33494|%s: esqlc arguments (-g, -G, -nln, -Ipathname, -nowarn, -V, -ansi,   -xopen, -local, -log, -EDname, -EUname,   -icheck|
|33495|%s 	   Arguments after cc go to c compiler only|
|33496|%s: Other arguments are passed to cc|
|33497|%s         Next argument is program name|
|33498|%s 	   Display the list of libraries used by esql at link time.|
|33499|%s        Run C preprocessor before esqlc|
|38700|%s    Run only the C preprocessor, no esqlc, compilation or linking|
|38701|%s        No protection of SQL keywords in SQL statements|
|38702|%s       No unprotection of SQL keywords, forces -onlycp|


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
|33510|Usage: finderr msgnum [msgnum2 ...]   finderr searches the file of error message explanations   distributed with GBase products and copies the text of one   or more error messages to the standard output.   If an unsigned number is given, a negative sign is assumed.   Examples:   finderr  327    (looks for message number -327)   finderr -327    (looks for message number -327)   finderr +1234   (looks for message number 1234)   finderr -233 107 113 134 143 144 +1541 | more   See the rofferr script for more formatting capabilities.|
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
