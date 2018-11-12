### Docker命令行参数解读
在使用Docker时，需要使用Docker命令行工具docker命令和Docker daemon建立通信。Docker daemon是Docker
守护进程，复制接收并分发执行Docker命令。  

可以使用docker命令或docker help命令来获取docker命令的清单。  

Docker命令的执行一般都需要root权限，因为Docker命令行工具docker和Docker daemon是同一个二进制文件，
而Docker daemon负责接收并执行来自docker的命令，它的运行需要root权限。同时，从Docker 0.5.2版本开始
，Docker daemon默认绑定一个Unix Socker来代替原来的TCP端口，该Unix Socker默认是属于root用户的。因此
，在执行Docker命令需要root权限。  

<div align="center"> <img src="https://github.com/ihuangch/blog/blob/master/Docker/pic/docker-socket.png" height="300px" /> </div><br>

随着Docker的不断发展，docker的子命令也有很多(run,build,attach)，其中核心子命令(run,exec)还有很多
复杂的可执行选项。对于特定的子命令，可以使用docker CMD --help命令来查看子命令的详细信息，包括子命令
的使用方法和可用的操作参数。  

<div align="center"> <img src="https://github.com/ihuangch/blog/blob/master/Docker/pic/docker-cmd.png" height="300px" /> </div><br>

从docker命令使用出发，梳理出命令结构图：  

<div align="center"> <img src="https://github.com/ihuangch/blog/blob/master/Docker/pic/docker-use.png" height="300px" /> </div><br>

#### 详细命令及参数
接下来的介绍一些常用的命令参数。
##### 1. Docker环境信息
- docker info：用于检查Docker是否正确安装。如果正确安装，输出Docker配置信息。
- docker version：结合docker info使用，能够提取到足够详细的信息。

##### 2. 容器生命周期管理
容器生命周期命令涉及容器启动，停止等功能。
- docker run：执行一个新命令在一个新容器
	-i：交互执行
	

