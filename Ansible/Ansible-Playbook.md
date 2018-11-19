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



