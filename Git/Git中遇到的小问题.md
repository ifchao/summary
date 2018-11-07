### 背景
    由于一直在虚拟机中使用git，每次安装虚拟机后，都会再次安装git去同步
    GitHub上的一些代码。因为git版本低或者是系统版本的原因总是有各种问题。
    所以这篇文章记录相关问题解决办法。
  
    OS：CentOS6.5
    GitVersion：Git 1.7.1

### 问题1：Git无法clone？
    解决：
        a. 把https换位git(可以clone但是无法彻底解决)
        b. 更新相关依赖的软件包nss libcurl curl nspr
            (实际只有nss需要更新)
    
### 问题2：Git无法push？
    解决：
        vim .git/config
```bash
url = https://username@github.com/username/example.git
```

### 问题3：Git提交后GitHub不更新contribution
    解决：
```bash
git config --global user.name [username]
git config --global user.email [email]
```

### 想法
由于一直还在使用CentOS6，所以总是能遇到很多奇怪的问题，也准备准备尽快以CentOS7
为主。不过是使用习惯的问题罢了。  
计划：  
CentOS6 --> CentOS7  
Python2 --> Python3

