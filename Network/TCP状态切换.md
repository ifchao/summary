### TCP协议
    这篇文章,是近期的一些总结,不是简单的介绍三次握手和四次挥手。
    而是把建立连接和断开连接中几乎所有可能出现的状态进行一些解释
    介绍。

#### 建立连接
    1. 三次握手建立连接
        三次握手建立连接,就是我们平时最常见的一种建立连接的方式,
        现在互联网中的网络也几乎都是这种方式。
            客户端(主动): SYN-->SYN_SEND-->ESTABLISHED
            服务端(被动): SYN_RCVD-->SYN,ACK-->ESTABLISHED

        三次握手状态图
    
    2. 服务端和客户端同时主动打开的状态
        这种情况有可能发生,但是几乎不会发生。
            客户端(主动连接7777端口): 
                SYN_SEND-->SYN_RCVD-->SYN,ACK-->ESTABLSIHED
            服务器(主动连接8888端口): 
                SYN_SEND-->SYN_RCVD-->SYN,ACK-->ESTABLISHED
        
        同时主动打开状态图

    3. 建立连接失败a
        场景:
            客户端为收到服务器SYN+ACK时,客户端程序崩溃退出了,客户端接
            收到服务器的ACK+SYN时,客户端回复RST。此时服务器处于
            SYN_RCVD状态,当接收到客户端RST时,则从SYN_RCVD转移到
            LISTEN状态。

    4. 建立连接失败b
        场景1:
            服务器进程异常,客户端发送SYN服务端响应RST
        场景2:
            服务器机器关闭的状态,服务器宕机等原因,使得客户端连接超时
        
#### 断开连接
    1. 四次挥手断开连接
        同样的四次挥手也是我们学习中最常见的一种断开方式。
            客户端(主动):
                FIN-->FIN_WAIT1-->FIN_WAIT-->TIME_WAIT-->CLOSE
            服务端(被动):
                ACK-->CLOSE_WAIT-->FIN-->LAST_ACK-->CLOSE
        
        四次挥手状态图
    
    2. 同时关闭断开连接
            客户端(主动):
                FIN-->FIN_WAIT1-->接收FIN,发送ACK-->CLOSING-->TIME_WAI--CLOSE
            服务器(主动):
                FIN-->FIN_WAIT1-->接收FIN,发送ACK-->CLOSING-->TIME_WAI--CLOSE

    3. 断开连接(没有FIN_WAIT2)(三次挥手)
        场景:
            被动关闭方,直接发送FIN+ACK,则主动方直接跳过FIN_WAIT2,进入TIME_WAIT状态
        
            客户端(主动):
                FIN-->FIN_WAIT1-->TIME_WAIT-->CLOSE
            服务器(主动):
                ESTABLISHED-->(同时发送ACK和FIN)CLOSE_WAIT-->LAST_ACK-->CLOSE
            
    


