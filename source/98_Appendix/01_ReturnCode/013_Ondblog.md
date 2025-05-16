# Ondblog 退出返回值  

|返回值|描述|用户操作|
|:---|:---|:---|
|1|An error reading the onconfig file.	|Check that the onconfig file is in the \$GBASEDBTXDIR/etc/\$ONCONFIG directory. If the BAR_ACT_LOG and BAR_DEBUG_LOG configuration parameters are set, make sure that the files are valid.|
|2|A linked list error.	|See the accompanying message.|
|3|The user is not authorized to run the command.	|Run the ondblog commands as the root user, user gbasedbt, as a Windows administrator, or as the owner of the database server.|
|4|Failed to set the GBASEDBTSHMBASE environment variable to -1.	|Contact GBase Software Support.|
|5|The database server is not online.	|Start the database server.|
|6|The command option is invalid.	|Correct the spelling of the option.|
|7|Failed to communicate with the backup utility.	|Check that the database server is online and that ON-Bar is configured.|
|9|Failed to allocate memory.	|Check the ON-Bar logs for more information. You might need to ask your System Administrator to either increase your swap space or to install more memory in your system.|
|16|Failed to open the file.	|Check the ON-Bar logs for more information.|
|17|Cannot change to the specified logging mode.	|Check the ON-Bar logs for more information.|
|18|Failed to change the logging mode.	|Check the ON-Bar logs for more information.|
|19|An SQL error occurred.	|Check the ON-Bar logs for more information.|
|20|An empty list problem occurred.	|Check the ON-Bar logs for more information.|