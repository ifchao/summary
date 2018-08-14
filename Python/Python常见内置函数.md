## Python常用的一些内置函数,包括一些工厂函数
    总结Python语言中一些常用的内置函数,进行分类整理,包括一些工厂函数
    其中一些并不是函数,而是一些实例的常用方法。
## Python中关键字、函数及方法的区别
    关键字:
        关键字是Python内置的,具有特殊意义的标识符,自定义标识符命名(变量名)时不可与之重复。
        可以通过以下方式查看Python内置的关键字内容。

```python
import keyword
print keyword.kwlist
```

```python
['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
```
    函数:
        函数是封装了一些独立的功能,可以直接调用,python内置了许多函数,同时可以自建函数来使用。

    方法:
        方法和函数类似,同样封装了独立的功能,但是方法是需要通过对象来调用,表示针对这个对象要做的
        操作,使用时采用点方法。






## 字符串(方法)
    字符串类型常用的一些内置方法(使用dir(str)查看所有str的可用方法):
    Python字符串常用的一些方法:
    1.字符串的搜索和替换
        string.count(str, beg=0, end=len(string)):返回str在string中出现的次数,可以指定范围
        string.capitalize():字符串string的首字母大写
        string.center(str1,str2):字符串放中间,两边str2补齐
        string.find(str, beg=0, end=len(sting)):检测str是否在string中,可以指定范围
                    如果是返回str开始的索引值,否则返回-1
        string.index(str, beg=0, end=len(string)):和find方法一样,只不过如果str不在string中会报异常
        string.replace(str1, str2, num=string.count(str1)): 把string中的str1替换为str2,替换不超过num次
        string.format():字符串格式化,它通过{}和:来代替%。
        string.lower():转换string中所有大写字符为小写
        string.decode('utf-8')：以指定编码格式解码string
        string.encode('utf-8')：以指定的编码格式编码string

    2.去除空格和特殊符号
        string.strip():去除空格和换行符
        string.strip(str):删除字符串str
        string.lstrip():去除左边的空格和换行符
        string.rstrip():去除右边的空格和换行符
    
    3.字符串的测试
        string.startswith(obj, beg=0, end=len(string)): 检查字符串是否以obj开始,可以指定范围
        string.endswith(obj, beg=0, end=len(string)):检查字符串是否以obj结束,可以指定范围
        string.isalnum():字符串是否全是字母和数字
        string.isalpha():是否全是字母,并至少有一个字符
        string.isdigit():是否全是数字

    4.字符串的分割和拼接
        strimg.split(str):以字符串str分割
        string.splitlines(num=string.count("\n")): 按照行分隔,返回一个包含作为元素的列表,num指定则仅切片num行
        string.join(seq):以string作为分隔符,将seq中所有的元素的字符串表示合并为一个新的字符串
        string[1]:切片

## 列表(方法)
    Python列表常用的一些方法:
        li.append(obj):向列表中添加一个对象。该方法无返回值,但是会修改原来的变量。
        li.count(obj):统计obj在列表中出现的次数。返回值为次数
        li.extend(seq):可以在列表的末尾一次性追加另一个序列seq的多个值。即可以用新列表扩展原有的列表。无返回值。
            和连接操作不同的是不返回一个新列表。
        li.index(obj, beg=0, end=len(li)):用于从列表中找出某个值第一个匹配项的索引位置,可以指定范围
        li.insert(index, obj):在索引为index的位置插入对象obj
        li.pop(index=-1):删除并返回指定位置的对象,默认是最后一个对象。返回值为删除的元素。
        li.remove(obj):在列表中删除找到的第一个obj对象,不存在返回一个valueError错误。返回值为None
        li.reverse():原地翻转列表。返回值为空
        li.sort(func=None, key=None, reverse=False):对列表原位置排序。reverse=True为逆序。返回值为None
    

## 元组(方法)
    Python元组常用的一些方法:
        tul.count(obj):统计obj在元组中出现的次数
        tul.index(obj, beg=0, end=len(tul)):返回从元组找到obj第一个索引位置

