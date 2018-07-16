import selenium
import pymongo
from pymongo import MongoClient
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import re
from pyquery import PyQuery as pq
browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)
def next_page(page_number):
    try:
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > input'))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit'))
        )
        input.clear()
        input.send_keys(page_number)
        submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > ul > li.item.active > span'),str(page_number))
        )
        import_to_mongodb(get_products())
    except TimeoutException:
        next_page(page_number)
def get_products():
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-itemlist .items .item'))
    )
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
         yield {
            'image':item.find('.pic .img').attr('data-src'),
            'price':item.find('.price').text()[2:],
            'deal':item.find('.deal-cnt').text()[:-3],
            'title':item.find('.J_ClickStat').text(),
            'shop':item.find('.shop').text(),
            'location':item.find('.location').text()
        }

def import_to_mongodb(product):
    db = MongoClient().test
    db.taobao.insert_many(product)
#解析网页
# def get_products():
#     #先判断是否加载完毕
#     try:
#         wait.until(
#             EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items item'))
#         )
#         html = browser.page_source #获取网页源码
#         doc = pq(html)#解析
#     #获取所有选择内容
#         items = doc('#mainsrp-itemlist .items .item').items()
#         for item in items:
#             product = {
#             #find  选择器   img这个标签下的
#                 'image' : item.find('.pic .img').attr('data-src'), #src属性
#             #'title' : item.find('.row .H').text(),
#                 'title': item.find('.J_ClickStat').text(),
#                 'sell' : item.find('.deal-cnt').text(),
#                 'price': item.find('.price').text(),
#                 'localtion':item.find('.location').text(),
#                 'shop' : item.find('.shop').text()
#             }
#             print(product)
#     except TimeoutException:
#         get_products()
def search():
    try:
        browser.get('https://www.taobao.com/')
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#q'))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button'))
        )
        input.send_keys('美食')
        submit.click()
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.total')))
        return total.text
    except TimeoutException:
        return search()
def main():
    total = search()
    total = int(re.findall('(\d+)',total)[0])
    for i in range(2,total+1):
        next_page(i)
if __name__ == '__main__':
    main()