<!-- cookielib.md --- 
;; 
;; Description: 
;; Author: Hongyi Wu(吴鸿毅)
;; Email: wuhongyi@qq.com 
;; Created: 六 6月 17 22:56:20 2017 (+0800)
;; Last-Updated: 二 6月 20 21:42:45 2017 (+0800)
;;           By: Hongyi Wu(吴鸿毅)
;;     Update #: 3
;; URL: http://wuhongyi.cn -->

# cookielib

cookielib模块的主要作用是提供可存储cookie的对象，以便于与urllib2模块配合使用来访问Internet资源。例如可以利用本模块的CookieJar类的对象来捕获cookie并在后续连接请求时重新发送。coiokielib模块用到的对象主要有下面几个：CookieJar、FileCookieJar、MozillaCookieJar、LWPCookieJar。


获取CookieJar实例的demo：

```python
#!/usr/bin/env python
#-*-coding:utf-8-*-

import urllib
import urllib2
import cookielib

#获取Cookiejar对象（存在本机的cookie消息）
cookie = cookielib.CookieJar()
#自定义opener,并将opener跟CookieJar对象绑定
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#安装opener,此后调用urlopen()时都会使用安装过的opener对象
urllib2.install_opener(opener)

url = "http://www.baidu.com"   
urllib2.urlopen(url)
```

用POST方法来访问网站的方式（用urllib2模拟一起post过程）：
```python
#! /usr/bin/env python
#coding=utf-8

import urllib2
import urllib
import cookielib

def login():
    email = raw_input("请输入用户名:")
    pwd = raw_input("请输入密码:")
    data={"email":email,"password":pwd}  #登陆用户名和密码
    post_data=urllib.urlencode(data)   #将post消息化成可以让服务器编码的方式
    cj=cookielib.CookieJar()   #获取cookiejar实例
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    #自己设置User-Agent（可用于伪造获取，防止某些网站防ip注入）
    headers ={"User-agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}
    website = raw_input('请输入网址:')
    req=urllib2.Request(website,post_data,headers)
    content=opener.open(req)
    print content.read()    #linux下没有gbk编码，只有utf-8编码

if __name__ == '__main__':
    login()
```

用python模拟登录的示例

```python
#  -*- coding: utf-8 -*-
# !/usr/bin/python

import urllib2
import urllib
import cookielib
import re

auth_url = 'http://www.nowamagic.net/'
home_url = 'http://www.nowamagic.net/';
# 登陆用户名和密码
data={
    "username":"nowamagic",
    "password":"pass"
}
# urllib进行编码
post_data=urllib.urlencode(data)
# 发送头信息
headers ={
    "Host":"www.nowamagic.net", 
    "Referer": "http://www.nowamagic.net"
}
# 初始化一个CookieJar来处理Cookie
cookieJar=cookielib.CookieJar()
# 实例化一个全局opener
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
# 获取cookie
req=urllib2.Request(auth_url,post_data,headers)
result = opener.open(req)
# 访问主页 自动带着cookie信息
result = opener.open(home_url)
# 显示结果
print result.read()
```

1. 使用已有的cookie访问网站
```python
import cookielib, urllib2

ckjar = cookielib.MozillaCookieJar(os.path.join('C:\Documents and Settings\tom\Application Data\Mozilla\Firefox\Profiles\h5m61j1i.default', 'cookies.txt'))

req = urllib2.Request(url, postdata, header)

req.add_header('User-Agent', \ 
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(ckjar) )

f = opener.open(req) 
htm = f.read() 
f.close()
```

2. 访问网站获得cookie，并把获得的cookie保存在cookie文件中
```python
import cookielib, urllib2

req = urllib2.Request(url, postdata, header) 
req.add_header('User-Agent', \ 
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')

ckjar = cookielib.MozillaCookieJar(filename) 
ckproc = urllib2.HTTPCookieProcessor(ckjar)

opener = urllib2.build_opener(ckproc)

f = opener.open(req) 
htm = f.read() 
f.close()

ckjar.save(ignore_discard=True, ignore_expires=True)
```

3. 使用指定的参数生成cookie,并用这个cookie访问网站
```python
import cookielib, urllib2

cookiejar = cookielib.CookieJar()
urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
values = {'redirect':", 'email':'abc@abc.com', 
          'password':'password', 'rememberme':", 'submit':'OK, Let Me In!'}
data = urllib.urlencode(values)

request = urllib2.Request(url, data)
url = urlOpener.open(request)
print url.info()
page = url.read()

request = urllib2.Request(url)
url = urlOpener.open(request)
page = url.read()
print page
```





```python
#encoding:utf8
import urllib2
import cookielib

#获取cookie,并将保存在变量中的cookie打印出来
def Cookie():
    #声明一个CookieJar对象来保存cookie
    cookie = cookielib.CookieJar()
    #创建cookie处理器
    handler = urllib2.HTTPCookieProcessor(cookie)
    #构建opener
    opener = urllib2.build_opener(handler)
    #创建请求
    res = opener.open('http://www.baidu.com')
    for item in cookie:
        print 'name:' + item.name + '-value:' + item.value

#将cookie保存在文件中
def saveCookie():
    #设置保存cookie的文件
    filename = 'cookie.txt'
    #声明一个MozillaCookieJar对象来保存cookie，之后写入文件
    cookie = cookielib.MozillaCookieJar(filename)
    #创建cookie处理器
    handler = urllib2.HTTPCookieProcessor(cookie)
    #构建opener
    opener = urllib2.build_opener(handler)
    #创建请求
    res = opener.open('http://www.baidu.com')
    #保存cookie到文件
    #ignore_discard的意思是即使cookies将被丢弃也将它保存下来
    #ignore_expires的意思是如果在该文件中cookies已经存在，则覆盖原文件写入
    cookie.save(ignore_discard=True,ignore_expires=True)

#从文件中获取cookie并且访问(我们通过这个方法就可以打开保存在本地的cookie来模拟登录)
def getCookie():
    #创建一个MozillaCookieJar对象
    cookie = cookielib.MozillaCookieJar()
    #从文件中的读取cookie内容到变量
    cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
    #打印cookie内容,证明获取cookie成功
    for item in cookie:
        print 'name:' + item.name + '-value:' + item.value
    #利用获取到的cookie创建一个opener
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    res = opener.open('http://www.baidu.com')
    print res.read()
```





> http://www.cnblogs.com/sysu-blackbear/p/3629770.html
> http://www.cnblogs.com/isuifeng/p/5903116.html

<!-- cookielib.md ends here -->
