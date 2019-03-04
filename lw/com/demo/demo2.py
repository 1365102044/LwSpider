
import requests
import re
from lxml import html

url = 'https://movie.douban.com/chart'
content = requests.get(url).text
a1 = 'class="pl2".*?<.*?="(.*?)".*?>(.*?)<span.*?>(.*?)</span>.*?"rating_nums">(.*?)</span>.*?"pl">(.*?)</span>'
a2 = '<div class="pl2".*?href="(.*?)".*?>(.*?)<span.*?<p class="pl">(.*?)</p>.*?"rating_nums">(.*?)</span>'
patter = re.compile(a2,re.S)
res =  re.findall(patter,content)
for ele in res:
    # r = re.sub(r'\n','',ele)
    print(ele)


