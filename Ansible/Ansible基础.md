___
- FileName: Ansible基础.md
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



