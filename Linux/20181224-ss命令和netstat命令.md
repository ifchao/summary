___
- FileName: 20181224-ss命令和netstat命令.md
- Author: ihuangch -huangch96@qq.com
- Description: ---
- Create:2018-12-24 13:19:15
___

### 背景
ss命令和netstat命令或许应该是运维人员最常用的命令之一了吧。  
无论是查询端口是否开启，或者是分析网络连接，统计tcp/udp等连接的数据，ss命令和netstat命令都
很常用。ss命令和netstat命令这两个命令的使用方法和选项大致相同，只是个别选项有些差别。

#### 1. ss命令(CentOS7 ss版本展示信息比较详细)
```
[root@centos-111 ~]# ss --help
Usage: ss [ OPTIONS ]
       ss [ OPTIONS ] [ FILTER ]
   -h, --help		this message
   -V, --version	output version information
   -n, --numeric	don't resolve service names
					不进行域名解析(常用)
   -r, --resolve       resolve host names
					解析/etc/hosts
   -a, --all		display all sockets
					显示所有sockets连接
   -l, --listening	display listening sockets
   					显示监听的端口(sockets)
   -o, --options       show timer information
   -e, --extended      show detailed socket information
   					   展示更多socket信息
   -m, --memory        show socket memory usage
   					   展示socker内存使用
   -p, --processes	show process using socket
   -i, --info		show internal TCP information
   -s, --summary	show socket usage summary
					展示socket使用汇总
   -4, --ipv4          display only IP version 4 sockets
   -6, --ipv6          display only IP version 6 sockets
   -0, --packet	display PACKET sockets
   -t, --tcp		display only TCP sockets
   					仅显示TCP sockets
   -u, --udp		display only UDP sockets
   					仅显示UDP sockets
   -d, --dccp		display only DCCP sockets
   					仅显示DCCP sockets
   -w, --raw		display only RAW sockets
   					仅显示RAW sockets
   -x, --unix		display only Unix domain sockets
   					仅显示Unix 文件 sockets
   -f, --family=FAMILY display sockets of type FAMILY

   -A, --query=QUERY, --socket=QUERY
       QUERY := {all|inet|tcp|udp|raw|unix|packet|netlink}[,QUERY]

   -D, --diag=FILE	Dump raw information about TCP sockets to FILE
   -F, --filter=FILE   read filter information from FILE
       FILTER := [ state TCP-STATE ] [ EXPRESSION ]
```

##### 1.1 ss -s 
```
[root@centos-111 ~]# ss -s
Total: 112 (kernel 120)
TCP:   6 (estab 2, closed 0, orphaned 0, synrecv 0, timewait 0/0), ports 2

Transport Total     IP        IPv6
*	  120       -         -        
RAW	  0         0         0        
UDP	  2         2         0        
TCP	  6         4         2        
INET	  8         6         2        
FRAG	  0         0         0        

```

##### 1.2 统计系统ESTAB连接
```
~]#ss -nat | grep ESTAB | wc -l

```

##### 1.3 统计连接最多的ip
```
~]#ss -nta | grep ESTAB | awk '{print $5}' | awk -F: '{print $1}' | sort | uniq -c | sort -nr
```


#### 2. netstat命令
```
[root@centos-112 ~]# netstat --help
usage: netstat [-vWeenNcCF] [<Af>] -r         netstat {-V|--version|-h|--help}
       netstat [-vWnNcaeol] [<Socket> ...]
       netstat { [-vWeenNac] -I[<Iface>] | [-veenNac] -i | [-cnNe] -M | -s [-6tuw] } [delay]

        -r, --route              display routing table
        -I, --interfaces=<Iface> display interface table for <Iface>
        -i, --interfaces         display interface table
        -g, --groups             display multicast group memberships
        -s, --statistics         display networking statistics (like SNMP)
        -M, --masquerade         display masqueraded connections

        -v, --verbose            be verbose
        -W, --wide               don't truncate IP addresses
        -n, --numeric            don't resolve names
        --numeric-hosts          don't resolve host names
        --numeric-ports          don't resolve port names
        --numeric-users          don't resolve user names
        -N, --symbolic           resolve hardware names
        -e, --extend             display other/more information
        -p, --programs           display PID/Program name for sockets
        -o, --timers             display timers
        -c, --continuous         continuous listing

        -l, --listening          display listening server sockets
        -a, --all                display all sockets (default: connected)
        -F, --fib                display Forwarding Information Base (default)
        -C, --cache              display routing cache instead of FIB
        -Z, --context            display SELinux security context for sockets

  <Socket>={-t|--tcp} {-u|--udp} {-U|--udplite} {-S|--sctp} {-w|--raw}
           {-x|--unix} --ax25 --ipx --netrom
  <AF>=Use '-6|-4' or '-A <af>' or '--<af>'; default: inet
  List of possible address families (which support routing):
    inet (DARPA Internet) inet6 (IPv6) ax25 (AMPR AX.25) 
    netrom (AMPR NET/ROM) ipx (Novell IPX) ddp (Appletalk DDP) 
    x25 (CCITT X.25) 

```
netstat 命令和ss命令大部分的使用方式相同，其中统计信息，不过是字段的位置不同需要修改一下


#### 3. Recv-Q 和 Send-Q的含义
Recv-Q 和 Send-Q 分别表示网络接收队列，发送队列。Q是Queue的缩写。  
这两个值通常应该为0，如果不为0可能是存在问题的。packets在两个队列里面都不应该有堆积状态。
可接受短暂的非0情况。  
如果接收队列Recv-Q一直处于阻塞状态，可能是遭受了拒绝服务 denial-of-service(dos) 攻击。  
如果发送队列Send-Q一直不能很快的清零，可能是有应用向外发送数据包过快，或者是对方接收数据包不够快。  

Recv-Q: 表示收到的数据已经在本地接收缓冲，但是还没有被进程取走，recv()
Send-Q: 对方没有收到的数据或者说没有Ack的数据，还是在本地缓冲


#### ss 与 netstat 对比
ss执行的时候消耗资源以及消耗的时间都比netstat少很多。  
ss的优势在于它能够显示更多更详细的有关tcp和连接状态的信息，而且比netstat更快速。  
原因如下：  
1. 当服务器socket连接数量变得非常大的时候，无论是使用netstat命令还是直接cat /proc/net/tcp,
执行速度都会很慢。
2. ss快的秘诀在于，它利用了TCP协议栈中tcp_diag。tcp_tiag是一个用于分析统计的模块，可以获得
Linux内核中第一手的信息，这就确保了ss的快捷高效。当然如果系统没有tcp_diag，ss也可以正常运行，
只是效率会变得慢一点(但是仍然比netstat快)


