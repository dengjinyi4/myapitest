#coding:utf-8
import sys
import warnings
import requests
import json
import ConfigParser
from passport.common import mysql
warnings.filterwarnings("ignore")
def checkphone(phone,type):  
    r=requests.get("https://passport.egou.com/check_phone.do?",params={"phone":phone,"type":type},verify=False)
    result=r.text
    return result
def expectcode(host,database,user,password,port,sql):
    mysql.connectdb(host, database, user, password, port)
    result=mysql.selete(sql)
    return result[0][0]
  
#case1:验证手机号登陆(手机号已注册)
config=ConfigParser.ConfigParser()
config.read('D:\javaworkspace\passport\passport\data_config')
host1=config.get("checkphone1","host")
database1=config.get("checkphone1","database")
user1=config.get("checkphone1","user")
password1=config.get("checkphone1","password")
port1=int(config.get("checkphone1","port"))
sql1=config.get("checkphone1","sql")
phone1=config.get("checkphone1","phone")
type1=config.get("checkphone1","type")
actvalue1=checkphone(phone1,type1)
json_str1=json.loads(actvalue1)
actcode1=json_str1["code"]
#print code   

expectcode1=expectcode(host1, database1, user1, password1,port1,sql1)
#print expectcode
if (expectcode1==1) and (actcode1==0):
    print "case1:验证手机号登陆(手机号已注册)--测试通过"
else:
    print "case1:验证手机号登陆(手机号已注册)--测试失败"
    
#case2:验证手机号登陆(手机号未注册)

host2=config.get("checkphone2","host")
database2=config.get("checkphone2","database")
user2=config.get("checkphone2","user")
password2=config.get("checkphone2","password")
port2=int(config.get("checkphone2","port"))
sql2=config.get("checkphone2","sql")
phone2=config.get("checkphone2","phone")
type2=config.get("checkphone2","type")

actvalue2=checkphone(phone2,type2)
actvalue2str=json.loads(actvalue2)
actcode2=actvalue2str["sub_msg"]
#print actcode2
expectcode2=expectcode(host2,database2,user2,password2,port2,sql2)
if (actcode2=='手机号未注册') and (expectcode2==0):
    print "case2:验证手机号登陆(手机号未注册)--测试通过"
else:
    print "case2:验证手机号登陆(手机号未注册)--失败"

#case3:验证手机号注册（手机号已注册）
host3=config.get("checkphone3","host")
database3=config.get("checkphone3","database")
user3=config.get("checkphone3","user")
password3=config.get("checkphone3","password")
port3=int(config.get("checkphone3","port"))
sql3=config.get("checkphone3","sql")
phone3=config.get("checkphone3","phone")
type3=config.get("checkphone3","type")

actvalue3=checkphone(phone3,type3)
actvalue3str=json.loads(actvalue3)
actcode3=actvalue3str["sub_msg"]
#print actcode3

expectcode3=expectcode(host3,database3,user3,password3,port3,sql3)

if (actcode3=="手机号已被注册") and (expectcode3==1):
    print"case3:验证手机号注册(手机号已注册)--测试通过" 
else:
    print"case3:验证手机号注册(手机号已注册)--测试失败"


#case4:验证手机号注册（手机号未注册）
host4=config.get("checkphone4","host")
database4=config.get("checkphone4","database")
user4=config.get("checkphone4","user")
password4=config.get("checkphone4","password")
port4=int(config.get("checkphone4","port"))
sql4=config.get("checkphone4","sql")
phone4=config.get("checkphone4","phone")
type4=config.get("checkphone4","type")


actvalue4=checkphone(phone4,type4)
actvalue4str=json.loads(actvalue4)
actcode4=actvalue4str["code"]
#print actcode3

expectcode4=expectcode(host4,database4,user4,password4,port4,sql4)

if (actcode4==0) and (expectcode4==0):
    print"case4:验证手机号注册(手机号未注册)--测试通过" 
else:
    print"case4:验证手机号注册(手机号未注册)--测试失败"

#case5:验证手机号登陆（手机号错误）
host5=config.get("checkphone5","host")
database5=config.get("checkphone5","database")
user5=config.get("checkphone5","user")
password5=config.get("checkphone5","password")
port5=int(config.get("checkphone5","port"))
sql5=config.get("checkphone5","sql")
phone5=config.get("checkphone5","phone")
type5=config.get("checkphone5","type")


actvalue5=checkphone(phone5,type5)
actvalue5str=json.loads(actvalue5)
actcode5=actvalue5str["sub_msg"]
#print actcode3

expectcode5=expectcode(host5,database5,user5,password5,port5,sql5)

if (actcode5=="请输入正确的手机号") and (expectcode5=="0"):
    print"case5:验证手机号登陆(手机号不正确)--测试通过" 
else:
    print"case5:验证手机号登陆(手机号不正确)--测试失败"


#case6:验证手机号注册（手机号错误）
host6=config.get("checkphone6","host")
database6=config.get("checkphone6","database")
user6=config.get("checkphone6","user")
password6=config.get("checkphone6","password")
port6=int(config.get("checkphone6","port"))
sql6=config.get("checkphone6","sql")
phone6=config.get("checkphone6","phone")
type6=config.get("checkphone6","type")


actvalue6=checkphone(phone6,type6)
actvalue6str=json.loads(actvalue6)
actcode6=actvalue6str["sub_msg"]
#print actcode3

expectcode6=expectcode(host6,database6,user6,password6,port6,sql6)

