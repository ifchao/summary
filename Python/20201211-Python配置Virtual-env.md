___
- FileName: 20201211-Python配置Virtual-env.md
- Author: ihuangch -huangch96@qq.com
- Description: ---
- Create:2020-12-11 15:24:36
___
工作中经常遇到多个项目使用不同的Python版本或者pip安装包，这样我们就需要配置python虚拟环境。virtualenv就是用来为一个应用创建一套“隔离”的Python运行环境。在此记录一下如何配置虚拟环境---备忘
所有第三方的包都会被pip安装到Python3的site-packages目录下.

1. 安装 virtualenv

```bash
pip3 install virtualenv
```

2. 安装virtualenvwrapper

```bash
pip3 install virtualenvwrapper
```

3. 配置virtualenvwrapper

```bash
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=$HOME/.virtual_environment_list
source /home/huangchaoqun6/.local/bin/virtualenvwrapper.sh
```

4. 相关命令

```bash
mkvirtualenv -p python3 Virtual_Env_Name # 创建虚拟环境
lsvirtualenv # 查看已经创建的虚拟环境
workon envName  # 进入对应的虚拟环境
deactivate # 退出当前虚拟环境
rmvirtualenv Env_Name # 删除对应的虚拟环境
cdvirtualenv # 进入当前虚拟环境目录
cdsitepackages # 进入当前虚拟环境安装包目录
```