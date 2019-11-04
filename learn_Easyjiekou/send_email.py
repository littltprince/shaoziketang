#encoding:utf-8
import smtplib #用于建立SMTP的链接
from email.mime.text import MIMEText #邮件需要的MIME格式

#1、编写邮件内容（email邮件需要专门的mime格式）
msg=MIMEText('测试邮件','plain','utf-8') #plain指普通邮件文本格式的内容
#2、组装Email头（发件人，收件人，主题）
msg['from']='yangchunyique@sina.com'#发件人
msg['To']='1124479307@qq.com'#收件人
msg['Subject']='api测试邮件'#主题
#3、链接SMTP服务器并发送邮件
smtp=smtplib.SMTP_SSL('smtp.sina.com')#smtp服务器地址，使用ssl模式
smtp.login('yangchunyique@sina.com','yangchunyique')#用户名和密码
smtp.sendmail("1124479307@qq.com","1280152206@qq.com",msg.as_string())
smtp.quit()
