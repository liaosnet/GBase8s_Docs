# Linux退出码、信号   
## 退出码（Exit Code）  

|返回值|描述|
|:--|:--|
|0|成功（Success），程序成功完成，无错误。|
|1|通用错误（General error），一般性错误，通常表示命令执行失败。|
|2|误用命令（Misuse of shell builtins），命令的用法错误，例如，缺少必要的参数。|
|126|命令不可执行（Command invoked cannot execute）， 尝试运行一个不可执行的命令，例如权限不足。|
|127|命令未找到（Command not found），尝试运行一个不存在的命令或脚本。|
|128|无效的退出参数（Invalid exit argument），使用了无效的退出状态码。|
|130|进程被 Ctrl+C 终止（Script terminated by Control-C），进程接收到 SIGINT 信号（中断信号）。|
|137|进程被 kill 命令终止（Script terminated by SIGKILL），进程接收到 SIGKILL 信号，通常是使用 kill -9 终止的。|
|139|段错误（Segmentation fault），进程因段错误（非法内存访问）而终止。|
|143|进程被 SIGTERM 终止（Script terminated by SIGTERM），进程接收到 SIGTERM 信号，通常是使用 kill 终止的。|
|255|退出状态码超出范围（Exit status out of range），一般表示程序返回了超出范围的退出状态码。|

## 信号（Signal）  
Unix 操作系统中的信号（signals）是一种软件中断，用于通知进程发生了某个特定事件。  

|信号|描述|
|:--|:--|
|SIGHUP (1)|挂起信号。通常用于告诉守护进程重新读取其配置文件。|
|SIGINT (2)|中断信号。当用户按下Ctrl+C时，发送此信号终止前台进程。|
|SIGQUIT (3)|退出信号。当用户按下Ctrl+\时发送，与SIGINT类似，但会产生核心转储(core dump)。|
|SIGILL (4)|非法指令信号。当进程尝试执行一段非法的机器语言指令时发送。|
|SIGTRAP (5)|跟踪/断点陷阱。主要用于调试。|
|SIGABRT (6)|中止信号。由abort函数发出，用于异常终止。|
|SIGBUS (7)|总线错误。非法地址访问，如对齐错误。|
|SIGFPE (8)|浮点异常。如除以零或溢出错误。|
|SIGKILL (9)|终止信号。强制终止进程，无法被捕获或忽略。|
|SIGUSR1 (10), SIGUSR2 (12)|用户自定义信号。留给用户使用，具体行为由应用定义。|
|SIGSEGV (11)|段错误。非法访问内存时发送。|
|SIGPIPE (13)|管道破裂。当进程写入无读端的管道时发送。|
|SIGALRM (14)|闹钟信号。由alarm系统调用产生，用于定时提醒。|
|SIGTERM (15)|终止信号。请求终止进程，可以被捕获，这是一种温和的终止方式。|
|SIGCHLD (17)|子进程状态改变信号。子进程结束时，父进程会收到此信号。|
|SIGCONT (18)|继续执行信号。使暂停的进程继续执行。|
|SIGSTOP (19)|停止执行信号。暂停进程的执行，无法被捕获或忽略。|
|SIGTSTP (20)|终端停止信号。当用户按下Ctrl+Z时发送，可以被捕获。|
|SIGTTIN (21), SIGTTOU (22)|终端输入/输出信号。后台进程尝试读写终端时发送。|


最后更新日期：2026-07-22  
