import requests
import re
from lxml import html
import pymysql


class fullCode:
    # def __init__(self):
    #     self.db = pymysql.connect(host='localhost',
    #                               user='root',
    #                               password='1113',
    #                               database='lwq',
    #                               # port=3306,
    #                               # charset='utf8mb4',
    #                               cursorclass=pymysql.cursors.DictCursor)
    #
    #     sql = 'CREATE TABLE IF NOT EXISTS t_sqbk(author VARCHAR(20),likenum VARCHAR(10),content VARCHAR(255))'
    #     self.db.cursor().execute(sql)
    #     self.db.commit()

    def noHtmlTag(self, content):
        print(content, sep='++++++++++')
        if not content:
            return content
        reg = re.compile('<[^>]*>')
        noTag = reg.sub('', content).replace('\n', '').replace(' ', '')
        return noTag

    def getCode(self,pageCount):
        try:
            # cursor = self.db.cursor()
            for indx in range(1,pageCount):
                url = 'https://www.qiushibaike.com/hot/page/' + str(indx)
                page = requests.Session().get(url).text
                print('\n\npage:'+page+'\n\n')
                pattern = re.compile(
                    '<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div.*?span>(.*?)</span>(.*?)<div class="stats">.*?"number">(.*?)</i>',
                    re.S)
                items = re.findall(pattern, page)
                for item in items:
                    haveImage = re.search("img",item[2])
                    if not haveImage:
                        # print(item[0],item[1],item[3])
                        # sql = "insert into t_sqbk(author,likenum,content) values (%s,%s,%s)"
                        values = [self.noHtmlTag(item[0]),str(item[3]),self.noHtmlTag(item[1])]
                        print(values)
                        # cursor.execute(sql,values)
                        # self.db.commit()
            # self.db.close()
        except Exception as e:
            print('error:'+ str(e))

    def start(self):
        self.getCode(2)

lwcode = fullCode()
lwcode.start()

