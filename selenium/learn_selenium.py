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
#browser = webdriver.Chrome()
#browser.get('http://www.taobao.com')
#input_first = browser.find_element_by_id('q')
#input_second = browser.find_element_by_css_selector('#q')
#input_third = browser.find_element_by_xpath('//*[@id="q"]')
#print(input_first)
#print(input_second)
#print(input_third)
#通用方法
#print(browser.find_element(By.ID,'q'))
#browser.close()

#多个元素
#list = browser.find_elements_by_css_selector('.service-bd li')
#print(list)
#browser.close()

#元素交互操作,webdriver api 查询
#input = browser.find_element_by_id('q')
#input.send_keys('ipad')
#button = browser.find_element_by_class_name('btn-search')
#button.click()

#交互动作 将动作加入动作链中串行执行 Action Chains api

#执行Js
#browser = webdriver.Chrome()
#browser.get('http://www.zhihu.com/explore')
#browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')#使用js完成下拉
#browser.execute_script('alert("To Bottom")')#提示框

#获取元素信息
#获取属性
#logo = browser.find_element_by_id('zh-top-link-logo')
#print(logo)
#print(logo.get_attribute('class'))

#获取文本值
#input = browser.find_element_by_class_name('zu-top-add-question')
#print(input.text)

#获取id，位置，标签名，大小
#.id,.location,.tag_name,.size

#等待
#隐式等待：webdriver没有在DOM中找到元素，将会继续等待，超出设定时间后则会
#抛出找不到元素。当查找元素没有立即出现的时候，隐式等待会等待一段时间在查找。
#browser = webdriver.Chrome()
#browser.implicitly_wait(10)
#browser.get('http://www.zhihu.com/explore')
#input = browser.find_element_by_class_name('zu-top-add-question')
#print(input)

#显示等待
#browser = webdriver.Chrome()
#browser.get('http://www.taobao.com')
#wait = WebDriverWait(browser,10)
#input = wait.until(EC.presence_of_element_located((By.ID,'q')))
#button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'bin-search')))
#print(input,button)

#前进后退
#browser.back()
#browser.forward()

#Cookies
#browser = webdriver.Chrome()
#browser.get('http://www.zhihu.com/explore')
#print(browser.get_cookies())
#browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'germey'})
#rint(browser.get_cookies())
#browser.delete_all_cookies()
#print(browser.get_cookies())

#选项卡管理
#browser = webdriver.Chrome()
#browser.get('http://www.baidu.com')
#browser.execute_script('window.open()')
#print(browser.window_handles)
#browser.switch_to_window(browser.window_handles[1])
#browser.get('http://www.taobao.com')
#browser.switch_to_window(browser.window_handles[0])
#browser.get('http://python.org')

#异常处理
try:
    brwoser.get('http://www.baidu.com')
except TimeoutException:
    print('Time Out')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()