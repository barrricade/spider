import requests
from pyquery import PyQuery as pq
html = requests.get('http://www.baidu.com').text
doc = pq(html)
#print(doc('#ftCon #cp'))
#print(doc('li'))

#查找元素
#子元素
#item= doc('#ftCon')
#lis = doc.find('#cp')
#print(lis)

#lis = item.children()
#print(lis)

#print(doc.children('#cp'))

#查找父元素
#print(item.parents())

#兄弟元素
#print(doc.siblings())

#遍历操作家items（）方法
#lis = doc('#cp').items()
#for item in lis:
#    print(item)  

#获取文本 加入text()方法
#a = doc('#cp')
#print(a.text())

#获取html 加入html（）方法
#print(doc('#cp').html())

#DOM操作
#removdclass('')
#doc().find('').remove()
#doc().attr('','')

#伪类选择器
