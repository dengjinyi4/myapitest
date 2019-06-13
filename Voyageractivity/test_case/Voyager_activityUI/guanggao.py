#!/usr/bin/env python
# encoding: utf-8
# coding=gbk
import os,time,datetime,re,sys
import mydriverpath
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

# 返回一个距离当前日期days天前的一个j天数组

def mywebdriver():
    chromedriver = mydriverpath.drvierpath()
    # chromedriver = r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver =  webdriver.Chrome(chromedriver)
    driver.get("http://ijifen.egou.com/activity/100001.htm?app_key=ijfe070de45c9714350")
    driver.set_page_load_timeout(5)

    return driver
def do():
    d=mywebdriver()
    time.sleep(5)
    d.find_element_by_class_name('pointer').click()

    WebDriverWait(d,20).until(lambda the_driver: the_driver.find_element_by_xpath('//*[@id="lotterWin"]/div/div[2]/a/div[1]/img').is_displayed())
    d.find_element_by_xpath('//*[@id="lotterWin"]/div/div[2]/a/div[1]/img').click()
    d.quit()

if __name__ == '__main__':
    count=sys.argv[1]
    if count=='':
        count=1
    for i in range(0,int(count)):
        do()
        print '广告第%s次展现并点击'%i



