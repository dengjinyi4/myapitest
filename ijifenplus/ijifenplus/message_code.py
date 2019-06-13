#coding:utf-8
import sys
import requests
import unittest
import json
import time 
import ConfigParser

class mytest(unittest.TestCase):

    def setup(self):
        pass

    def message_code(self,phone):
        jar = requests.cookies.RequestsCookieJar()
        jar.set('ijf_wdata1', 'MS8vMi8vMS8vMS8vMzcvLzNhNDhlZDFmZjE2OGFhMTA5ZjFmZWRiOGJjZTZhMzQ2Ly8wYzY%3D', domain='.ijifen.egou.com', path='/')
        r=requests.get("http://ijifen.egou.com/exchange/yhjSendSMS.htm?",{"phone":phone},cookies=jar)
        result=r.text
        return result
    
    def teardown(self):
        pass
#手机号正常    
    def testmessage_code1(self):
        config=ConfigParser.ConfigParser()
        config.read('D:\javaworkspace\ijifenplus\common\data_config')
        phone1=config.get("message_code","phone1")
        actvalue=self.message_code(phone1)
        actvalue1=json.loads(actvalue)
        actvalue11=actvalue1["code"]
        self.assertEqual(actvalue11,'0')
#手机号错误        
    def testmessage_code2(self):
        config=ConfigParser.ConfigParser()
        config.read('D:\javaworkspace\ijifenplus\common\data_config')
        phone2=config.get("message_code","phone2")
        actvalue=self.message_code(phone2)
        actvalue1=json.loads(actvalue)
        actvalue11=actvalue1["error_msg"]
        self.assertEqual(actvalue11,'手机号错误')


if __name__== '__main__':
    unittest.main()
    
    
        
        
        
        
    
    
    
        