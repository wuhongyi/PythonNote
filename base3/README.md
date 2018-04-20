<!-- README.md --- 
;; 
;; Description: 
;; Author: Hongyi Wu(吴鸿毅)
;; Email: wuhongyi@qq.com 
;; Created: 五 4月 20 23:13:46 2018 (+0800)
;; Last-Updated: 五 4月 20 23:48:31 2018 (+0800)
;;           By: Hongyi Wu(吴鸿毅)
;;     Update #: 4
;; URL: http://wuhongyi.cn -->

# README

本章节内容主要收集、摘录于以下网站：

> http://www.runoob.com/python3/python3-tutorial.html


----

## 第一个Python3.x程序

```python
#!/usr/bin/python3
 
print("Hello, World!");
```

将以上代码保存在hello.py文件中并使用python命令执行该脚本文件。

```bash
python3 hello.py
```

*关于实例中第一行代码#!/usr/bin/python3 的理解：*

- 如果调用python脚本时，使用:
```bash
python script.py
```
*#!/usr/bin/python3* 被忽略，等同于注释。

- 如果调用python脚本时，使用:
```bash
./script.py
```
*#!/usr/bin/python3* 指定解释器的路径。

----

## 标识符

- 第一个字符必须是字母表中字母或下划线 _ 。
- 标识符的其他的部分由字母、数字和下划线组成。
- 标识符对大小写敏感。

在 Python 3 中，非 ASCII 标识符也是允许的了。


## python保留字

保留字即关键字，我们不能把它们用作任何标识符名称。Python 的标准库提供了一个 keyword 模块，可以输出当前版本的所有关键字：

```python
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```


## 注释

Python中单行注释以 **#** 开头，实例如下：

```python
#!/usr/bin/python3

# 第一个注释
print ("Hello, Python!") # 第二个注释
```

多行注释可以用多个 **#** 号，还有 **'''** 和 **"""**：

```python
#!/usr/bin/python3

# 第一个注释
# 第二个注释

'''
第三注释
第四注释
'''

"""
第五注释
第六注释
"""
print ("Hello, Python!") 
```



## 行与缩进

python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。

缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。实例如下：

```python
if True:
    print ("True")
else:
	print ("False")
	```
	
以下代码最后一行语句缩进数的空格数不一致，会导致运行错误：

```python
if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
  print ("False")    # 缩进不一致，会导致运行错误
```

## import 与 from...import

在 python 用 **import** 或者 **from...import** 来导入相应的模块。

将整个模块(somemodule)导入，格式为： **import somemodule**

从某个模块中导入某个函数,格式为： **from somemodule import somefunction**

从某个模块中导入多个函数,格式为： **from somemodule import firstfunc, secondfunc, thirdfunc**

将某个模块中的全部函数导入，格式为： **from somemodule import ***


## 数字(Number)类型

python中数字有四种类型：整数、布尔型、浮点数和复数。

- int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
- bool (布尔), 如 True。
- float (浮点数), 如 1.23、3E-2
- complex (复数), 如 1 + 2j、 1.1 + 2.2j


## 字符串(String)

python中单引号和双引号使用完全相同。

- 使用三引号('''或""")可以指定一个多行字符串。
- 转义符 '\'
- 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
- 按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
- 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
- Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
- Python中的字符串不能改变。
- Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
- 字符串的截取的语法格式如下：变量[头下标:尾下标]
- word = '字符串'
- sentence = "这是一个句子。"
- paragraph = """这是一个段落，
- 可以由多行组成"""

```python
#!/usr/bin/python3

str='wuhongyi'

print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始的后的所有字符
print(str * 2)             # 输出字符串两次
print(str + '你好')        # 连接字符串

print('------------------------------')

print('hello\nwuhongyi')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nwuhongyi')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
```




<!-- README.md ends here -->
