#encoding:utf-8
import xlrd
from xlutils.copy import copy
import os
from utils.public import *
from utils.excelData import *
'''定义Excel的操作'''
class operationExcel:
    '''读取Excel中的sheet内容'''
    def getExcel(self):
         excel=xlrd.open_workbook(data_dir('data','testcase.xls'))
         sheet=excel.sheet_by_index(0)
         return sheet
    '''获取Excel的行数'''
    def get_rows(self):
        return self.getExcel().nrows
    '''获取单元格的内容'''
    def get_row_col(self,row,col):
        return self.getExcel().cell_value(row,col)
    '''获取请求地址'''
    def get_URL(self,row):
        return self.get_row_col(row,getURL())
    '''获取请求参数'''
    def get_requestdata(self,row):
        return self.get_row_col(row,getrequest_data())
    '''获取预期结果'''
    def get_Expect(self,row):
        return self.get_row_col(row,getExpect())
    '''获取实际结果'''
    def get_Result(self,row):
        return self.get_row_col(row,getResult())
    '''获取用例ID'''
    def get_CaseID(self,row):
        return self.get_row_col(row,getCaseID())
    '''获取用例标题'''
    def get_title(self,row):
        return self.get_row_col(row,gettitle())


