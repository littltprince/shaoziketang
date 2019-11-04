import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # 混合MIME格式，支持上传附件
from email.header import Header  # 用于使用中文邮件主题

# 1.  编写邮件内容
with open('report.html', encoding='utf-8') as f:  # 打开html报告
    email_body = f.read()  # 读取报告内容

msg = MIMEMultipart()  # 混合MIME格式
msg.attach(MIMEText(email_body, 'html', 'utf-8'))  # 添加html格式邮件正文（会丢失css格式）

# 2. 组装Email头（发件人，收件人，主题）
msg['From'] = 'test_results@sina.com'  # 发件人
msg['To'] = '2375247815@qq.com'  # 收件人
msg['Subject'] = Header('接口测试报告', 'utf-8')  # 中文邮件主题，指定utf-8编码

# 3. 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('report.html', 'rb').read(), 'base64', 'utf-8')  # 二进制格式打开
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="report.html"'  # filename为邮件中附件显示的名字
msg.attach(att1)

# 4. 连接smtp服务器并发送邮件
smtp = smtplib.SMTP_SSL('smtp.sina.com')  # smtp服务器地址 使用SSL模式
smtp.login('test_results@sina.com', 'hanzhichao123')  # 用户名和密码
smtp.sendmail("test_results@sina.com", "2375247815@qq.com", msg.as_string())
smtp.sendmail("test_results@sina.com", "superhin@126.com", msg.as_string())  # 发送给另一个邮箱
smtp.quit()


