# Onclean 退出返回值  

|返回值|描述|
|:--|:--|
|0|Successful|
|1|Failure because of one of the following problems:<br />- Incorrect environment variable settings<br />- Incorrect privileges to run the onclean command<br />- Incorrect command syntax<br />- Corrupted information<br />- Running the onclean command without the -k option on a server that is still online<br />|
|2|Failure because one or more OS system calls used by onclean returned an error.|