<!-- BeautifulSoup.md --- 
;; 
;; Description: 
;; Author: Hongyi Wu(吴鸿毅)
;; Email: wuhongyi@qq.com 
;; Created: 五 6月 16 23:20:53 2017 (+0800)
;; Last-Updated: 六 6月 17 12:05:26 2017 (+0800)
;;           By: Hongyi Wu(吴鸿毅)
;;     Update #: 2
;; URL: http://wuhongyi.cn -->

# BeautifulSoup

[Beautiful Soup 4.2.0 文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html)

Beautiful Soup是python的一个库，最主要的功能是从网页抓取数据。官方解释如下：

- Beautiful Soup提供一些简单的、python式的函数用来处理导航、搜索、修改分析树等功能。它是一个工具箱，通过解析文档为用户提供需要抓取的数据，因为简单，所以不需要多少代码就可以写出一个完整的应用程序。
- Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码。你不需要考虑编码方式，除非文档没有指定一个编码方式，这时，Beautiful Soup就不能自动识别编码方式了。然后，你仅仅需要说明一下原始编码方式就可以了。
- Beautiful Soup已成为和lxml、html6lib一样出色的python解释器，为用户灵活地提供不同的解析策略或强劲的速度。


Beautiful Soup 安装:  
```bash
pip install BeautifulSoup  #Beautiful Soup 3
pip install BeautifulSoup4  # Beautiful Soup 4
```

```python
from BeautifulSoup import BeautifulSoup  #Beautiful Soup 3
from bs4 import BeautifulSoup  # Beautiful Soup 4
```



> http://cuiqingcai.com/1319.html

<!-- BeautifulSoup.md ends here -->
