### 什么是HTTPS?
HTTPS 是HTTP协议的安全版本，HTTP协议(超文本传输协议)是在浏览器和连接的网站之间发送数据的协议。HTTPS末尾的S代表的是安全的意思。这意味着浏览器和网站之间的所有通信都是加密的。HTTPS通常用于保护机密的在线交易，例如网上银行和在线购物等。  

Internet Explorer，Firefox和Chrome等web浏览器会在地址栏显示挂锁的图标来显示HTTPS连接有效。  
<div align="center"> <img src="../Network/pics/http-vs-https.png" height="300px" /> </div><br>

### HTTPS有什么作用?
正确配置后HTTPS连接可以保证三件事:
- 保密性。 访问者的连接已经加密，隐藏了URL，Cookie和其他敏感的元数据
- 真实性。 访问者确定访问的真实的网站，而不是模仿的网站或者是中间人
- 完整性。 访问者和网站之间发送的数据没有被修改或者篡改  
一个HTTPS的请求会使你无法完整的查看报文头部的信息.  

### HTTPS安全在哪些部分?
使用curl命令分别进行抓包分析:  
(使用curl命令而不使用浏览器，是因为谷歌默认浏览器访问都为https请求的)
对比访问https://www.google.com 和 http://www.google.com  

curl --head http://www.google.com  

<div align="center"> <img src="../Network/pics/http-head.png" height="300px" alt="http-head"/> </div><br>
<div align="center"> <img src="../Network/pics/http-mes.png" height="300px" alt="http-mes"/> </div><br>

curl --head https://www.google.com  

<div align="center"> <img src="../Network/pics/https-head.png" height="300px" alt="https-head"/> </div><br>
<div align="center"> <img src="../Network/pics/https-mes.png"  alt="https-head"/> </div><br>

从上面几张图片可以看到使用curl命令访问http网站和https网站是两种不同的报文，其中http方式访问网站使用head方法，
会直接返回相关的http response 报文，并且使用tcpdump会看到相关的http请求报文和响应报文内容。而使用https方式访问
网站时，在www.google.com，显示的http协议为http/2，并且使用tcpdump看不到相关的请求报文和响应报文的内容。  
由此可以看见https在一定程度上确实是比http安全的。  

### HTTPS是怎么工作的?
#### SSL协议和TLS协议?






