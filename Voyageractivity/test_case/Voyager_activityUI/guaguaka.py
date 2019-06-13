#coding:utf-8

from selenium import webdriver
import os
import time 
from selenium.webdriver.common.action_chains import ActionChains
from common import  mysql
def guaguaka():
    chromedriver = "C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver =  webdriver.Chrome(chromedriver)
    driver.get('https://display.adhudong.com/site_login_ijf.htm?app_key=adhu225e7fc828c248b2&user_id=not_login&sign=b0ece1b5caf6ad3ab91b10b9c6e110c5')
    driver.maximize_window()
    time.sleep(2)
    logid=driver.current_url[59:77]
    print '广告位98'
    print "adzone_click_id:"+logid
    # 点击刮刮卡 开始刮奖
    driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div[2]/div/div[1]').click()
    time.sleep(5)
#    mycanvas=driver.find_element_by_xpath('/html/body/div/div[3]/div[1]/div/div[1]/div')
    mycanvas1=driver.find_element_by_xpath('//*[@id="scratch-img"]')
    action = ActionChains(driver)
    action.click_and_hold(mycanvas1).move_by_offset(10,20)
    action.click_and_hold(mycanvas1).move_by_offset(10,60)
    action.click_and_hold(mycanvas1).move_by_offset(10,100)
    action.click_and_hold(mycanvas1).move_by_offset(10,140)
    action.click_and_hold(mycanvas1).move_by_offset(10,180)
    action.click_and_hold(mycanvas1).move_by_offset(10,120)
    action.click_and_hold(mycanvas1).move_by_offset(50,20)
    action.click_and_hold(mycanvas1).move_by_offset(50,60)
    action.click_and_hold(mycanvas1).move_by_offset(50,100)
    action.click_and_hold(mycanvas1).move_by_offset(50,140)
    action.click_and_hold(mycanvas1).move_by_offset(50,180)
    action.click_and_hold(mycanvas1).move_by_offset(50,120)
    action.click_and_hold(mycanvas1).move_by_offset(80,20)
    action.click_and_hold(mycanvas1).move_by_offset(80,60)
    action.click_and_hold(mycanvas1).move_by_offset(80,100)
    action.click_and_hold(mycanvas1).move_by_offset(80,140)
    action.click_and_hold(mycanvas1).move_by_offset(80,180)
    action.click_and_hold(mycanvas1).move_by_offset(80,120)
    action.click_and_hold(mycanvas1).move_by_offset(120,20)
    action.click_and_hold(mycanvas1).move_by_offset(120,60)
    action.click_and_hold(mycanvas1).move_by_offset(120,100)
    action.click_and_hold(mycanvas1).move_by_offset(120,140)
    action.click_and_hold(mycanvas1).move_by_offset(120,180)
    action.click_and_hold(mycanvas1).move_by_offset(120,120)
    action.click_and_hold(mycanvas1).move_by_offset(1200,20)
    action.click_and_hold(mycanvas1).move_by_offset(1200,60)
    action.click_and_hold(mycanvas1).move_by_offset(1200,100)
    action.click_and_hold(mycanvas1).move_by_offset(1200,140)
    action.click_and_hold(mycanvas1).move_by_offset(1200,180)
    action.click_and_hold(mycanvas1).move_by_offset(1200,120)
    action.click_and_hold(mycanvas1).move_by_offset(200,20)
    action.click_and_hold(mycanvas1).move_by_offset(200,60)
    action.click_and_hold(mycanvas1).move_by_offset(200,100)
    action.click_and_hold(mycanvas1).move_by_offset(200,140)
    action.click_and_hold(mycanvas1).move_by_offset(200,180)
    action.click_and_hold(mycanvas1).move_by_offset(200,120)
    action.click_and_hold(mycanvas1).release().perform()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[2]/img').click()
    driver.quit()
    return logid
def count():
  time.sleep(5)
  logid=guaguaka()
  time.sleep(8)
  tmpsql=mysql.tmpsql(logid)
  x=[]
  for i in tmpsql:
      x.append(mysql.myselect(i))
  return sum(x)
if __name__ == '__main__': 
  print count()