#coding:utf-8

print "=======================砸蛋抽奖====================="
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os 
import sys
import time 
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from common import  mysql
def zadan():
    mobile_emulation = {"deviceName":"iPhone 6"}  
    chrome_options = Options()  
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation) 
    chromedriver="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
    driver.delete_all_cookies()
    driver.get('https://display.adhudong.com/site_login_ijf.htm?app_key=adhu72b3c49ed71a4854&user_id=not_login&sign=9f8b2c8dcf13ad5e580e42d35d12046c')
    driver.maximize_window()
    logid=driver.current_url[56:74]
    print logid
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div[2]/div[5]/div[1]').click()
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[4]').click()
    time.sleep(2)
    driver.back()
    # print"抽奖流程正常"
    time.sleep(2)
    
    

    driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/span').click()
    WebDriverWait(driver,20).until(lambda the_driver: the_driver.find_element_by_xpath('/html/body/section/div/ul/li/a/div[2]/p').is_displayed())
    # print "我的奖品信息展示正常"
    driver.back()
    driver.quit()
    return logid
    
def zadanwawajicount():
  logid=zadan()
  tmpsql=mysql.tmpsql(logid)
  x=[]
  for i in tmpsql:
      x.append(mysql.myselect(i))
  return sum(x)
if __name__ == '__main__': 
    
  print zadanwawajicount()         