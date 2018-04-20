<!-- py2py3.md --- 
;; 
;; Description: 
;; Author: Hongyi Wu(吴鸿毅)
;; Email: wuhongyi@qq.com 
;; Created: 五 4月 20 23:15:08 2018 (+0800)
;; Last-Updated: 五 4月 20 23:22:06 2018 (+0800)
;;           By: Hongyi Wu(吴鸿毅)
;;     Update #: 1
;; URL: http://wuhongyi.cn -->

# Python2.x与3​​.x版本区别

> http://www.runoob.com/python/python-2x-3x.html

----

## print 函数

print语句没有了，取而代之的是print()函数。 Python 2.6与Python 2.7部分地支持这种形式的print语法。在Python 2.6与Python 2.7里面，以下三种形式是等价的：

```python
print "fish"
print ("fish") #注意print后面有个空格
print("fish") #print()不能带有任何其它参数
```
然而，Python 2.6实际已经支持新的print()语法：

```python
from __future__ import print_function
print("fish", "panda", sep=', ')
```


<!-- py2py3.md ends here -->
