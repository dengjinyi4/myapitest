#coding:utf-8
print "########################九宫格抽奖##########################"
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os 
import sys
import time 
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from common import  mysql

def jiugongge():
    mobile_emulation = {"deviceName":"iPhone 6"}  
    chrome_options = Options()  
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation) 
    chromedriver="C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe"
    driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
    url='https://display.adhudong.com/site_login_ijf.htm?app_key=adhuc0fcad1a253b40e7&user_id=not_login&sign=ea80436de54566c6d0ec33f5c7c8d3e4'
    driver.get(url)
    driver.maximize_window()
    logid=driver.current_url[58:76]
    print "adzone_click_id:"+logid
    print'\n'
    print '访问的地址是:'+url
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="lottery-wrapper"]/div').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[7]/div/div[4]/div[3]').click()
    time.sleep(5)
    # driver.back()
    # # print"抽奖流程正常"
    # driver.find_element_by_xpath('/html/body/div[1]/div[4]').click()
    # WebDriverWait(driver,20).until(lambda the_driver: the_driver.find_element_by_xpath('/html/body/section/div/ul/li[1]/a/div[2]/p').is_displayed())
    # # print "我的奖品信息展示正常"
    # driver.back()
    driver.quit()
    return logid
def jiugonggecount():
  logid=jiugongge()
  time.sleep(8)
  tmpsql=mysql.tmpsql(logid)
  x=[]
  for i in tmpsql:
      x.append(mysql.myselect(i))
#  return sum(x)
  return sum(x)
if __name__ == '__main__': 
    
  print jiugonggecount()    