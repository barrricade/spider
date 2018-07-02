import re
#.的使用 站位符，不包括换行符
secrer_code2 = 'Quotes to Scrape'
secret_code = 'hadk.fali-fxxIxxfasdjifja134xxlovexx2345sdfxxyouxx8dfse'
'''a = 'xy123'
print(re.findall('x..',a))'''
#*的使用 匹配之前的元素无数次
'''a = 'xyxy123'
b = re.findall('x*',a)
print(b)'''
#?的使用方法 匹配之前的字符一次或0次
'''a = 'xy123'
b = re.findall('x?',a)
print(b)'''
#.*的使用 贪心算法
'''a = 'xyxy123'
b = re.findall('xx.*xx',secret_code)
print(b)'''
#.*?的使用 非贪心算法
'''b = re.findall('xx(.*?)xx',secret_code)
print(b)'''
b = re.findall('\w+',secrer_code2)
print(b)
