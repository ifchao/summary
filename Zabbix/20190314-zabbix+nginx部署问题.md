___
- FileName: 20190314-zabbix+nginx部署问题.md
- Author: ihuangch -huangch96@qq.com
- Description: ---
- Create:2019-03-15 16:30:39
___

### 部署zabbix 3.4.15 
公司zabbix-server版本比较老，现在重新部署zabbix。并前端使用nginx作为web访问入口。
其中有些配置需要记录。


####1. zabbix php文件目录权限设置
- /usr/share/zabbix/
- /etc/zabbix/web/
一般安装zabbix 默认的zabbix，php文件等都会在/usr/share/zabbix目录下，所以当nginx作为前端
web访问入口的时候，需要给予这个目录对应的权限。  
一般你php-fpm的启动用户是需要相对应的执行权限。  
/etc/zabbix/web/这个目录下记录zabbix web页面的启动的php脚本，所以也需要给予执行权限

####2. zabbix 中对于php的要求与配置
- 1.php version>5.4.0
- 2./etc/php.ini修改的配置

	
```bash
shell> chmod -R 777 /var/lib/php/session/

session.save_handler = /var/lib/php/session  # 解决无法点击下一步的问题
date.timezone = "Asia/Shanghai"				 # 时区设置
max_input_time = 300
max_execution_time = 300

```


