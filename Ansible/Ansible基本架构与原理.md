___
- FileName: Ansible基本架构与原理.md
- Author: ihuangch -huangch96@qq.com
- Description: ---
- Create:2018-11-15 19:34:14
___

### Ansible介绍
##### 常用自动化运维工具：
Ansible：python编写，中小型应用环境  

Saltstack：python编写，一般需要agent，执行效率更高  

Puppet：ruby编写，大型公司使用  


##### Ansible功能：
1、命令传输  
2、命令执行，应用部署，配置管理，任务流编排  

##### Ansible特性
1、模块化：调用特定的模块，完成特定的服务  
2、基于python语言实现，有Paramiko，PyYaml，Jinja2三个关键模块  
3、支持自定义模块，可以使用任何编程语言编写模块  
4、部署简单，基于python和ssh，无需agent  
5、安全，基于OpenSSH  
6、基于playbook编排任务  
7、幂等性：一个任务执行一遍和n遍效果一样，不因重复执行带来意外情况  
8、yaml格式编排任务，支持丰富的数据结构  
9、较强大的多层解决方案

##### Ansible主要组成部分
- ansible playbooks：任务剧本，编排定义ansible任务集的配置文件，由ansible顺序依次执行，通常是json格式的yaml文件
- inventory：ansible管理主机的清单/etc/ansible/hosts
- modules：ansible执行命令的功能模块，多数为内置核心模块，也可以自定义
- plugins：模块功能的补充，如连接类型插件，循环插件，变量插件，过滤插件
- api：提供第三反程序调用的应用程序编程接口
- ansible：组合inventory，api，modules，plugins，可以理解为ansible命令工具，核心执行工具

<div align="center"> <img src="https://github.com/ihuangch/blog/blob/master/Ansible/pic/ansible-arch.png" /> </div><br>

##### Ansible命令执行来源：
- user：普通用户
- cmdb：配置管理数据库，API调用
- public/private cloud api调用
- user->ansible playbook -> ansible

<div align="center"> <img src="https://github.com/ihuangch/blog/blob/master/Ansible/pic/ansible-work.png" /> </div><br>

###### 利用Ansible实现管理的方式：
Ad-Hoc：即ansible命令，主要用于临时使用场景
ansible-playbook用于长期规划好的，大型项目的场景，需要有前提的规划


**注意事项:**
- 1、ansible的主机一般称为主控端，中控，master或者堡垒机
- 2、主控端python版本2.6以上
- 3、被控端python版本小于2.4需要安装python-simplejson
- 4、被控端如果开启SELinux需要安装libselinux-python
- 5、Windows不能作为主控端



#### Ansible安装：
1. yum安装
2. 编译安装
3. pip安装
4. git安装

#### 相关文件
- /etc/ansible/ansible.cfg：主配置文件，配置ansible工作特性
- /etc/ansible/hosts：主机清单
- /etc/ansible/roles/：存放角色的目录
- /usr/bin/ansible：主程序，临时命令执行工具，链接文件
- /usr/bin/ansible-doc：查看帮助文档
- /usr/bin/ansible-galaxy：下载上传优秀代码或者roles模块的官网平台
- /usr/bin/ansible-playbook：定制自动化任务，编排剧本工具
- /usr/bin/ansible-pull：远程执行命令的工具
- /usr/bin/ansible-vault：文件加密工具
- /usr/bin/ansible-console：基于console界面与用户交互执行工具


#### Ansible系列命令介绍
##### ansible命令
ansible <host-pattern> [-m module_name] [-a args]  
	
	--version：显示版本
	[group] --list-hosts：列出主机
	-m module_name：指定模块
	-v,-vv,-vvv：详细过程
	-k,--ask-pass：提示输入密码，默认基于key验证
	-K,--ask-become-pass：提示输入sudo口令
	-C,--check：检查，并不执行
	-T,--timeout=#：执行命令超时时间，默认10s
	-u,--user=Remote_User：执行远程命令的用户
	-b,--become：代替旧版的sudo切换

ansible的Host-patter：  

	all：表示所有主机
	*：通配符
	:：或关系 'web1:web2'，在web1组或者在web2中
	:&：与关系 'web1:&web2'，在web1组并且在web2中
	:!：非关系 'web1:!web2'，在web1中，不在web2中。只能使用单引号
	综合逻辑
	正则表达式等


##### ansible-doc命令
	
	ansible-doc；查看帮助
	ansible-doc -l：列出当前的模块列表
	ansible-doc module_name：显示模块的帮助
	ansible-doc -s module_name：简单显示模块信息


##### ansible-galaxy命令
连接https://galaxy.ansible.com下载相应的roles  
	
	ansible-galaxy list：列出所有已经安装galaxy
	ansible-galaxy install xxx_galaxy：安装需要的galaxy
	ansible-galaxy remove xxx_galaxy：删除galaxy

##### ansible-pull命令
推送命令至远程，效率无限提升，对运维人员的要求比较高

##### ansible-vault命令
加密playbook文件

	ansible-vault encrypt xxx.yml 加密
	ansible-vault decrypt xxx.yml 解密

##### ansible-consule命令
交互式工具

##### ansible-playbook命令 
执行yaml文件，通过剧本进行操作

	ansible-playbook -C/--check xxx.yml：检查，不修改远程主机

#### Ansible执行过程
1. 加载自己的配置文件/etc/ansible/ansible.cfg
2. 加载自己对应的模块文件，如command，通过ansible-doc可以查看
3. 通过ansible将模块或者命令生成对应的临时py文件，并将文件传输至远程服务器的对应执行用户$HOME/.ansible/tmp/ansible-tmp-数字/xxx.py文件
4. 给文件+x执行
5. 执行并返回结果
6. 删除临时py文件，sleep 0退出

- 执行状态
	
	
	绿色：执行成功并且没有改变的操作
	黄色：执行成功并且对目标主机做了变更的操作
	红色：执行失败




