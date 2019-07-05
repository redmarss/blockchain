#conding:utf-8

import requests
import re

starturl = "http://www.heibanke.com/lesson/crawler_ex00/"

num = 0

r = requests.get(starturl)
reg = re.compile('<h3>(.*?)</h3>')

f = re.findall(reg,r.text)
print(f)