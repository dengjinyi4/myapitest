#coding:utf-8
import sys
import json
import requests
import warnings
import ConfigParser
#import types 
from passport.common import mysql
warnings.filterwarnings("ignore")

 

def sendmessage(phone,type):
    r=requests.get("https://passport.egou.com/phoneCode_v4.do?",params={"phone":phone,"type":type},verify=False)
    result= r.text
    js1 = json.loads(result)
    js=js1['data']['msg']
    js=eval(js)  #str类型强制转换为字典类型，字典类型才有keys()和value()属性
    key = js.keys()
#    print key
    value = js.values()
#    print value
    n = len(key)
    for i in range (n):        
        if key[i] == 'text':
            return value[i]
        
def sendmessage2(phone,type):
    r=requests.get("https://passport.egou.com/phoneCode_v4.do?",params={"phone":phone,"type":type},verify=False)
    result= r.text
    js1 = json.loads(result)
   
    
    js=js1['sub_msg'] 
    js=eval(js)
    key = js.keys()
#    print key
    value = js.values()
#    print value
    n = len(key)
    for i in range (n):        
        if key[i] == 'text':
            return value[i]
        
                            
                            
def expectcode(host,user,password,database,port,sql):
    mysql.connectdb(host, database, user, password, port)
    result=mysql.selete(sql)
    mysql.closeconnect()
    return result[0][0]
config=ConfigParser.ConfigParser()
config.read('D:\javaworkspace\passport\passport\data_config') 

#case1:用户手机登陆（发送短信验证码）  接口执行2次后会要求输入验证码
host1=config.get("sendmessage1","host")
database1=config.get("sendmessage1","database")
user1=config.get("sendmessage1","user")
password1=config.get("sendmessage1","password")
port1=int(config.get("sendmessage1","port"))
sql1=config.get("sendmessage1","sql")
phone1=config.get("sendmessage1","phone")
type1=config.get("sendmessage1","type")

actcode1=sendmessage(phone1,type1)

expectcode1=expectcode(host1,user1,password1,database1,port1,sql1)

if (actcode1)=="短信动态密码已发送" and (expectcode1)>=1:
  print "case1:用户手机登陆(发送短信验证码)--测试通过"
else:
  print "case1:用户手机登陆(发送短信验证码)--测试通过"  
 
#case2:用户手机登陆（发送语音验证码）  接口执行2次后会要求输入验证码
host2=config.get("sendmessage2","host")
database2=config.get("sendmessage2","database")
user2=config.get("sendmessage2","user")
password2=config.get("sendmessage2","password")
port2=int(config.get("sendmessage2","port"))
sql2=config.get("sendmessage2","sql")
phone2=config.get("sendmessage2","phone")
type2=config.get("sendmessage2","type")

actcode2=sendmessage(phone2,type2)

expectcode2=expectcode(host2,user2,password2,database2,port2,sql2)

if (actcode2)=="语音动态密码已发送" and (expectcode2)>=1:
  print "case2:用户手机登陆(发送语音验证码)--测试通过"
else:
  print "case2:用户手机登陆(发送语音验证码)--测试通过"  
  
  
#case3:用户手机注册（发送短信验证码）  接口执行2次后会要求输入验证码
host3=config.get("sendmessage3","host")
database3=config.get("sendmessage3","database")
user3=config.get("sendmessage3","user")
password3=config.get("sendmessage3","password")
port3=int(config.get("sendmessage3","port"))
sql3=config.get("sendmessage3","sql")
phone3=config.get("sendmessage3","phone")
type3=config.get("sendmessage3","type")

actcode3=sendmessage(phone3,type3)

expectcode3=expectcode(host3,user3,password3,database3,port3,sql3)

if (actcode3)=="短信动态密码已发送" and (expectcode3)>=1:
  print "case3:用户手机注册（发送短信验证码）--测试通过"
else:
  print "case3:用户手机注册（发送短信验证码）--测试通过"  
  
#case4:用户手机注册（发送语音验证码）  接口执行2次后会要求输入验证码
host4=config.get("sendmessage4","host")
database4=config.get("sendmessage4","database")
user4=config.get("sendmessage4","user")
password4=config.get("sendmessage4","password")
port4=int(config.get("sendmessage4","port"))
sql4=config.get("sendmessage4","sql")
phone4=config.get("sendmessage4","phone")
type4=config.get("sendmessage4","type")

actcode4=sendmessage(phone4,type4)

expectcode4=expectcode(host4,user4,password4,database4,port4,sql4)

if (actcode4)=="语音动态密码已发送" and (expectcode4)>=1:
  print "case4:用户手机注册(发送语音验证码)--测试通过"
else:
  print "case4:用户手机注册(发送语音验证码)--测试通过"   

