### 正则表达式
    正则表达式相对来说，还算熟悉，在使用Linux系统中，grep，sed，awk，find等这些命令
    都会使用正则表达式。正则表达式，可能是每个人都会有不同的表示方法。毕竟这是一种思维
    每个人处理数据的想法不一样，所编写的正则表达式可能也是不相同的。
### Python中的正则表达式
    Python中正则表达式，应该说每种编程语言应该都有一些自身语言特性的正则表达式。但是一些
    标准的匹配的元字符所表达的意思是一样的。

    1. 表示字符
        .   : 匹配任意一个字符
        []  : 匹配[]中列举的字符,^取反
        \d  : 匹配数字,即0-9
        \D  ：匹配非数字
        \s  : 匹配空白,即空格,tab,\n等
        \S  ：匹配非空白
        \w  : 匹配单词字符,即a-z,A-Z,0-9
        \W  : 匹配非单词字符
    2. 表示次数
        *   : 匹配前一个字符出现0次或无限次,即可有可无
        +   : 匹配前面一个字符出现1次或者无限次,即至少有一次
        ?   ：匹配前面一个字符出现1次或者0次,即要么1次,要么没有
        {m} : 匹配前面一个字符出现m次
        {m,}: 匹配前面一个字符至少m次
        {m,n}: 匹配前面一个字符m-n次
    3. 位置锚定
        ^   : 匹配字符串开头
        $   : 匹配字符串结尾
        \b  : 匹配一个单词的边界
        \B  : 匹配非单词边界
    4. 匹配分组
        |   : 匹配左右任意一个表达式
        (ab): 将括号中字符作为一个分组
        \num: 引用分组num匹配到的字符串
        (?P<name>): 分组别名
        (?P=name): 引用别名为name分组匹配到的字符串
    
### Python中的re模块
    Python中需要通过正则表达式对字符串进行匹配的时候,可以使用re模块。
    1. re.match(pattern,string):尝试从字符串的起始位置匹配一个模式。
        如果不是起始位置成功的话,match()就返回None而不是空字符串。
        匹配成功返回匹配对象。可以使用group(num)或groups()获取匹配到的对象。
```
    In [1]: import re
    In [1]: import re

    In [2]: p = r"hello"

    In [3]: result = re.match(p, "hello world")

    In [4]: result.group()
    Out[4]: 'hello'

    In [5]: result = re.match(p, "hellooooooworld")

    In [6]: result.group()
    Out[6]: 'hello'

    In [7]: result = re.match(p, "hellworld")

    In [8]: print(result)
    None

    In [11]: result = re.match(p, "wwhelloww")

    In [12]: print(result)          #这里并没有匹配hello
    None

```

    2. re.search(pattern,string)
        search方法和match方法很相似,区别在于match()函数只检测re是不是在string的开始
        位置匹配,search()会扫描整个string查找匹配。

```
    In [18]: p = r"hello"

    In [19]: result = re.search(p, "helloworld")

    In [20]: result.group()
    Out[20]: 'hello'

    In [22]: result = re.search(p, "wwhelloww")

    In [23]: result.group()         #hello不在开头,也匹配了
    Out[23]: 'hello'
```

    3. re.split(pattern, string[, maxsplit])
        split()方法按照能够匹配的子串将string分割后返回列表。
        maxsplit用于指定最大分割次数,不指定将全部分割。

```
    In [24]: re.split(r"\d+", "one1two2three3four4")
    Out[24]: ['one', 'two', 'three', 'four', '']

    In [25]: re.split(r"\||,|-", "one|two,three,four-five")
    Out[25]: ['one', 'two', 'three', 'four', 'five']
```

    4. re.sub(pattern, repl, string[, count])
        使用repl替换string中每一个匹配到的子串返回替换后的字符串
        当repl是一个字符串时,可以使用\num引用分组,但是不能使用编号0
        当repl是一个方法时,这个方法只接受一个参数(匹配到的对象),并返回一个字符串
        用于替换,返回的字符串中不能再引用分组。
        count用于指定最多替换次数,不指定时全部替换

```
    In [26]: re.sub(r"\d+", '1000', "s = 50")
    Out[26]: 's = 1000'

    In [37]: re.sub(r"(\w+) = (\d+)", r'\2 = \1', "s = 50")
    Out[37]: '50 = s'

    In [38]: def add(temp):
    ...:     strNum = temp.group()
    ...:     num = int(strNum) + 1
    ...:     return str(num)
    ...: 
    ...: 

    In [39]: re.sub(r"\d+", add, "s = 50")
    Out[39]: 's = 51'
```

    5. re.findall(pattern, string)
        搜索string,以列表形式返回全部能够匹配的子串
```
    In [40]: re.findall(r"\d+", "one1two2three3four4five5")
    Out[40]: ['1', '2', '3', '4', '5']
```

    6. re.finditer(pattern, string)
        和findall一样,不过返回的是迭代器
```
    In [41]: re.finditer(r"\d+", "one1two2three3four4five5")
    Out[41]: <callable_iterator at 0x7fb17413d320>
    
    In [42]: for i in re.finditer(r"\d+", "one1two2three3four4five5"):
        ...:     print(i)
        ...:     
    <_sre.SRE_Match object; span=(3, 4), match='1'>
    <_sre.SRE_Match object; span=(7, 8), match='2'>
    <_sre.SRE_Match object; span=(13, 14), match='3'>
    <_sre.SRE_Match object; span=(18, 19), match='4'>
    <_sre.SRE_Match object; span=(23, 24), match='5'>
    
    In [43]: for i in re.finditer(r"\d+", "one1two2three3four4five5"):
        ...:     print(i.group())
        ...:     
        ...:     
    1
    2
    3
    4
    5
```







