#coding:utf-8
import sys
import os
import time
import unittest
import requests
import json
import ConfigParser
class mytest(unittest.TestCase):
    def setup(self):
        pass
    
    def immediate_exchange(self,award_id):
        jar = requests.cookies.RequestsCookieJar()
        jar.set('ijf_wdata1', 'MS8vMi8vMS8vMS8vMzcvLzNhNDhlZDFmZjE2OGFhMTA5ZjFmZWRiOGJjZTZhMzQ2Ly8wYzY%3D', domain='.ijifen.egou.com', path='/')
        r=requests.get("http://ijifen.egou.com/exchange/immediateRedeem.htm?",{"award_id":award_id},cookies=jar)
        result=r.text
        return result

    def tearDown(self):
        pass
      
    def test_immediate_exchange1(self):
        config=ConfigParser.ConfigParser()
        config.read('D:\javaworkspace\ijifenplus\common\data_config')
        award_id1=config.get("ijifenplus","award_id1")
        actvalue=self.immediate_exchange(award_id1)
        actvalue1=json.loads(actvalue)
        actvalue11=actvalue1["code"]
        self.assertEqual(actvalue11,0)
 
        
    def test_immediate_exchange2(self):
        config=ConfigParser.ConfigParser()
        config.read('D:\javaworkspace\ijifenplus\common\data_config')
        award_id2=config.get("ijifenplus","award_id2")
        actvalue=self.immediate_exchange(award_id2)
        actvalue2=json.loads(actvalue)
        actvalue22=actvalue2["code"]
        self.assertEqual(actvalue22,23) 
        
    def test_immediate_exchange3(self):
        config=ConfigParser.ConfigParser()
        config.read('D:\javaworkspace\ijifenplus\common\data_config')
        award_id3=config.get("ijifenplus","award_id3")
        actvalue=self.immediate_exchange(award_id3)
        actvalue3=json.loads(actvalue)
        actvalue33=actvalue3["code"]
        self.assertEqual(actvalue33,41)    
        

if __name__=='__main__':
    
    unittest.main()
    
        