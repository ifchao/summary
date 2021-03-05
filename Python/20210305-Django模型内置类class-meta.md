___
- FileName: 20210305-Django模型内置类class-meta.md
- Author: ihuangch -huangch96@qq.com
- Description: ---
- Create:2021-03-05 09:33:51
___

# Django Model 内置类class meta作用

Django ORM可以通过内嵌类 "class meta" 给你的 model 定义元数据，具体使用方法如下:

```python
class ModelsName(models.Model):
    bar = models.CharField(maxlength=30)

    class meta:
        #...
```
model的元数据，即数据库表的元数据，针对整个数据库表，不是一个字段的数据

# class meta有哪些属性，具体什么作用

- app_label： django 默认创建的数据库表名 `appName_modelName` 这种格式，如果在其他地方写了一个model类，但是这个model属于另外一个app，则需要指定这个app_label属性，`app_label='myapp'`
- db_table: 自定义数据库表名，`db_table='my_tableName'` 不指定的话，使用默认名称 `appName_modelName`
- ordering: Django模型对象返回的记录结果集是按照哪个字段排序的，
```
ordering = ['-order_date'] 
# 返回结果对 order_date 降序排序，'-' 表示降序
ordering = ['pub_date']
# 返回结果对 pub_date 升序排序   
ordering = ['-pub_date', 'author']
# 返回结果对 pub_date 降序排序，author 升序排序
ordering = ['?order_date']
# 返回结果随机排序 '?' 表示随机 
```
- abstract: 如果设置为 True 则表示设置为抽象基类，作用是为其他的 model 类提供一些公有属性，避免重复编码
- verbose_name: 为 model 起一个更可读名字
- unique_together: 当需要通过两个字段保持唯一性时使用。在数据库进行写表操作的时候，往往会遇到两个字段组合起来唯一使用的情况，如IP和Port。这个时候 unique_together 就很有用了，可以这样设置 `unique_together = (('ip', 'port'), )` 