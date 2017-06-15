<!-- PythonNote.md --- 
;; 
;; Description: 
;; Author: Hongyi Wu(吴鸿毅)
;; Email: wuhongyi@qq.com 
;; Created: 三 2月 17 21:59:38 2016 (+0800)
;; Last-Updated: 三 2月 17 22:45:31 2016 (+0800)
;;           By: Hongyi Wu(吴鸿毅)
;;     Update #: 6
;; URL: http://wuhongyi.cn -->

# Python 笔记

## 吴鸿毅(wuhongyi@qq.com)

----

### 数字和表达式

长整型数：普通整数只能介于-2147483648与2147483647之间，如果真的需要大数，可以使用长整型数。长整型数书写方法和普通整数一样，但是结尾有个L。

十六进制写法为：

~~~
0xAF
~~~

八进制写法为：

~~~
052
~~~

首数字都是0。


### 变量

变量名可以包括字母、数字和下划线。变量不能以数字开头。

### 打印输出

~~~
print("Out Put.")

x = 3*4
print(x)
print("zzzz"+x)
~~~

### 获取用户输入

~~~
x = input("提示符:")

y = input()

name = raw_input("what:")
~~~

等待终端输入并赋值给变量。

### 模块

使用 **import** 来导入模块。然后按照模块.函数的格式使用该模块的函数。尽量多使用这个形式。

~~~
import  模块
模块.函数
~~~

在确定不会导入多个同名函数（从不同模块导入）的情况下，可能不希望每次在每次调用函数的时候都写上模块的名字，可使用以下形式：

~~~
from  模块  import  函数
函数
~~~

----




----

Python基础教程（第二版）.pdf  P

----


<!-- PythonNote.md ends here -->
