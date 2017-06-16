<!-- requests.md --- 
;; 
;; Description: 
;; Author: Hongyi Wu(吴鸿毅)
;; Email: wuhongyi@qq.com 
;; Created: 五 6月 16 21:08:56 2017 (+0800)
;; Last-Updated: 五 6月 16 21:41:16 2017 (+0800)
;;           By: Hongyi Wu(吴鸿毅)
;;     Update #: 1
;; URL: http://wuhongyi.cn -->

# requests

导入requests库：
```python
import requests #导入requests库
```

```python
r = requests.get('https://unsplash.com') #像目标url地址发送get请求，返回一个response对象
print(r.text) #r.text是http response的网页HTML
```

----

## get 请求

```python
r = requests.get("https://unsplash.com")
```
其实就是向网站发送了一个get请求，然后网站会返回一个response。r 就是response。可以在运行的时候查看r的type。
```python
print(type(r))
```

get请求还可以传递参数：
```python
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
```
上面代码向服务器发送的请求中包含了两个参数key1和key2，以及两个参数的值。实际上它构造成了如下网址：
```python
http://httpbin.org/get?key1=value1&key2=value2
```

----

## POST请求

无参数的post请求：
```python
r = requests.post("http://httpbin.org/post")
```


有参数的post请求：
```python
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
```
post请求多用来提交表单数据，即填写一堆输入框，然后提交。





<!-- requests.md ends here -->
