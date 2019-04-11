___
- FileName: 20190408-kubernetes基础.md
- Author: ihuangch -huangch96@qq.com
- Description: ---
- Create:2019-04-08 15:28:54
___

### 1. Kubernetes特性
Kubernetes是一种用于在一组主机上运行和协同容器化应用程序的系统，旨在提供可预测性、可扩展性
与高可用性的方法来完全管理容器化应用程序和服务的生命周期的平台。  
它具有以下几个重要特性：
- 1.自动装箱，构建与容器之上，基于资源依赖及其他约束自动完成容器部署且不影响其可用性，并通过调度
机制混合关键应用和非关键型应用的工作负载于同一节点以提升资源利用率
- 2.自我修复，支持容器故障后自动重启、节点故障后重新调度容器
- 3.水平扩展，支持通过简单ing了或UI手动水平扩展，以及基于CPU等资源负载率的自动水平扩展机制
- 4.服务发现和负载均衡，Kubernetes通过其附加组件之一的KubeDNS或者CoreDNS为系统内置了服务发现功能，
它为每个Service配置DNS名称，并允许集群内的客户端直接使用此名称发出访问请求，而Service则通过iptables
或ipvs内建了负载均衡机制
- 5.自动发布和回滚，Kubernetes支持灰度更新应用程序或配置信息，它会监控更新过程中应用程序的健康状态，
以确保它不会在同一时刻杀掉所有实例，而此过程中一旦有故障发生，就会立即自动执行回滚操作
- 6.密钥和配置管理，Kubernetes的ConfigMap实现了配置数据与Docker镜像解耦，需要时，仅对配置作出变更而
无须重新构建Docker镜像，这为应用开发部署带来了很大的灵活性。此外对于应用所依赖的敏感数据，若密码等，
Kubernetes专门提供了Secret对象为其解耦，既便利了应用的快速开发和交付，又提供了一定程度上的安全保障。
- 7.存储编排，Kubernetes支持Pod对象按需自动挂载不同类型的存储系统，这包括节点本地存储、公有云服务商的云存储
，以及网络存储系统。
- 8.批量处理执行，除了服务型应用，Kubernetes还支持批处理座椅及CI，如果需要一样可以实现容器故障后恢复。


### 2. Kubernetes概念和术语
#### 1. Master
Master是集群的网关和中枢，负责诸如为用户和客户端暴露API、跟踪其他服务器的健康状态、以最优方式调度工作负载，
以及编排其他组件之间的通信等任务，它是用户或客户端与集群之间的核心联络点，并负责Kubernetes系统的大多数
集中式管控逻辑。
#### 2. Node
Node是Kubernetes集群的工作节点，负责接收来自Master的工作指令并根据指令相应的创建或销毁Pod对象，以及调整
网络规则以合理的路由和转发流量等。  
Kubernetes将所有Node的资源集中在一处形成一台更加强大的“服务器”，在用户将应用部署于其上时，Master会使用调度
算法，将其自动指派至某个特定的Node运行。在Node加入集群或从集群中移除时，Master也会按需重新编排影响到的Pod（
容器）。
#### 3. Pod
Kubernetes 并不直接运行容器，而是使用一个抽象的资源对象来封装一个或者多个容器，这个抽象即为Pod，它是Kuberne
tes的最小调度单元。同一Pod中的容器共享网络名称空间和存储资源，这些容器可经由本地回环接口lo直接通信，但是
彼此之间又在Mount、User及PID等名称空间保持隔离。Pod应该尽量保持小。
#### 4. 资源标签
Label是将资源进行分类的标识符，资源标签其实就是key-value数据。标签旨在制定对象如Pod辨识性的属性，这些属性仅
对用户存在特定的意义。
#### 5. 标签选择器
Label Selector，它是一种根据Label来过滤符合条件的资源对象的机制。
#### 6. Pod控制器
虽然Pod是Kubernetes的最小调度单元，但是用户通常并不会直接部署和管理Pod对象，而是借助于另一类抽象-控制器
（Controller)对其进行管理。用于工作负载的控制器是一种管理Pod生命周期的资源抽象，它们是Kubernetes上的一类
对象，而非单个资源对象，包括ReplicationContraller、ReplicaSet、Deployment、StatefulSet、Job等。
#### 7. 服务资源
Service是建立在一组Pod对象之上的资源抽象，它通过标签选择其选定一组Pod对象，并为这组Pod对象定义一个统一的
固定访问入口（通常是一个IP地址）。若Kubernetes集群中存在DNS附件，就会在Service创建时为其自动配置一个DNS
名称以便客户端进行服务发现。到达Service IP的请求将被负载至其后的端点----各个Pod对象之上，因此Service从本质
上来讲是一个四层代理服务。另外，Service还可以将集群外部流量引入到集群中来。
#### 8. 存储卷
Volume是独立于容器文件系统之外的存储空间，常用于扩展容器的存储空间并为它提供持久存储的能力。Kubernetes集群
上的存储卷大体可分为临时卷、本地卷和网络卷。临时卷和本地卷都位于Node本地，一旦Pod被调度至其他Node，这种
类型的存储卷将无法访问到。因此临时卷和本地卷通常用于数据缓存，持久化的数据则需要放置于持久卷中。

