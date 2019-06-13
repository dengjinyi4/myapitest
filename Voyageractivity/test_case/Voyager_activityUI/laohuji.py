#coding:utf-8
print "########################老虎机抽奖##########################"
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os 
import sys
import time 
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from common import  mysql

def laohuji():
    mobile_emulation = {"deviceName":"iPhone 6"}  
    chrome_options = Options()  
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation) 
    chromedriver="C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe"
    driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
    url='https://display.adhudong.com/site_login_ijf.htm?app_key=adhu6b250ae20dd9469e&user_id=not_login&sign=94d51910fad4f371358aaeec37f5b247'
    driver.get(url)
    driver.maximize_window()
    logid=driver.current_url[62:80]
    print "adzone_click_id:"+logid
    print'\n'
    print '访问的地址是:'+url
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[4]/button[2]').click()
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/div[3]/div[2]/button').click()
    time.sleep(5)
#     driver.back()
#     # print"抽奖流程正常"
# #    print logid
#     driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[4]/button[1]').click()
#     WebDriverWait(driver,20).until(lambda the_driver: the_driver.find_element_by_xpath('/html/body/section/div/ul/li[1]/a').is_displayed())
#     # print "我的奖品信息展示正常"
#     driver.back()
    driver.quit()
    return logid
    
def laohujicount():
  logid=laohuji()
  time.sleep(8)
  tmpsql=mysql.tmpsql(logid)
  x=[]
  for i in tmpsql:
      x.append(mysql.myselect(i))
  return sum(x)
if __name__ == '__main__': 
    
  print laohujicount()        