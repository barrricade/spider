import re
#.的使用 站位符，不包括换行符
#secrer_code2 = 'Quotes to Scrape'
#secret_code = 'hadk.fali-fxxIxxfasdjifja134xxlovexx2345sdfxxyouxx8dfse'
#a = 'xy123'
#print(re.findall('x..',secret_code))
#*的使用 匹配之前的元素无数次
#a = 'xyxy123'
#b = re.findall('x*',a)
#print(b)
#?的使用方法 匹配之前的字符一次或0次
#a = 'xy123'
#b = re.findall('x?',a)
#print(b)
#.*的使用 贪心算法,xx中间所有字符都匹配
#a = 'xyxy123'
#b = re.findall('xx.*xx',secret_code)
#print(b)
#.*?的使用 非贪心算法,只匹配xx和xx中间的字符
#b = re.findall('xx(.*?)xx',secret_code)
#print(b)
#b = re.findall('\w+',secrer_code2)
#end = time.time()
#print(b,end-start)

#re.match(patten,string,flags=0)
content = 'Hello 123 4567 World_This is a Regex Demo'

#常规匹配
#result = re.match('^Hello\s\d\d\d\s\d\d\d\d\s.*Demo$',content)
#print(result)

#泛匹配
#result = re.match('^Hello.*Demo$',content)
#print(result)

#匹配目标
#result = re.match('^Hello\s(\d.*)World.*Demo$',content)
#print(result.group(1))
#123 4567 

#贪婪匹配
#result = re.match('^Hello.*(\d+).*Demo$',content)
#print(result.group(1))
#7

#非贪婪匹配
#result = re.match('^He.*?(\d+.*)\d.*Demo$',content)
#print(result.group(1))
#123 4567

