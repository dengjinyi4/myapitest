# encoding=utf-8
__author__ = 'aidinghua'
import time
print "===============收钱吧抽奖==============="
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from common import mysql
def shouqianba():
    chromedriver="C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe"
#    driver=webdriver.Chrome(chromedriver)
    mobile_emulation={"device_name":"iphone6"}
    chrome_options=Options()
 #   chrome_options.add_experimental_option("mobileEmulation",mobile_emulation)
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    driver=webdriver.Chrome(chromedriver,chrome_options=chrome_options)
    driver.get('https://display.adhudong.com/site_login_ijf.htm?app_key=adhuda64ff7c536945c0')
    driver.maximize_window()
    logid=driver.current_url[60:78]
    print logid

    time.sleep(2)
     #点击第一张图
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div[2]/ul/li[1]/div/div[1]').click()
    time.sleep(3)
    #    clickbuttoon=driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div[2]/ul/li[1]/div/div[2]/div[2]/div[2]')
    #    while clickbuttoon.is_displayed():
    #      print 111111111111
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div[2]/ul/li[1]/div/div[2]/div[3]').click()
    time.sleep(3)
    driver.back()
    #点击第二张图
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div[2]/ul/li[2]/div/div[1]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div[2]/ul/li[2]/div/div[2]/div[3]').click()
    time.sleep(3)
    driver.back()
    #点击第三张图
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div[2]/ul/li[3]/div/div[1]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div[2]/ul/li[3]/div/div[2]/div[3]').click()
    time.sleep(3)
    driver.back()
    #点击第四张图
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div[2]/ul/li[4]/div/div[1]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div[2]/ul/li[4]/div/div[2]/div[3]').click()
    time.sleep(3)
    driver.back()
    #点击第五张图
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div[2]/ul/li[5]/div/div[1]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div[2]/ul/li[5]/div/div[2]/div[3]').click()
    time.sleep(3)
    driver.back()
    #点击第六张图
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div[2]/ul/li[6]/div/div[1]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div[2]/ul/li[6]/div/div[2]/div[3]').click()
    time.sleep(3)
    driver.back()
    return logid

def shouqianbacount():
    logid=shouqianba()
    tmpsql=mysql.tmpsql(logid)
    x=[]
    for i in tmpsql:
        x.append(mysql.myselect(i))

    return sum(x)

if __name__=='__main__':

    print shouqianbacount()
