#encoding:utf-8
from utils.public import *
from utils.operationExcel import operationExcel
from utils.excelData import *
import json
'''定义对json文件的操作'''
class operationJson:
    ''''''
    def __init__(self):
        self.excel=operationExcel()
    '''读取json文件的内容'''
    def getReadJson(self):
        with open(data_dir('data','requestData.json'),encoding='utf-8') as fp:
            rdata=json.load(fp)
            return rdata
    '''获得json的内容，并以字符串的形式输出，“”，’‘为字典'''
    def getRequestData(self,row):
        return json.dumps(self.getReadJson()[self.excel.get_requestdata(row=row)])

# opear=operationJson()
# print(opear.getRequestData(1),type)