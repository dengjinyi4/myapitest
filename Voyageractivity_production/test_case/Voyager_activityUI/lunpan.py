#coding:utf-8
# print "########################轮盘抽奖##########################"
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os 
import sys
import time 
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from common import  mysql
def lunpan():
    mobile_emulation = {"deviceName":"iPhone 6"}  
    chrome_options = Options()  
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation) 
    # chromedriver="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    chromedriver=mysql.mydriverpath()
    driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
    url='https://display.intdmp.com/site_login_ijf.htm?app_key=adhu5e20439ff2ac48fa'
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)
    logid=driver.current_url[55:73]
    picdir='C:/auto/Voyageractivity_production/test_case/Voyager_activityUI/pic/'
    pic_patch=picdir+str(logid)+'_'+timenow()+'.png'
    driver.get_screenshot_as_file(pic_patch)
    # print "adzone_click_id:"+logid
    # print'\n'
    # print '访问的地址是:'+url
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div[2]').click()
    time.sleep(5)
    pic_patch=picdir+str(logid)+'_'+timenow()+'.png'
    driver.get_screenshot_as_file(pic_patch)
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[6]/div/div/div[3]/div[3]/div[2]/button/span').click()
    time.sleep(5)
    pic_patch=picdir+str(logid)+'_'+timenow()+'.png'
    driver.get_screenshot_as_file(pic_patch)
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
  tmpsql=mysql.tmpsql(logid)
  x=[]
  for i in tmpsql:
      x.append(mysql.myselect(i))
  return sum(x),logid
def timenow():
  return str(time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime()))
if __name__ == '__main__': 
    
  print lunpancount()  