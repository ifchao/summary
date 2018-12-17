### DNS原理
#### DNS服务
    DNS服务：Domain Name Sercver,域名解析服务器，是进行域名和与之相应的IP地址转换的服务器。 
    将域名映射为IP地址的过程就称为"域名解析"
    1. DNS服务器的类型：
        主DNS服务器：维护所负责解析的域内的解析库服务器，解析库由管理员维护。
        从DNS服务器：从主DNS服务器或者从其他从DNS服务器复制(区域传送)一份解析库  
        缓存DNS服务器：只负责接收客户端的解析请求，然后向根服务器发起迭代查询，对查询结果进行
                      缓存。本地可以不提供区域解析。监听外部地址即可。
        转发器： 只负责转发DNS请求，转发给另一台DNS主机做查询，本地不做缓存。

    2. DNS服务的解析类型：
        正向解析：Name查询IP地址
        反向解析：IP地址查找Name

#### DNS查询的类型 
    1. 递归查询 
        当主机发出一次请求后，就得到最终的返回结果。发生在C/S之间。
        A->B->C->D

    2. 迭代查询  
        每一次查询都需要发送一次请求。(DNS服务器的工作模式)
        (1) 本地DNS服务器首先向根域root(.)DNS服务器查询，得到顶级域DNS服务器的IP地址。
        (2) 本地DNS服务器再向顶级域TLD(.com)DNS服务器查询，得到二级域DNS服务器的IP地址。
        (3) 本地DNS服务器再向二级域SLD(.example.com)DNS服务器查询，得到下级DNS服务器地址。
        A->B, B不知道，B知道C知道
        A->C, C不知道，C知道D知道
        A->D, D知道，返回结果，如果D不知道就继续向下一层查询。
        
#### DNS进行域名解析的过程  
    1. 客户端发出DNS服务请求，进行解析主机名或者IP地址。(递归查询)
    2. DNS服务器接收到客户端的请求后：
        (1) 检查DNS服务器的缓存，若查到请求的地址或域名，则发出应答。(无结果，下一步)
        (2) 检查DNS服务器自身的数据库，若查到请求的地址和域名，则发出应答。(无结果，下一步)
        (3) 将请求发给根域DNS服务器，并依次从根域查询到顶级域，由顶级域查询到二级域，二级域查
        询到三级域，直到找到请求的地址或者域名，则发出应答，找不到则返回错误。DNS服务器收到应
        答后，现在缓存中存储，然后才将结果返回给客户端。(迭代查询)

#### DNS资源记录(RR)的格式和常见记录类型 /var/named/*.zone
    格式：name [TTL] IN RRtype value 
    ;：表示注释内容
    @：表示当前域，主配置文件中zone后面的名称 
    $: 定义全局变量，如首行中 $TTL 1D
    SOA: 起始授权记录，解析库中第一条记录，有且仅能有1个,标明主服务器
    NS：专用于标明当前区域的DNS服务器
    A:  IPv4正向解析
    PTR:IPv4反向解析
    CNAME: 别名记录，别名写在IN前面，IN后面为真实域名
    MX: 邮件交换器

#### 一个RR资源记录的例子
    name [TTL] IN RRtype value 
    /var/named/hcq.com.zone
    $TTL    1D 
    @  IN SOA exam1.hcq.com. nsadmin.exam1.hcq.com.(
    ┆   ┆2017101201;            #序列号
    ┆   ┆2H;                    #刷新间隔
    ┆   ┆10M;                   #重试间隔
    ┆   ┆1W;                    #过期间隔
    ┆   ┆1D;                    #TTL
        )
 
    @              IN NS exam1.hcq.com.

    exam1.hcq.com. IN A 192.168.56.101
    exam2.hcq.com. IN A 192.168.56.102
    exam3.hcq.com. IN A 192.168.56.103
 
    www1.hcq.com. IN CNAME exam1.hcq.com.
    www2.hcq.com. IN CNAME exam2.hcq.com.
    www3.hcq.com. IN CNAME exam3.hcq.com.

    其中@可以体会为 hcq.com. , hcq.com. 并不是文件名称，而是在配置文件中域名称:

    zone "hcq.com" IN {
    type master;
    file "hcq.com.zone";
    allow-update { 192.168.56.102; };  
    };

