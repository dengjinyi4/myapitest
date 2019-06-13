#coding:utf-8
print "========================套牛抽奖=============================="
import os
import sys
import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from common import mysql

def taoniu():
    chromedriver="C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe"
    driver=webdriver.Chrome(chromedriver)
    mobile_emulation={"device_name":"iphone 6"}
    chrome_options=Options()
    chrome_options.add_experimental_option("mobileEmulation",mobile_emulation)
    driver=webdriver.Chrome(chromedriver,chrome_options=chrome_options)
    driver.get("https://display.adhudong.com/site_login_ijf.htm?app_key=adhubed3e0325df74865&user_id=not_login&sign=332764ef3726490a8717df387bc4a8af")
    
    driver.maximize_window()
    logid=driver.current_url[57:75]
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[4]/div/button').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[10]/div/div[3]/div[2]/div[2]/img').click()
    time.sleep(5)
#    driver.back()
#    print "抽奖流程正常"

#    driver.find_element_by_xpath('//*[@id="root"]/div/div/button[2]').click()
#    WebDriverWait(driver,20).until(lambda the_driver: the_driver.find_element_by_xpath('/html/body/section/div/ul/li[1]/a/div[2]/p').is_displayed())
#    print "我的奖品正常"
#    driver.back()
    driver.quit()
    return logid


def taoniucount():
    logid=taoniu()
    time.sleep(8)
    tmpsql=mysql.tmpsql(logid)
    x=[]
    for i in tmpsql:
        x.append(mysql.myselect(i))
    # print sum(x)
    return sum(x)

if __name__=="__main__":
    print taoniucount()