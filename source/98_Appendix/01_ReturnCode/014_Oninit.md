# Oninit 退出返回码  

|返回值|描述|用户操作|
|:--|:--|:--|
|0|The database server was initialized successfully.|The database server started.|
|1|Server initialized has failed. Look at any error messages written to stderr or the online message log.|Take the appropriate action based on the error messages written to stderr or the online message log.|
|87|The database server has detected security violations or certain prerequisites are missing or incorrect.|(UNIX and Mac OS only) Check if user and group gbasedbt exists. Check if the server configuration file (onconfig) and sqlhosts file exists and has the correct permissions. Check if the environment variables GBASEDBTDIR, ONCONFIG, and SQLHOSTS have a valid value and their length does not exceed 255 characters. Check if the environment variable GBASEDBTDIR specifies an absolute path and does not have any spaces, tab, new lines, or other incorrect characters. Check if role separation-related subdirectories under the $GBASEDBTDIR directory, such as aaodir and dbssodir, have the correct ownership. Run the onsecurity utility to diagnose and fix any issues.|
|170|The database server failed to initialize the dataskip structure.|Free some physical memory on the system and try to start the database server again.|
|172|The database server failed to initialize the listener threads.|Free some system resources, check the configuration parameter values for the number of listener threads to start when the database server starts up, and try to start the database server again.|
|173|The database server failed to initialize data replication.|Free some physical memory in the system and try to start the database server again.|
|174|The database server failed to start fast recovery threads.|Free some physical memory in the system and try to start the database server again.|
|175|The database server failed to initialize the root dbspace.|Check the root dbspace related parameters in server configuration file (onconfig) to make sure that the path for the root dbspace is valid.|
|176|Shared disk secondary server initialization failed.|Check the entries in sqlhosts file (UNIX) or SQLHOSTS registry key (Windows) to make sure that you are using the value of the DBSERVERNAME configuration for the primary server correctly. Check if the value for the SDS_PAGING configuration parameter in the server configuration file (onconfig) is correct. Free some system resources and try to start the database server again.|
|177|The database server failed to start the main_loop thread.|Free some physical memory on the system and try to start the database server again.|
|178|The database server failed to initialize the memory required for page conversion.|Free some physical memory on the system and try to start the database server again.|
|179|The database server was unable to start CPU VPs.|Free some physical memory on the system and try to start the database server again.|
|180|The database server was unable to start the ADM VP.|Free some physical memory on the system and try to start the database server again.|
|181|The database server failed to initialize kernel AIO.|Free some physical memory on the system and try to start the database server again.|
|182|The database server was unable to start IO VPs.|Free some physical memory on the system and try to start the database server again.|
|183|The database server failed to initialize the memory required for asynchronous I/O operations.|Free some physical memory on the system and try to start the database server again.|
|184|The database server failed to initialize memory required for parallel database queries. (PDQ)|Free some physical memory on the system and try to start the database server again.|
|185|The database server failed to initialize various SQL caches.|Free some physical memory on the system and try to start the database server again.|
|186|The database server failed to initialize the Global Language Support (GLS) component.|Free some physical memory on the system and try to start the database server again.|
|187|The database server failed to initialize the Associated Service Facility (ASF) components.|Check the entries in sqlhosts file.|
|188|The database server was unable to start the CRYPTO VP.|Free some physical memory on the system and try to start the database server again.|
|189|The database server was unable to initialize the alarm program.|Free some physical memory on the system and try to start the database server again.|
|190|The database server failed to initialize the auditing component.|Free some physical memory on the system and try to start the database server again.|
|192|The database server failed to restore the Window station and desktop.|(Windows only) Try to shut down the database server after freeing some system resources.|
|193|The database server failed to create daemon processes.|(UNIX and Mac OS only) Free some system resources and try to startup the database server once again.|
|194|The database server failed to redirect the file descriptors properly.|(UNIX and Mac OS only) Check the availability of the /dev/null device and try to start the database server again.|
|195|The database server failed to initialize the current directory for use.|Check the validity of the current working directory from where the database server is being initialized.|
|196|The database server failed to initialize the /dev/null device.(AIX® only) |Check the validity of the /dev/null device.|
|197|The database server failed to find the password information for the user trying to initialize the database server.|Verify that the user password is valid.|
|198|The database server failed to set the resource limits.|(UNIX and Mac OS only) Verify, and if required, increase the resource limits for processes on the host computer.|
|200|The database server did not have enough memory to allocate structures during initialization.|Free some physical memory on the system and try to start the database server again.|
|206|The database server could not allocate the first resident segment.|Check the values of the BUFFERPOOL and LOCKS configuration parameters in the server configuration file (onconfig) to make sure that they can be accommodated with the available memory on the host computer.|
|207|The database server failed to initialize shared memory and disk space.|Free some physical memory in the system, check the validity of all the chunks in the database server, and try to start the database server again.|
|208|The database server failed to allocate structures from shared memory.|Free some system resources and try to start the database server again.|
|209|The database server encountered a fatal error during the creation of shared memory.|Free some physical memory in the system and try to start the database server again.|
|210|The database server requested memory for the resident segment that exceeded the maximum allowed.|Reduce the size of the resident segment by lowering the values of the BUFFERPOOL and LOCKS configuration parameters.|
|220|The database server failed to read the audit configuration file.|Check that the audit configuration file (adtcfg) exists and is valid.|
|221|The database server could not detect the default directory for DUMPDIR. Usually it is the $GBASEDBTDIR/tmp directory.|Create the $GBASEDBTDIR/tmp directory if it is not present.|
|222|The database server detected an error in the value of the DBSERVERALIASES configuration parameter in the server's configuration file.|Verify that the values for the DBSERVERALIASES configuration parameter are valid and they have corresponding entries in the sqlhosts file (UNIX) or SQLHOSTS registry key (Windows).|
|223|The database server detected an error with the value of the DBSERVERNAME configuration parameter in the server's configuration file.|Verify that the value of the DBSERVERNAME configuration parameter is valid and it has a corresponding entry in the sqlhosts file (UNIX) or SQLHOSTS registry key (Windows).|
|224|The database server detected an error with the value of the HA_ALIAS configuration parameter in the server's configuration file.|Correct the value of the HA_ALIAS configuration parameter in the server configuration file (onconfig).|
|225|The database server detected too many entries for the NETTYPE configuration parameter or the DBSERVERALIASES configuration parameter in the server's configuration file.|Reduce the number of instances of the NETTYPE or DBSERVERALIASES configuration parameters in server configuration file (onconfig) and try to start the database server again.|
|226|The database server could not find an entry for the DBSERVERNAME configuration parameter in the sqlhosts file or the contents of the sqlhosts file are not valid.|Check the entries in the sqlhosts file.|
|227|Incorrect serial number.|Reinstall the database server.|
|228|The user does not have the necessary DBSA privileges to invoke the executable.|The user must have DBSA privileges or be a part of the GBasedbt-Admin group (Windows).|
|229|The database server could not initialize the security sub-system.|(Windows only) The user does not the necessary user rights on the host or is not part of the GBase-Admin group.|
|230|The database server, if started as a process on Windows platform , timed out while trying to build the required system databases during initialization. |(Windows only)Check the event log on the host to determine why the service could not be opened or could not be started. The database server might have timed out while trying to build the system databases. Free some system resources and try to start the database server again.|
|231|GBase service startup failed when the “oninit -w” command was run as a process on the command line.|(Windows only) Check the event log on the host to determine why the service start has failed.|
|233|The database server failed to initialize the Pluggable Authentication Module (PAM).|Check the configuration for the PAM library on the system.|
|235|The database server detected errors for certain configuration parameter values in the server's configuration file.|Inspect the server configuration file (onconfig) for any errors.|
|236|The database server detected an error while trying to restrict the allowable values for the GBase edition in use.|Check if the SDS_ENABLE configuration parameter is set to 1 in the server configuration file (onconfig). Check if the server name specified with the oninit -SDS command matches the value of the HA_ALIAS or DBSERVERNAME configuration parameter. Check if the shared disk used is part of an existing shared disk cluster.|
|237|The database server could not find the server configuration file.|Ensure that the server configuration file exists and is valid.|
|238|The database server detected an incorrect value for the GBASEDBTSERVER environment variable or the value did not match the value of the DBSERVERNAME configuration parameter in the server's configuration file.|(Windows only) Check the value of the GBASEDBTSERVER environment variable and the corresponding entry in the registry.|
|239|The database server detected an incorrect or non-existent value for the GBASEDBTDIR environment variable.|(Windows only) Check the value of the GBASEDBTDIR environment variable.|
|240|Incorrect command-line options were issued to the database server.|Correct the command-line options issued to the database server at startup.|
|248|The database server failed to create the GBase loader domain file.|(AIX only) Check if the /var/adm/ifx_loader_domain file is present.|
|249|The database server failed to dynamically load the PAM library.|The PAM library is not available for the database server. Install the PAM libraries.|
|250|The database server failed to dynamically load the ELF library.|The ELF library is not available to the database server. Install the libelf packages.|
|255|There was an internal error during server initialization. Look at any error messages written to stderr or to the online message log.|Take the appropriate action based on the error messages written to stderr or the online message log.|