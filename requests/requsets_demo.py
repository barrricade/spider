import requests
#response = requests.get('http://www.baidu.com')

#各种请求方式
#requests.post('http://httpbin.org/post')
#requests.put('http://httpbin.org/put')
#requests.delete('http://httpbin.org/delete')
#requests.head('http://httpbin.org/get')
#requests.options('http://httpbin.org/get')

#带参数的get请求
#response = requests.get('http://httpbin.org/get?name=germey&age=22')
#print(response.text)

#a = {
#    'name':'germey',
#    'age':22
#}
#response = requests.get('http://httpbin.org/get',params=data)
#print(response.text)

#解析json
#response = requests.get('http://httpbin.org/get')
#print(response.json())

#获取二进制信息并保存图片
#response = requests.get('https://avatars3.githubusercontent.com/u/26743428?s=40&v=4')
#with open ('/home/jakey/spider_file/1.JPEG','wb') as f:
#    f.write(response.content)

#添加header
#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0'}
#response = requests.get('http://www.zhihu.com/explore',headers=headers)
#print(response.text)

#基本post请求
#data = {'name':'germey','age':22}
#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0'}
#response = requests.post('http://www.baidu.com/post',data=data,headers=headers)
#print(response.text)

#响应
#response = requests.get('http://www.baidu.com')
#print(response.status_code)
#print(response.headers)
#print(response.cookies)
#print(response.url)
#print(response.history)

#状态码的判断
#response = requests.get('http://www.baidu.com')
#exit() if not response.status_code==200 else print('Request Successfully')

#高级操作

#文件上传
#files = {'file':open('/home/jakey/spider_file/1.JPEG','rb')}#wb,rb二进制编码
#response = requests.post("http://httpbin.org/post",files=files)
#print(response.text)

#获取cookie
#response = requests.get('http://www.baidu.com')
#print(response.cookies)
#for key,value in response.cookies.items():
#    print(key + '=' +value)

#会话维持
#s = requests.Session()
#s.get('http://httpbin.org/cookies/set/number/123445')
#response = s.get('http://httpbin.org/cookies')
#print(response.text)

#证书验证
#未认证的证书报错
#response = requests.get('https://travel.12306.cn/portal')
#print(response.status_code)

#出现连接警告
#response = requests.get('https://travel.12306.cn/portal',verify=False)
#print(response.status_code)

#import urllib3
#urllib3.disable_warnings()
#response = requests.get('https://travel.12306.cn/portal',verify=False)
#print(response.status_code)

#代理设置
#proxies = {
#    'http':'http://127.0.0.1:9743',
#    'https':'https://127.0.0.1:9743'
#}
#response = requests.get('http://www.baidu.com',proxies=proxies)
#print(response.status_code)

#超时设置
#response = requests.get('http://www.baidu.com',timeout = 1)
#print(response.status_code)

#认证设置
from requests.auth import HTTPBasicAuth
r = requests.get('http://120.27.34.24:9001',auth=HTTPBasicAuth('user','123'))
print(r.status_code)