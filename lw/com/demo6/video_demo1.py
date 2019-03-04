
import requests
# from bs4 import BeautifulSoup
from lxml import etree
import urllib
import re

class getVideoClass(object):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Safari/605.1.15'
    }
    def getVideoUrl(self):
        oriUrl = 'http://www.pearvideo.com/video_1367621'
        res = requests.get(oriUrl,headers=self.headers).text
        print(res)
        # xpath_source = etree.HTML(res)
        # video_source = xpath_source.xpath('//video[@autoplay="autoplay"]')
        # video_url = video_source[0].attrib['src']
        # print(video_url)
        # return video_url
        rec = re.compile('http://video.*?mp4.*?mp4',re.S)
        video_url = re.findall(rec,res)
        return video_url[0]

    def getVideo(self):
        url = self.getVideoUrl()
        urllib.request.urlretrieve(url,'test.mp4')
        print('下载完成！')

if __name__ == '__main__':
    getVideoClass().getVideo()