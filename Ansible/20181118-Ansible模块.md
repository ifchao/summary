___
- FileName: Ansible模块.md
- Author: ihuangch -huangch96@qq.com
- Description: ---
- Create:2018-11-18 19:21:37
___

### Ansible常用模块
- 1、command模块：默认模块，可忽略-m选项
	```
	ansible all -m command -a 'mkdir /test'
	ansible all -m command -a 'creat=/etc/fstab cat /etc/fstab'
	# 文件不存在不执行
	```
- 2、shell模块：执行shell命令，支持特殊符号管道等
	```
	ansible all -m shell -a 'echo passwd|password --stdin User_name'
	```

- 3、script模块：运行脚本，不需要提前拷贝脚本
	```
	ansible all -m script -a '/path/script/filename'
	```

- 4、copy模块：复制
	```
	ansbile all -m copy -a 'src=/path/source/file dest=/path/dest/file backup=yes'
	ansible all -m copy -a 'content="hello\nworld\n" dest=/path/dest/file'
	# 在使用copy模块的时候可以指定文件的权限属性等
	```

- 5、fetch模块：从客户端抓取文件，和copy模块相反
	```
	ansible all -m fetch -a 'src=/path/remotehost/file dest=/path/file'
	# src只能是文件，目录可以先tar，dest可以为目录
	```

- 6、file模块：管理文件
	```
	ansible all -m file -a 'path=/path/filename state=touch'
	ansible all -m file -a 'path=/path/dir state=directory'
	ansible all -m file -a 'path=/path/dir state=absent'
	ansible all -m file -a 'src=/path/name dest=/path/name.lnk state=link' 
	```

- 7、hostname模块
	```
	ansible all -m hostname -a 'name=xxxx_name'
	```

- 8、corn模块
	```
	ansible all -m corn -a 'minute=* weekday=1,3,5 job="/usr/bin/echo 123"'
	```

- 9、yum模块
	```
	ansible all -m yum -a 'name=xxxx_name'
	ansible all -m yum -a 'name=/path/xxx/file.rpm'
	```

- 10、service模块
	```
	ansible all -m service -a 'name=xxxx_service state=started enable=yes'
	```

- 11、user模块
	```
	ansible all -m user -a 'name=xxx shell=/sbin/nologin system=yes'
	ansible all -m user -a 'name=xxx state=absent'
	```


