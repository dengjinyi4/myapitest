#coding:utf-8
#coding:utf-8#coding:utf-8
import time
print "=======================iphonex轮盘抽奖====================="
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from common import  mysql
def iphonexlunpan():
    chromedriver="C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe"
    driver = webdriver.Chrome(chromedriver)
    mobile_emulation = {"deviceName":"iPhone 6"}
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(chromedriver,chrome_options = chrome_options)
    driver.get('https://display.adhudong.com/site_login_ijf.htm?app_key=adhuc9166bbe0b034644&user_id=not_login&sign=58009fe7b8544e8422cc3892504d28d6')
    driver.maximize_window()
    logid=driver.current_url[65:83]
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div[2]').click()
    time.sleep(6)
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[6]/div/div/div[3]/div[3]/div[2]/button').click()
    time.sleep(5)
#   driver.back()
#   print"抽奖流程正常"
#

    
#    print logid
#    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[7]').click()
#    WebDriverWait(driver,20).until(lambda the_driver: the_driver.find_element_by_xpath('/html/body/section/div/ul/li/a/div[2]/p').is_displayed())
#    print "我的奖品信息展示正常"
#   driver.back()
#    driver.quit()
    return logid
def iphonexlunpancount():
  logid=iphonexlunpan()
  time.sleep(8)
  tmpsql=mysql.tmpsql(logid)
  x=[]
  for i in tmpsql:
      x.append(mysql.myselect(i))
#  return sum(x)
  return sum(x)
if __name__ == '__main__': 
   print iphonexlunpancount()   