<!-- Tuples.md --- 
;; 
;; Description: 
;; Author: Hongyi Wu(吴鸿毅)
;; Email: wuhongyi@qq.com 
;; Created: 三 6月 21 22:33:14 2017 (+0800)
;; Last-Updated: 三 6月 21 22:39:13 2017 (+0800)
;;           By: Hongyi Wu(吴鸿毅)
;;     Update #: 1
;; URL: http://wuhongyi.cn -->

# Tuples  元组

Python的元组与列表类似，不同之处在于元组的元素不能修改。  
元组使用小括号，列表使用方括号。  
元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。  
```python
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";
```

## 创建空元组

```python
tup1 = ();
```
元组中只包含一个元素时，需要在元素后面添加逗号
```python
tup1 = (50,);
```
元组与字符串类似，下标索引从0开始，可以进行截取，组合等。

## 访问元组

元组可以使用下标索引来访问元组中的值，如下实例:
```python
#!/usr/bin/python
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print "tup1[0]: ", tup1[0]
print "tup2[1:5]: ", tup2[1:5]
```

## 修改元组

元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下实例:
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# 以下修改元组元素操作是非法的。
# tup1[0] = 100;

# 创建一个新的元组
tup3 = tup1 + tup2;
print tup3;
```


## 删除元组

元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下实例:
```python
#!/usr/bin/python
tup = ('physics', 'chemistry', 1997, 2000);
print tup;
del tup;
print "After deleting tup : "
print tup;
```
以上实例元组被删除后，输出变量会有异常信息



----

## 元组内置函数

Python元组包含了以下内置函数

- cmp(tuple1, tuple2)   比较两个元组元素。
- len(tuple)   计算元组元素个数。
- max(tuple)   返回元组中元素最大值。
- min(tuple)   返回元组中元素最小值。
- tuple(seq)   将列表转换为元组。
























----

> http://www.runoob.com/python/python-tuples.html

<!-- Tuples.md ends here -->
