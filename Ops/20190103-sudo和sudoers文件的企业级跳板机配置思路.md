___
- FileName: 20190103-sudo和sudoers文件的企业级跳板机配置思路.md
- Author: ihuangch -huangch96@qq.com
- Description: ---
- Create:2019-01-03 20:30:18
___

### 背景
公司大概有4000+的机器，这些机器都不可以使用密码进行登录，只有使用密钥通过跳板机进行登录。
每个用户通过自己的用户名和密钥进行登录跳板机，通过跳板机登录到目标机器，目标机器的用户
分为开发和运维两类。每个开发同事只能通过跳板机使用公用的开发账号，登入到目标主机，进行相应
的操作。此时对于账号的sudo和跳板机sudo的关机就是很必要的了。

### sudo 使用
sudo 命令是Linux上的一个非常有用的工具，它允许系统管理员分配给普通用户一些合理的"权限"，让
他们执行一些只用root用户或其它特许用户才能完成的任务，比如：运行一些mount，reboot，su等命令，
编辑一些系统配置文件等。这样就会减少了root用户的登录次数和管理时间，也提高了系统安全性。

#### sudo 命令的特点
- sudo能够限制指定用户在指定主机上运行某些命令
- sudo可以提供日志，忠实的记录每个用户使用sudo做了些什么，并且能够将日志传到中心主机或者日志服务器
- sudo为系统管理员提供配置文件，允许系统管理员集中的管理用户的使用权限和使用的主机。默认的存放位置/etc/sudoers
- sud使用时间戳文件来完成类似"检票"的系统。当用户执行sudo并且输入密码后，用户获得了一张默认存活期为300秒的"入场券"(默认值可以在编译的时候改变)。超时以后，用户必须重新输入密码。

#### sudo 执行命令的过程
将当前用户切换到超级用户下，或者切换到指定的用户下。然后以超级用户或其指定切换到的用户身份
执行命令，执行完成后，直接退回到当前用户。  
具体过程:  
- 当用户执行sudo时，系统会主动寻找/etc/sudoers文件，判断该用户是否有执行sudo的权限
- 确认用户具有可执行的sudo权限后，让用户输入自己的密码确认
- 密码输入成功，则开始执行sudo后续的命令


#### 不需要输入密码的情况
- root执行sudo时不需要输入密码(sudoers文件中有配置root ALL=(ALL) ALL这样一条规则)
- 欲切换的身份和执行者的身份相同，不需要输入密码
- /etc/sudoers文件设置为允许用户在不输入该用户的密码的情况下使用所有命令(%wheel ALL=(ALL) NOPASSWD:ALL)


#### sudo 命令选项
```bash
[root@centos-112 ~]# sudo --help
sudo - execute a command as another user

usage: sudo -h | -K | -k | -V
usage: sudo -v [-AknS] [-g group] [-h host] [-p prompt] [-u user]
usage: sudo -l [-AknS] [-g group] [-h host] [-p prompt] [-U user] [-u user] [command]
usage: sudo [-AbEHknPS] [-r role] [-t type] [-C num] [-g group] [-h host] [-p prompt] [-u user] [VAR=value] [-i|-s] [<command>]
usage: sudo -e [-AknS] [-r role] [-t type] [-C num] [-g group] [-h host] [-p prompt] [-u user] file ...

Options:
  -A, --askpass               use a helper program for password prompting
  -b, --background            run command in the background
  -C, --close-from=num        close all file descriptors >= num
  -E, --preserve-env          preserve user environment when running command
  -e, --edit                  edit files instead of running a command
  -g, --group=group           run command as the specified group name or ID
  -H, --set-home              set HOME variable to target user's home dir
  -h, --help                  display help message and exit
  -h, --host=host             run command on host (if supported by plugin)
  -i, --login                 run login shell as the target user; a command may also be specified
  -K, --remove-timestamp      remove timestamp file completely
  -k, --reset-timestamp       invalidate timestamp file
  -l, --list                  list user's privileges or check a specific command; use twice for longer format
  -n, --non-interactive       non-interactive mode, no prompts are used
  -P, --preserve-groups       preserve group vector instead of setting to target's
  -p, --prompt=prompt         use the specified password prompt
  -r, --role=role             create SELinux security context with specified role
  -S, --stdin                 read password from standard input
  -s, --shell                 run shell as the target user; a command may also be specified
  -t, --type=type             create SELinux security context with specified type
  -U, --other-user=user       in list mode, display privileges for user
  -u, --user=user             run command (or edit file) as specified user name or ID
  -V, --version               display version information and exit
  -v, --validate              update user's timestamp without running a command
  --                          stop processing command line arguments

```

