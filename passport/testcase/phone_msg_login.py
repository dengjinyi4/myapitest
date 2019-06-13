#coding:utf-8
import sys
import warnings
import json
import requests
import redis
import ConfigParser
import time
from passport.common import mysql
warnings.filterwarnings('ignore')

config=ConfigParser.ConfigParser()

config.read('D:\javaworkspace\passport\passport\data_config') 

def sendmessage(phone,type):
    r=requests.get("https://passport.egou.com/phoneCode_v4.do?",params={"phone":phone,"type":type},verify=False)
    result= r.text
    return result

def phone_msg_login(phone,vcode):    
    r=requests.get("https://passport.egou.com/loginByPhone.do?",params={"phone":phone,"vcode":vcode},verify=False)
    result= r.text
    return result
def expectcode(host,user,password,database,port,sql):
    mysql.connectdb(host,database,user,password,port)
    result=mysql.selete(sql)
    return result
    mysql.closeconnect()
    return result[0][0]
def expectcodedel(host,user,password,database,port,sql):
    mysql.connectdb(host,database,user,password,port)
    result=mysql.deletedb1(sql)
    return result
    mysql.closeconnect()
#case1:手机号验证码登陆(验证码正确)    
host1=config.get("phone_msg_login1", "host")
user1=config.get("phone_msg_login1","user")
password1=config.get("phone_msg_login1","password")
database1=config.get("phone_msg_login1","database")
port1 = int(config.get("phone_msg_login1","port"))
sql11=config.get("phone_msg_login1","sql1")
sql12=config.get("phone_msg_login1","sql2")
sql13=config.get("phone_msg_login1","sql3")
phone1=config.get("phone_msg_login1","phone")
type1=config.get("phone_msg_login1","type")

sendmessage(phone1,type1)
time.sleep(5)
#print result
vcode_f1=expectcode(host1,user1,password1,database1,port1,sql11) 
#print vcode_f
vcode1=vcode_f1[0][0]
#print vcode1
actvalue1=phone_msg_login(phone1,vcode1)
#print actvalue1
actvaluestr=json.loads(actvalue1)
actcode1=actvaluestr["msg"]
#print actcode1


expectcode1=expectcode(host1,user1,password1,database1,port1,sql13)
#print expectcode1
#print expectcode1[0][0]
if (actcode1)=="OK" and (expectcode1[0][0])==1:
    print "case1:手机号验证码登陆(验证码正确)--测试通过 "
else:
    print "case1:手机号验证码登陆(验证码正确)--测试失败 "

#清除数据库
excodedel1=expectcodedel(host1,user1,password1,database1,port1,sql12)   

''''清除redis
#portgroup=['13500','13501','13502','13503','13504','13505']
#for i in range(5):
# try:
#  pool=redis.ConnectionPool(host='172.16.9.4',port=portgroup[i],db=0) 
#  r=redis.StrictRedis(connection_pool=pool)
#  r.delete("phone:code:send:phone_login13261746654")
# except Exception,e: 
#  print Exception,":",e '''

#case2:手机号验证码登陆(验证码错误)  

host2=config.get("phone_msg_login2", "host")
user2=config.get("phone_msg_login2","user")
password2=config.get("phone_msg_login2","password")
database2=config.get("phone_msg_login2","database")
port2 = int(config.get("phone_msg_login2","port"))
sql21=config.get("phone_msg_login2","sql1")
sql22=config.get("phone_msg_login2","sql2")
sql23=config.get("phone_msg_login2","sql3")
phone2=config.get("phone_msg_login2","phone")
type2=config.get("phone_msg_login2","type")

result=sendmessage(phone2,type2)
time.sleep(5)
#print result
vcode_f2=expectcode(host2,user2,password2,database2,port2,sql21) 
#print vcode_f2
vcode2=5050 
#print vcode2
actvalue2=phone_msg_login(phone2,vcode2)
#print actvalue2
actvaluestr2=json.loads(actvalue2)
actcode2=actvaluestr2["sub_code"] 
#print actcode2


expectcode2=expectcode(host2,user2,password2,database2,port2,sql23)
#print expectcode1
#print expectcode1[0][0]
if (actcode2)=="vcode_error" and (expectcode2[0][0])==1:
    print "case2:手机号验证码登陆(验证码正确)--测试通过 "
else:
    print "case2:手机号验证码登陆(验证码正确)--测试失败 "

#清除数据库
expectcodedel(host2,user2,password2,database2,port2,sql22)  

#case3:手机号验证码登陆(手机格式错误)

host3=config.get("phone_msg_login3", "host")
user3=config.get("phone_msg_login3","user")
password3=config.get("phone_msg_login3","password")
database3=config.get("phone_msg_login3","database")
port3 = int(config.get("phone_msg_login3","port"))
sql31=config.get("phone_msg_login3","sql1")
sql32=config.get("phone_msg_login3","sql2")
sql33=config.get("phone_msg_login3","sql3")
phone3=config.get("phone_msg_login3","phone")
type3=config.get("phone_msg_login3","type")

result=sendmessage(phone3,type3)
time.sleep(5)
#print result

vcode3=5050 
actvalue3=phone_msg_login(phone3,vcode3)
#print actvalue2
actvaluestr3=json.loads(actvalue3)
actcode3=actvaluestr3["sub_code"] 

#print actcode2


expectcode3=expectcode(host3,user3,password3,database3,port3,sql33)
#print expectcode1
#print expectcode1[0][0]
if (actcode3)=="phone_error" and (expectcode3[0][0])==0:
    print "case2:手机号验证码登陆(验证码正确)--测试通过 "
else:
    print "case2:手机号验证码登陆(验证码正确)--测试失败 "

#清除数据库
expectcodedel(host3,user3,password3,database3,port3,sql32)  


#case4:手机号验证码登陆(手机对应的账户冻结)    

host4=config.get("phone_msg_login4", "host")
user4=config.get("phone_msg_login4","user")
password4=config.get("phone_msg_login4","password")
database4=config.get("phone_msg_login4","database")
port4 = int(config.get("phone_msg_login4","port"))
sql41=config.get("phone_msg_login4","sql1")
sql42=config.get("phone_msg_login4","sql2")
sql43=config.get("phone_msg_login4","sql3")
phone4=config.get("phone_msg_login4","phone")
type4=config.get("phone_msg_login4","type")

result=sendmessage(phone4,type4)
time.sleep(5)
#print result

vcode4=5050 
actvalue4=phone_msg_login(phone4,vcode4)
#print actvalue2
actvaluestr4=json.loads(actvalue4)
actcode4=actvaluestr4["sub_code"] 

#print actcode4


expectcode4=expectcode(host4,user4,password4,database4,port4,sql43)
#print expectcode4
#print expectcode1[0][0]
if (actcode4)=="freezed" and (expectcode4[0][0])=='freezed':
    print "case2:手机号验证码登陆(验证码正确)--测试通过 "
else:
    print "case2:手机号验证码登陆(验证码正确)--测试失败 "


