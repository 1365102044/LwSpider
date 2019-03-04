
import csv

# 把数据写入表格
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
