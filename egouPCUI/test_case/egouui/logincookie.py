#!/usr/bin/env python
# encoding: utf-8
import os,time,requests
from selenium import webdriver
def mywebdriver():
    chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver =  webdriver.Chrome(chromedriver)
    driver.get("http://www.egou.com/")
    driver.set_page_load_timeout(5)
    driver.delete_all_cookies()
    driver.add_cookie({'name':'egouUser', 'value':'dTE0Njg1NDMzNzg2MzcvLzg0NmRiMDViZmMwOTZkN2YwODYzMDZhZDBiOTQ2NTBhLy85NTg5NDI4Ly8vLzFlYzAwNjM%3D','domain':'.egou.com'})
    return driver
def myegou(url,elementxpath):
    driver=mywebdriver()
    driver.set_page_load_timeout(20)
    try:
        driver.get(url)
        tmp=driver.find_element_by_xpath(elementxpath).text
    except Exception,e:
        print e.message
        print 'This is error:'
    # time.sleep(5)
    # print(driver.current_url)
    driver.close()
    return tmp
if __name__ == '__main__':
    fanlixiangqingg=myegou('http://my.egou.com/order.htm','/html/body/div[5]/div[4]/div[6]/div[1]/div[2]/div[1]/p[5]/a')

    print fanlixiangqingg