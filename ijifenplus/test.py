import sys
import os
import time
import unittest
import requests
import json
import ConfigParser
def immediate_exchange(award_id):
    
        jar = requests.cookies.RequestsCookieJar()
        jar.set('ijf_wdata1', 'MS8vMi8vMS8vMS8vMzcvLzNhNDhlZDFmZjE2OGFhMTA5ZjFmZWRiOGJjZTZhMzQ2Ly8wYzY%3D', domain='.ijifen.egou.com', path='/')
        r=requests.get("http://ijifen.egou.com/exchange/immediateRedeem.htm?",{"award_id":award_id},cookies=jar)
        result=r.text
        return result

config=ConfigParser.ConfigParser()
config.read('D:\javaworkspace\ijifenplus\common\data_config')
award_id1=config.get("ijifenplus","award_id1")
print award_id1
actvalue1=immediate_exchange(award_id1)
print actvalue1
actcode1=json.loads(actvalue1)
actvalue11=actcode1["code"]
print actvalue11


config=ConfigParser.ConfigParser()
config.read('D:\javaworkspace\ijifenplus\common\data_config')
award_id2=config.get("ijifenplus","award_id2")
print award_id2
actvalue2=immediate_exchange(award_id2)
print actvalue2
actcode2=json.loads(actvalue2)
actvalue22=actcode2["code"]
print actvalue22 
