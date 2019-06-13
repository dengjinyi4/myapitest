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
    for m in range(10):
        mobile_emulation = {"deviceName":"iPhone 6"}
        chrome_options = Options()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        chromedriver="C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe"
        driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
        url='http://display.eqigou.com/site_login_ijf.htm?app_key=adhu96062b9a717e48ed'
        driver.get(url)
        driver.maximize_window()
        logid=driver.current_url[60:78]
        print "adzone_click_id:"+logid
        print'\n'
        print '访问的地址是:'+url
        for i in range(7):
            time.sleep(10)
            driver.find_element_by_xpath('//*[@id="lottery-wrapper"]/div[1]').click()
            time.sleep(10)
            current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            pic_path = 'd:\\pics\\' + str(m) + '_' + str(i)+ '.png'
            driver.get_screenshot_as_file(pic_path)
            driver.refresh()
            # driver.find_element_by_xpath('/html/body/div[2]/div/div[1]').click()
            time.sleep(5)
            i +=1
        driver.quit()
        m+=1
    return logid
def jiugonggecount():
      logid=jiugongge()
      tmpsql=mysql.tmpsql(logid)
      x=[]
      for i in tmpsql:
          x.append(mysql.myselect(i))
    #  return sum(x)
      return sum(x)
if __name__ == '__main__':
    print jiugongge()