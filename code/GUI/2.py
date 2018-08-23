#!/usr/bin/python  
#-*-coding:utf-8-*-
# 2.py --- 
# 
# Description: 
# Author: Hongyi Wu(吴鸿毅)
# Email: wuhongyi@qq.com 
# Created: 四 8月 23 12:08:56 2018 (+0800)
# Last-Updated: 四 8月 23 12:09:07 2018 (+0800)
#           By: Hongyi Wu(吴鸿毅)
#     Update #: 1
# URL: http://wuhongyi.cn 

from Tkinter import *           # 导入 Tkinter 库
root = Tk()                     # 创建窗口对象的背景色
                                # 创建两个列表
li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
listb  = Listbox(root)          #  创建两个列表组件
listb2 = Listbox(root)
for item in li:                 # 第一个小部件插入数据
    listb.insert(0,item)
 
for item in movie:              # 第二个小部件插入数据
    listb2.insert(0,item)
 
listb.pack()                    # 将小部件放置到主窗口中
listb2.pack()
root.mainloop()                 # 进入消息循环

# 
# 2.py ends here
