# coding=utf-8
import requests
import json
from lw.com.tools.LWFuncTools import lwprint
from lxml import etree
import pymysql
import time
import asyncio
import concurrent.futures as cf #多线程
import asyncio
from aiohttp import ClientSession


# 获取数据
class spiderCompositonTool:
    # lwcursor = self.db.cursor();
    loop = asyncio.get_event_loop()


    # 首页的主列表分类
    home_list_type = ['一年级作文','二年级作文','三年级作文','四年级作文','五年级作文','六年级作文',]
    deatil_tables = ['t_compoistion_deatil','t_compoistion_deatil1','t_compoistion_deatil2','t_compoistion_deatil3','t_compoistion_deatil4','t_compoistion_deatil5','t_compoistion_deatil6']

    def __init__(self):
        self.db = pymysql.connect(host='localhost',
                                  user='root',
                                  password='1234567890',
                                  database='compostion',
                                  # port=3306,
                                  # charset='utf8mb4',
                                  cursorclass=pymysql.cursors.DictCursor)

        # self.lwConst.list_table = 't_composition_list'
        # self.lwConst.deatil_table = 't_composition_lists'

        lwcursor = self.db.cursor()
        # 列表
        # if lwcursor.execute('show tables like "t_compoistion_list"'):
        list_table = 'CREATE TABLE IF NOT EXISTS t_compoistion_list1(ID TEXT,catename TEXT,subcatename TEXT,title TEXT,tags TEXT,views TEXT,good TEXT,edittime TEXT,lengths TEXT,fl TEXT,fv TEXT)'
        lwcursor.execute(list_table)

        lables_table = 'CREATE TABLE IF NOT EXISTS t_compoistion_lables(lable TEXT,lable_content TEXT)'
        lwcursor.execute(lables_table)

        # 详情
        # if lwcursor.execute('show tables like "t_compoistion_deatil"'):

        deatil_table = 'CREATE TABLE IF NOT EXISTS t_compoistion_deatil1(ID TEXT,title TEXT,content TEXT)'
        lwcursor.execute(deatil_table)

        self.db.commit()

    # 获取首页子列表数据
    def requestHomeListDatas(self):
        for typename in self.home_list_type:
            currentpage = 1
            para = {'catename': typename, 'p': currentpage, 'pagesize': '20', 'order': 'views', }
            url = 'http://ibaby.ipadown.com/api/zuowen/zw.list.php'
            res = requests.get(url=url,params=para, )
            res_json = self.toJson(res)
            datalist = res_json['results']
            totalpage = res_json['totalpage']
            lwprint('-------总共页数：'+ str(totalpage))

            # 保存第一页数据
            self.saveListDatas(datalist)

            # 遍历请求下面页数的数据
            while(50 >= currentpage):
                # time.sleep(1)
                currentpage = currentpage + 1
                para = {'catename': typename, 'p': currentpage, 'pagesize': '20', 'order': 'views', }
                self.requestHomeListMoreDatas(url,currentpage,para)

    # 下一页的数据请求
    def requestHomeListMoreDatas(self,url,p,param):
        res = requests.get("http://ibaby.ipadown.com/api/zuowen/zw.list.php",
                           param, )
        res_json = self.toJson(res)
        datalist = res_json['results']
        self.saveListDatas(datalist)

    # 保存数据
    def saveListDatas(self,listdata):
        for dict in listdata:
            sql = "insert into t_compoistion_list1(ID,catename,subcatename,title,tags,views,good,edittime,lengths,fl,fv) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = [dict['ID'], dict['catename'],dict['subcatename'],dict['title'],dict['tags'],dict['views'],dict['good'],dict['edittime'],dict['length'],dict['fl'],dict['fv']]
            lwprint(values)
            self.db.cursor().execute(sql, values)
            self.db.commit()
            # 获取详情数据
            # self.requestDeatilDatas(dict['ID'])

    # 获取列表数据 首页进入的列表
    def fecthListDatas(self):
       res = requests.get("http://ibaby.ipadown.com/api/zuowen/zw.list.php",{'catename':'一年级作文','p':'1','pagesize':'1','order':'views',},)
       resstr = str(res.content,encoding='utf-8')
       res_json = json.loads(resstr,encoding='utf-8')
       datalist = res_json['results']


    # 遍历数据
    def handlerListDatas(self,datalist):
        lwprint(datalist)
        list_ids = []
        for val in datalist:
            idstr = val['ID']
            list_ids.append(idstr)
            self.fecthDeatilDatas(idstr)
        lwprint(list_ids)


    # 从数据库中取id 取获取详情
    def getIDfromBD(self,start):

        # for index,table_name in enumerate(self.deatil_tables):
        #     int pagesize = 383228/ self.deatil_tables.count()
        #     int st = index*pagesize
        #
        #     lwcursor = self.db.cursor()
        #     lwcursor.execute('select ID from {} limit {}},{}}'.format(table_name,st,pagesize))
        #     res = lwcursor.fetchall()
        #     for id in res:
        #         self.requestDeatilDatas(id=id['ID'])


        lwprint('\n******************start:'+str(start)+'\n')
        lwcursor = self.db.cursor()
        sql = "select ID from t_compoistion_list1 limit {},{}".format(str(self.start),'500' )
        lwcursor.execute(sql)
        res = lwcursor.fetchall()
        # lwprint(res)

        # for id in res:
        #     self.requestDeatilDatas(id=id['ID'])
            # self.loop.run_until_complete(self.requestDeatilDatas(id=id['ID']))

        self.runGetDeatil(res)

    #  获取详情数据
    def requestDeatilDatas(self,id):
        header = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
        res = requests.get('http://ibaby.ipadown.com/api/zuowen/zw.detail.php', headers=header,verify=False,params={'id': id})
        data_str = res.text
        pageSource = etree.HTML(data_str)
        article_source = pageSource.xpath('//div[@class="article-body"]/p/text()')
        title = pageSource.xpath('//h1/text()')[0]

        lwprint(id+':'+title)
        # lwprint(article_source)

        # 保存详情数据
        mutablestr = ''
        for tem in article_source:
            mutablestr = mutablestr + '**' + str.replace(tem,"'","")
        sql = "insert into t_compoistion_deatil(ID,title,content) values ('{}','{}','{}')".format(id,title,mutablestr)
        # sql = 'insert into t_compoistion_deatil(ID,title,content) values (%s,%s,%s)'
        # values = [id,title,mutablestr]
        lwprint(sql)
        ress = self.db.cursor().execute(sql)
        self.db.commit()
        # lwprint(ress)

    # 获取不同lable下的数据
    def getDatasWithLable(self):
        lable_list = ["话题作文","动物植物","人物描写","自然环境","情感励志","假日节日","热门事件"]
        for la in lable_list:
            url = 'http://ibaby.ipadown.com/api/zuowen/zw.tags.category.php'
            res = requests.get(url,{'category':la})
            json = self.toJson(res)
            self.saveDatasLablesWithJson(json,la)


    # 保存不同标签下的数据
    def saveDatasLablesWithJson(self,json,title):
        json_list_str = ','.join(json)
        lwcursor = self.db.cursor()
        sql = "INSERT INTO t_compoistion_lables VALUES ('{0}','{1}');".format(title,json_list_str)
        lwprint(sql)
        lwcursor.execute(sql)
        self.db.commit()
        for keyword in json:
            self.loopGetDatasWithKeysWords(keyword)

    def getDatasWithKeysWords(self,keywords,currentpage):
        url = 'http://ibaby.ipadown.com/api/zuowen/zw.list.php'
        para = {'keywords': keywords, 'p': currentpage, 'pagesize': '20', 'order': 'views', }
        res = requests.get(url=url, params=para, )
        res_json = self.toJson(res)
        datalist = res_json['results']
        self.saveListDatas(datalist)

    def loopGetDatasWithKeysWords(self,keywords):
        currentpage = 1
        while(10 >= currentpage):
            self.getDatasWithKeysWords(keywords, currentpage)
            currentpage = currentpage + 1


    # 将获取到的数据转成需要的json
    def toJson(self,data):
        resstr = str(data.content, encoding='utf-8')
        res_json = json.loads(resstr, encoding='utf-8')
        return res_json

    # if __name__ == '__main__':
    def getDataWithid(self,id):

        sql = " select * from t_compoistion_list where ID = "+ id
        subtitle = '诗歌'
        args = '%' + subtitle + '%'
        sqlQueryTitle = "select * from t_compoistion_list where tags like '%s'" % args

        # values = [id]
        # res = self.db.cursor().execute(sql, values)
        lwprint(sqlQueryTitle)
        lwcursor = self.db.cursor()
        lwcursor.execute(sqlQueryTitle)
        res = lwcursor.fetchall()
        lwprint(res)
        self.db.commit()

    def get_title(self,i):
        pass

    async def lwthread(self):
        with cf.ThreadPoolExecutor(max_workers=10) as executor:
            loop = asyncio.get_event_loop()
            futures = (loop.run_in_executor(executor, self.get_title, i) for i in range(10))
            for result in await asyncio.gather(*futures):
                pass

    start = 29500
    tasks = []
    url = "http://ibaby.ipadown.com/api/zuowen/zw.detail.php"
    loop = asyncio.get_event_loop()
    async def getDeatilDatasWithID(self,id):
        semaphore = asyncio.Semaphore(100)  # 限制并发量为500
        async with semaphore:
            async with ClientSession() as session:
                async with session.get(self.url, params={'id': id}) as response:
                    return await response.text()


    def runGetDeatil(self,id_list):
        for id in id_list:
            task = asyncio.ensure_future(self.getDeatilDatasWithID(id['ID']))
            self.tasks.append(task)
        result = self.loop.run_until_complete(asyncio.gather(*self.tasks))
        # print(result)
        for res in result:
            self.handleDeatilDatas(res)

        self.start = self.start + 500
        if(self.start <= 30000):
            time.sleep(10)
            self.getIDfromBD(self.start)

    def handleDeatilDatas(self,res):
        pageSource = etree.HTML(res)
        article_source = pageSource.xpath('//div[@class="article-body"]/p/text()')
        title = str(pageSource.xpath('//h1/text()')[0])
        idstr = str(pageSource.xpath('//input[@id="ID"]/@value')[0])
        title = str.replace(title,"'","&")
        # lwprint(idstr + ':' + title)
        # lwprint(article_source)

        # 保存详情数据
        mutablestr = ""
        for tem in article_source:
            mutablestr = mutablestr + '**' + str.replace(tem,"'","&")
        sql = "insert into t_compoistion_deatil1(ID,title,content) values ('{}','{}','{}')".format(idstr, title, mutablestr)
        ress = self.db.cursor().execute(sql)
        self.db.commit()

    def initCount(self):
        pass


if __name__ == '__main__':
    spider =  spiderCompositonTool()
    spider.getIDfromBD(spider.start)
    spider.loop.close()
    # spiderCompositonTool().requestHomeListDatas()
    # spiderCompositonTool().getDatasWithLable()