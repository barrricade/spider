#request(url,data=None,timeout,cafile=None,cadefault=False,context=None)
from urllib import request,parse
#请求baidu的网页源代码并解码
#response = urllib.request.urlopen('http://www.baidu.com')
#print(response.read().decode('utf-8'))
#通过post传入
#data = bytes(urllib.parse.urlencode({'world':'hello'}),encoding='utf8')
#response = urllib.request.urlopen('http://httpbin.org/get')
#print(response.read())
#timeout的使用，给出的相应时间
#response = urllib.request.urlopen('http://python.org',timeout=100)
#print(response.read().decode('utf-8'))
#print(type(response))
#print(response.status)
#print(response.getheaders())

#request.Request模块
#request = urllib.request.Request('http://www.baidu.com')
#response = urllib.request.urlopen(request)
#print(response.read().decode('utf-8'))

url = 'http://httpbin.org/POST'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0','Host':'httpbin.org' }

dict = {
    'name':'Germey'
    }
data = bytes(parse.urlencode(dict),encoding='utf8')
req = request.Request(url=url,data=data,headers=headers,method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))