## 字典(方法)
    Python字典常用的一些方法:
        dic.clear():清除字典中所有的项。无返回值
        dic.copy():返回一个具有相同键值对的新字典.(浅复制)。在副本中替换值得时候,原字典不受影响
        dic.fromkeys(seq):使用给定的键建立一个新的字典。返回值为一个新的字典,每个键默认对应的值为None
        dic.get(key):返回指定key的value。如果不存在返回None。
        dic.has_key(key):如果key在字典中存在,返回True。否则返回False
        dic.items():返回一个包含字典中(键, 值)对元组的列表
        dic.keys():返回一个包含字典中键的列表
        dic.values():返回一个包含字典中所有值得列表
        iteritems()/iterkeys()/itervalues():和对应的非迭代方法一样,不过返回的是一个迭代器。需要使用.next获得返回值。
        dic.pop(key):删除并返回dict[key]。key不存在,引发keyError异常。
        dic.popitem():随机弹出一个key
        dic.setdefault(key,default=None):方法和get类似。当key不存在时,dict[key]=default为它赋值。
        dic.update(d):用一个字典项更新另外一个字典



## 集合(方法)
    Python集合常用的一些方法
    可变集合
        s.add(obj):在集合s中添加对象obj
        s.remove(obj):在集合中删除对象obj,如果obj不是集合s中的元素,引发KeyError错误
        s.pop():删除s中的任意一个对象。并返回删除的值。
        s.clear():删除集合s中的任意一个对象
        s.discard(obj):如果obj是集合s中的任意一个元素,从集合中删除对象obj
        s.update(t):用t中的元素,修改s,即返回s现在包含s或t的成员
        s.intersection_update(t):返回s中的成员是共同属于s和t的元素
        s.difference_update(t):返回s中的成员属于s但是不包含在t中的元素
        s.symmetric_difference_update(t):s中的成员更新为那些包含在s或t中,单不是s和t共有的元素。
    所有集合:
        s.issubeset(t):如果s是t的子集,返回True。否则返回False。
        s.issuperset(t):如果t是s的超集,返回True。否则返回False。
        s.union(t):返回一个新集合,该集合是s和t的并集
        s.intersection(t):返回一个新集合,该集合是s和t的交集
        s.difference(t):返回一个新集合,该集合是s的成员,不是t的成员
        s.sysmetric_difference(t):返回一个新集合,该集合是s或t的成员,但不是s和t的共有成员
        s.copy():返回一个新集合。是集合s的浅复制。


## 文件(方法和函数)
    Python文件常用的内置函数和方法
    函数：
        open(fileName, 'mode'):以指定mode模式打开文件
    方法：
        file.close():关闭打开的文件
        file.read(size):直接读取字节到字符串中,最多读取指定给定数目个字节。
        file.readline(size):读取打开文件的一行,然后整行整行的输出。
        file.readlines():读取所有行然后把他们作为一个字符串列表返回
        file.write(str):把含有文本数据和或二进制数据块的字符串写到文件中去
        file.writelines(seq):接受一个字符串列表作为参数,将他们写入到文件中。不会自动加入行结束符。
                          如果需要,必须在调用前给每行结尾加上行结束符。
        file.tell():返回当前在文件中的位置
        file.flush():刷新文件的内部缓存区
        file.next():返回文件的下一行
    内置属性:
        file.closed:True表示文件已经被关闭,否则为False
        file.encoding:返回文件所使用的编码
        file.mode:文件打开是的访问模式
        file.name:文件的name
        

## 内置函数
    Python中一些常见的内置函数和类方法等其中一些属于工厂函数
    查看Python中内置变量和函数的的方式
```python
dir(__builtins__)
```
    bin():返回一个整数int或long的二进制表示
    callable(obj):检查一个对象是否可以调用,如果返回True,obj仍然可能调用失败
    chr():0-255的整数作为参数,返回对应的字符
    cmp(x,y):比较2个对象,如果x<y返回-1,如果x==y返回0,如果x>y返回1
    classmethod():装饰器,修饰对应的函数不需要实例化,不需要self参数,但是第一个参数需要是表示自身类的cls参数。
                  可以调用类的属性,类的方法。即类方法

    compile(source, filename):将一个字符串编译为字节代码。
    delattr(x, 'foobar'):删除属性。相当于del x.foobar
    dir():不带参数时,返回当前范围内的变量、方法和定义的类型列表；带参数时,返回参数的属性、方法列表。如果参数包含 
          方法__dir__(),该方法将被调用。如果参数不包含__dir__(),该方法将最大限度地收集参数信息。
    enumerate():用于将一个可以遍历的数据对象组合为一个索引序列,同时列出数据和数据下标。一般用在for循环中
