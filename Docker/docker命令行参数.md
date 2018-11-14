### Docker命令行参数解读
在使用Docker时，需要使用Docker命令行工具docker命令和Docker daemon建立通信。Docker daemon是Docker
守护进程，复制接收并分发执行Docker命令。  

可以使用docker命令或docker help命令来获取docker命令的清单。  

Docker命令的执行一般都需要root权限，因为Docker命令行工具docker和Docker daemon是同一个二进制文件，
而Docker daemon负责接收并执行来自docker的命令，它的运行需要root权限。同时，从Docker 0.5.2版本开始
，Docker daemon默认绑定一个Unix Socker来代替原来的TCP端口，该Unix Socker默认是属于root用户的。因此
，在执行Docker命令需要root权限。  

<div align="center"> <img src="https://github.com/ihuangch/blog/blob/master/Docker/pic/docker-socket.png" /> </div><br>

随着Docker的不断发展，docker的子命令也有很多(run,build,attach)，其中核心子命令(run,exec)还有很多
复杂的可执行选项。对于特定的子命令，可以使用docker CMD --help命令来查看子命令的详细信息，包括子命令
的使用方法和可用的操作参数。  

<div align="center"> <img src="https://github.com/ihuangch/blog/blob/master/Docker/pic/docker-cmd.png"  /> </div><br>

从docker命令使用出发，梳理出命令结构图：  

<div align="center"> <img src="https://github.com/ihuangch/blog/blob/master/Docker/pic/docker-use.png"  /> </div><br>

#### 详细命令及参数
接下来的介绍一些常用的命令参数。
#### 1. Docker环境信息
- docker info：用于检查Docker是否正确安装。如果正确安装，输出Docker配置信息。
- docker version：结合docker info使用，能够提取到足够详细的信息。

#### 2. 容器管理[container]
在新版中container也是docker的一个子命令，用于管理容器，后续可以接相关的容器管理命令，例如：start,ps等  

- docker run：执行一个新命令在一个新容器,是Docker的核心命令之一，用户可以使用的选项很多。
	所有的选项的说明可以通过docker run --help查看

	docker run [options] Image [CMD] [Arg]  

		-i：使用交互模式，始终保持输入流开发  

		-t：分配一个伪终端，一般两个参数结合时使用-it，即在容器中利用打开的终端交互操作  

		--name：指定docker run命令启动的容器的名字，若不指定，Docker为容器随机分配一个名字  

		-c：用于给运行在容器中的所有进程分配CPU的shares值。这是一个相对权重，实际处理能力还和宿主机CPU相关  

		-d：容器在后台运行

		-m：用于限制为容器中所欲进程分配的内存总量，以B，K，M，G为单位  

		-v: 用于挂载一个volume，可以用多个-v参数同时挂载多个volume。  
			volume格式：[host-dir]:[container-dir]:[rw|ro]  

		-p：用于将容器的端口暴露给宿主机的端口。（端口映射），这样可以让外部主机通过宿主机的端口来访问容器内的应用。  
			常用格式：hostport:container-port
		
- docker [container] start|stop|restart|kill [options] CONTAINER：容器启动，停止，重启，杀死容器。[container]在新版中可以使用，
	应该是给相关命令进行分类。用户使用可以使用也可以不用。

		docker run命令可以新建一个容器来运行，对于已经存在的容器，通过start|stop|restart|kill命令来
		启动、停止和重启。使用docker run命令新建一个容器时，会产生一个容器ID，start|stop|restart|kill
		命令容器ID来选择容器(容器ID不输入全部同样可以)。一些情况也可以使用容器名称来选择容器。  

		docker start命令使用-i选项来开启交互模式，始终保持输入流开放。使用-a选项附加标准输入，输出或
		错误输出。此外docker stop和docker restart命令使用-t选项来设定容器停止前的等待时间。

	在交互模式中，在docker命令行中使用exit，会使容器终止。Ctrl+d同样也会使容器终止。

- docker [container] ps：展示容器

		-a：显示所有容器

- docker [container] logs [options] CONTAINER：显示容器的log
- docker [container] atach|exec [options] CONTAINER :进入容器操作
		
		使用atach，在stdin中exit，会导致容器的停止。使用exec不会导致容器停止。

- docker [container] export|import [options] CONTAINER：导出或导入容器
		
		eg:
			# docker export xxxxxCONID > xxfileName.tar
			将导出容器快照到本地文件
			# dcoker /path/to/fileName.tar example/imagerepo
			从容器快照文件中导入为镜像

- docker [container] rm [options] CONTAINER：删除一个处于终止终止状态的容器
	
- docker [container] prune：清理所有处于终止状态的容器

- docker [container] inspect [CONT]：查看容器信息

		
#### 4.镜像管理
image 子命令。同样也可以不使用子命令操作。
- docker pull [OPTIONS] NAME[:TAG|@DIGEST]：获取镜像

		默认：官方仓库最新版本的软件


- docker images | docker image ls：列出已经存在的镜像

- docker image rm [options] <IMage> | docker rmi [options] <IMage>：删除镜像

		可以通过镜像短ID，镜像长ID，镜像名或者镜像摘要来删除

- docker search <IMage>：搜索镜像

