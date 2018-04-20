<!-- List.md --- 
;; 
;; Description: 
;; Author: Hongyi Wu(吴鸿毅)
;; Email: wuhongyi@qq.com 
;; Created: 二 6月 20 22:32:14 2017 (+0800)
;; Last-Updated: 三 6月 21 22:20:15 2017 (+0800)
;;           By: Hongyi Wu(吴鸿毅)
;;     Update #: 3
;; URL: http://wuhongyi.cn -->

# List.md

序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。  
Python有6个序列的内置类型，但最常见的是列表和元组。  
序列都可以进行的操作包括索引，切片，加，乘，检查成员。  
此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。  
列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。

列表的数据项不需要具有相同的类型  
创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。如下所示：
```python
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"];
```
与字符串的索引一样，列表索引从0开始。列表可以进行截取、组合等。


## 访问列表中的值

使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符，如下所示：
```python
#!/usr/bin/python
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]
```

## 更新列表

你可以对列表的数据项进行修改或更新，你也可以使用append()方法来添加列表项，如下所示：
```python
#!/usr/bin/python
list = ['physics', 'chemistry', 1997, 2000];
print "Value available at index 2 : "
print list[2];
list[2] = 2001;
print "New value available at index 2 : "
print list[2];
```

## 删除列表元素

可以使用 del 语句来删除列表的的元素，如下实例：
```python
#!/usr/bin/python
list1 = ['physics', 'chemistry', 1997, 2000];
print list1;
del list1[2];
print "After deleting value at index 2 : "
print list1;
```

----

## Python列表函数&方法

Python包含以下函数:

- cmp(list1, list2)   比较两个列表的元素
- len(list)   列表元素个数
- max(list)   返回列表元素最大值
- min(list)   返回列表元素最小值
- list(seq)   将元组转换为列表

Python包含以下方法:

- list.append(obj)   在列表末尾添加新的对象
- list.count(obj)   统计某个元素在列表中出现的次数
- list.extend(seq)   在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
- list.index(obj)   从列表中找出某个值第一个匹配项的索引位置
- list.insert(index, obj)   将对象插入列表
- list.pop(obj=list[-1])   移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
- list.remove(obj)   移除列表中某个值的第一个匹配项
- list.reverse()   反向列表中元素
- list.sort([func])   对原列表进行排序

----

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

list01 = ['runoob', 786, 2.23, 'john', 70.2]
list02 = [123, 'john']

print list01
print list02

# 列表截取
print list01[0]
print list01[-1]
print list01[0:3]

# 列表重复
print list01 * 2

# 列表组合
print list01 + list02

# 获取列表长度
print len(list01)

# 删除列表元素
del list02[0]
print list02

# 元素是否存在于列表中
print 'john' in list02  # True

# 迭代
for i in list01:
    print i

# 比较两个列表的元素
print cmp(list01, list02)

# 列表最大/最小值
print max([0, 1, 2, 3, 4])
print min([0, 1])

# 将元组转换为列表
aTuple = (1,2,3,4)
list03 = list(aTuple)
print list03

# 在列表末尾添加新的元素
list03.append(5)
print list03

# 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list03.extend(list01)
print list03

# 统计某个元素在列表中出现的次数
print list03.count(1)

# 从列表中找出某个值第一个匹配项的索引位置
print list03.index('john')

# 将对象插入列表
list03.insert(0, 'hello')
print list03

# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print list03.pop(0)
print list03

# 移除列表中某个值的第一个匹配项
list03.remove(1)
print list03

# 反向列表中元素
list03.reverse()
print list03

# 对原列表进行排序
list03.sort()
print list03
```














----

> http://www.runoob.com/python/python-lists.html

<!-- List.md ends here -->
