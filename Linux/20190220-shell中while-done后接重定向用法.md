___
- FileName: 20190220-shell之while_read_line用法.md
- Author: ihuangch -huangch96@qq.com
- Description: ---
- Create:2019-02-20 13:53:58
___

### while done 重定向使用
while读取文件的方法:
- 1.将文件的内容通过管道(|)或重定向(<)的方式传给while
- 2.while中调用read将文件内容读取出来，并赋值给read后跟随的变量(变量可以是多个，根据每行的内容可以改变)

#### 管道传输文件内容
