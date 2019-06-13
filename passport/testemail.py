#coding:utf-8
import smtplib

from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
from email.header import Header

#第三方服务
email_host='mail.emar.com'
email_user='aidinghua@emar.com'
email_pass='lyj58579331'

email_msg="This is a testing mail from python"

sender=['aidinghua@emar.com']
receivers=['84723062@qq.com']

#message=MIMEText(email_msg,'plain','utf-8')

message=MIMEMultipart()
message['from']=Header('菜鸟教程','utf-8')
message['to']=Header('测试','utf-8')
subject='Python 邮件发送测试'
message['subject']=Header(subject,'utf-8')

message.attach(MIMEText('python测试邮件发送','plain','utf-8'))

att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="test.txt"'

message.attach(att1)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(email_host,25)
    smtpObj.login(email_user,email_pass)
    smtpObj.sendmail(sender,receivers,message.as_string())
    
except smtplib.SMTPException:
    print "Error,无法发送邮件"
    



