#encoding:utf-8
import pymysql
'''1、建立与数据库的链接'''
connect =  pymysql.connect(host='rm-bp114amjgol8u794hho.mysql.rds.aliyuncs.com',
                           port=3306,
                           user='shaoziceshi',
                           password='mZ8NZoCe4oVD9d6IyhnY',
                           db='shaozi2019',
                           charset='utf8')
'''2、从连接建立游标，从而操作数据库'''
cur=connect.cursor()
'''3、查询数据库'''
sql="SELECT distinct (app_version)  FROM `sz_user` WHERE phone = 17713162100  "
cur.execute(sql)
'''4、获取查询结果'''
result=cur.fetchall()
print(result)
