# 近日概述
    这一段时间突然就忙了起来，写这篇文章出现在TimeLine已经好几天了，但是这些天都没有写，不得
    不说这拖延症真的是可怕。虽然也忙但是可以每天都写一点的。这一压又是好几天都没有写总结了。
# MySQL数据库
    这个就不需要一些话介绍了，因为介绍也没有什么意义。这篇文章主要是针对读完<MySQL必知必会>这
    本书的总结吧。没有什么特别高深的内容，只是MySQL相关的操作。

# MySQL相关的一些基本概念
    MySQL是一种二维表拥有行和列。
    列：表中的一个字段，所有的表都是有一个或者多个列组成的。
    数据类型：所容许的数据的类型。每个表列都有相应的数据类型，它限制(或容许)该列中存储的数据
    行：表中的数据都是按行来存储的。表中的一个记录。所保存的每个记录存储在自己的行内。
    主键：表中每一行都应该有可以唯一标识自己的一列(或一组列)其值能够唯一区分表中的每个行。
        主键满足条件：
            1.任意两行都不具有相同的主键值。
            2.每个行都必须具有一个主键值。
        主键应该遵循的习惯：
            1.不更新主键列中的值
            2.不重用主键列的值
            3.不在主键列中使用可能会更改的值
    
# 数据库相关的操作
    创建：create database dataName;
    查看：show databases;
    切换：use DataBaseName;

# 创建表
```sql
create table mytable (
    id int not null auto_increment,
    col1 int not nulll default 1,
    col2 varchar(45) null,
    primary key ('id')
);
```

# 插入(增加)

**普通插入**
```sql
insert into mytable(col1, col2)
values(var1, var2);
```

**插入检索出来的数据**
```sql
insert into mytable1(col1, col2)
select col1, col2
from mytable2;
```

**将一个表的内容复制到一个新表中**
```sql
create table newtable as
select * form mystable;
```

# 更新
```sql
update mytable 
set col1 = var1
where id = 1;
```

# 删除
```sql
delete from mystable
where id = 1;
```

# 修改表

**添加列**
```sql
alter table mystable
add col char(20);
```

**删除列**
```sql
alter table mytable
drop column col;
```

**删除表**
```sql
drop table mytable;
```

# 查询数据

```sql
select col1 from mytable;
```

**关键字distinct**
```sql
--相同值只会出现一次。它作用于所有列，也就是说所有列的值都相同才算相同。关键字后面的字段都受影响
select distinct col1, col2
from mytable;
```

**关键字limit**
```sql
--limit限制返回的行数。可以有两个参数,第一个参数为起始行(即这一行向下开始)，第二个参数为返回的总行数
select col1, col2
from mytable
limit 0,5;/limit 5; --返回前5行
```
```sql
select col1, col2 --返回3-5行
from mytable
limit 2,3
```

**排序关键字asc**
```sql
select *
from mytable
order by col1 asc, col2 desc;--asc顺序,desc降序
```

**过滤数据**  
不进行过滤的数据非常多，如果不过滤数据就进行发送，会很浪费带宽，  
所以应该使用SQL语句在服务器端进行过滤，减少带宽的消耗。

```sql
select *
from mytable
where col1 is NULL
```

下面是where字句可以使用的操作符  

|  操作符 | 说明  |
| ------------ | ------------ |
| = <  >  | 等于 小于 大于 |
| <> !=  | 不等于  |
| <= !> | 小于等于 |
| >= !< | 大于等于 |
| BETWEEN | 在两个值之间 |
| IS NULL | 为NULL值 |

**AND OR**用于连接多个过滤条件，优先处理AND必要时可以用()来决定优先级  
**IN**用于匹配一组值，其后也可以接一个 SELECT 子句，从而匹配子查询得到的一组值  
**NOT**用于否定一个条件

```sql
select * 
from mytable 
where col1 < 1000 and col2 > 30;
```
```sql
select *
from mytable
where col1 in (1001,1009); --in指的是1001，和1009两个值，不是1001-1009
```

**通配符**  
通配符也是用在过滤语句中，但它只能用于文本字段。  
不要滥用通配符，通配符位于开头处匹配会非常慢。  

    like操作符
        %:任何字符出现任意次数
    	_:任何字符出现一次
```sql
select *
from mytable
where clo like '[^AB]%'; --匹配不以AB开始的任意字符
```


**计算字段**  
在数据库服务器上完成数据的转换和格式化的工作往往比客户端上快的多，  
并且转换和格式化后的数据量更少的话可以减少网络通信量  
计算字段通常需要使用 **AS** 关键字来取别名，否则输出的时候字段名为计算表达式  

```sql
select col1*col2 as cc2
from mytable
```

**concat()**函数用于连接连个字段。许多数据库会使用空格把一个值填充为列宽，因此  
连接的结果会出现一些不必要的空格使用 **TRIM()** 可以去除首尾空格。

```sql
select concat(Trim(col1), '(', Trim(col2), ')')
from mytable
```

# 函数
各个DBMS的函数功能都是不相同的，所以不可移植

## 文本处理类函数
| 函数 | 说明 |
| ----------- | ---------- |
| left() right() | 左边或者右边字符 |
| lower() upper() | 转换为小写或大写 |
| ltrim() rtim() | 去除左边或者右边空格 |
| length() | 长度 |
| sundex() | 转换为语音值 |
其中，**soundex()** 是将一个字符串转换为描述语言表示的字母数字木事的算法，它是根据发音而不是字母比较

```sql
select *
from mytable
where soundex(col1) = soundex('apple')
```

## 日期和时间处理 

- 日期格式: YYYY-MM-DD
- 时间格式: HH:MM:SS

| 函数 | 说明 |
| ----------- | ---------- |
| Adddate() | 增加一个日期 |
| Addtime() | 增加一个时间 |
| CurDate() | 返回当前日期 |
| CurTime() | 返回当前时间 |
| Date() | 返回日期时间的日期部分 |
| DateDiff() | 计算两个日期之差 |
| Time() | 返回一个日期时间的时间部分 |
| Year() | 返回一个日期时间的年份部分 |
| Now() | 返回当前日期和时间 |

```sql
mysql> select now();
        -> '2018-06-05 14:01:52'
```

## 数值处理
| 函数 | 说明 |
| ------ | ------ |
| sin() | 正弦 |
| cos() | 余弦 |
| tan() | 正切 |
| abs() | 绝对值 |
| sort() | 平方根 |
| mod() | 余数 |
| exp() | 指数 |
| PI() | 圆周率 |
| rand() | 随机数 |

## 汇总
| 函数 | 说明 |
| ------ | ------ |
| avg() | 返回某列的平均值 |
| count() | 返回某列的行数 |
| max() | 返回某列的最大值 |
| min() | 返回某列的最小值 |
| sum() | 返回某列值之和 |

```sql
select avg(distinct col1) as avg_col
from mytable
```

# 分组
分组就是把具有相同的数据的值得行放在同一组中。  
可以对同一分组数据使用汇总函数进行处理，例如求分组数据的平均值等。  
指定的分组字段处理能让数据按该字段进行分组，也可以按该字段进行排序。

```sql
select col, count(*) as num
from mytble
group by col;
```



