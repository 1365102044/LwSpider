
import pymysql

# 把爬取的数据 插入到MySQL数据库中

class LWMySqlTool(object):

    # 初始化 tableName:表名，fields:字段集合/以,分割字符串
    def __init__(self,tableName,fields):
        if not tableName or not fields:
            raise RuntimeError('参数有误 tableName:{} fields:{}'.format(tableName,fields))
        else:
            self.fields = self.getFields(fields)
            self.tableName = tableName
            self.db = pymysql.connect(host='localhost',
                                      user='root',
                                      password='1113',
                                      database='lwq',
                                      # charset='utf-8',
                                      cursorclass=pymysql.cursors.DictCursor )
            # sql = 'CREATE TABLE IF NOT EXISTS t_boyuInfor (id int(10) primary key not null auto_increment,project_name VARCHAR(225),image_url VARCHAR(225),address VARCHAR(225),min_month_rent int(10),max_month_rent int(10),room_min_price int(10),room_type_count int(10),district VARCHAR(225), city VARCHAR(225))'
            sql = self.getSqlOfCreateTable(self.fields)
            self.db.cursor().execute(sql)
            self.db.commit()

    # 获取字段集合
    def getFields(self,fields):
        if type(fields) == str:
            return  fields.split(',')
        elif type(fields) == list:
            return fields
        else:
            return fields


    # 得到创建table的SQL
    def getSqlOfCreateTable(self,fields):
        if type(fields) != list :
            raise RuntimeError('字段集合参数类型有误 type:{}'.format(type(fields)))
        else:
            sql = 'CREATE TABLE IF NOT EXISTS {} (id int(10) primary key not null auto_increment'.format(self.tableName)
            self.filesK = fields[0]
            self.filesV = '%s'
            for i in range(0,len(fields)):
                if fields[i]:
                    sql = sql + ',{} VARCHAR(225)'.format(fields[i])
                    if i > 0:
                        self.filesK = self.filesK + ',{}'.format(fields[i])
                        self.filesV = self.filesV + ',%s'
            sql = sql + ')'
            print('sql:' + sql)
        return sql

    # 插入数据，数据顺序和初始化字段顺序和长度保持一致，无数据是可使用''代替，
    def insertDatas(self,values):
        if len(values) == len(self.fields):
            sql = 'insert into {} ({}) values ({})'.format(self.tableName,self.filesK,self.filesV)
            print(values)
            self.db.cursor().execute(sql,values)
            self.db.commit()
        else:
            raise RuntimeError('要插入的数据集合与初始化的字段集合长度不一致 len:{}'.format(len(values)))

