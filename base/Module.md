<!-- Module.md --- 
;; 
;; Description: 
;; Author: Hongyi Wu(吴鸿毅)
;; Email: wuhongyi@qq.com 
;; Created: 二 6月 20 22:26:10 2017 (+0800)
;; Last-Updated: 三 6月 21 22:31:59 2017 (+0800)
;;           By: Hongyi Wu(吴鸿毅)
;;     Update #: 2
;; URL: http://wuhongyi.cn -->

# 模块

Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句。  
模块让你能够有逻辑地组织你的 Python 代码段。  
把相关的代码分配到一个模块里能让你的代码更好用，更易懂。  
模块能定义函数，类和变量，模块里也能包含可执行的代码。  


## import 语句

模块的引入

模块定义好后，我们可以使用 import 语句来引入模块，语法如下：
```python
import module1[, module2[,... moduleN]
```
比如要引用模块 math，就可以在文件最开始的地方用 import math 来引入。在调用 math 模块中的函数时，必须这样引用：
```python
模块名.函数名
```
当解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入。  
搜索路径是一个解释器会先进行搜索的所有目录的列表。如想要导入模块 support.py，需要把命令放在脚本的顶端：
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# 导入模块
import support
 
# 现在可以调用模块里包含的函数了
support.print_func("Runoob")
```

一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行。





*未完*





























----

> http://www.runoob.com/python/python-modules.html

<!-- Module.md ends here -->
