
import requests
from bs4 import BeautifulSoup

class getPriceClass(object):
    start_Url = 'http://www.ziroom.com/z/nl/z3.html?qwd=望京'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}


    def getPraceWithUrl(self,cur_url):
        res = requests.get(cur_url,headers = self.headers).text
        print(res)
        soup = BeautifulSoup(res,'xml')
        li_item = soup.find_all('li',class_='clearfix')
        for ele in li_item:
            print(ele)

    def getDataWithPageNum(self):
        for i in range(1,2):
            self.getPraceWithUrl(cur_url = self.start_Url + '&p='+str(i))


if __name__ == '__main__':
    getPriceClass().getDataWithPageNum()
