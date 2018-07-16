import requests
from urllib.parse import urlencode
import re
import time
from requests.exceptions import RequestException
import json
from bs4 import BeautifulSoup
def get_one_page(offset,keyword):
    data = {'offset':offset,
    'format': 'json',
    'keyword': keyword,
    'autoload': 'true',
    'count':'20',
    'cur_tab': 1
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    try:
        response = requests.get(url)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None 
def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')

def get_page_detail(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1',
               'Referer':'http://www.mzitu.com/'
               }
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None
def parse_page_detail(html):
    soup = BeautifulSoup(html,'lxml')
    for ul in soup.select('title'):
        title = ul.get_text()
        return title
def main():
    html = get_one_page(0,'街拍')
    parse_page_index(html)
    for url in parse_page_index(html):
        print(url)
        time.sleep(10)
        html = get_page_detail(url)
        print(html)
    # print(parse_page_detail(html))
if __name__ == '__main__':
    main()