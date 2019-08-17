#encoding:utf-8
import pymysql
'''1、建立与数据库的链接'''
connect =  pymysql.connect(host='rm-bp1bje06598f827uqo.mysql.rds.aliyuncs.com',
                           port=3306,
                           user='shaozi_user',
                           password='6EaG7ac@&6-Z2A7*9T8MDd71#ceF91f9',
                           db='shaozi2018',
                           charset='utf8')
'''2、从连接建立游标，从而操作数据库'''
cur=connect.cursor()
'''3、查询数据库'''
sql="SELECT *  FROM `sz_user` WHERE phone = 17713162100 "
cur.execute(sql)
'''4、获取查询结果'''
result=cur.fetchall()
print(result)
