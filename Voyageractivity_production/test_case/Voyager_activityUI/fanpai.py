#coding:utf-8
print "########################翻牌抽奖#######################"
import os 
import sys
import time 
import datetime
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
#import MySQLdb as mysql,time,datetime
from common import mysql

def fanpai():
    mobile_emulation = {"deviceName":"iPhone 6"}  
    chrome_options = Options()  
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    chromedriver=mysql.mydriverpath()
    driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
    url='https://display.adhudong.com/site_login_ijf.htm?app_key=adhue0495ffec75549ca&user_id=not_login&sign=70f5aeab053f745263a8ce24457d22d4'
    driver.get(url)
    time.sleep(3)
    driver.maximize_window()
    # logid=driver.current_url[52:70]
    logid=driver.current_url[54:72]
    picdir='C:/auto/Voyageractivity_production/test_case/Voyager_activityUI/pic/'
    pic_patch=picdir+str(logid)+'_'+timenow()+'.png'
    print pic_patch
    try:
      x=driver.get_screenshot_as_file(pic_patch)
      print x
    except Exception, e:
      print e.message
    # print "adzone_click_id:"+logid
    # print'\n'
    # print '访问的地址是:'+url
    time.sleep(9)
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[4]/div').click()
    time.sleep(9)
    pic_patch=picdir+str(logid)+'_'+timenow()+'.png'
    driver.get_screenshot_as_file(pic_patch)
    try:
      driver.find_element_by_xpath('//*[@id="root"]/div/div/div[10]/div/div/div[3]/div[3]/div[3]/button').click()
      pic_patch=picdir+str(logid)+'_'+timenow()+'.png'
      driver.get_screenshot_as_file(pic_patch)
    except Exception as e:
      print e.message
    time.sleep(9)
    driver.quit()
    return logid
def fanpaicount():
  logid=fanpai()
  tmpsql=mysql.tmpsql(logid)
  x=[]
  for i in tmpsql:
      x.append(mysql.myselect(i))
  return sum(x),logid
def timenow():
  return str(time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime()))
#  print sum(x)
if __name__ == '__main__': 
    
  fanpaicount()
  # print 1
  # print(time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime())) 