### sudoers 文件
##### /etc/sudoers文件详解  
- sudo的配置文件是sudoers文件，它允许系统管理员集中的管理用户的使用权限和使用的主机。  
- 默认的存放位置/etc/sudoers，属性必须为0411  
- /etc/sudoers文件中每行算一个规则，前面带有#号可以当作是说明的内容，并不执行
- 如果规则很长，一行列不下时，可以用\号来续行
- /etc/sudoers的规则可以分为两类
	- 别名定义(非必须)
	- 授权规则(必须)

使用visudo命令编辑时，退出会提示错误
##### /etc/sudoers 文件中别名规则
```bash
# 别名规则定义格式
Alias_Type NAME = item1, item2
ALias_Type NAME1 = item1, item2, item3 : Name = item4, item5

# 别名类型
Host_Alias: 定义主机别名
User_Alias: 用户别名, 别名成员可以是用户，用户组(前面要加%号)
Runas_Alias: 用来定义runas别名，这个别名指定的是"目的用户", 即sudo允许切换至的用户
Cmnd_Alias: 定义命令别名


NAME: 就是别名，NAME的命名是包含大写字母，下划线以及数字，但是必须以一个大写字母开头
item: 就是别名的成员，一个别名下有多个成员，成员与成员之间，通过“,”号分隔成员必须是有效并事实
存在的。比如主机名，可以通过w查看用户的主机名或IP地址
item成员受别名类型制约，定义什么类型的别名，就要有什么类型的成员项目。
Host_Alias:成员必须是与主机相关联，比如是主机名(包括远程登录的主机名)，IP单个，或整段，掩码等
User_Alias和Runas_Alias:必须用系统用户当作成员
Cmnd_Alias:必须是系统存在的文件，文件名可以用通配符表示，命令需要绝对路径

别名规则是每行算一个规则，如果一个别名规则一行容不下时，通过\来续行，
同一类型别名的定义，一次也可以定义几个别名，用:隔开

```

##### /etc/sudoers 授权规则
授权规则是分配权限的执行规则，我们前面所讲到的定义别名主要是威力更方便的授权引用别名;  
授权规则可以看man sudoers文件，总体为这个模式:  
授权用户 主机=命令动作
如果不需要密码直接允许命令的，应该加`NOPASSWD:`参数，但是可以省略

```bash
#授权用户 主机=[(切换到哪些用户或用户组)][是否需要密码验证] 命令1,[(切换到哪些用户或用户组)][是否需要密码验证] [命令2],....
#[]中的内容可以省略，命令和命令之间用,号分隔;在[(切换到哪些用户或用户组)]，如果省略，则默认为
#root用户，如果时ALL，则代表能切换到所有用户，注意要切换到的目的用户必须用()号括起来，比如(ALL),(root)

#用户user1授权
user1 ALL=(root) /bin/chown, /bin/chmod
#组group1授权
%group1 ALL=(root) /usr/sbin/*, /sbin/*
#不能执行命令
user1 ALL=(root) /bin/chown, !/bin/chmod



```


