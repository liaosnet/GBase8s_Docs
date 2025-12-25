# GBase 8s数据库错误代码  
第四部分  


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
|1200|Sun&#124;Mon&#124;Tue&#124;Wed&#124;Thu&#124;Fri&#124;Sat&#124;|
|1201|Jan&#124;Feb&#124;Mar&#124;Apr&#124;May&#124;Jun&#124;Jul&#124;AugSep&#124;Oct&#124;Nov&#124;Dec&#124;|
|1202|Press RETURN to continue.|
|1203|Cannot find message file.  Check GBASEDBTDIR and DBLANG.|
|1204|The type of your terminal is unknown to the system.|
|1205|128-173|
|1206|January&#124;February&#124;March&#124;Apri&#124;|May&#124;June&#124;|
|1207|July&#124;August&#124;September&#124;October&#124;November&#124;December&#124;|
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
|21407|usage: { %s [-p] [-s serialnum key] [-c cmeSN] file ... &#124;   %s { -r DT_RPATH &#124; -t } file }|
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
|-33416|Usage: ifx_getversion [product_name &#124; library_name]   where [product_name &#124; library_name] is:   clientsdk   esql   dmi&#124; libdmi   libcli[.a&#124;.so]   libgls[.a&#124;.so]   libos[.a&#124;.so]   libasf[.a&#124;.so]   libsql[.a&#124;.so]   libgen[.a&#124;.so]|
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

