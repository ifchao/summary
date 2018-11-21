___
- FileName: Ansible-Playbook.md
- Author: ihuangch -huangch96@qq.com
- Description: ---
- Create:2018-11-19 19:44:38
___

### 什么是playbook
playbook是一个或多个'play'组成的列表。  
play的主要功能在于将事先归并为一组的主机装扮成事先通过ansible中的task定义好的角色。从根本上
来讲，所谓task无非是调用ansible的一个module。  
将多个play组织在一个playbook中，即可以让它们连同事先编排机制同唱一台大戏。  
playbook采用yaml语言编写。  

### playbook核心元素
- hosts：执行的远程主机列表
- tasks：任务集
- varniables：内置变量或自定义变量在playbook中调用
- templates：模板，可替换模板文件中的变量并实现一些简单逻辑的文件
- handlers和notity：结合使用，由特定条件触发的操作，满足条件方才执行，否则不执行
- tags：标签，指定某条任务执行，用于选择运行playbook中的部分代码，ansible具有幂等性，因此会跳过没有变化的部分，即便如此，有些代码为测试其确实没有发生变化的时间会很长。此时，如果确信没有变化，就可以通过tags跳过此些代码片段


##### hosts:
主机列表  
格式：  
hosts: hostName|GroupName|host-partern  
hosts支持ansible命令中使用的匹配主机列表的方式。  

##### tasks:
任务列表  
格式：  
1. anction:module arguments
2. moudle:arguments（建议使用）
shell和command命令，无需key=value模式  
shell:/usr/bin/echo 'hello world'  

如果命令或者脚本的退出码不为0，可以使用如下方式替代：  
```
	tasks:
	  - name: run this command and ignore the result
	    shell: /usr/bin/cmd || /bin/true
```
或者使用ignor_errors来忽略错误信息：
```
	tasks:
	  - name: run this command and ignore the resule
	    shell: /usr/bin/cmd
		ignore_errors: True
```

##### handlers和notify结合使用触发条件
Handlers： tasks列表，这些task与前面的task并没有本质上的不同，用于当关注的资源发生变化时，才
会采取一定的操作。  
Notify：此anction可用于在每个play的最后被触发，这样可以避免多次有改变发生时每次都执行指定的
操作，仅在所有的变化发生完后，一次性的执行指定的操作。在notify中列出的操作称为handler，也
即notify中调用handler中定义的操作。  
```
---
- hosts: 192.168.56.112
  remote_user: root

  task:
    - name: copy conf file
	  copy: src=/root/httpd.conf dest=/etc/httpd/conf/ backup=yes
	  notify: restart service
	- name: start service
	  service: name=httpd state=started enable=yes

  handlers:
    - name: restart service
	  service: name=httpd state=restarted enabled=yes
```
在上面的yml文件中，如果httpd服务已经启动，修改httpd.conf，再通过copy模块，复制到远程主机的
时候，httpd服务不会重启，这个时候就需要notify这个条件触发。notify后面的值就是handlers中
name的名称。  

##### tags
标签：任务可以通过'tags'打标签，而后可以再ansible-playbook命令上使用-t选项进行调用
```
---
- hosts: 192.168.56.112
  remote_user: root

  tasks:
    - name: copy conf file
	  copy: src=/root/httpd.conf dest=/etc/httpd/conf/ backup=yes
	- name: restart servie 
	  service: name=httpd state=restart enable=yes
	  tags: rshttpd
```
ansible-playbook -t rshttpd xxx.yml

##### varniables
变量，playbook中变量的使用：  
变量名：仅能由字母，数字和下划线组成，而且只能以字母开头  
通过{{ var }}，来引用变量  

变量来源：
1. ansible setup facts 远程主机的所有变量，且只能以字母开头
2. 在/etc/ansible/hosts中定义
普通变量：主机组中主机单独定义，优先级高于公共变量  
公共组变量：针对主机组中所有主机定义统一变量
3. 通过命令行指定变量，优先级最高
ansible-playbook -e varname=value
4. 在playbook中定义
```
vars:
  - var1: value1
  - var2: value2
```
5. 在独立的yml文件中定义
6. 在role中定义

eg:  
<div align="center"> <img src="https://github.com/ihuangch/blog/blob/master/Ansible/pic/ansible-var.png" /> </div><br>
```
---
- hosts: test1
  remote_user: root

  tasks:
    - name: set hostname
	  hostname: name={{ nodename }}{{ http_port }}.{{ domainname }}
```

##### templates
template也是ansible中的一个模块
模板，文本文件，嵌套有脚本（使用模板编程语言编写）  
Jinja2语言，
