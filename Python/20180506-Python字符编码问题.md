### Python字符编码
    Python字符编码，关于字符转换很多人都遇到过问题。这个问题也涉及很多方面，包括编码，解码等。
    以及相关字符，字节表示的方法等。同样的Python2和Python3中字符编码又有不同。因为多次入坑所以需要写篇文章
    记录一下。以防自己再次入坑。

### 字符编码格式
    1.ASCII
        把英文字母,相关标点符号等转换为二进制数据，以供计算机识别。
    2.GBK,GB2312
        解决计算机无法处理中文的问题。
        GBK包括了GB2312的所有内容，同时增加了近20000个新的汉字（包括繁体）和符号
    3.Unicode
        英文和中文的问题都已经解决，但是例如日语，韩语，阿拉伯语等，就是通过Uniconde(万国码)解决的
        Unicode用两个字符来表示一个字符，可以提供65535种字符，足够覆盖世界上的所有符号。
    4.utf-8
        Unicode的出现，提供了统一的标准，但对于英文世界的国家来说，一个字节完全够用，如果使用
        Unicode会浪费大量空间，为了解决这个问题提出了utf-8，一种针对Unicode的可变长度字符编码，可
        以使用1-4个字节表示一个符号，根据不同的符号变化字节长度，当字符在ASCII编码范围时，用一个字
        节表示，兼用ASCII。
        Unicode是内存编码的表示方案(规范)，而utf-8是如何保持和传输Unicode的方案(实现)

    总的来说:
    1.为了处理英文字符出现了ASCII码
    2.为了处理中文字符出现了GBK等
    3.为了处理各国字符通用出现了Unicode
    4.为了提高Unicode存储和传输性能，产生了utf-8

### Python2中相关编码
    1.Python2中默认的字符编码是ASCII码，也就是说Python在处理数据时，只要数据没有指定它的编码类型,
      Python默认将其当做ASCII处理。这时候如果代码中包含中文时，在运行时会提示出错。
```
    #! /usr/bin/python
    s = "你好"
    print s 
```
    这样直接执行代码就会出现以下这种情况，所以解决的方法是在投币加上编码声明:
    # -*- encoding: utf-8 -*-,这样就不会出现下面的语法错误。
    或者 # encoding=utf8
```    
    root@localhost ~]# python 1.py
      File "1.py", line 3
    SyntaxError: Non-ASCII character '\xe4' in file 1.py on line 3, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
```
    查看Python中的默认的字符编码，
    这里的默认的字符编码是一些python方法中默认是的编码，开头的encoding是对于文件内容的编码
```
    In [1]: import sys

    In [2]: sys.getdefaultencoding()
    Out[2]: 'ascii
```

    2. Python2.7中的str和Unicode
       Python2中的字符串一般有两种类型,unicode和str
       str类型，Python2中会自动将字符串转换为合适的编码的字节字符串，这个时候字符和字节没有所为固
       定的一一对应的关系。
       unicode则是用Unicode编码的字符串，这个时候一个字符对应两个字节，一一对应

       直接赋值字符串时，类型为str，str为字节串，会按照开头的encoding来编码成一个个的字节。
       赋值的时候，在字符串前面加个u，类型则为Unicode，直接按照Unicode编码

```
    #!/usr/bin/env python
    # -*- encoding: utf-8 -*-
    
    s1 = "你好"
    print type(s1)    #输出为 <type 'srt'>,按照开头的encoding编码成相应的字节
    print len(s1)     #输出为6,按utf8编码,一个汉字占3个字节,2个所以长度6
    
    s2 = u"哈哈"      #输出为 <type 'unicode'>,用unicode编码,两个字节一个字符
    print type(s2)    #输出为2,Unicode用字符个数来计算长度,从这个角度看,Unicode才是真正意义上的字符串类型
    print len(s2)   

    #所以python3中默认字符串为Unicode编码
    [root@localhost ~]# python 1.py
    <type 'str'>
    6
    <type 'unicode'>
    2
```

        对于中文的明显区别:
            对于经常处理中文字符串的人,统一用unicode编码就可以避免这些问题了。
```
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    s1 = "一二三四"
    print s1[-2:] == '三四' #返回false

    s2 = u"一二三四"
    print s2[-2:] == u"三四" #返回true,这就是认为Unicode才是真正意义上的字符串

    [root@localhost ~]# python 2.py
    False
    True
```
    
    3.python2.7中的encode和decode
        encode的正常使用:对Unicode类型进行encode,得到字节串str类型。(编码)
            unicode -> encode(根据指定编码) -> str
        decode的正常使用:对str类型进行decode,得到Unicode类型。(解码)
            str -> decode(根据指定编码) -> unicode
    
```
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    
    s1 = u"你好"
    print type(s1)
    print type(s1.encode("utf8"))
    
    
    s2 = "字节串"
    print type(s2)
    print type(s2.decode("utf8"))

    [root@localhost ~]# python 3.py
    <type 'unicode'>
    <type 'str'>
    <type 'str'>
    <type 'unicode'>
```
    总结:
        encode函数是把数据编码为指定编码格式的字节串
        decode函数是把相关编码的字节串解码为unicode
    
### Python2处理文件编码问题
    1. 文件的读写 
        首先需要记住的是:文件的读出和写入都用str类型,就是一个个字节来进行读写的
    
```
    #查看文件的编码
    import chardet
    with open(filename, 'r') as f:
        data = f.read()
        return chardet.detect(data)
```

    2. 一般处理方法
        1.首先把源文件的默认encoding和系统默认编码改为utf8
        2.程序执行过程统一使用unicode类型
        3.对于读写文件,得到的是str,对str进行相应的encode和decode就可以了
    

### Python3的文件编码问题
    相对来说，python3还是改进了很多的，关于字符编码这一方面就改变的容易理解很多了。
    1. Python3的源码文件默认编码格式为utf8,所以python3中可以不用在.py文件中写encoding声明。
       并且系统传递给python的字符,不再受系统默认编码影响,统一为unicode编码。
```
    In [1]: import sys

    In [2]: sys.getdefaultencoding()
    Out[2]: 'utf-8'

    #!/usr/bin/env python

    s = '你好'

    print(type(s))
    print(s)

    [root@localhost ~]# python3 4.py 
    <class 'str'>
    你好

```

    2. Python3中将字符串和字节序列做了区别
       字符串str是字符串标准形式,就是python2中的unicode编码
       bytes类似Python2中的str有各种编码区别。
       bytes通过解码(decode)转化为srt,str通过编码(encode)转化成bytes

    总结:
        Python3中，str就是真实的字符串，就是unicode
        所以一般需要把字符串编码为不同的编码格式，以便于在不同的平台上显示字符串。


	3. 刚开始接触python的时候会出现这样的情况
```
	In [24]: i = ['你好', '世界']

	In [25]: print i
	['\xe4\xbd\xa0\xe5\xa5\xbd', '\xe4\xb8\x96\xe7\x95\x8c']

	In [26]: for c in i:
	    ...:     print c
		    ...:     
			你好
			世界
	In [27]: print i[0]
	你好
```
		当你直接打印这个list(tuple,dict)时,打印的是这个list呈现给计算机的识别的字节串。
		而通过print输出时,则呈现的是字符串。便于人类阅读。(python3貌似没有出现这种问题)
