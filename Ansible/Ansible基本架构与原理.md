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

<div align="center"> <img src="https://github.com/ihuangch/blog/blob/master/Ansible/pic/ansible-arch.png" /> </div><br





