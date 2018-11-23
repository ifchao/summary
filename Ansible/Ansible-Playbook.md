___
- FileName: Ansible-Playbook.md
- Author: ihuangch -huangch96@qq.com
- Description: ---
- Create:2018-11-19 19:44:38
___
#
#
### 1. 什么是playbook
___
playbook是一个或多个'play'组成的列表。  
play的主要功能在于将事先归并为一组的主机装扮成事先通过ansible中的task定义好的角色。从根本上
来讲，所谓task无非是调用ansible的一个module。  
将多个play组织在一个playbook中，即可以让它们连同事先编排机制同唱一台大戏。  
playbook采用yaml语言编写。  

### 2. playbook核心元素
___
- hosts：执行的远程主机列表
- tasks：任务集
- varniables：内置变量或自定义变量在playbook中调用
- templates：模板，可替换模板文件中的变量并实现一些简单逻辑的文件
- handlers和notity：结合使用，由特定条件触发的操作，满足条件方才执行，否则不执行
- tags：标签，指定某条任务执行，用于选择运行playbook中的部分代码，ansible具有幂等性，因此会跳过没有变化的部分，即便如此，有些代码为测试其确实没有发生变化的时间会很长。此时，如果确信没有变化，就可以通过tags跳过此些代码片段

<div align="center"> <img src="https://github.com/ihuangch/blog/blob/master/Ansible/pic/playbook.png" /> </div><br>

#### 2.1 hosts:
主机列表  
格式：  
hosts: hostName|GroupName|host-partern  
hosts支持ansible命令中使用的匹配主机列表的方式。  

#### 2.2 tasks:
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

#### 2.3 handlers和notify结合使用触发条件
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

#### 2.4 tags
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

#### 2.5 varniables
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
  var1: value1
  var2: value2
```

5. 在独立的yml文件中定义
6. 在role中定义

eg:  
<div align="center"> <img src="https://github.com/ihuangch/blog/blob/master/Ansible/pic/playbook-var.png" /> </div><br>

```
---
- hosts: test1
  remote_user: root

  tasks:
    - name: set hostname
	  hostname: name={{ nodename }}{{ http_port }}.{{ domainname }}
```

#### 2.6 templates
template也是ansible中的一个模块
模板，文本文件，嵌套有脚本（使用模板编程语言编写）  
Jinja2语言:  

	字面量：  
		字符串：使用单引号或双引号
		数字：整数，浮点数
		列表：[item1, item2, ...]
		元组：(item1, item2, ...)
		字典；{key1:value1, key2:value2, ....}
		布尔型：true/fales
	算术运算：+，-，*，/，//，%，**  
	比较运算：==，!=，>，>=，<，<=
	逻辑运算：and，or，not
	流表达式：for，if，when


<div align="center"> <img src="https://github.com/ihuangch/blog/blob/master/Ansible/pic/template.png" /> </div><br>

由于ansible是由jinja2来实现template系统，所以使用*.j2的文件后缀名。
每个模板文件一般为xxxx.j2  
只需要事先定义变量和模板，就可以用它动态产生远端的shell scripts、设定配置文件等
。换句话说，我们可以用一份teplate来产生开发，测试，和正式环境等不同环境的设定。

#### 2.7 roles
Ansible自1.2版本引入的新特性，用于层次性，结构化的组织playbook，roles能够根据层次型结构自动
装载变量文件、tasks以及handler等。要使用roles只需要在playbook中使用include指令即可。简单来讲
，roles就是通过分别将变量，文件，任务，模板以及处理器放置于单独的目录中，并可以便捷的include
他们的一种机制。角色一般用于基于主机构建服务的场景中，单也可以是用于构建守护进程等场景中。  
复杂场景：建议使用roles，代码复用度高。如：
	
	变更指定主机或主机组
	命名不规范维护和传承成本大
	某些功能需要多个playbook，通过include实现



#### 2.8 使用示例
包含了一个play的playbook的例子：  

```
---
- hosts: webservers
  vars:
    http_port: 80
	max_clients: 200
  remote_user: root
  tasks:
  - name: ensuer apache is at the latest version
    yum:
	  name: httpd
	  state: latest
  - name: write the apache config file
    template:
	  src: /srv/httpd.j2
	  dest: /etc/httpd.conf
	notify:
	- restart apache
  - name: ensuer apache is running
    service:
	  name: httpd
	  state: started
  handlers:
    - name: restart apache
	  service:
	    name: httpd
		state: restarted
```

下面是包含了多个play的playbook

```
---
- hosts: webservices
  remote_user: root

  tasks:
    - name: ensure apache is at the latest version
	  yum:
	    name: httpd
		state: latest
	- name:
	  template:
	    src: /srv/httpd.j2
		dest: /etc/httpd.conf

- hosts: databases
  remote_user: root

  tasks:
    - name: ensuer postgresql is at the latest version
	  yum:
	    name: postgresql
		state: latest
	- name: ensuer theat postgresql is started
	  service:
	    name: postgresql
		state: started
