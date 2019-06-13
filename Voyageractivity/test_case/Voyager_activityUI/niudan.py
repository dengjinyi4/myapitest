#coding:utf-8
#coding:utf-8#coding:utf-8
import time
print "=======================扭蛋抽奖====================="
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from common import  mysql
def niudan():
    chromedriver="C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe"
    driver = webdriver.Chrome(chromedriver)
    mobile_emulation = {"deviceName":"iPhone 6"}
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(chromedriver,chrome_options = chrome_options)
    driver.get('https://display.adhudong.com/site_login_ijf.htm?app_key=adhu63e1ad45bd0a4305&user_id=not_login&sign=e843c3225320017139edc402953a1f6c')
    driver.maximize_window()
    logid=driver.current_url[60:78]
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[5]').click()
    time.sleep(6)
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[4]/div/div[2]/div[2]/img').click()
    time.sleep(5)
#   driver.back()
#   print"抽奖流程正常"
    time.sleep(2)
#

    
#    print logid
#    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[7]').click()
#    WebDriverWait(driver,20).until(lambda the_driver: the_driver.find_element_by_xpath('/html/body/section/div/ul/li/a/div[2]/p').is_displayed())
#    print "我的奖品信息展示正常"
#   driver.back()
#    driver.quit()
    return logid
def niudancount():
  logid=niudan()
  time.sleep(8)
  tmpsql=mysql.tmpsql(logid)
  x=[]
  for i in tmpsql:
      x.append(mysql.myselect(i))
#  return sum(x)
  return sum(x)
if __name__ == '__main__': 
    
   print niudancount()   