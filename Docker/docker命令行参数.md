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
- docker run：执行一个新命令在一个新容器,是Docker的核心命令之一，用户可以使用的选项很多。
	所有的选项的说明可以通过docker run --help查看

	docker run [options] Image [CMD] [Arg]  

		-i：使用交互模式，始终保持输入流开发  

		-t：分配一个伪终端，一般两个参数结合时使用-it，即在容器中利用打开的终端交互操作  

		--name：指定docker run命令启动的容器的名字，若不指定，Docker为容器随机分配一个名字  

		-c：用于给运行在容器中的所有进程分配CPU的shares值。这是一个相对权重，实际处理能力还和宿主机CPU相关  

		-m：用于限制为容器中所欲进程分配的内存总量，以B，K，M，G为单位  

		-v: 用于挂载一个volume，可以用多个-v参数同时挂载多个volume。  
			volume格式:[host-dir]:[container-dir]:[rw|ro]  

		-p：用于将容器的端口暴露给宿主机的端口。（端口映射），这样可以让外部主机通过宿主机的端口来访问容器内的应用。  
			常用格式:hostport:container-port
- docker start|stop|restart|kill：  

	docker run命令可以新建一个容器来运行，对于已经存在的容器，通过start|stop|restart|kill命令来
	启动、停止和重启。使用docker run命令新建一个容器时，会产生一个容器ID，start|stop|restart|kill
	命令容器ID来选择容器。一些情况也可以使用容器名称来选择容器。  

	docker start命令使用-i选项来开启交互模式，始终保持输入流开放。使用-a选项附加标准输入，输出或
	错误输出。此外docker stop和docker restart命令使用-t选项来设定容器停止前的等待时间。



	

