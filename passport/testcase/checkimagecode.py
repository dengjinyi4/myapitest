#coding:utf-8
import sys
import warnings
import requests
import json
import ConfigParser
import unittest
from passport.common import mysql
warnings.filterwarnings("ignore")

def checkimagecode(vcode,vcode_id):  
   r=requests.get("https://passport.egou.com/validateImgCode.do?",params={"vcode":vcode,"vcode_id":vcode_id},verify=False)
   result=r.text
   return result
 
  
#case1:图形验证码正确   执行该用例之前需要访问https://passport.egou.com/imgvcode.jpg 获取最新的vcode_id和vode填充到dataconfig文件汇总
config=ConfigParser.ConfigParser()
config.read('D:\javaworkspace\passport\passport\data_config')
vcode1=config.get("checkimagecode1","vcode")
vcode_id1=config.get("checkimagecode1","vcode_id")
 
actcode1=checkimagecode(vcode1,vcode_id1)
#print actcode1
expectcode1=1
#print expectcode1
if int(actcode1)==int(expectcode1):
    print "case1:验证图片验证码(图片验证码正确)--测试通过"
else:
    print "case1:验证图片验证码(图片验证码正确)--测试失败"
    
#case2:图形验证码错误
config=ConfigParser.ConfigParser()
config.read('D:\javaworkspace\passport\passport\data_config')
vcode2=config.get("checkimagecode2","vcode")
vcode_id2=config.get("checkimagecode2","vcode_id")
 
actcode2=checkimagecode(vcode2,vcode_id2)
print actcode2
expectcode2=0
print expectcode2
if int(actcode2)==int(expectcode2):
    print "case2:验证图片验证码(图片验证码错误)--测试通过"
else:
    print "case2:验证图片验证码(图片验证码错误)--测试失败"
    
    
          
