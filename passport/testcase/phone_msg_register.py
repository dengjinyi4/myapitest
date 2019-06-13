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

def phone_msg_register(phone,vcode,password):    
    r=requests.get("https://passport.egou.com/registerByPhone.do?",params={"phone":phone,"vcode":vcode,"password":password},verify=False)
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
#case1:手机号验证码注册(验证码正确)    
host1=config.get("phone_msg_register1", "host")
user1=config.get("phone_msg_register1","user")
password1=config.get("phone_msg_register1","password")
database1=config.get("phone_msg_register1","database")
port1 = int(config.get("phone_msg_register1","port"))
sql11=config.get("phone_msg_register1","sql1")
sql12=config.get("phone_msg_register1","sql2")
sql13=config.get("phone_msg_register1","sql3")
phone1=config.get("phone_msg_register1","phone")
type1=config.get("phone_msg_register1","type")
password_user1=config.get("phone_msg_register1","password_user")
sqld11=config.get("phone_msg_register1","sqld11")
sqld12=config.get("phone_msg_register1","sqld22")

result1=sendmessage(phone1,type1)
#print result
time.sleep(5)
vcode_f1=expectcode(host1,user1,password1,database1,port1,sql11) 
#print vcode_f1 
vcode1= vcode_f1[0][0]
#print vcode1 
actvalue1=phone_msg_register(phone1,vcode1,password_user1)
#print actvalue1
actvaluestr=json.loads(actvalue1)
#print actvaluestr
actcode1=actvaluestr["msg"]
#print actcode1


expectcode1=expectcode(host1,user1,password1,database1,port1,sql13)
#print expectcode1
#print expectcode1[0][0]
if (actcode1)=="OK" and (expectcode1[0][0])==1:
    print "case1:手机号验证码注册(验证码正确)--测试通过 "
else:
    print "case1:手机号验证码注册(验证码正确)--测试失败 "

#清除数据库
excodedel1=expectcodedel(host1,user1,password1,database1,port1,sql12)  
excodedeld11=expectcodedel(host1,user1,password1,database1,port1,sqld11)  
excodedeld12=expectcodedel(host1,user1,password1,database1,port1,sqld12)  


#case2:手机号验证码注册(验证码错误)  
host2=config.get("phone_msg_register2", "host")
user2=config.get("phone_msg_register2","user")
password2=config.get("phone_msg_register2","password")
database2=config.get("phone_msg_register2","database")
port2 = int(config.get("phone_msg_register2","port"))
sql21=config.get("phone_msg_register2","sql1")
sql22=config.get("phone_msg_register2","sql2")
sql23=config.get("phone_msg_register2","sql3")
phone2=config.get("phone_msg_register2","phone")
type2=config.get("phone_msg_register1","type")
password_user2=config.get("phone_msg_register2","password_user")


result2=sendmessage(phone2,type2)
#print result
time.sleep(5)
vcode_f2=expectcode(host2,user2,password2,database2,port2,sql21) 
#print vcode_f2 
vcode2= 5050

actvalue2=phone_msg_register(phone2,vcode2,password_user2)
#print actvalue2
actvaluestr=json.loads(actvalue2)
#print actvaluestr
actcode2=actvaluestr["sub_code"]
#print actcode2


expectcode2=expectcode(host2,user2,password2,database2,port2,sql23)
#print expectcode2
#print expectcode2[0][0]
if (actcode2)=="vcode_error" and (expectcode2[0][0])==1:
    print "case2:手机号验证码注册(验证码错误)--测试通过 "
else:
    print "case2:手机号验证码注册(验证码错误)--测试失败 "

#清除数据库
#excodedel2=expectcodedel(host2,user2,password2,database2,port2,sql22)  

#清除redis
portgroup=['13500','13501','13502','13503','13504','13505']
for i in range(5):
 try:
  pool=redis.ConnectionPool(host='172.16.9.4',port=portgroup[i],db=0) 
  r=redis.StrictRedis(connection_pool=pool)
  r.delete("phone:code:error:phone_register13689874585")
  r.delete("phone:code:send:phone_register13689874585")
 except Exception,e: 
  print Exception,":",e    
    
#case3:手机号验证码注册(手机号格式错误)
      
host3=config.get("phone_msg_register3", "host")
user3=config.get("phone_msg_register3","user")
password3=config.get("phone_msg_register3","password")
database3=config.get("phone_msg_register3","database")
port3 = int(config.get("phone_msg_register3","port"))
sql31=config.get("phone_msg_register3","sql1")
sql32=config.get("phone_msg_register3","sql2")
sql33=config.get("phone_msg_register3","sql3")
phone3=config.get("phone_msg_register3","phone")
type3=config.get("phone_msg_register3","type")
password_user3=config.get("phone_msg_register3","password_user")


result3=sendmessage(phone3,type3)
#print result3
time.sleep(5)
vcode_f3=expectcode(host3,user3,password3,database3,port3,sql31) 
#print vcode_f3 
vcode3= 5050

actvalue3=phone_msg_register(phone3,vcode3,password_user3)
#print actvalue3
actvaluestr=json.loads(actvalue3)
#print actvaluestr
actcode3=actvaluestr["sub_code"]
#print actcode3


expectcode3=expectcode(host3,user3,password3,database3,port3,sql33)
#print expectcode3
#print expectcode3[0][0]
if (actcode3)=="phone_error" and (expectcode3[0][0])==0:
    print "case3:手机号验证码注册(手机号格式错误)--测试通过 "
else:
    print "case3:手机号验证码注册(手机号格式错误)--测试失败 "    
    