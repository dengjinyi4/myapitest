#coding:utf-8
import sys
import time 
import unittest
import json
import requests
import ConfigParser
import MySQLdb
from common import mysql
    
def apply_exchange(code,phone,award_id,alipayCount,terminal):
        jar = requests.cookies.RequestsCookieJar()
        jar.set('ijf_wdata1', 'MS8vMi8vMS8vMS8vMzcvLzNhNDhlZDFmZjE2OGFhMTA5ZjFmZWRiOGJjZTZhMzQ2Ly8wYzY%3D', domain='.ijifen.egou.com', path='/')
        r=requests.get("http://ijifen.egou.com/exchange/commentary.htm?",{"code":code,"phone":phone,"award_id":award_id,"alipayCount":alipayCount,"terminal":terminal},cookies=jar)
        result=r.text
        return result
def message_code(phone):
        jar = requests.cookies.RequestsCookieJar()
        jar.set('ijf_wdata1', 'MS8vMi8vMS8vMS8vMzcvLzNhNDhlZDFmZjE2OGFhMTA5ZjFmZWRiOGJjZTZhMzQ2Ly8wYzY%3D', domain='.ijifen.egou.com', path='/')
        r=requests.get("http://ijifen.egou.com/exchange/yhjSendSMS.htm?",{"phone":phone},cookies=jar)
        result=r.text
        return result
def get_expected_code(host,database,user,password,port,sql): 
        mysql.connectdb(host, database,user,password,port) 
        result=mysql.selete(sql)
        mysql.closeconnect()
        return result[0][0]
    
config=ConfigParser.ConfigParser()
config.read('D:\javaworkspace\ijifenplus\common\data_config')
code1=config.get("apply_exchange","code1")
phone1=config.get("apply_exchange","phone1")
award_id1=config.get("apply_exchange","award_id1")
alipayCount1=config.get("apply_exchange","alipayCount1")
terminal1=config.get("apply_exchange","terminal1")
actvalue=apply_exchange(code1,phone1,award_id1,alipayCount1,terminal1)
print actvalue
actvalue1=json.loads(actvalue)
actvalue11=actvalue1["error_msg"]
print actvalue11
        
config=ConfigParser.ConfigParser()
config.read('D:\javaworkspace\ijifenplus\common\data_config')
phone2=config.get("apply_exchange","phone2")
award_id2=config.get("apply_exchange","award_id2")
alipayCount2=config.get("apply_exchange","alipayCount2")
terminal2=config.get("apply_exchange","terminal2")
phonecode=config.get("apply_exchange","phone2")
actphonecode=message_code(phonecode)
host = config.get("apply_exchange","host")
port = int(config.get("apply_exchange","port"))
database = config.get("apply_exchange","database")
user = config.get("apply_exchange","user")
password = config.get("apply_exchange","password")
sql=config.get("apply_exchange","sql")
expect_code=get_expected_code(host,database,user,password,port,sql) 
time.sleep(3)
print expect_code
code2=int(expect_code) 
actvalue=apply_exchange(code2,phone2,award_id2,alipayCount2,terminal2)
print actvalue
actvalue2=json.loads(actvalue)
actvalue22=actvalue2["code"]   

print actvalue22    
        