if (actcode6=="请输入正确的手机号") and (expectcode6=="0"):
    print"case6:验证手机号注册(手机号不正确)--测试通过" 
else:
    print"case6:验证手机号注册(手机号不正确)--测试失败"


#case7:验证手机号登陆（手机号对应的账号已冻结）
host7=config.get("checkphone7","host")
database7=config.get("checkphone7","database")
user7=config.get("checkphone7","user")
password7=config.get("checkphone7","password")
port7=int(config.get("checkphone7","port"))
sql7=config.get("checkphone7","sql")
phone7=config.get("checkphone7","phone")
type7=config.get("checkphone7","type")


actvalue7=checkphone(phone7,type7)
actvalue7str=json.loads(actvalue7)
actcode7=actvalue7str["sub_msg"]
#print actcode3

expectcode7=expectcode(host7,database7,user7,password7,port7,sql7)

if (actcode7=="账号已冻结，请联系客服解冻") and (expectcode7=="freezed"):
    print"case7:验证手机号登陆(手机号对应的账号已冻结)--测试通过" 
else:
    print"case7:验证手机号登陆(手机号对应的账号已冻结)--测试失败"


#case8:验证手机号注册（手机号对应的账号已冻结）

host8=config.get("checkphone8","host")
database8=config.get("checkphone8","database")
user8=config.get("checkphone8","user")
password8=config.get("checkphone8","password")
port8=int(config.get("checkphone8","port"))
sql8=config.get("checkphone8","sql")
phone8=config.get("checkphone8","phone")
type8=config.get("checkphone8","type")


actvalue8=checkphone(phone8,type8)
actvalue8str=json.loads(actvalue8)
actcode8=actvalue8str["sub_msg"]
#print actcode3

expectcode8=expectcode(host8,database8,user8,password8,port8,sql8)

if (actcode8=="手机号已被注册") and (expectcode8=="freezed"):
    print"case8:验证手机号注册(手机号对应的账号已冻结)--测试通过" 
else:
    print"case8:验证手机号注册(手机号对应的账号已冻结)--测试失败"

#case9:验证手机号登陆（手机号为空）
host9=config.get("checkphone9","host")
database9=config.get("checkphone9","database")
user9=config.get("checkphone9","user")
password9=config.get("checkphone9","password")
port9=int(config.get("checkphone9","port"))
sql9=config.get("checkphone9","sql")
phone9=config.get("checkphone9","phone")
type9=config.get("checkphone9","type")


actvalue9=checkphone(phone9,type9)
actvalue9str=json.loads(actvalue9)
actcode9=actvalue9str["sub_msg"]
#print actcode3


if (actcode9=="手机号不能为空"):
    print"case9:验证手机号登陆（手机号为空）--测试通过" 
else:
    print"case9:验证手机号登陆（手机号为空）--测试失败"
    
    

#case10:验证手机号注册（手机号为空）
host10=config.get("checkphone10","host")
database10=config.get("checkphone10","database")
user10=config.get("checkphone10","user")
password10=config.get("checkphone10","password")
port10=int(config.get("checkphone10","port"))
sql10=config.get("checkphone10","sql")
phone10=config.get("checkphone10","phone")
type10=config.get("checkphone10","type")


actvalue10=checkphone(phone10,type10)
actvalue10str=json.loads(actvalue10)
actcode10=actvalue10str["sub_msg"]

 
#print actcode3


if (actcode10=="手机号不能为空"):
    print"case10:验证手机号注册（手机号为空）--测试通过" 
else:
    print"case10:验证手机号注册（手机号为空）--测试失败"


#case11:验证手机号登陆（手机号已屏蔽验证码）

host11=config.get("checkphone11","host")
database11=config.get("checkphone11","database")
user11=config.get("checkphone11","user")
password11=config.get("checkphone11","password")
port11=int(config.get("checkphone11","port"))
sql11=config.get("checkphone11","sql")
phone11=config.get("checkphone11","phone")
type11=config.get("checkphone11","type")


actvalue11=checkphone(phone11,type11)
actvalue11str=json.loads(actvalue11)
actcode11=actvalue11str["sub_msg"]

expectcode11=expectcode(host11,database11,user11,password11,port11,sql11)
if (actcode11=="该手机号已申请屏蔽接收动态密码，解除屏蔽请联系客服") and (expectcode11==1):
    print"case11:验证手机号登陆（手机号已屏蔽验证码）--测试通过" 
else:
    print"case11:验证手机号登陆（手机号已屏蔽验证码）--测试失败" 
     

#case12:验证手机号注册（手机号已屏蔽验证码）

host12=config.get("checkphone12","host")
database12=config.get("checkphone12","database")
user12=config.get("checkphone12","user")
password12=config.get("checkphone12","password")
port12=int(config.get("checkphone12","port"))
sql12=config.get("checkphone12","sql")
phone12=config.get("checkphone12","phone")
type12=config.get("checkphone12","type")


actvalue12=checkphone(phone12,type12)
actvalue12str=json.loads(actvalue12)
actcode12=actvalue12str["sub_msg"]

expectcode12=expectcode(host12,database12,user12,password12,port12,sql12)

if (actcode12=="手机号已被注册") and (expectcode12==1):
    print"case12:验证手机号注册（手机号已屏蔽验证码）--测试通过" 
else:
    print"case12:验证手机号注册（手机号已屏蔽验证码）--测试失败" 
     