#### 5.数据卷管理
volume 子命令。在容器中管理数据主要有两种方式：
- 数据卷（volumes）
- 挂载主机目录（Bind mounts）
##### 数据卷
数据卷是一个可以提供一个或者多个容器使用的特殊目录，它绕过UFS，可以提供很多游泳的特性
- 1.数据卷可以在容器间共享和重用
- 2.对数据卷的修改会立即生效
- 3.对数据卷的更新，不会影响镜像
- 4.数据卷会默认一直存在，即使容器被删除。

**数据卷的使用，类似与Linux下对于目录或者文件进行mount，镜像中的被指定为挂载点的目录中的文件会被隐藏，能显示看的是挂载的数据卷**

- docker volume create my-vol：创建一个数据卷
- docker volume ls：查看所有的数据卷
- docker volume inspect my-vol：查看指定数据卷的信息
在使用docker run命令的时候，使用--mount标记将数据卷挂载到容器里。在一次docker run中可以挂载多个数据卷。  
```
# docker run -d -P \
	--name web \        					# 指定容器名称
	# -v my-vol:/webapp \ 					# 挂载数据卷
	--mount source=my-vol,target=/webapp \  #挂载数据卷
	training/webapp \ 						#镜像名称
	python app.py 							#执行的命令
```

- docker volume rm <vol-name>：删除某个数据卷
数据卷是被设计用来持久化数据的，它的生命周期独立与容器，Docker不会在容器被删除后自动删除数据卷，
并且也不存在垃圾回收这样的机制来处理没有任何容器引用的数据卷。如果需要在删除容器的同时移除数据卷。
可以在删除容器时使用docker rm -v这个命令。无主的数据卷可能会占据很多空间，要清理使用以下命令。
- docker volume pure：清楚所有无主数据卷

##### 挂载主机目录作为数据卷
使用--mount选项可以指定挂载一个本地主机的目录到容器中。
```
# docker run -d -P \ 					# 后台运行，并指定随机端口
	--name web \
	# -v /src/webapp:/opt/webapp \
	--mount type=bind,source=/src/webapp,target=/opt/webapp \
	# --mount type=bind,source=/src/webapp,target=/opt/webapp,readonly \
	training/webapp \
	python app.py
```
本地目录的路径必须时绝对路径，以前使用-v参数时入股哦本地目录不存在Docker会自动为你创建一个文件夹。  
现在使用--mount时，如果本地目录不存在，Docker会报错。  
Docker挂载主机目录的默认权限时读写，也可以通过增加readonly指定为只读。  
加了readonly后，就挂载为只读来了。如果在容器内/opt/webapp目录新建文件，会报错。  

##### 挂载一个本机主机文件作为数据卷
使用--mount也可以从主机挂载单个文件到容器中
```
# docker run --rm -it \ 			# --rm:当容器退出时，自动删除容器
	# -v /tmp/filename:/root/filename \
	--mount type=bind,source=/tmp/filename,target=/root/filename \
	ubuntu:17.10 \
	bash
```

#### 6.基础网络管理
Docker允许通过外部访问容器或者容器互联的方式提供通信。
##### 外部访问容器
容器中可以运行一些网络应用，如果需要让外部主机能够访问这些内容，可以通过-P或者-p参数来指定端口映射。  

- 使用-p则可以指定要映射的端口，并且，在一个指定的端口上只可以绑定一个容器。  
	支持的格式有：ip:hostPort:containerPort | ip::containerPort | hostPort:containerPort


```
docker run -p 80:8080 -d tarining/webapp python app.py
# 默认绑定本地所有接口上的所有地址
docker run -p 127.0.0.1::8080 -d tarining/webapp python app.py
# 映射到指定地址的任意端口
docker run -p 127.0.0.1:80:8080 -d tarining/webapp python app.py
# 映射到指定地址的指定端口
docker run -p 127.0.0.1:80:8080/udp -d tarining/webapp python app.py
# 映射时指明协议
```
- docker port CONTAINER_NAME [port]：查看当前映射的端口配置，也可以查看到绑定的地址

**注意：**
- 容器有自己的内部网络和ip地址（使用docker inspect可以获取所有的变量，Docker还可以有一个可变的网络配置）
- -p参数可以使用多次用来绑定多个端口

##### 容器互联
随着Docker网络的完善，建议将容器加入自定义的Docker网络来连接多个容器，而不是使用--link参数。  
network子命令可以管理Docker网络  

###### 创建网络
- docker network create -d bridge my-net：创建一个新的Docker网络。-d指明网络的类型

###### 连接容器
- docker run -it --rm --name busybox1 --network my-net busybox sh
	运行一个容器并加入到my-net网络

##### 配置DNS
自定义配置容器的主机名和DNS。  
Docker利用虚拟文件来挂载容器的3个相关配置文件。  
这种机制可以让宿主主机DNS信息发生更新后，所有Docker容器的DNS配置通过/etc/resolv.conf文件立刻得到更新。

配置全部容器的DNS，也可以在/etc/docker/daemon.json文件中增加以下内容来设置:  
```
{
"dns":[
	"114.114.114.114",
	"8.8.8.8"
	]
}
```



	

