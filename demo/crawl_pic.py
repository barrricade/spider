import requests
import re 
from requests.exceptions import RequestException
import json
def get_one_page(offset,keyword):
    data = {'offset':offset,
    'format': 'json',
    'keyword': keyword,
    'autoload': 'true',
    'count':'20',
    'cur_tab': 1
    }
    response = requests.get('https://www.toutiao.com/search_content/?',params = data)
    try:
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None 
def main():
    html = get_one_page(0,'街拍')
    data = json.load(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')
if __name__ == '__main__':
    main()