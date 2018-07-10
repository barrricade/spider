#requests+Regular expression
import requests
from requests.exceptions import RequestException
import re 
import json
import pandas as pd
import pymongo
from pymongo import MongoClient

def get_one_url(url):
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0'}
        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?(\d+)</i>.*?data-src="(.*?)".*?"name"'
                        +'.*?title="(.*?)".*?"star">(.*?)</p>'
                        +'.*?releasetime">(.*?)</p>'
                        +'.*?integer">(.*?)</i>.*?fraction">(\d)</i>.*?</dd>',re.S) 
    items = re.findall(pattern,html)
    for item in items:
        yield{
            '排名':item[0],
            '电影':item[2],
            '电影图片':item[1],
            '主演':item[3].strip()[3:],
            '上映时间':item[4].strip()[5:],
            '评分':item[5]+item[6]
            }

def write_to_file(data):
    data = data[['排名','电影','电影图片','主演','上映时间','评分']]
    data.to_csv('/home/jakey/workspace/movies.csv',index=False,encoding='utf-8',mode = 'a')

def import_to_mongodb(html):
    db = MongoClient().test
    db.movies.insert_many(parse_one_page(html))

def main(offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    html = get_one_url(url)
    #for item in parse_one_page(html):
    #    print(item)
    data = pd.DataFrame(parse_one_page(html))
    write_to_file(data)
    import_to_mongodb(html)

if __name__ == '__main__':
    for i in range(10):
        main(i*10)