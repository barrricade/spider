import requests
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0'}
response = requests.get('http://maoyan.com/board/4?offset=0',headers = headers)
print(response.text)