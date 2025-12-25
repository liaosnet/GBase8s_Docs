# GBase 8s数据库错误代码  
第一部分  

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
