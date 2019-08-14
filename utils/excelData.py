#encoding:utf-8
'''定义Excel的变量'''
class ExcelVariabe:
    CaseID=0
    title=1
    URL=2
    request_data=3
    Expect=4
    Result=5
'''获得用例编号'''
def getCaseID():
    return ExcelVariabe.CaseID
'''获得测试标题'''
def gettitle():
    return ExcelVariabe.title
'''获得接口地址'''
def getURL():
    return ExcelVariabe.URL
'''获得请求参数'''
def getrequest_data():
    return ExcelVariabe.request_data
'''获得预期结果'''
def getExpect():
    return ExcelVariabe.Expect
'''获得实际结果'''
def getResult():
    return ExcelVariabe.Result
'''获取请求头信息'''
def getHeadersValue():
    Headers={
        'Content-Type':'application/x-www-form-urlencoded'
    }
    return Headers