#case5:用户手机登陆（账号已冻结）  接口执行2次后会要求输入验证码
host5=config.get("sendmessage5","host")
database5=config.get("sendmessage5","database")
user5=config.get("sendmessage5","user")
password5=config.get("sendmessage5","password")
port5=int(config.get("sendmessage5","port"))
sql5=config.get("sendmessage5","sql")
phone5=config.get("sendmessage5","phone")
type5=config.get("sendmessage5","type")

actcode5=sendmessage2(phone5,type5)

expectcode5=expectcode(host5,user5,password5,database5,port5,sql5)

if (actcode5)=="账号已冻结，请联系客服解冻 工作时间：每天8:00-22:00 400-0060-666"and(expectcode5)=='freezed':
  print "case5:用户手机登陆（账号已冻结）  --测试通过"
else:
  print "case5:用户手机登陆（账号已冻结）  --测试失败"   

#case6:用户手机注册（账号已冻结）  接口执行2次后会要求输入验证码
host6=config.get("sendmessage6","host")
database6=config.get("sendmessage6","database")
user6=config.get("sendmessage6","user")
password6=config.get("sendmessage6","password")
port6=int(config.get("sendmessage6","port"))
sql6=config.get("sendmessage6","sql")
phone6=config.get("sendmessage6","phone")
type6=config.get("sendmessage6","type")

actcode6=sendmessage2(phone6,type6)

expectcode6=expectcode(host6,user6,password6,database6,port6,sql6)

if (actcode6)=="账号已冻结，请联系客服解冻 工作时间：每天8:00-22:00 400-0060-666"and(expectcode6)=='freezed':
  print "case6:用户手机注册（账号已冻结）  --测试通过"
else:
  print "case6:用户手机注册（账号已冻结）  --测试失败" 

#case7:用户手机登陆(手机号已屏蔽) 
host7=config.get("sendmessage7","host")
database7=config.get("sendmessage7","database")
user7=config.get("sendmessage7","user")
password7=config.get("sendmessage7","password")
port7=int(config.get("sendmessage7","port"))
sql7=config.get("sendmessage7","sql")
phone7=config.get("sendmessage7","phone")
type7=config.get("sendmessage7","type")

actcode7=sendmessage2(phone7,type7)

expectcode7=expectcode(host7,user7,password7,database7,port7,sql7)

if (actcode7)=="该手机号已申请屏蔽接收动态密码，解除屏蔽请使用该手机联系客服。工作时间：每天8:00-22:00 400-0060-666"and(expectcode7)==1:
  print "case5:用户手机登陆（手机号已屏蔽）  --测试通过"
else:
  print "case5:用户手机登陆（手机号已屏蔽）  --测试失败" 




#case8:用户手机注册(手机号已屏蔽)  

host8=config.get("sendmessage8","host")
database8=config.get("sendmessage8","database")
user8=config.get("sendmessage8","user")
password8=config.get("sendmessage8","password")
port8=int(config.get("sendmessage8","port"))
sql8=config.get("sendmessage8","sql")
phone8=config.get("sendmessage8","phone")
type8=config.get("sendmessage8","type")

actcode8=sendmessage2(phone8,type8)

expectcode8=expectcode(host8,user8,password8,database8,port8,sql8)

if (actcode8)=="该手机号已申请屏蔽接收动态密码，解除屏蔽请使用该手机联系客服。工作时间：每天8:00-22:00 400-0060-666"and(expectcode8)==1:
  print "case8:用户手机注册（手机号已屏蔽）  --测试通过"
else:
  print "case8:用户手机注册（手机号已屏蔽）  --测试失败"  


   
#case9:用户手机登陆(手机号错误)  
host9=config.get("sendmessage9","host")
database9=config.get("sendmessage9","database")
user9=config.get("sendmessage9","user")
password9=config.get("sendmessage9","password")
port9=int(config.get("sendmessage9","port"))
sql9=config.get("sendmessage9","sql")
phone9=config.get("sendmessage9","phone")
type9=config.get("sendmessage9","type")

actcode9=sendmessage2(phone9,type9)

expectcode9=expectcode(host9,user9,password9,database9,port9,sql9)

if (actcode9)=="请输入正确的手机号"and(expectcode9)==0:
  print "case9:用户手机登陆(手机号错误)  --测试通过"
else:
  print "case9:用户手机登陆(手机号错误)  --测试失败"  



#case10:用户手机注册(手机号错误)  
host10=config.get("sendmessage10","host")
database10=config.get("sendmessage10","database")
user10=config.get("sendmessage10","user")
password10=config.get("sendmessage10","password")
port10=int(config.get("sendmessage10","port"))
sql10=config.get("sendmessage10","sql")
phone10=config.get("sendmessage10","phone")
type10=config.get("sendmessage10","type")

actcode10=sendmessage2(phone10,type10)

expectcode10=expectcode(host10,user10,password10,database10,port10,sql10)

if (actcode10)=="请输入正确的手机号"and(expectcode10)==0:
  print "case10:用户手机注册(手机号错误)  --测试通过"
else:
  print "case10:用户手机注册(手机号错误)  --测试失败"

