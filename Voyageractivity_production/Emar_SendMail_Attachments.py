# -*- coding: utf-8 -*-  
import smtplib  
import email.MIMEMultipart# import MIMEMultipart  
import email.MIMEText# import MIMEText  
import email.MIMEBase# import MIMEBase  
import os.path  
import requests as r
import mimetypes  
import email.MIMEImage# import MIMEImage  
  
def sendTestreport(file_name,mailto,mailSubject,mailText):

	From = "dengjinyi@emar.com"

	server = smtplib.SMTP("mail.emar.com")
	# server.login("1","111111") #仅smtp服务器需要验证时  

	# 构造MIMEMultipart对象做为根容器  
	main_msg = email.MIMEMultipart.MIMEMultipart()  

	# 获取html内容
	f = open(file_name, 'r')#filename，文件路径、名称，如果有\，注意转义或者开头加r，mode读取的模式，r读取，w写入，，
	read = f.read()#获取内容并储存在变量里
	f.close()#关闭文件，节省内存

	# 构造MIMEText对象做为邮件HTML样式显示内容并附加到根容器  
	text_msg = email.MIMEText.MIMEText(mailText+read,'html','utf-8')
	main_msg.attach(text_msg)  
	  
	# 构造MIMEBase对象做为文件附件内容并附加到根容器  
	ctype,encoding = mimetypes.guess_type(file_name)  
	if ctype is None or encoding is not None:  
	    ctype='application/octet-stream'  
	maintype,subtype = ctype.split('/',1)  
	file_msg=email.MIMEImage.MIMEImage(open(file_name,'rb').read(),subtype)  
	print ctype,encoding  
	  
	## 设置附件头  
	basename = os.path.basename(file_name)  
	file_msg.add_header('Content-Disposition','attachment', filename = basename)#修改邮件头  
	main_msg.attach(file_msg)  
	  
	# 设置根容器属性  
	main_msg['From'] = From  
	main_msg['To'] = ",". join(mailto)
	main_msg['Subject'] = mailSubject  
	main_msg['Date'] = email.Utils.formatdate( )  
	  
	# 得到格式化后的完整文本  
	fullText = main_msg.as_string( )  
	  
	# 用smtp发送邮件  
	try:  
	    server.sendmail(From, mailto, fullText)  
	finally:  
	    server.quit()  

def senderrormail(mailto,mailSubject,mailText):

	From = "dengjinyi@emar.com"

	server = smtplib.SMTP("mail.emar.com")
	# server.login("1","111111") #仅smtp服务器需要验证时

	# 构造MIMEMultipart对象做为根容器
	main_msg = email.MIMEMultipart.MIMEMultipart()

	# # 获取html内容
	# f = open(file_name, 'r')#filename，文件路径、名称，如果有\，注意转义或者开头加r，mode读取的模式，r读取，w写入，，
	# read = f.read()#获取内容并储存在变量里
	# f.close()#关闭文件，节省内存

	# 构造MIMEText对象做为邮件HTML样式显示内容并附加到根容器
	text_msg = email.MIMEText.MIMEText(mailText,'html','utf-8')
	main_msg.attach(text_msg)

	# 构造MIMEBase对象做为文件附件内容并附加到根容器
	# ctype,encoding = mimetypes.guess_type(file_name)
	# if ctype is None or encoding is not None:
	#     ctype='application/octet-stream'
	# maintype,subtype = ctype.split('/',1)
	# file_msg=email.MIMEImage.MIMEImage(open(file_name,'rb').read(),subtype)
	# print ctype,encoding

	# ## 设置附件头
	# # basename = os.path.basename(file_name)
	# file_msg.add_header('Content-Disposition','attachment', filename = basename)#修改邮件头
	# main_msg.attach(file_msg)

	# 设置根容器属性
	main_msg['From'] = From
	main_msg['To'] = ",". join(mailto)
	main_msg['Subject'] = mailSubject
	main_msg['Date'] = email.Utils.formatdate( )

	# 得到格式化后的完整文本
	fullText = main_msg.as_string( )

	# 用smtp发送邮件
	try:
	    server.sendmail(From, mailto, fullText)
	finally:
	    server.quit()

def myini(ip,type):
    if type=='106':
        url='http://eops.emar.com/tools/jobs/nginx_api/?srcip=123.59.17.106&destip='+ip
    elif type=='71':
        url='http://eops.emar.com/tools/jobs/nginx_api/?srcip=47.74.155.71&destip='+ip
    # re=r.get('http://eops.emar.com/tools/jobs/nginx_api/?srcip=123.59.17.16&destip=123.59.17.106')
    print url
    re=r.get(url)
    print re.text
    if (re.json()['code']==200):
        pass
    else:
        print '调用接口返回值不是200'
        senderrormail(['dengjinyi@emar.com'],'自动化测试出现异常1111111','环境初始化脚本出现异常请检查'+str(re.text))
        raise NameError('环境初始化脚本出现异常请检查')
if __name__ == '__main__':
	myini('123.59.17.106','106')
	# to_list=['dengjinyi@emar.com']
	# sendTestreport("D:/work/auto/yiqifa/report/Report2014-11-26-18-04.html",to_list,'易购api自动化测试报告','</pre><h1>你好</h1><pre>')