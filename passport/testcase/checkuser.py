#coding:utf-8
import sys
import requests
import json
import ConfigParser
import warnings
from passport.common import mysql
warnings.filterwarnings("ignore")
def checkuser(name):
 r=requests.get("https://passport.egou.com/check_v2.do?",params={'username':name},verify=False)
 return r
def get_expected_code(host,database,user,password,port,sql): 
    mysql.connectdb(host, database,user,password,port) 
    result=mysql.selete(sql)
    mysql.closeconnect()
    return result[0][0]
#case1 用户名存在
config = ConfigParser.ConfigParser()
config.read('D:\javaworkspace\passport\passport\data_config')
host =  config.get('checkuser1', 'host')
database = config.get('checkuser1', 'database')
user = config.get('checkuser1', 'user')
password = config.get('checkuser1', 'password')
port = int(config.get('checkuser1', 'port'))
sql = config.get('checkuser1', 'sql')

expect_code=get_expected_code(host,database,user,password,port,sql)
#print expect_code

result1=checkuser('beyond20088')
#print result1.text
json_str=json.loads(result1.text)
code=json_str['code']
#print code

if (expect_code==1)and(code)==0: 
    print "case1:验证用户是否存在接口(用户名存在) ---测试通过"
   
else:
    print "case1:验证用户是否存在接口(用户名存在) ---测试失败"

#case2 用户名不存在
config = ConfigParser.ConfigParser()
config.read('D:\javaworkspace\passport\passport\data_config')
host =  config.get('checkuser2', 'host')
database = config.get('checkuser2', 'database')
user = config.get('checkuser2', 'user')
password = config.get('checkuser2', 'password')
port = int(config.get('checkuser2', 'port'))
sql = config.get('checkuser2', 'sql')

expect_code=get_expected_code(host,database,user,password,port,sql)
#print expect_code


result2=checkuser('be22323')
#print result2.text
json_str=json.loads(result2.text)
code=json_str['code']
#print code
if (expect_code==0)and(code==43):
    print "case2:验证用户是否存在接口(用户名不存在)---测试通过"
else:
    print "case2:验证用户是否存在接口(用户名存在 )---测试失败"
 