#### 9. Name 和 Namespace
Name是Kubernetes集群中资源对象的标识符，它们的作用域通常是名称空间（Namespace），因此名称空间是名称的额外限定
机制。在同一个名称空间中，同一类型资源对象的名称必须具有唯一性。名称空间通常用于实现租户或项目的资源隔离，从而
形成逻辑分组。

#### 10. Annotation
Annotation(注解)是另一种附加在对象之上的key-value类型的数据，但它拥有更强大的数据容量。Annotation常用于将各种
非标识型元数据附加到对象上，但是不能用于标识和选择对象。

#### 11. Igress
Kubernetes将pod对象和外部网络环境进行了隔离，Pod和Service等对象间的通信都使用其内部专用地址进行，如需要开放某些
Pod对象对象提供给外部用户访问，则需要为其请求流量打开一个通往Kubernetes集群内部的通道，除了Service之外，Ingress
也是这类通道的实现方式之一。


### 2. Kubernetes集群组件
#### 2.1 Master组件
Kubernetes集群控制由多个组件组成，这些组件可以统一运行于单一Master节点，也可以通过多副本的模式同时运行于多个节点，
为Master提供高可用功能。甚至可以运行于Kubernetes集群自身之上。主要有以下组件：
##### 2.1.1 API Server
API Server负责输出RestFul风格的Kubernets API，它是发往集群的所有Rest操作命令的接入点，并负责接收、校验并响应所有
的REST请求，结果状态存储于etcd中。因此，API Server是整个集群的网关。
##### 2.1.2 集群状态存储（Cluster State Store----etcd）
Kubernetes集群的所有状态信息都需要持久存储于存储系统etcd中，etcd是由CoreOS基于Raft协议开发的分布式key-value存储，
可用于服务发现，共享配置和一致性保障等（如数据库主节点选择，分布式锁等）。因此etcd是独立的组件，并不隶属于Kubernetes
集群自身。生产环境中需要部署etcd集群，确保服务的高可用性。  
同时etcd还提供监控（watch）功能，监听推送和变更。在Kubernetes集群中，etcd的变化，会通知API Server，并由其通过
watch API向客户端输出。
##### 2.1.3 控制管理器（Controller Manager）
Kubernetes中，集群级别的大多数功能都是由几个被称为控制器的进程执行实现的，这几个进程被集成于kube-controller-manager
守护进程中。由控制器完成的主要功能包括：
- 生命周期功能：包括Namespace创建和生命周期、Event垃圾回收、Pod终止相关的垃圾回收、级联垃圾回收和Node垃圾回收。
- API业务逻辑：如ReplicaSet执行Pod扩展等

##### 2.1.4 调度器（Scheduler）
Kubernetes是用于部署和管理大规模容器应用的平台，API Server确认Pod对象的创建请求之后，便需要由Scheduler根据集群内各节点
的可用资源状态，以及要运行的容器的资源需求做出调度决策。Kubernetes支持用户自定义调度器


#### 2.2 Node组件
Node负责提供运行容器的各种依赖环境，并接收Master的管理
##### 2.2.1 Kubelet
Node的核心代理程序，Kubelet是运行于工作节点上面的守护进程，它从API Server接收关于Pod对象的配置信息并确保它们处于目标状态。
kubelet会在API Server上注册当前工作节点，定期向Master回报节点资源使用情况，并通过cAdvisor监控容器和节点的资源占用状况
##### 2.2.2 容器运行环境
每个Node都要提供一个容器运行是环境，负责下载镜像并运行容器。Kubelet支持Docker、RKT、cri-o和Fraki等
##### 2.2.3 Kube-proxy
每个工作节点都需要运行一个kube-proxy进程，它能够按需为Service资源对象生成iptables或ipvs规则，从而捕获当前Service的
ClusterIP的流量并转发至正确的后端Pod对象

#### 2.3 核心附件
##### 2.3.1 KubeDNS：
在kubernetes集群中调度运行提供DNS服务的Pod，同一集群中的其他Pod可使用此DNS服务解决主机名。1.11版本后默认使用CoreDNS，
之前版本为kube-dns。SKy-DNS则更早
##### 2.3.2 Kubernetes Dashboard
Kubernetes集群的可以通过Web UI来管理集群中的应用和集群自身
##### 2.3.4 Heapster
容器和节点的性能监控和分析系统。逐渐使用Prometheus结合其他组件取代
##### 2.3.5 Ingress Controller
Service是一组工作于传输层的负载均衡器，而Ingress是在应用层实现的HTTP（s）负载均衡机制。不过，Ingress资源自身并不能进行
“流量穿透”，它仅是
