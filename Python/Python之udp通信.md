### 相关知识描述
    关于网络协议的相关知识，不在本文中进行介绍。
    Python可以通过socket模块进行网络中的计算机相互通信。

### socket
    socket也就是套接字，理解套接字，可以认为他就是ip地址，端口，和应用协议组成的。(自己是这么认为的)
    互联网中的每一台主机，都是通过IP地址来标识的，通过IP地址可以访问一台主机，想要和另外一台主机的
    相关程序进行连接就需要通过port来进行标识不同的应用进程，而相关的应用协议就是发送数据的方式。
    因此，套接字也可以认为是进程间通信的一种方式，只不过是不同主机之间的进程的通信。

### Python中的socket模块
    socket函数:
    Python语言可以通过socket模块中的socket函数进行套接字的创建,关闭等。
```
    from socket import *
    udpSocket = socket(AF_INET, SOCK_DGRAM)
```
    上述代码就是如何创建一个套接字。通过socket模块中的，socket函数创建了一个套接字udpSocket。
    AF_INET表示的是使用IPv4的地址通信，SICK_DGRAM，表示使用的udp协议。通过socket协议可以定义
    不同类型的socket。

    定义接收方的地址:
    当我们创建了一个套接字以后，我们需要定义接收方的地址
    接收方的地址是以元组的形式存在的,这个元组是2元的，分别是表示的是IP地址和Port
```
    sendAddr = ('192.168.56.1', 8080)
```

    sendto函数:
    这样我们就可以通过udp协议发送数据了 
```
    udpSocket.sendto('hahahhahh', sendAddr)
```

    bind函数:
    一般作为udp客户端的时候,是不需要绑定端口号的，但是作为服务端就需要绑定端口号。绑定端口号，
    就是把进程和端口绑定在一起，客户端和对应的进程进行连接。
    bind函数的参数是一个元组
```
    udpSocket.bind(("", 6789)) #绑定监听的IP地址和端口
```
    IP地址不填写，表示监听主机中的所有IP地址。

    revvfrom函数:
    通过recvfrom函数接受数据
```
    udpSocket.recvfrom(1024)
```
    其中1024表示发送一次数据的最大的字节数。recvfrom函数返回一个元组。包含2个元素。
    第0个元素是字符串，表示发送方发送的内容。(可能需要解码)
    第1个元素是一个元组，这个元组包含两个元素，发送方的IP和Port


### Python实现简单的udp聊天室
```
    from socket import *
    def udptalk():
        udpSocket = socket(AF_INET, SOCK_DGRAM)
        udpSocket.bind(("", 6789))
        while True:
            recvInfo = udpSocket.recvfrom(1024)
            print("[%s]:%s" % (str(recvInfo[1]), recvInfo[0].decode("gb2312")))
```

### 关于Python3中的编码与解码
    使用encode函数进行编码
        encode("utf-8")

    使用decode函数进程解码
        decode("utf-8)
    
    其中关于Python2中相关的编码解码问题在此先不讨论。

    