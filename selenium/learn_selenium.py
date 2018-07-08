from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
#browser = webdriver.Chrome()
#selenium基本操作
#try:
#    browser.get('http://www.baidu.com')
#    input = browser.find_element_by_id('kw')
#    input.send_keys('Python')
#    input.send_keys(Keys.ENTER)
#    wait = WebDriverWait(browser,10)
#    wait.until(EC.presence_of_all_elements_located((By.ID,'content_left')))
#    print(browser.current_url)
#    print(browser.get_cookies())
#   print(browser.page_source)
#finally:
#    browser.close()

#声明浏览器对象
#browser = webdriver.Chrome()

#访问页面
#browser = webdriver.Chrome()
#browser.get('http://www.taobao.com')
#print(browser.page_source)
#browser.close()

#查找元素
#单个元素
browser = webdriver.Chrome()
browser.get('http://www.taobao.com')
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first)
print(input_second)
print(input_third)
#通用方法
print(browser.find_element(By.ID,'q'))
browser.close()