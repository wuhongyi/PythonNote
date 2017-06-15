<!-- urllib.md --- 
;; 
;; Description: 
;; Author: Hongyi Wu(吴鸿毅)
;; Email: wuhongyi@qq.com 
;; Created: 四 6月 15 22:46:35 2017 (+0800)
;; Last-Updated: 四 6月 15 23:40:07 2017 (+0800)
;;           By: Hongyi Wu(吴鸿毅)
;;     Update #: 2
;; URL: http://wuhongyi.cn -->

# urllib

## urllib.urlopen(url[,data[,proxies]])

打开一个url的方法，返回一个文件对象，然后可以进行类似文件对象的操作。本例试着打开google

```python
import urllib
f = urllib.urlopen('http://www.google.com.hk/')
firstLine = f.readline()   #读取html页面的第一行
firstLine
```
 
urlopen返回对象提供方法：  
- read() , readline() ,readlines() , fileno() , close() ：这些方法的使用方式与文件对象完全一样
- info()：返回一个httplib.HTTPMessage对象，表示远程服务器返回的头信息
- getcode()：返回Http状态码。如果是http请求，200请求成功完成;404网址未找到
- geturl()：返回请求的url


## urllib.urlretrieve(url[,filename[,reporthook[,data]]])

urlretrieve方法将url定位到的html文件下载到你本地的硬盘中。如果不指定filename，则会存为临时文件。

urlretrieve()返回一个二元组(filename,mine_hdrs)

临时存放：

```python
filename = urllib.urlretrieve('http://www.google.com.hk/')
type(filename)
filename[0]
filename[1]
```

存为本地文件:

```python
filename = urllib.urlretrieve('http://www.google.com.hk/',filename='/home/dzhwen/python文件/Homework/urllib/google.html')
type(filename)
filename[0]
filename[1]
```
 

## urllib.urlcleanup()

清除由于urllib.urlretrieve()所产生的缓存

 

## urllib.quote(url)和urllib.quote_plus(url)

将url数据获取之后，并将其编码，从而适用与URL字符串中，使其能被打印和被web服务器接受。

```python
urllib.quote('http://www.baidu.com')
urllib.quote_plus('http://www.baidu.com')
```

## urllib.unquote(url)和urllib.unquote_plus(url)

与前面的函数相反。

## urllib.urlencode(query)

将URL中的键值对以连接符&划分

这里可以与urlopen结合以实现post方法和get方法：

GET方法：

```python
import urllib
params=urllib.urlencode({'spam':1,'eggs':2,'bacon':0})
params
f=urllib.urlopen("http://python.org/query?%s" % params)
print f.read()
```

POST方法：

```python
import urllib
parmas = urllib.urlencode({'spam':1,'eggs':2,'bacon':0})
f=urllib.urlopen("http://python.org/query",parmas)
f.read()
```


----

> http://www.jianshu.com/p/9b7fb13ac6c6



<!-- urllib.md ends here -->
