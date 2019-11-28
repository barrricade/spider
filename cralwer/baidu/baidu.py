from bs4 import BeautifulSoup
import requests
import elasticsearch_dsl
from elasticsearch import Elasticsearch

client = Elasticsearch("localhost:9200")
def structured_data(content):
    for tag in content:
        result = {"title": tag.get("title"),
                  "text": tag.string,
                  "href": "http://tieba.baidu.com" + tag.get("href")}
        client.index(index="baidu",body=result)
        yield result


baidu = requests.get(
    "http://tieba.baidu.com/f?kw=%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8&ie=utf-8").text
soup = BeautifulSoup(baidu, features="html5lib")
content = soup.find_all("a", "j_th_tit")
for item in structured_data(content):
    print(item)
