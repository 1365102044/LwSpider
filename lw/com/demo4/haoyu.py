import requests
import json
import pymysql

# 获取 好寓官网中 每个城市下的房源信息

class haoyuInfor(object):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Safari/605.1.15'
    }
    page_url = 'http://pms.hntpsjwy.com/v2/officialWebsit/house/room_type_list'

    citys_url = ' http://pms.hntpsjwy.com/v2/officialWebsit/hotCity/list'
    citys_request_json = {"userid":"fdfc16f6a42941db82f23230fba55f59","token":"7b041888-5fce-440f-9f62-d2faa50c4dc5","gcid":"0371070"}


    def __init__(self):
        self.db = pymysql.connect(host='localhost',
                                  user='root',
                                  password='1113',
                                  database='lwq',
                                  # charset='utf-8',
                                  cursorclass=pymysql.cursors.DictCursor)
        sql = 'CREATE TABLE IF NOT EXISTS t_haoyuInfor (id int(10) primary key not null auto_increment,houseItemName VARCHAR(225),image_url VARCHAR(225),houseItemAddress VARCHAR(225),minRental int(10),maxRental int(10),city VARCHAR(225))'
        self.db.cursor().execute(sql)
        self.db.commit()

    # 获取所有城市的列表
    def getCitysInfor(self):
        res = requests.post(self.citys_url,headers=self.headers,json=self.citys_request_json).text
        citys_info_json = json.loads(res)
        citys_list = citys_info_json['result']['list']
        citys_arr = []
        for ele in citys_list:
            self.getInfor(self.page_url, ele['name'])

    # 根据城市获取每个城市的数据
    def getInfor(self,cur_url,curr_city):
        index = curr_city.find('市')
        if index != -1:
            curr_city = curr_city[0:index]
        pageinfor_request_json = {"userid":"fdfc16f6a42941db82f23230fba55f59","token":"7b041888-5fce-440f-9f62-d2faa50c4dc5","gcid":"0371070","pageSize":8,"params":{"likeName":"","city":curr_city,"cityId":"d94bba14-dec1-11e5-bcc3-00163e1c066c","orderField":"","orderType":"asc","isDelete":1}}
        res = requests.post(cur_url,headers=self.headers,json=pageinfor_request_json).text
        infor =  json.loads(res)
        infor_list = infor['result']['list']

        for ele in infor_list:
            sql = 'insert into t_haoyuInfor (houseItemName,image_url,houseItemAddress,minRental,maxRental,city) values (%s,%s,%s,%s,%s,%s)'
            values = [ele['houseItemName'],ele['picList'][0]['big'],ele['houseItemAddress'],ele['minRental'],ele['maxRental'],curr_city]
            print(values)
            self.db.cursor().execute(sql,values)
            self.db.commit()

    # 开始
    def startGetInfor(self):
        self.getCitysInfor()

if __name__ == '__main__':
    haoyuInfor().startGetInfor()