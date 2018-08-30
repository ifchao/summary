### HTTP web服务器

#### httpd服务器的基本知识  
    httpd:是Apache HTTP服务器的主程序，被设计为一个独立运行的后台进程，它会建立一个处理请求的子进程或者线程的池。  
    httpd的特性：  
    (1)高度模块化：Core+Modules(核心+模块的方式)  
    (2)DSO：Dynamic Shared Object(支持动态装卸载)  
    (3)MPM：Multipath Processing Module(多路处理模块)  
#### httpd MPM 三种模型?  
    1. prefork模型： 多线程模型,每个进程响应一个请求(稳定性好,并发能力有限)  
    一个主进程： 负责生成和销毁子进程,创建套接字,接受客户端请求，并将请求分发给子进程  
    n个子进程：每个子进程负责响应一个请求  
    工作特性：httpd服务启动的时候，会预先生成多个空闲进程，等待客户端进行连接，但是由于prefork模型，  
    是调用I/O复用模型中的select()函数来生成空闲进程的，所以空闲进程数应该小于1024  
     
    2. worker模型：多线程多进程模型，每个线程响应一个请求(占用内存少，高并发相对优秀一些)  
    一个主进程：负责生成和销毁子进程，创建套接字，接受客户端请求，并将请求分发给子进程  
    n个子进程：每个子进程生成多个线程  
    多个线程：每个线程响应一个请求
    工作特性：由于在Linux中，进程是很轻量的，所以Linux中prefork和worker模型的区别不是特别大。
    但是在这种模式下，如果某个子进程出现问题，那么这个子进程下面的进程都会出现问题。  
  
    3. event模型：基于事件驱动机制模型，多进程模型，每个进程响应多个请求  
    一个主进程：负责生成和销毁子进程，负责创建套接字，接受客户端请求，并将请求分发给子进程
    子进程：基于事件驱动机制直接响应多个请求  
    工作特性：解决了keep-alive长连接的时候占用线程资源被浪费的问题(某些线程因为被keep-alive,空挂在那里等待，
    中间几乎没有请求过来，甚至会等待超时)，event模型中，会有一个专门的线程来管理这些keep-alive类型的线程，
    当有真实请求过来的时候，将请求传递给服务进程，执行完毕后，又允许它释放，增强了在高并发场景下的请求处理
    能力。  

    event模型在Apache2.2中是试验阶段，Apache2.4中已经可以应用在生产环节中。  
#### httpd相关配置  
    1. 站点路径访问控制  
    基于本地文件系统路径，支持级联  
    <Directory "/path/to/some_dir">  
    </Directory>  
    <File>...</File>  
    <FileMatch>...</FileMatch>  
    基于URL实现  
    <Location "/path/to/some_url">  
    </Location>    

    2. Directory容器中的访问控制协议  
    options：后面跟一个或多个空格分隔的选项的列表  
        1. indexes：当访问的路径下没有主页面时，将所有资源以列表的形式呈现给用户，谨慎使用   
        2. FollowSymLinks：允许跟踪符号链接文件所指向的源文件  
        3. None，All：一个都没有或者所有，多数情况为None  
    AllowOverride None/All：是否运行覆盖，一般都为None  

    3. Directory容器中基于IP的访问控制  
    apache2.2:  
        order allow,deny：定义生效次序  
        Allow|Deny from all|ip|net：拒绝或者允许一个ip或网段或者全部eg:Allow from 192.168.56.0/24  
    apache2.4:  
        Require all granted：允许所有主机  
        Require all deny：拒绝所有主机  
        <RequireAll>   
            RequireAll all granted 
            Require not ip 192.168.56.2|192.168.56.0/24 
            Require not host HOST_NAME
        </RequireAll>  
    注意：Apache2.4中控制特定IP类都需要<RequireAll>    

    4. 虚拟主机  
    基于IP：为每个虚拟主机提供一个IP地址  
    基于PORT：为每个虚拟主机提供至少一个port  
    基于FQDN：为每个虚拟主机使用至少一个FQDN，httpd2.2需要开启NameVirtualHost  
    注意：可以混用上述三种虚拟主机,一般虚拟主机不可以和中心主机混用。需要注释DocumentRoot   

    5. 日志记录
    ErrorLog logs/error_log：定义错误日志的文件路径  
    LogLevel warn：指定日志级别  
    日志级别：debug,info,notice,warn,error,crit,alert,emerg级别由低到高 
    CustomLog logs/access_log combined：访问日志路径
    指定日志格式和名称:  
    LogFormat "....." Format_Name
    CustomLog logs/path Format_name 
        %h：客户端IP地址  
        %l：Remote logname 多为空
        %u：Remote User  多为空
        %t：服务器收到请求的时间  
        %r：First line of request 请求报文的首行信息(method url version)  
        %s：status，响应状态码，%>s表示最后请求的状态  
        %b：响应报文的大小，单位是字节   
        %{Referer}i：请求报文中Referer首部的值，即从哪个页面中链接过来的eg:\"%{Referer}i\",\转义"
        %{User-Agent}i：用户的代理
        %{Foobar}i：Foobar为http报文中的首部  

    6. 路径别名  
    Alias,它是Apache的mod_alias模块的一部分，它使用一个URL路径，并且使此路径重定向到文件系统上的一个目录
    或者文件来替换它。  
    Alias /images "/var/data/images"
        http://www.FQDN.com/images/example.png  
        /var/data/images/example.png

    7. 基于用户的访问控制 
    认证质询：响应报文WWW-Authenticate,响应码为401拒绝客户端请求，并说明客户端提供账号和密码。客户端用户
    填入账号和密码后再次发送请求报文，认证通过时，则服务器发送响应的资源。
    认证方式：1.basic(明文)  2.digest(消息摘要)
    Basic认证实例：
    <Directory "">
        Option None
        AllowOverride None
        AuthType Basic
        AuthName "One_String"
        AuthUserFile "/Path/to"
        Require user USERNAME1,USERNAME2
    </Directory>
    注意：Require valid-user 表示所有用户

#### httpd相关的命令
    1. httpd命令
    #httpd -V：查看服务器详细信息，包括版本，使用MPM等
    #httpd -l：列出静态编译的模块
    #httpd -M：查看静态编译和动态装卸载的模块   
    #httpd -t：检测配置文件是否有语法错误  
    
    2. apachectl命令
    configtest：检测配置文件
    fullstatus: 显示服务器完整状态信息  
    restart：重新启动
    status：查看服务器摘要状态信息
    stop：停止服务器

    3. htpasswd命令：提供账号密码文件
    htpasswd -cmsD /path/to username 
    -c：自动创建此处文件，仅在文件不存在时使用  
    -m：md5格式加密  
    -s：sha格式加密
    -D：删除用户
    
    4. ad命令：压力测试工具
    ab -k -c 200 -n 200000 192.168.56.101/index.html
    -n：总请求数
    -c：模拟的并发数
    -k：以持久连接测试
    