```python
#普通
>>>i = 0
>>> seq = ['one', 'two', 'three']
>>> for element in seq:
...     print i, seq[i]
...     i +=1
... 
0 one
1 two
2 three
```

```python
#使用enumerate
>>>seq = ['one', 'two', 'three']
>>> for i, element in enumerate(seq):
...     print i, element
... 
0 one
1 two
2 three
```

    evel():用来执行一个字符串表达式,并返回表达式的值。
```python
x = 7
eval('3 * x')
#>>>21
```

    execfile(filename):用来执行一个文件
    filter(function, iterable):用于过滤序列,过滤掉不符合条件的元素
    getattr(obj, name):返回一个实例对象的属性值
    globals():以字典类型返回当前位置的全部全局变量
    hasattr(obj, name):判断对象是否包含对应的属性。返回Bool值
    hash(obj):获取一个对象的哈希值
    help([obj]):查看函数或模块用途的详细说明
    hex():用于将10进制数转换为16进制
    id(obj):获取对象的内存地址
    isinstance(obj,classinfo):判断一个对象是否是一个已知的类型,类似type()
    issubclass(class, classInfo):判断参数class是否是类型参数classInfo的子类
    iter():用来生成迭代器
    locals():以字典类型返回当前位置的全部局部变量
    map(function, iterable):根据提供的函数对指定序列做映射
```python
def square(x)
    return x ** 2
map(square, [1,2,3,4,5])
#[1,4,9,16,25]
map(lambda x: x ** 2, [1,2,3,4,5])
#[1,4,9,16,25]
# 提供了两个列表,对相同位置的列表数据进行相加
map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
#[3, 7, 11, 15, 19]
```
    memoryview(obj):返回给定参数的内存查看对象。返回元组列表
    next(iterator):返回迭代器的下一个项目。iterator.next()
    property():在新式类中返回属性值
    range(start, stop[, step])：返回一个整数列表。一般用在for循环中。从start开始到stop结束。不包含stop。默认从0开始
    xrange(start, stop[, step]):生成的不是一个列表,是一个生成器。
    raw_input():获取控制台的输入,返回字符串类型。
    reload(module):用于重载之前的模块
    repr(obj):返回字符串对象。以解释器读取的形式。和str()不同在于str()便于人类读取
    round(x [,n]):返回浮点数x的四舍五入值,n是保留几位小数
    sorted():对所有可迭代对象进行排序操作。sort应用在list上
    staticmethod():返回函数的静态方法。装饰器
    vars(obj):返回对象obj的属性和属性值得字典对象。
    zip():将可迭代对象作为参数,将对象中对应的元素打包成一个个元组,返回由这些元组组成的列表。
```python
a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped = zip(a,b)     # 打包为元组的列表
#[(1, 4), (2, 5), (3, 6)]
zip(a,c)              # 元素个数与最短的列表一致
#[(1, 4), (2, 5), (3, 6)]
zip(*zipped)          # 与 zip 相反,可理解为解压,返回二维矩阵式
#[(1, 2, 3), (4, 5, 6)]
```
    __import__(name):用于动态加载模块。
	__doc__:获取docString文档
```python
import os
# 打印os模块的文档
print os.__doc__
# 打印os模块walk方法的文档
print os.walk__doc__
```







## 工厂函数
    工厂函数是指这些内置函数都是类对象,当调用它们时,实际是创建了一个类实例.
    1.int(),float(),long(),complex(),bool()生成数字
    2.str(),unicode():生成字符串
    3.list(),tuple():生成列表或元组
    4.dict():生成字典
    5.set(),frozenset():生成可变集合或不可变集合
    6.type():查看类型
    7.file(name):创建文件