#### PTR反向解析RR资源记录的例子
    反向解析：
        区域名称:网络地址反写。 .in-addr.arpa.
        192.168.56. --> 56.168.192.in-addr.arpa.
    /var/named/192.168.56.zone 
    $TTL 1D
    @   IN  SOA exam1.hcq.com. dnsadmin.exam1.hcq.com. (
                2017112901;
                1H; 
                5M; 
                7D; 
                1D; 
        )
    @   IN NS  exam1.hcq.com.

    101 IN PTR exam1.hcq.com.
    102 IN PTR exam2.hcq.com.
    103 IN PTR exam3.hcq.com.
    104 IN PTR exam4.hcq.com.

    @仍然是当前域的的名称。
    zone "56.168.192.in-addr.arpa" {
        type master;
        file "192.168.56.zone";
        allow-update { 192.168.56.102; };
    };    

#### 主从DNS服务器的配置   
    1. 从服务器应该为一台独立的名称服务器
    2. 主服务器的区域解析库文件中必须有一条NS记录是指向从服务器的  
    3. 从服务器只需要定义区域，而无需提供解析库文件，解析库文件应该放置/var/named/slaves/目录中。
    4. 主服务器得允许从服务器做区域传送
    5. 主从服务器时间应该同步
    6. bind程序的版本应该保持一致，否则应该从高，主低。

    1. 完全区域传送 
        第一次传送区域文件，通常是传送完整的区域文件，这叫做"完全区域传送"
    2. 增量区域传送 
        后续传送区域文件，通常是传送增量的区域文件，这叫做"增量区域传送"
        而且传送区域文件，为了保证区域文件的完整性，使用的是tcp协议进行传输的 。
        如果主服务器出现问题，不响应从服务器的询问，经过一段时间的尝试，仍然没有响应，
        从服务器就不再对DNS请求做应答,放弃解析。从服务器不会取而代之，而只是提供冗余能力。
    

    主DNS配置文件：
        zone "zone_name" IN{
            type master;
            file "zone_name.zone";
            allow_update {IP;};      #IP是从DNS服务器的IP
        };
    从DNS配置文件：
        zone "zone_name" IN{
            type slave;
            master {IP;};            #主DNS服务器IP
            file "slaves/zone_name.zone";
        }
    
#### 转发DNS服务器的配置
    注意：被转发的DNS服务器需要能够为请求者做递归，否则转发请求不予进行。
    1. 全部转发
        Options{
            forward {first|only};
            forwardders {IP;};          #将查询转发到的目的IP地址
        }
    
    2. 区域转发 
        zone "zone_name" IN {
            type forward;
            forward {first|only};
        }

    first：转发后如果查询不到结果，则进行本机查询 
    only：转发后如果查询不到结果，不进行本机查询  

#### DNS服务器的相关访问控制
    访问控制的指令：
    allow-query {}: 允许查询的主机，白名单 
    allow-transfer {}: 允许区域传送的主机，白名单 
    allow-recursion {}：允许递归的主机
    allow-update {}：允许更新区域数据库中的内容  

    访问控制的acl：
    none：没有主机
    any：任意主机
    local：本机 
    localnet：本机网段 

    acl "acl_name" {        
        ip;
        ip;
        net/prelen;
    }               #自定义访问控制的acl


#### DNS中的view
    注意：
    一个bind服务器可以定义多个view，每个view中可定义一个或者多个zone；每个view用来匹配
    一组客户端，多个view内可能需要对同一个区域进行解析，但使用不同的区域解析库文件。
    view VIEW_name {
        match-clients {};
    }

    1. 一旦启用了view，所有的zone都只能定义在view中 
    2. 仅有必要在匹配到允许递归请求的客户所在view中定义根区域 
    3. 客户端请求到达时，是自上而下检查每个view所服务的客户端列表  

#### 相关的命令
    1. host [options] FQDN
        -a：显示详细的DNS信息
        -c：指定查询类型
        -r：查询域名的时候，不使用递归查询 
    
    2. nslookup FQD
        可以交互式查询

    3. dig [options] FQDN
        @<IP>: 指明域名服务器进行解析
        -x<IP>: 反向查询
        -t <rrtype>: 指明查询的类型

