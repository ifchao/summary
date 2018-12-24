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

#### 1. ss命令
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

   -4, --ipv4          display only IP version 4 sockets
   -6, --ipv6          display only IP version 6 sockets
   -0, --packet	display PACKET sockets
   -t, --tcp		display only TCP sockets
   -u, --udp		display only UDP sockets
   -d, --dccp		display only DCCP sockets
   -w, --raw		display only RAW sockets
   -x, --unix		display only Unix domain sockets
   -f, --family=FAMILY display sockets of type FAMILY

   -A, --query=QUERY, --socket=QUERY
       QUERY := {all|inet|tcp|udp|raw|unix|packet|netlink}[,QUERY]

   -D, --diag=FILE	Dump raw information about TCP sockets to FILE
   -F, --filter=FILE   read filter information from FILE
       FILTER := [ state TCP-STATE ] [ EXPRESSION ]
```
