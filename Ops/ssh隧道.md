### 
- Author: ihuangch
- Date: 2018-11-08
- Email: huangch96@qq.com
###

___

### 背景
公司需要一台巴西地区的vpn，由于之前使用haproxy进行代理，haproxy代理也相对安全一些，但是由于验证
文件无法及时更新，导致代理服务器总是出现滥用的情况。这时想到了ssh也可以做端口转发，就尝试使用了
一下。顺便也学习一下ssh隧道的相关知识。  

### 什么是SSH隧道?
隧道是把一种网络协议封装进另外一种网络协议进行传输的技术。这里我们讨论的是ssh隧道，所以所有的网络
通信协议都是加密的。ssh隧道，又被称为端口转发，因为ssh隧道通常会绑定一个本地端口，所有发向这个端口
的数据包，都会被加密并透明地传输到远端系统。  

ssh隧道可以用于通过ssh加密传输在网络上传输一些没有加密的流量。例如，ftp协议自身是没有加密的，我们
可以使用ssh隧道在ftp服务器和客户端之间安全的传输文件。ssh隧道还提供了绕过防火墙的一些方法，并且
加密自己的流量。  

### SSH隧道的类型?
ssh隧道有3种类型:

	1. 动态端口转发(SOCKS代理)
	2. 本地端口转发
	3. 远程端口转发

###### 端口转发:
Port Forwarding，有时被叫做隧道，是ssh为网络安全通信使用的一种方法。端口转发是转发一个网络端口从
一个网络节点到另一个网络节点的行为，其使一个外部用户从外部经过一个被激活的路由器到达一个在私有
内部ip地址上的一个端口。  
----摘自百度百科  

同时ssh正向隧道、ssh反向隧道、又分别对应哪种端口转发？？？  
接下来会一一分析。  

### 动态端口转发:
动态端口转发允许配置一个本地端口，以便将数据通过隧道传输到所有远程主机。但是，要利用这个功能，连接
到这个端口的客户端应用程序应该使用SOCKS协议发送流量。客户端创建SOCKS代理，并且应用程序（如浏览器）
使用socks协议来指定当流量离开ssh隧道的另一端时应该传输的地址。  
<div align="center"> <img src="https://github.com/ihuangch/blog/blob/master/Ops/pic/ssh-D.png" height="300px" /> </div><br>


###### 动态端口转发网络拓扑图:
<div align="center"> <img src="https://github.com/ihuangch/blog/blob/master/Ops/pic/ssh-Dy.png" height="300px" /> </div><br>

###### 代理服务器:
```
ssh -D [bind_address:]port user@edge_node
ssh -D 0.0.0.0:9080 user@edge_node
```
	
	参数说明:
		bind_address:绑定的ip地址，默认会绑定在本地回环地址127.0.0.1，如果空值或者为*，会绑定
					 本地所有的IP地址，如果希望绑定的端口仅供本机使用，可以指定为localhost。
		port:指定本地绑定的端口


通过这样配置，我们就可以通过图中的代理服务器，访问相对应的国家的网络。当然我们需要在自己的网络
配置好socks协议，相关的服务器地址ip和port。
###### 优点:
配置完成后，通过socks，可以访问edge_node中网络中的所有服务。
###### 确定:
用户需要额外配置socks协议


### 本地端口转发:
通过SSH隧道，将一个远端机器能够访问到的地址和端口，映射为一个本地的端口。  
<div align="center"> <img src="https://github.com/ihuangch/blog/blob/master/Ops/pic/ssh-L.png" height="300px" /> </div><br>

###### 本地端口转发网络拓扑图:
<div align="center"> <img src="https://github.com/ihuangch/blog/blob/master/Ops/pic/ssh-Local.png" height="300px" /> </div><br>

###### 代理服务器:
```
ssh -L [bind_address:]port:host:hostport 
```

	参数说明:
		bind_address:绑定的ip地址。本地回环地址，如果空值或者为*，则绑定本地所有ip地址。
		port:指定本地绑定的端口
		host:指定数据包转发目标地址的IP，如果目标主机和代理是同一台主机时该参数指定为localhost
		hostport:目标主机的端口

通过这样配置，我们访问图中的2018端口，就可以访问后端的3306端口了。
###### 优点:
不用设置代理
###### 缺点:
不同的服务需要不同的设置

### 远程端口转发:
远程端口转发用于某些单向阻隔的内网环境。比如防火墙。再防火墙之后，内网主机可以直接访问公网主机。
但是外网主机却无法访问内网主机的服务。如果内网主机向外网主机建立一个远程转发端口，就可以让外网
主机通过该端口访问内网主机的服务。  

<div align="center"> <img src="https://github.com/ihuangch/blog/blob/master/Ops/pic/ssh-R.png" height="300px" /> </div><br>

###### 远程端口转发网络拓扑图:
<div align="center"> <img src="https://github.com/ihuangch/blog/blob/master/Ops/pic/ssh-Re.png" height="300px" /> </div><br>

###### 代理服务器:
```
ssh -R [bind_address:]port:host:hostport
```
	
	参数说明:
		bind_address:需要转发到远程主机的ip地址
		port:指定远程主机绑定的端口
		host:指定发送数据包的源IP，如果源主机和代理是同一台主机时该参数指定为localhost
		hostport:源主机的端口

通过这样配置，把本机的3306端口，转发到远程主机的2018端口。
###### 优点:
不用设置代理
###### 缺点:
不同的服务需要不同的设置

		
