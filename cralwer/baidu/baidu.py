from bs4 import BeautifulSoup
import requests
import elasticsearch_dsl
from elasticsearch import Elasticsearch

client = Elasticsearch("localhost:9200")

#结构话数据并保存到es
def structured_data(content):
    for tag in content:
        result = {"title": tag.get("title"),
                  "text": tag.string,
                  "href": "http://tieba.baidu.com" + tag.get("href")}
        client.index(index="baidu",body=result)
        # yield result
    return "ok"
#获取网页并分析
def get_html(url):
    baidu = requests.get(url, timeout=30)
    baidu.encoding = baidu.apparent_endconding
    soup = BeautifulSoup(baidu, features="lxml")
    comment = soup.find_all("a", "j_th_tit")
    structured_data(comment)