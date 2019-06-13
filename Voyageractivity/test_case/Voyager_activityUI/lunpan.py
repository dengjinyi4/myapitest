#coding:utf-8
print "########################轮盘抽奖##########################"
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os 
import sys
import time 
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import *
from common import  mysql
def lunpan():
    mobile_emulation = {"deviceName":"iPhone 6"}  
    chrome_options = Options()  
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    chromedriver="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
    url='https://display.adhudong.com/site_login_ijf.htm?app_key=adhud24b8f1a47174868&user_id=not_login&sign=4faa143b49442ae60a56d9594a4223c8'
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)
    logid=driver.current_url[59:77]
    print "adzone_click_id:"+logid
    print'\n'
    print '访问的地址是:'+url
    driver.find_element_by_xpath('/html/body/section/div[2]/div[2]/div/div[2]/div[2]').click()
    time.sleep(8)
    driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div[3]/div[2]/button').click()
    time.sleep(5)
    # driver.back()
    # # print"抽奖流程正常"
    

    # driver.find_element_by_xpath('/html/body/section/div[1]/a').click()
    # WebDriverWait(driver,20).until(lambda the_driver: the_driver.find_element_by_xpath('/html/body/section/div/ul/li/a/div[2]/p').is_displayed())
    # # print "我的奖品信息展示正常"
    # driver.back()
    driver.quit()
    return logid
def lunpancount():
  logid=lunpan()
  time.sleep(8)
  tmpsql=mysql.tmpsql(logid)
  x=[]
  for i in tmpsql:
      x.append(mysql.myselect(i))
  return sum(x)
if __name__ == '__main__': 
  print lunpancount()  