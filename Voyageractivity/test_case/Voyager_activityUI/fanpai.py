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
    chromedriver="C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe"
    driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
    url='https://display.adhudong.com/site_login_ijf.htm?app_key=adhu8b3931d74f1f44d1&user_id=not_login&sign=dc6c70023ee709c4e2d4211ee51407f3'
    driver.get(url)
    driver.maximize_window()
    logid=driver.current_url[54:72]
    print "adzone_click_id:"+logid
    print'\n'
    print '访问的地址是:'+url
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[4]/div').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[10]/div/div/div[3]/div[3]/div[3]/button').click()
    time.sleep(5)
    # driver.back()
    # # print"抽奖流程正常"
    # driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/a').click()
    # WebDriverWait(driver,20).until(lambda the_driver: the_driver.find_element_by_xpath('/html/body/section/div/ul/li[1]/a/div[2]/p').is_displayed())
    # # print "我的奖品信息展示正常"
    # driver.back()
    driver.quit()
    return logid

def fanpaicount():
  logid=fanpai()
  time.sleep(8)
  tmpsql=mysql.tmpsql(logid)
  x=[]
  for i in tmpsql:
      x.append(mysql.myselect(i))
  return sum(x)
#  print sum(x)
if __name__ == '__main__': 
    
  print fanpaicount()