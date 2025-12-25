# GBase 8s数据库错误代码  
第三部分  

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

