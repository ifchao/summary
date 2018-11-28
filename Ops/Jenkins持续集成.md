___
- FileName: Jenkins持续集成集成.md
- Author: ihuangch -huangch96@qq.com
- Description: ---
- Create:2018-11-22 11:45:52
___

### 1 相关概念
#### 1.1 持续集成(Continuous Integration)
大师Mratin Fowler对持续集成是这样定义的：持续集成是一种软件开发实践，即团队开发成员经常集成
他们的工作，通常每个成员至少集成一次，也就意味着每天可能会发生多次集成。每次集成都通过自动化
的构建（包括编译，发布，自动化测试）来验证，从而尽快的发现集成错误。许多团队发现这个过程可以
大大减少集成的问题，让团队能够更快的开发内聚的软件。  
**主要好处:**
- 1、快速发现错误。每完成一点更新，就集成到主干，可以快速发现错误，定位错误也比较容易。  
- 2、防止分支大幅偏离主干。如果不是经常集成，主干又在不断更新，会导致以后集成的难道变大，甚至难以集成。  
**持续集成的目的:**
- 让产品可以快速迭代，同时还能保持高质量。它的核心措施是，代码集成到主干之前，必须通过自动化测试。只要有一个测试用例失败，就不能集成。

<div align="center"> <img src="https://github.com/ihuangch/blog/blob/master/Ops/pic/ci.png" /> </div><br> 

总的来说：就是持续集成就是每天都把代码集成到同一个分支，然后经过编译，测试，打包之后将程序
保存(在一个新的仓库中)。

#### 1.2 持续交付(Continuous Delivery)
持续交付指的是：频繁的将软件的新版本，交付给质量团队或者用户，以供评审。如果评审通过代码就
进入生产阶段。  
持续交付可以看作持续集成的下一步。在持续集成的基础上，将集成后的代码，部署到更贴近真实运行
环境的（类生产环境）中。比如，我们完成单元测试后，可以把代码部署到连接数据库的staging环境中
进行更多的测试。如果代码没有问题，可以继续手动部署到生产环境中。  
持续交付强调的是，不管怎么更新，软件是随时随地的可以交付的。  

<div align="center"> <img src="https://github.com/ihuangch/blog/blob/master/Ops/pic/cd1.png" /> </div><br> 

#### 1.3 持续部署(Continuous Deployment)
持续部署是持续交付的下一步，指的是代码通过评审以后，自动部署到生产环境中。  

<div align="center"> <img src="https://github.com/ihuangch/blog/blob/master/Ops/pic/cd2.png" /> </div><br> 


### 2 Jenkins
Jenkins是一个独立的开源自动化服务器。可以用于自动化各种任务。如构建，测试和部署软件。  
#### 2.1 开发流程
##### 2.1.1 传统开发上线流程
需求分析->原型设计->开发代码->提交测试->内网部署->确认上线->备份数据(外网)->外网更新->最终测试  
如果发现外网部署的代码有移除，需要及时回滚。  

<div align="center"> <img src="https://github.com/ihuangch/blog/blob/master/Ops/pic/code-old.png" /> </div><br> 

##### 2.1.2 主流开发上线流程

<div align="center"> <img src="https://github.com/ihuangch/blog/blob/master/Ops/pic/code-new.png" /> </div><br> 

通过Hudson/Jenkins工具平台实现全自动部署+测试，Jenkins是一个可扩展的持续集成引擎，是一个开源项目
目的提供一个开发易用的软件平台，使软件的持续集成变成可能。Jenkins非常易于安装和配置，简单易用。  
简单来说方便如下人员:  
1. 开发人员：写好代码，不需要自己进行源码编译，打包等工作，直接将代码分支放在svn/git仓库即可。  
2. 运维人员：减轻人工干预的错误率，同时解放运维人员繁杂的上传代码，手动备份，更新。
3. 测试人员：可以通过jenkins进行简单的代码及网站测试。  
持续集成组件：  
1. 一个自动构建过程，包括自动编译，分发，部署和测试。
2. 一个代码存储库，即需要版本控制软件来保障代码的可维护性，同时作为构建过程的素材库，如svn，git。
3. 一个jenkins持续集成服务器。

#### 2.2 安装Jenkins
##### 2.2.1 安装要求：  
1. Java8环境
2. 1Gram以上
##### 2.2.2 安装Java8
通过rpm包安装。  
通过oracle官网下载jdk8相关版本
```
# rpm -ivh jdk-8u191-linux-x64.rpm
# java -version                     # 验证是否安装成功，查看对应版本
# cat /etc/profile.d/java8.sh       # 此文件自己创建

[root@www82 ~]# cat /etc/profile.d/java8.sh 
JAVA_HOME=/usr/java/jdk1.8.0_191-amd64/
JRE_HOME=/usr/java/jdk1.8.0_191-amd64/jre
PATH=$PATH:$JAVA_HOME/bin:$JRE_HOME/bin
CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib
export JAVA_HOME JRE_HOME PATH CLASSPATH

# ls /usr/java/                     # 判断JAVA_HOME等路径是否正确
# source /etc/profile.d/java8.sh    # 重新载入配置文件
# echo $PATH						# 判断环境变量是否加入成功
[root@www82 ~]# echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/usr/java/jdk1.8.0_191-amd64//bin:/usr/java/jdk1.8.0_191-amd64/jre/bin:/root/bin
```
##### 2.2.3 安装Jenkins
```
wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat/jenkins.repo
rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key
yum install jenkins
systemctl start jenkins  #
ss -ntl | grep 8080
```

##### 2.2.4 Jenkins-Maven
maven工具，对ant工具的进一步改进，在make工具中，如果需要编译某些源文件，首先安装编译器等工具，
有时候需要不同版本的编译器，在java编译器需要不同的各种包的支持，如果把每个包都下载下来，在
makefile中进行配置制定，当需要的包很多的时候，很难管理。  
maven像make一样，是一个构建(build)工具，maven可以控制编译，控制连接，可以生成各种报告，进行测试，
通过脚本对maven进行控制，实现这些流程控制。  
maven项目对象模型POM(project object model)可以通过一小段描述信息，来管理项目的构建，报告和文档的
软件项目管理工具。Maven除了以程序构建能力为特色外，还提供高级项目管理工具。  
pom是maven项目中的文件，使用xml表示，名称叫做pom.xml。在maven中，当谈到project的时候，不仅仅是
一堆包含代码的文件。一个project往往包含一个配置文件，包括了与开发者有关的缺陷跟踪系统，组织，与
许可，项目的url，项目依赖，以及其他。包含了所有与这个项目相关的东西。事实上，在maven世界中，
project可以什么都没有，甚至没有代码，但是必须包含pom.xml文件。  

