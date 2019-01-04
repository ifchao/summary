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
```bash
