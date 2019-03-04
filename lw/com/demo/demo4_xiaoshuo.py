
import requests
import re
from bs4 import BeautifulSoup
from lxml import html
import os
import time
from threading import Thread

class getCode(object):

    baseurl = 'https://www.biqukan.com'
    currtenPage = '/1_1094/5403177.html'
    currentIndx = 1
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

    def getText(self):
        soup = self.getStart()
        tex = soup.find_all('div',class_ = 'showtxt')
        for ele in tex:
            self.saveTextToFiled(ele.text,soup)

    def getStart(self):
        res = requests.get(self.baseurl + self.currtenPage,headers = self.headers).text
        soup = BeautifulSoup(res, 'xml')
        return soup

    def getNextPageUrl(self,soup):
        divs = soup.find('div',class_='page_chapter')

        la = divs.find_all('a')
        for las in la:
            ats = las.attrs
            if las.text == '下一章':
                for e in ats:
                    self.currtenPage = ats[e]
                    self.currentIndx += 1
                    print('第'+ str(self.currentIndx) +'页，地址：' +ats[e])
                    return



    def getFiledPath(self):
        folder = os.getcwd()[:-4] + '小说'
        if not os.path.exists(folder):
            os.makedirs(folder)
        return folder

    def saveTextToFiled(self,tex,soup):
        print(tex)
        filedPath = self.getFiledPath() + '/第'+str(self.currentIndx) +'章.text'
        with open(filedPath,'w',encoding='UTF-8') as f:
            f.write(tex)
        print('第'+str(self.currentIndx)+'章，写入完成')
        self.getNextPageUrl(soup)

    def getTextForRange(self):
        for ele in range(1,6):
            self.getText()

            print('++++++++++++++++{}'.format(ele))

if __name__ == '__main__':
    getCode().getTextForRange()





