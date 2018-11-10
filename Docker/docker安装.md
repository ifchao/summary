### Docker安装
Docker是一个轻量级虚拟化技术，它具备传统虚拟机无与伦比的优势。更简易的安装和使用方式，
更快的速度、服务集成和开发流程自动化，都使docker被广大技术爱好者青睐。

Docker分为CE和EE两大版本。  
CE(社区版)，免费，支持周期7个月。  
EE(企业版)，强调安全付费使用，支持周期24个月。  

在这里主要介绍一下CE:
Doceker CE分为stable，test，nightly三个更新频道。每6个月发布一个stable。  
(1809,1903,1909...)  

官网上有各种环境的安装指南。这里主要介绍Docker CE在CentOS上的安装。  

##### 安装Docker的基本要求:
- Docker只支持64位CPU架构的计算机，目前不支持32位CPU
- 建议Linux内核版本位3.10及以上
- Linux内核需要开启cgroups和namespace功能
- 对于非Linux内核的平台，如Windows和OS X，需要安装使用Boot2Docker

##### 具体的安装步骤:(CentOS)
#### 警告:
1. 下面操作是在root用户下进行。你也可以不使用root用户，使用sudo也是ok的。  
2. 请不要在没有配置yum源的情况下直接使用yum命令安装Docker。
###### 系统要求:
Docker CE支持64位版本CentOS7，并且要求内核版本不低于3.10。CentOS 7 满足最低内核的要求，
但是由于内核版本比较低，部分功能（如overlay2存储层驱动）无法使用，并且部分功能可能不太
稳定。  

###### 1.卸载旧版本:
旧版本的Docker称为docker或者docker-engine，使用以下命令卸载旧版本：
```
yum remove docker \
	docker-client \
	docker-client-latest \
	docker-common \
	docker-latest \
	docker-latest-logrotate \
	docker-logrotate \
	docker-selinux \
	docker-engine-selinux \
	docker-engine
```

###### 2.安装依赖包:
```
yum install -y yum-utils \
	device-mapper-persistent-data \
	lvm2
```
yum-utils：管理repository及扩展包的工具 (主要是针对repository)，使用yum-config-manager需要安装yum-utils包。  
device-mapper-persistent-data：设备映射工具。  
lvm2：lvm管理工具，也有设备映射的作用。  

###### 3.安装yum源:
```
yum-config-manager \
	--add-repo \
	https://mirrors.ustc.edu.cn/docker-ce/linux/centos/docker-ce.repo

# 官方源
# yum-config-manager \
# 	  --add-repo \
#	  https://download.docker.com/linux/centos/docker-ce.repo
```
测试版本:
```
yum-config-manager --enable docker-ce-test
```
每日构建版本:
```
yum-config-manager --enable docker-ce-nightly
```

###### 4.安装Docker CE:
```
yum makecache 
yum install docker-ce
```

###### 6.启动Docker CE:
```
systemctl enable docker
systemctl start docker
```

###### 5.建立docker用户组:
默认情况下，docker命令会使用Unix socket与Docker引擎通信。只有root用户和docker组的用户
可以访问Docker引擎的Unix socket。出于安全考虑，一般Linux系统不会直接使用root用户。
因此更好的做法是将需要使用docker的用户加入docker用户组里面。  

```
groupadd docker
usermod -Ga docker USER_Name
```

###### 6.测试docker是否安装正确:
```
docker run hello-world

Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
ca4f61b1923c: Pull complete
Digest: sha256:be0cd392e45be79ffeffa6b05338b98ebb16c87b255f48e297ec7f98e123905c
Status: Downloaded newer image for hello-world:latest
Hello from Docker!
This message shows that your installation appears to be working correctly.
To generate this message, Docker took the following steps:
1. The Docker client contacted the Docker daemon.
2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
(amd64)
3. The Docker daemon created a new container from that image which runs the
executable that produces the output you are currently reading.
4. The Docker daemon streamed that output to the Docker client, which sent it
to your terminal.
To try something more ambitious, you can run an Ubuntu container with:
$ docker run -it ubuntu bash
Share images, automate workflows, and more with a free Docker ID:
https://cloud.docker.com/
For more examples and ideas, visit:
https://docs.docker.com/engine/userguide/
```
如果输出以上信息，则说明安装成功。

###### 7.配置国内镜像
在/etc/docker/daemon.json中写入如下内容:(如果文件不存在，则新建文件)
```
{
"registry-mirrors":[
	"https://registry.docker-cn.com"
	]
}
```
然后重新启动服务:  
```
systemctl daemon-reload
systemctl restart docker
```

###### 7.添加内核参数:
默认配置下:  
如果在CentOS中使用Docker CE看到下面这些警告信息:
```
WARNING: bridge-nf-call-iptables is disabled
WARNING: bridge-nf-call-ip6tables is disabled
```
添加内核配置参数启用这些功能:
vim /etc/sysctl.conf
```
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
sysctl -p     # 重载sysctl.conf
```

#### 参考文档
- [Docker官方CentOS安装文档](https://docs.docker.com/engine/installation/linux/docker-ce/centos/)
