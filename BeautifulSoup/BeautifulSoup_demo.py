from bs4 import BeautifulSoup
import requests
content = requests.get('http://book.douban.com').text
soup = BeautifulSoup(content,'lxml')
#print(soup.prettify())
#print(soup.title.string)

#标签选择器
#选择元素
#print(soup.title)
#print(soup.head)
#print(soup.p)

#获取名称
#print(soup.title.name)

#获取属性
#print(soup.p['name'])

#获取内容
#print(soup.p.string)

#嵌套选择
#print(soup.head.title.string)

#子节点和子孙节点
#print(soup.p.contents)返回所有的子节点
#print(soup.p.childer)

#获取父节点和祖先节点
#print(soup.a.parent)
#print(list(enumerate(soup.a.parents)))

#获取兄弟节点
#print(list(enumerate(soup.a.next_sibilings)))
#print(list(enumerate(soup.a.previous_sibilings)))

#CSS选择器 select直接传入CSS选择器
#print(soup)
#print(soup.select('.book-info .name')) #class，从class = name开始匹配
#print(soup.select('#list-2 .element'))#id标签中的class

#循环获取
#for ul in soup.select('ul'):
#    print(ul.select('li'))

#获取属性
#for ul in soup.select('ul'):
#    print(ul('id'))

#获取内容
for ul in soup.select('li'):
    print(ul.get_text())
#print(soup)