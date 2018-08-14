### tcpdump
   tcpdump命令行版本的一个抓包工具，因为最近也在使用wireshark，所以准备把tcpdump命令的使用方法
   也总结一下。

### tcpdump命令选项
    tcpdump的命令格式是:
        tcpdump [ -AdDefIJKlLnNOpqRStuUvxX ] [ -B buffer_size ] [ -c count ]
                [ -C file_size ] [ -G rotate_seconds ] [ -F file ]
                [ -i interface ] [ -j tstamp_type ] [ -m module ] [ -M secret ]
                [ -Q|-P in|out|inout ]
                [ -r file ] [ -s snaplen ] [ -T type ] [ -w file ]
                [ -W filecount ]
                [ -E spi@ipaddr algo:secret,...  ]
                [ -y datalinktype ] [ -z postrotate-command ] [ -Z user ]
                [ expression ]
    相关的命令选项是很多的，在此，只介绍一些常用的。便于日常的使用。

    抓包选项:
        -c <Num>:指定要抓取的包的数量,注意是最终获取的包的数量。是满足各个选项条件的包的数量，不是总处理的包的数量
        -i interface:指定tcpdump需要监听的网卡。如果没有指定，则为默认的编号最小的那个网卡
        -n:对地址以数字方式显示，否则显示主机名
        -nn:使用-nn选项时，不仅ip地址使用数字显示，端口也使用数字显示，否则显示端口对应的协议
        -N:不打印host的域名部分，www.acd.com，只打印www
        -P:指定要抓取的包是流入还是流出的包。值为in|out|inout，默认为inout
        -s snaplen:设置tcpdump的数据包抓取长度，如果不设置默认将会是65525字节。
   
    输出选项:
        -e:输出每行中的数据链路层的头部信息，例如源MAC和目标MAC
        -q:快速打印输出。即打印很少的协议相关信息，输出行比较简短
        -X:输出包的头部数据，以16进制和ASCII码两种方式输出
        -XX:更详细输出包的头部数据
        -v:当分析和打印的时候，产生详细的输出
        -vv:产生比-v更详细的输出
        -vvv:比-vv更详细的输出
    
    其他选项:
        -D:列出可用于抓包的接口 
        -F:从文件中读取抓包的表达式，如果使用此选项，命令行其他表达式失效
        -w filename:将抓取的包输出到文件中
        -r file:从指定的文件中读取数据

```
    [root@localhost ~]# tcpdump -i eth0 -c 10 -nn -q
    tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
    listening on eth0, link-type EN10MB (Ethernet), capture size 65535 bytes
    20:37:19.195328 ARP, Request who-has 10.0.2.2 tell 10.0.2.15, length 28
    20:37:19.197203 ARP, Reply 10.0.2.2 is-at 52:54:00:12:35:02, length 46
    20:37:19.197221 IP 10.0.2.15.58325 > 119.29.29.29.53: UDP, length 43
    20:37:19.280311 IP 119.29.29.29.53 > 10.0.2.15.58325: UDP, length 43
    20:37:25.622213 IP 10.0.2.15.53452 > 119.29.29.29.53: UDP, length 31
    20:37:25.676366 IP 119.29.29.29.53 > 10.0.2.15.53452: UDP, length 90
    20:37:25.676672 IP 10.0.2.15 > 115.239.210.27: ICMP echo request, id 14348, seq 1, length 64
    20:37:25.723246 IP 115.239.210.27 > 10.0.2.15: ICMP echo reply, id 14348, seq 1, length 64
    20:37:25.723869 IP 10.0.2.15.56683 > 119.29.29.29.53: UDP, length 45
    20:37:27.679231 IP 119.29.29.29.53 > 10.0.2.15.56683: UDP, length 45
    10 packets captured
    10 packets received by filter
    0 packets dropped by kernel
```

    
### tcpdump命令中相关的表达式
    表达式的作用可以解析数据报文，达到筛选指定数据包的作用。
    tcpdump的表达式由一个或者多个修饰符组成。有三种修饰符
    1.type:指定抓取封包(ID)的主机或者端口
    可以给定的值有host|net|port|portrange,默认为host
    eg:"host www","net 192.168.56","port 80" "portrange 1000-3000"
    
    2.dir:指定封包(ID)的方向
    可以给定的值有src|dst|src or dst|src and dst,默认为src or dst
    eg:"src net 192.168.23"：源网络为192.168.23的数据包
       "src or dic prot 22": 源端口或目的端口为22的数据包

    3.proto:指定封包(ID)的协议
    可以给定的值有tcp|udp|arp|ip|ether|icmp
    eg:"tcp port 21"

    所以一般表达式形式为 proto dir type ID

    表达式修饰符之间可以使用操作符:
        and(&&)|or(||)|not(!)，这样可以组成复杂的条件表达式。
        使用()可以改变表达式的优先级,但是需要注意的是括号需要转义
    
```
    [root@localhost ~]# tcpdump -i eth1 -c 10 -nn port 22 -q
    tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
    listening on eth1, link-type EN10MB (Ethernet), capture size 65535 bytes
    20:55:35.315801 IP 192.168.56.110.22 > 192.168.56.1.59088: tcp 208
    20:55:35.323310 IP 192.168.56.110.22 > 192.168.56.1.59088: tcp 128
    20:55:35.323635 IP 192.168.56.1.59088 > 192.168.56.110.22: tcp 0
    20:55:35.323770 IP 192.168.56.110.22 > 192.168.56.1.59088: tcp 128
    20:55:35.364510 IP 192.168.56.1.59088 > 192.168.56.110.22: tcp 0
    20:55:35.364693 IP 192.168.56.110.22 > 192.168.56.1.59088: tcp 192
    20:55:35.373393 IP 192.168.56.110.22 > 192.168.56.1.59088: tcp 192
    20:55:35.373699 IP 192.168.56.1.59088 > 192.168.56.110.22: tcp 0
    20:55:35.373856 IP 192.168.56.110.22 > 192.168.56.1.59088: tcp 128
    20:55:35.404540 IP 192.168.56.110.22 > 192.168.56.1.59088: tcp 192
    10 packets captured
    12 packets received by filter
    0 packets dropped by kernel
    You have new mail in /var/spool/mail/root
```

还有一些其他选项和相关表达式，如果需要使用，查询man文档。
最后英语真的很重要。
