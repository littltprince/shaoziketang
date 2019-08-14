#encoding utf-8
# dict1={'name':'王三','age':3}
# print(dict1['name'])
# '''判断key是否存在'''
# age=1
# if dict1.__contains__('age'):
#     if age>3:
#         print(dict1['age'])
#     else:
#         print('sorry ,no key')
#
#
#
# 1:   '''通用的异常情况处理'''
# try:
#     ssah
# except Exception as e:
#     print(e.args)
# else:
#     print('pass')

# for a,b in dict1.items():
#     print(a,':',b)
import requests
import json
#post请求
data={字典}
r=requests.post(url='/API/House/search',data=data)
respone=r.json()
print(json.dumps(respone,indent=True,ensure_ascii=False))



# print(dict1.values())
# print(dict1['name'])
'''字典循环'''
# for key in  dict1.keys()
#     print(key.title())