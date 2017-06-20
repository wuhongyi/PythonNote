<!-- File.md --- 
;; 
;; Description: 
;; Author: Hongyi Wu(吴鸿毅)
;; Email: wuhongyi@qq.com 
;; Created: 日 6月 18 09:46:10 2017 (+0800)
;; Last-Updated: 二 6月 20 22:09:31 2017 (+0800)
;;           By: Hongyi Wu(吴鸿毅)
;;     Update #: 2
;; URL: http://wuhongyi.cn -->

# File


## open 函数

你必须先用Python内置的open()函数打开一个文件，创建一个file对象，相关的方法才可以调用它进行读写。
语法：
```python
file object = open(file_name [, access_mode][, buffering])
```
各个参数的细节如下：
- file\_name：file\_name变量是一个包含了你要访问的文件名称的字符串值。
- access\_mode：access\_mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
- buffering:如果buffering的值被设为0，就不会有寄存。如果buffering的值取1，访问文件时会寄存行。如果将buffering的值设为大于1的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。

不同模式打开文件的完全列表：  
- r	    以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
- rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
- r+	打开一个文件用于读写。文件指针将会放在文件的开头。
- rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
- w	    打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
- wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
- w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
- wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
- a	    打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
- ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
- a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
- ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。

*File对象的属性*  
一个文件被打开后，你有一个file对象，你可以得到有关该文件的各种信息。  
以下是和file对象相关的所有属性的列表：  
- file.closed	返回true如果文件已被关闭，否则返回false。
- file.mode	    返回被打开文件的访问模式。
- file.name	    返回文件的名称。
- file.softspace	如果用print输出后，必须跟一个空格符，则返回false。否则返回true。


## close()方法

File 对象的 close（）方法刷新缓冲区里任何还没写入的信息，并关闭该文件，这之后便不能再进行写入。

当一个文件对象的引用被重新指定给另一个文件时，Python 会关闭之前的文件。用 close（）方法关闭文件是一个很好的习惯。

语法：
```python
fileObject.close();
```


## write()方法

write()方法可将任何字符串写入一个打开的文件。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。

write()方法不会在字符串的结尾添加换行符('\n')：  
语法：
```python
fileObject.write(string);
```
在这里，被传递的参数是要写入到已打开文件的内容。


write() 方法用于向文件中写入指定字符串。
在文件关闭前或缓冲区刷新前，字符串内容存储在缓冲区中，这时你在文件中是看不到写入的内容的。

## read()方法

read（）方法从一个打开的文件中读取一个字符串。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。

语法：
```python
fileObject.read([count]);
```
在这里，被传递的参数是要从已打开文件中读取的字节计数。该方法从文件的开头开始读入，如果没有传入count，它会尝试尽可能多地读取更多的内容，很可能是直到文件的末尾。


## 文件定位

tell()方法告诉你文件内的当前位置；换句话说，下一次的读写会发生在文件开头这么多字节之后。

seek（offset [,from]）方法改变当前文件的位置。Offset变量表示要移动的字节数。From变量指定开始移动字节的参考位置。
如果from被设为0，这意味着将文件的开头作为移动字节的参考位置。如果设为1，则使用当前的位置作为参考位置。如果它被设为2，那么该文件的末尾将作为参考位置。

例子：
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# 打开一个文件
fo = open("foo.txt", "r+")
str = fo.read(10);
print "读取的字符串是 : ", str
 
# 查找当前位置
position = fo.tell();
print "当前文件位置 : ", position
 
# 把指针再次重新定位到文件开头
position = fo.seek(0, 0);
str = fo.read(10);
print "重新读取字符串 : ", str
# 关闭打开的文件
fo.close()
```

----

## 重命名和删除文件

Python的os模块提供了帮你执行文件处理操作的方法，比如重命名和删除文件。  
要使用这个模块，你必须先导入它，然后才可以调用相关的各种功能。  
rename()方法：  
rename()方法需要两个参数，当前的文件名和新文件名。  
语法：
```python
os.rename(current_file_name, new_file_name)
```
例子：
下例将重命名一个已经存在的文件test1.txt。
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
 
# 重命名文件test1.txt到test2.txt。
os.rename( "test1.txt", "test2.txt" )
```

*remove()方法*

你可以用remove()方法删除文件，需要提供要删除的文件名作为参数。  
语法：
```python
os.remove(file_name)
例子：
下例将删除一个已经存在的文件test2.txt。
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
 
# 删除一个已经存在的文件test2.txt
os.remove("test2.txt")
```python

## Python里的目录

所有文件都包含在各个不同的目录下，不过Python也能轻松处理。os模块有许多方法能帮你创建，删除和更改目录。

*mkdir()方法*

可以使用os模块的mkdir()方法在当前目录下创建新的目录们。你需要提供一个包含了要创建的目录名称的参数。
语法：
```python
os.mkdir("newdir")
```python
例子：
下例将在当前目录下创建一个新目录test。
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
 
# 创建目录test
os.mkdir("test")
```


*chdir()方法*

可以用chdir()方法来改变当前的目录。chdir()方法需要的一个参数是你想设成当前目录的目录名称。  
语法：
```python
os.chdir("newdir")
```
例子：
下例将进入"/home/newdir"目录。
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
 
# 将当前目录改为"/home/newdir"
os.chdir("/home/newdir")
```

*getcwd()方法*

getcwd()方法显示当前的工作目录。  
语法：
```python
os.getcwd()
```
例子：  
下例给出当前目录：  
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

# 给出当前的目录
print os.getcwd()
```

*rmdir()方法*

rmdir()方法删除目录，目录名称以参数传递。  
在删除这个目录之前，它的所有内容应该先被清除。  
语法：
```python
os.rmdir('dirname')
```
例子：  
以下是删除" /tmp/test"目录的例子。目录的完全合规的名称必须被给出，否则会在当前目录下搜索该目录。

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
 
# 删除”/tmp/test”目录
os.rmdir( "/tmp/test"  )
```




> http://www.runoob.com/python/file-methods.html

<!-- File.md ends here -->
