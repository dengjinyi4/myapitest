#coding:utf-8
import sys
import json
import requests
import warnings
import ConfigParser
from passport.common import mysql
warnings.filterwarnings("ignore")
 
def userlogin(username,password,randNum,vcode_id,v):
    r=requests.get("https://passport.egou.com/login_v2.do?",params={"username":username,"password":password,"randNum":randNum,"vcode_id":vcode_id,"v":v},verify=False)
    result= r.text
    return result

def expectcode(host,user,password,database,port,sql):
    mysql.connectdb(host, database, user, password, port)
    result=mysql.selete(sql)
    mysql.closeconnect()
    return result[0][0]
config=ConfigParser.ConfigParser()
config.read('D:\javaworkspace\passport\passport\data_config') 

#case1:用户名密码登陆（用户名和密码正确）
host1=config.get("userlogin1","host")
database1=config.get("userlogin1","database")
user1=config.get("userlogin1","user")
password1=config.get("userlogin1","password")
port1=int(config.get("userlogin1","port"))
sql1=config.get("userlogin1","sql")
username1=config.get("userlogin1","username")
password11=config.get("userlogin1","password11")
randNum1=config.get("userlogin1","randNum")
vcode_id1=config.get("userlogin1","vcode_id")
v1=config.get("userlogin1","v")


actvalue1=userlogin(username1,password11,randNum1,vcode_id1,v1)
actcodestr1=json.loads(actvalue1)
actcode1=actcodestr1["code"]

expectcode1=expectcode(host1,user1,password1,database1,port1,sql1)

if (actcode1)==0 and (expectcode1)==1:
    print "case1:用户名密码登陆（用户名和密码正确）--测试通过"
else:
    print "case1:用户名密码登陆（用户名和密码正确）--测试失败"
    
#case2:用户名密码登陆（用户不存在）
host2=config.get("userlogin2","host")
database2=config.get("userlogin2","database")
user2=config.get("userlogin2","user")
password2=config.get("userlogin2","password")
port2=int(config.get("userlogin2","port"))
sql2=config.get("userlogin2","sql")
username2=config.get("userlogin2","username")
password22=config.get("userlogin2","password22")
randNum2=config.get("userlogin2","randNum")
vcode_id2=config.get("userlogin2","vcode_id")
v2=config.get("userlogin2","v")

actvalue2=userlogin(username2,password22,randNum2,vcode_id2,v2)
actvalue2str=json.loads(actvalue2)
actcode2=actvalue2str["sub_msg"]

expectcode2=expectcode(host2,user2,password2,database2,port2,sql2)

if (actcode2)=="用户不存在" and (expectcode2)==0:
    print "case2:用户名密码登陆（用户不存在）--测试通过"
    
else:
    print "case2:用户名密码登陆（用户不存在）--测试失败"  
    
         
#case3:用户名密码登陆（用户冻结）
host3=config.get("userlogin3","host")
database3=config.get("userlogin3","database")
user3=config.get("userlogin3","user")
password3=config.get("userlogin3","password")
port3=int(config.get("userlogin3","port"))
sql3=config.get("userlogin3","sql")
username3=config.get("userlogin3","username")
password33=config.get("userlogin3","password33")
randNum3=config.get("userlogin3","randNum")
vcode_id3=config.get("userlogin3","vcode_id")
v3=config.get("userlogin3","v")

actvalue3=userlogin(username3,password33,randNum3,vcode_id3,v3)
actvalue3str=json.loads(actvalue3)
actcode3=actvalue3str["sub_msg"]

expectcode3=expectcode(host3,user3,password3,database3,port3,sql3)
 
if (actcode3)=="用户已冻结" and (expectcode3)=="freezed":
    print "case3:用户名密码登陆（用户冻结）--测试通过"
    
else:
    print "case3:用户名密码登陆（用户冻结）--测试失败"  


#case4:用户名密码登陆（密码错误）    
host4=config.get("userlogin4","host")
database4=config.get("userlogin4","database")
user4=config.get("userlogin4","user")
password4=config.get("userlogin4","password")
port4=int(config.get("userlogin4","port"))
sql4=config.get("userlogin4","sql")
username4=config.get("userlogin4","username")
password44=config.get("userlogin4","password44")
randNum4=config.get("userlogin4","randNum")
vcode_id4=config.get("userlogin4","vcode_id")
v4=config.get("userlogin4","v")

actvalue4=userlogin(username4,password44,randNum4,vcode_id4,v4)
actvalue4str=json.loads(actvalue4)
actcode4=actvalue4str["sub_msg"]
expectcode4=expectcode(host4,user4,password4,database4,port4,sql4)

if (actcode4)=="密码有误，您还有4次尝试机会" and (expectcode4)==0:
    print "case4:用户名密码登陆（密码错误）--测试通过"
    
else:
    print "case4:用户名密码登陆（密码错误）--测试失败"  

