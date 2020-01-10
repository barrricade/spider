from bs4 import BeautifulSoup
import requests
import elasticsearch_dsl
from elasticsearch import Elasticsearch

client = Elasticsearch("localhost:9200")


def get_html(url):
    page = requests.get(url, timeout=40)
    page.encoding = page.apparent_encoding
    page = BeautifulSoup(page.text, features="lxml")
    analysis_page(page)


def analysis_page(page):
    contents = page.find_all('li')
    for item in contents:
        tag = item.find('div', class_='pic')
        txt = item.find('div', class_='txt')
        if tag and txt:
            image_tag = tag.find('img')
            button = tag.find('a')
            actors = txt.find('p', class_='pActor').find_all('a')
            title = image_tag.get('title', "")
            img = image_tag.get('src', "")
            time = txt.find('p', class_='pTit').find(
                'span', class_='sIntro')
            if time:
                time = time.text
            detail = button.get('href', "")
            actor = [i.string for i in actors]
            introduction = txt.find('p', 'pTxt').text
            result = {
                'title': title,
                'img': img,
                'release_time': time,
                'actors': actor,
                'introduction': introduction,
                'detail': detail
            }
            structured_data(result)
    print('储存完毕')


def structured_data(result):
    client.index(index="movies", body=result)
    print('正在存储')


if __name__ == '__main__':
    get_html(url="http://dianying.2345.com/top/")
