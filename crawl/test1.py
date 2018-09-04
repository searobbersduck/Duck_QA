#!/usr/bin/env python
# @Time    : 2018/8/7 下午5:52
# @Author  : SeaRobbersAndDuck
# @Site    : 
# @File    : test1.py.py
# @Software: PyCharm

import urllib.request
url = 'https://www.baidu.com'
file = urllib.request.urlopen('https://www.baidu.com')
data = file.read()
print(data)
with open('./text.html', 'wb') as f:
    f.write(data)
print(file.info)
print(file.getcode())
print(file.geturl())
print(urllib.request.quote(url))
print(urllib.request.unquote(url))

header = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

request = urllib.request.Request(url, headers=header)
response = urllib.request.urlopen(request).read()

with open('./text2.html', 'wb') as f:
    f.write(response)

url='http://www.baidu.com/s?wd='
key='fengxin的博客'
key_code=urllib.request.quote(key)  #因为URL里含中文，需要进行编码
url_all=url+key_code

request = urllib.request.Request(url_all, headers=header)
response = urllib.request.urlopen(request).read()

response = response.encode('gbk','ignore').decode('gbk')

with open('./text3.html', 'wb') as f:
    f.write(response)