```

上面两个例子皆摘自Ansible官方文档


### 3. Playbook重要元素详解
___
这部分详解介绍Playbook的varniables，template，和roles等  

#### 3.1 varniables
关于变量命名规则前面已经提到，只能由字母，数字和下划线组成，而且只能以字母开头  
##### 3.1.1 定义变量在主机清单中/etc/ansible/hosts文件  
```
# 组内主机单独变量
[host1]
192.168.56.112 http_port=8080
192.168.56.113 http_port=8090

# 公共组变量
[host1:vars]
nodename=www
domainname=hcq.com
```

##### 3.1.2 定义变量在文件中xxxx.yml  
```
---
# 变量文件无需特别格式，把变量名表示即可
http_port: 8080
hostname: www
domainname: hcq.com
```

```
---
- hosts: webser
  remote_user: root
  vars:
    hostname: www2        # 优先级比外部文件高
  vars_file:
    - /path/to/var/xxx.yml
```

##### 3.1.3 定义变量在playbook执行文件中

```
---
- hosts: webser
  remote_user: root
  vars: 
    hostname: www3
```

##### 3.1.4 ansible setup fect中获取远程主机变量

```
# 查看远程主机的变量
ansible all -m setup [-a 'filter=xxxxx']
[root@www82 ~]# ansible 192.168.56.113 -m setup -a "filter=ansible_distribution*"
192.168.56.113 | SUCCESS => {
"ansible_facts": {
        "ansible_distribution": "CentOS", 
		    "ansible_distribution_file_parsed": true, 
			"ansible_distribution_file_path": "/etc/redhat-release", 
			"ansible_distribution_file_variety": "RedHat", 
			"ansible_distribution_major_version": "7", 
			"ansible_distribution_release": "Core", 
		    "ansible_distribution_version": "7.4.1708"
    }, 
    "changed": false
}

# xxx.yml配置文件
---
- hosts: webser
  remote_user: user

  tasks:
    - name: create file
	  file: name={{ ansible_distribution }}.abs state=touch

# xxx.yml
--- 
- hosts: webser
  remote_user: user

  tasks:
    - name: install httpd
	  yum: name=httpd
	  when: ansible_distribution == "CentOS"
```

##### 3.1.5 在roles中定义变量  
在role中定义变量，实际和在文件中定义变量也是类似。  

##### 3.1.6 通过命令行选项指定变量

```
ansible-playbook -e 'varname=value'
```

##### 3.1.7 在playbook使用变量的一些细节
```
---
- hosts: webser
  remote_user: root

  vars:
    time: "{{ var1 }}/2"   # 需要加上双引号，对变量进行算术运算
```
**注意：**
变量的优先级：
- 命令行优先级最高
- 主机清单中定义的连接变量
- 大多数其他变量(play中的变量，included变量，role中的变量)
- 主机清单中定义的其他变量
- 系统发现的facts
- role默认变量

#### 3.2 Templates
通过模板可以轻松的修改配置文件或者修改文件内容  
官方文档中还有很多template的高级用法，包括过滤器等  

##### 3.2.1 template for语句
```
{% for vhost in nginx_vhost %}
server{
listen {{ vhost.listen | default('80 default_server') }};
}
{% endfor %}


# 示例
# //temnginx.yml
---
- hosts: webser
  remote_user: root
  vars:
    nainx_vhosts:
	  - web1
	  - web2
	  - web3
  tasks:
    - name: template config
	  template: src=nginx.conf.j2 dest=/etc/nginx/nginx.conf

# //template/nginx.conf.j2
{% for vhost in nginx_vhosts %}
server{
  listen {{ vhost }}
}
{% endfor %}

# 生成的结果：
server{
  listen web1
}
server{
  listen web2
}
server{
  listen web3
}
```

##### 3.2.2 template if语句
```
{% if vhost.server_name is definded %}
server_name {{ vhost.server_name }}
{% endif %}
```

#### 3.3 roles
##### 3.3.1 roles工作流
<div align="center"> <img src="https://github.com/ihuangch/blog/blob/master/Ansible/pic/ansible-roles.png" /> </div><br>

##### 3.3.2 roles基本结构
<div align="center"> <img src="https://github.com/ihuangch/blog/blob/master/Ansible/pic/roles-arch.png" /> </div><br>

#### 3.4 playbook中when语句
- 条件测试：如果需要根据变量、facts或此前任务执行的结果来作为某task执行与否的前提时，要用到条件测试，通过when语句实现，在task中使用，jinja2的语法格式
```
---
- hosts: webser
  remote_user: root

  tasks:
    - name: shut down system
	  shell: /sbin/shutdown -h now
	  when: ansible_distribution == "CentOS"
```

#### 3.5 playbook中的循环(迭代)
```
---
- hosts: localhost
  remote_user: root

  vars:
    some_packages:
	  - zsh
	  - curl
	  - httpd
	  - php
	  - mysql
  tasks:
    - name: install some packages
	  yum: name={{ item }} state=installed
	  with_items: "{{ some_packages }}"      # 注意必须有双引号
```

