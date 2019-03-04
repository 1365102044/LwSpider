
import requests
import re
from bs4 import BeautifulSoup
import json
import pymysql
import csv
import os
import time
from threading import Thread
from multiprocessing import Process

from lw.com.tools.LWCsvTool import *
from lw.com.tools.LWCsvTool import LWCsvTools
from lw.com.tools.LWMySqlTool import *
from lw.com.tools.LWOsTool import *


# 获取 泊寓房源数据 （现只获取公寓模式下的数据，户型模式下数据同理）
class boyuInforClass(object):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Safari/605.1.15'
    }
    info_url = 'https://www.inboyu.com/project/get-list-data?_r=0.14447833247878772'

    def __init__(self):

        # self.lwMySqlTool = LWMySqlTool('t_boyuInfor','project_name,image_url,address,min_month_rent,max_month_rent,room_min_price,room_type_count,district')
        pass

    # 获取数据
    def pageInfor(self):

        self.initCsv ()

        cookiesStr = 'Hm_lpvt_3beb3a49852087bd2bb5e807c0381c29=1545390209; Hm_lvt_3beb3a49852087bd2bb5e807c0381c29=1545389925; cityId=1734a7ef-3140-11e6-8744-00163e003632; _csrf=3d773b620badd125633e385c512daea7361bb83bb1a633a75f895d793c31125da%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22Ml8sMwGKAu01r7GRWSUOz01KfMtTcNgc%22%3B%7D; acw_tc=784c10e615453899229418018e200bbe1852e99648019c074c2deea3e6857e'
        cookies = {'Cookie': cookiesStr}
        res = requests.get(self.info_url,headers=self.headers,cookies=cookies).text
        res_json = json.loads(res)
        infor_list = res_json['data']['project']

        for ele in infor_list:
            values = [ele['project_name'],ele['cover'],ele['address'],ele['min_month_rent'],ele['max_month_rent'],ele['room_min_price'],ele['room_type_count'],ele['district']]

            # 把数据插入数据库
            # self.lwMySqlTool.insertDatas(values)

            # 把数据写入CSV
            self.writeFile(values)

            # 下载图片
            # self.saveImage ( ele['project_name'], ele['cover'] )

    # 获取图片文件路径
    def getFiledPath(self):
        cur = os.getcwd()
        print(cur)
        folder = os.getcwd() + '/泊寓房源图片'
        if not os.path.exists(folder):
            os.makedirs(folder)
        return folder

    # 保存图片
    def saveImage(self,projectName,imageUrl):
        res = requests.get(imageUrl)
        LWOsTool(os.getcwd()+'/泊寓房源图片').saveDatas(projectName+'.jpg',res.content)

    # 初始化CSV
    def initCsv(self):
        headers = ['project_name', 'image_url', 'address', 'min_month_rent', 'max_month_rent', 'room_min_price',
                 'room_type_count', 'district']
        self.lwcsvTools = LWCsvTools ( 'boyu.csv' )
        self.lwcsvTools.lw_writeHeaders(headers)

    # 逐行写入
    def writeFile(self,data):
        self.lwcsvTools.lw_writeListToCsv(data)

    # 读取写入的表格的数据
    def readCsvFile(self):
        self.lwcsvTools = LWCsvTools ( 'boyu.csv' )
        lists = self.lwcsvTools.lw_readeListFromCsv()
        for ele in lists:
            print(ele)



if __name__ == '__main__':

    # 存数据
    boyuInforClass().pageInfor()

    # 读取数据
    # boyuInforClass().readCsvFile()





# 读写文件工具类
class LWOsTool(object):

    def __init__(self,filePath = os.getcwd()):
        if filePath:
            self.currentPath = filePath
        if not os.path.exists(self.currentPath):
            os.makedirs(self.currentPath)

    def saveDatas(self,fileName,datas):
        cur_modle = 'a+'
        if type(datas) == bytes:
            cur_modle = 'wb+'
        if fileName:
            self.currentPath = self.currentPath + '/{}'.format(fileName)

        try:
            with open (self.currentPath,cur_modle ) as file:
                file.write (datas)
        except RuntimeError as error:
            print(error)


# 把数据写入表格工具类
class LWCsvTools(object):

    # 初始化表格
    def __init__(self,filePath):
        if not filePath:
            raise RuntimeError('传入的参数异常：filePath:{}'.format(filePath))
        else:
            self.filePath = filePath

    # 写入头标题
    def lw_writeHeaders(self,headers):
        if not headers:
            raise RuntimeError('传入的参数异常：headers:{}'.format(headers))
        else:
            with open(self.filePath,'w',newline='',encoding='utf-8-sig') as csvfile:
                csv.writer(csvfile).writerow(headers)

    # 写入数据
    def lw_writeListToCsv(self,lists):
        if not lists:
            raise RuntimeError('要写入的数据格式异常：%s'.format(lists))
        with open(self.filePath,'a+',newline='',encoding='utf-8-sig') as csvfile:
            csv.writer(csvfile).writerow(lists)

    # 从CSV表格中读取数据
    def lw_readeListFromCsv(self):
        with open(self.filePath,'r+',newline='',encoding='utf-8-sig') as csvfile:
            csvreader = csv.reader(csvfile)
            lists = []
            for row in csvreader:
                lists.append(row)
            return lists