```bash
## Sudoers allows particular users to run various commands as
## the root user, without needing the root password.
##
## Examples are provided at the bottom of the file for collections
## of related commands, which can then be delegated out to particular
## users or groups.
## 
## This file must be edited with the 'visudo' command.

## Host Aliases
## Groups of machines. You may prefer to use hostnames (perhaps using 
## wildcards for entire domains) or IP addresses instead.
# Host_Alias     FILESERVERS = fs1, fs2
# Host_Alias     MAILSERVERS = smtp, smtp2

## User Aliases
## These aren't often necessary, as you can use regular groups
## (ie, from files, LDAP, NIS, etc) in this file - just use %groupname 
## rather than USERALIAS
# User_Alias ADMINS = jsmith, mikem


## Command Aliases
## These are groups of related commands...

## Networking
# Cmnd_Alias NETWORKING = /sbin/route, /sbin/ifconfig, /bin/ping, /sbin/dhclient, /usr/bin/net, /sbin/iptables, /usr/bin/rfcomm, /usr/bin/wvdial, /sbin/iwconfig, /sbin/mii-tool

## Installation and management of software
# Cmnd_Alias SOFTWARE = /bin/rpm, /usr/bin/up2date, /usr/bin/yum

## Services
# Cmnd_Alias SERVICES = /sbin/service, /sbin/chkconfig

## Updating the locate database
# Cmnd_Alias LOCATE = /usr/bin/updatedb

## Storage
# Cmnd_Alias STORAGE = /sbin/fdisk, /sbin/sfdisk, /sbin/parted, /sbin/partprobe, /bin/mount, /bin/umount

## Delegating permissions
# Cmnd_Alias DELEGATING = /usr/sbin/visudo, /bin/chown, /bin/chmod, /bin/chgrp 

## Processes
# Cmnd_Alias PROCESSES = /bin/nice, /bin/kill, /usr/bin/kill, /usr/bin/killall

## Drivers
# Cmnd_Alias DRIVERS = /sbin/modprobe

# Defaults specification

#
# Refuse to run if unable to disable echo on the tty.
#
Defaults   !visiblepw

Defaults    env_reset
Defaults    env_keep =  "COLORS DISPLAY HOSTNAME HISTSIZE KDEDIR LS_COLORS"
Defaults    env_keep += "MAIL PS1 PS2 QTDIR USERNAME LANG LC_ADDRESS LC_CTYPE"
Defaults    env_keep += "LC_COLLATE LC_IDENTIFICATION LC_MEASUREMENT LC_MESSAGES"
Defaults    env_keep += "LC_MONETARY LC_NAME LC_NUMERIC LC_PAPER LC_TELEPHONE"
Defaults    env_keep += "LC_TIME LC_ALL LANGUAGE LINGUAS _XKB_CHARSET XAUTHORITY"

Defaults    secure_path = /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

## Next comes the main part: which users can run what software on 
## which machines (the sudoers file can be shared between multiple
## systems).
## Syntax:
##
## 	user	MACHINE=COMMANDS
##
## The COMMANDS section may have other options added to it.
##
## Allow root to run any commands anywhere 
root	ALL=(ALL) 	ALL

## Allows members of the 'sys' group to run networking, software, 
## service management apps and more.
# %sys ALL = NETWORKING, SOFTWARE, SERVICES, STORAGE, DELEGATING, PROCESSES, LOCATE, DRIVERS

## Allows people in group wheel to run all commands
%wheel	ALL=(ALL)	ALL

## Same thing without a password
# %wheel	ALL=(ALL)	NOPASSWD: ALL

## Allows members of the users group to mount and unmount the 
## cdrom as root
# %users  ALL=/sbin/mount /mnt/cdrom, /sbin/umount /mnt/cdrom

## Allows members of the users group to shutdown this system
# %users  localhost=/sbin/shutdown -h now

## Read drop-in files from /etc/sudoers.d (the # here does not mean a comment)
#includedir /etc/sudoers.d
```


#### 常见解决方案
开发使用一个公用的账号登录主机，运维使用ops登录主机，在跳板机进行组的分类，
如果用户是dev组，则通过跳板机登录目标主机的用户默认为:dev
每台主机的sudoer文件添加相关的规则(大致规则，一些细节自己根据需求改动)
```bash
defaults:ops !requiretty
Cmnd_Alias NCMD=/sbin/*, /usr/sbin/*, /bin/dd, /usr/bin/passwd
Cmnd_Alias NSU=/bin/su

DEV ALL=(ALL) ALL,!NSU,!NCMD
OPS ALL=(ALL) NOPASSWD: ALL

```
