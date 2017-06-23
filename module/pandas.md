<!-- pandas.md --- 
;; 
;; Description: 
;; Author: Hongyi Wu(吴鸿毅)
;; Email: wuhongyi@qq.com 
;; Created: 五 6月  2 21:24:41 2017 (+0800)
;; Last-Updated: 五 6月 23 23:52:02 2017 (+0800)
;;           By: Hongyi Wu(吴鸿毅)
;;     Update #: 5
;; URL: http://wuhongyi.cn -->

# pandas

> http://pandas.pydata.org/
> http://pandas.pydata.org/pandas-docs/stable/whatsnew.html
> http://pandas.pydata.org/pandas-docs/stable/10min.html

----




----

## 数据加载

*导入文本数据*

1、导入文本格式数据(CSV)的方法：

方法一：使用pd.read_csv()，默认打开csv文件。

```python
import pandas as pd
df = pd.reas_csv("aaa.csv")
print(df)
```

方法二：使用pd.read.table(),需要指定是什么样分隔符的文本文件。用sep=””来指定。

```python
import pandas as pd
df = pd.read_table("aaa.csv",sep=",")
print(df)
```

2、当文件没有标题行时

可以让pandas为其自动分配默认的列名。

```python
import pandas as pd
df = pd.read_csv("aaa.csv",header = None)
print(df)
```

也可以自己定义列名。

```python
import pandas as pd
df = pd.read_csv("aaa.csv",names=['a','b','c','d','message'])
print(df)
```

3、将某一列作为索引，比如使用message列做索引。通过index\_col参数指定’message’。

```python
import pandas as pd
names=['a','b','c','d','message']
df = pd.read_csv("aaa.csv",names=names,index_col="message")
print(df)
```

4、要将多个列做成一个层次化索引，只需传入由列编号或列名组成的列表即可。

```python
import pandas as pd
df = pd.read_csv("aaa.csv",index_col=["key1","key2"])
print(df)
```

5、文本中缺失值处理，缺失数据要么是没有(空字符串)，要么是用某个标记值表示的，默认情况下，pandas会用一组经常出现的标记值进行识别，如NA、NULL等。查找出结果以NAN显示。

```python
import pandas as pd
df = pd.read_csv("aaa.csv",na_values=['NA'])
#或者
df = pd.read_csv("aaa.csv",na_values=['NULL'])
print(df)
```

6、逐块读取文本文件

如果只想读取几行(避免读取整个文件)，通过nrows进行制定即可。

```python
import pandas as pd
df = pd.read_csv("aaa.csv",nrows=2)
print(df)
```

7、对于不是使用固定分隔符分割的表格，可以使用正则表达式来作为read\_table的分隔符。

```python
import pandas as pd
df = pd.read_csv("aaa.csv",sep='\s+')
print(df)
# (’\s+’是正则表达式中的字符)。
```

*导入JSON数据*

JSON数据是通过HTTP请求在Web浏览器和其他应用程序之间发送数据的标注形式之一。通过json.loads即可将JSON对象转换成Python对象。(import json) 对应的json.dumps则将Python对象转换成JSON格式。

*导入EXCEL数据*


直接使用read\_excel(文件名路径)进行获取，与读取CSV格式的文件类似。

*导入数据库数据*

主要包含两种数据库文件，一种是SQL关系型数据库数据，另一种是非SQL型数据库数据即MongoDB数据库文件。





----

> http://www.cnblogs.com/chaosimple/p/4153083.html

[python数据分析笔记——数据加载与整理](http://www.36dsj.com/archives/77293)

<!-- pandas.md ends here -->
