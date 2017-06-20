<!-- urllib2.md --- 
;; 
;; Description: 
;; Author: Hongyi Wu(吴鸿毅)
;; Email: wuhongyi@qq.com 
;; Created: 四 6月 15 23:02:50 2017 (+0800)
;; Last-Updated: 二 6月 20 21:42:45 2017 (+0800)
;;           By: Hongyi Wu(吴鸿毅)
;;     Update #: 2
;; URL: http://wuhongyi.cn -->

# urllib2

urllib2模块的 OpenerDirector 操作类。这是一个管理很多处理类（Handler）的类。而所有这些 Handler 类都对应处理相应的协议，或者特殊功能。分别有下面的处理类：
- BaseHandler
- HTTPErrorProcessor
- HTTPDefaultErrorHandler
- HTTPRedirectHandler
- ProxyHandler
- AbstractBasicAuthHandler
- HTTPBasicAuthHandler
- ProxyBasicAuthHandler
- AbstractDigestAuthHandler
- ProxyDigestAuthHandler
- AbstractHTTPHandler
- HTTPHandler
- HTTPCookieProcessor
- UnknownHandler
- FileHandler
- FTPHandler
- CacheFTPHandler








## Debug Log

使用 urllib2 时，可以通过下面的方法把 debug Log 打开，这样收发包的内容就会在屏幕上打印出来，方便调试，有时可以省去抓包的工作
```python
import urllib2
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.google.com')
```


> http://www.cnblogs.com/sysu-blackbear/p/3629770.html



<!-- urllib2.md ends here -->
