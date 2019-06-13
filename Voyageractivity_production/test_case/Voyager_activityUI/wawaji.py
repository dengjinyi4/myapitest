#coding:utf-8

print "########################娃娃机抽奖##########################"
import os 
import sys
import time
import datetime 
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from common import  mysql
def wawaji():
    mobile_emulation = {"deviceName":"iPhone 6"}  
    chrome_options = Options()  
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation) 
    chromedriver="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
    driver.get('https://display.adhudong.com/site_login_ijf.htm?app_key=adhua5bf121ce752495e&user_id=not_login&sign=49556f7d66fa82c31e4091cd2c8fdb7a')
    driver.maximize_window()
    logid=driver.current_url[59:77]
    print "adzone_click_id:"+logid
    time.sleep(2)
    js="var q=document.documentElement.scrollTop=100000"  
    driver.execute_script(js)  
    time.sleep(2)  
       
    driver.find_element_by_xpath('/html/body/div[1]/div/div[7]/a[2]').click()
    time.sleep(6)
    driver.find_element_by_xpath('/html/body/div[4]/div/div[4]/div[3]').click()
    time.sleep(2)
    driver.back()
    # print"抽奖流程正常"
    

    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[7]/a[3]').click()
    WebDriverWait(driver,20).until(lambda the_driver: the_driver.find_element_by_xpath('/html/body/section/div/ul/li/a/div[2]/p').is_displayed())
    # print "我的奖品信息展示正常"
    driver.back()
    driver.quit()
    return logid

def wawajicount():
  logid=wawaji()
  tmpsql=mysql.tmpsql(logid)
  x=[]
  for i in tmpsql:
      x.append(mysql.myselect(i))
  return sum(x)

if __name__ == '__main__': 
    
  print wawajicount()     
  