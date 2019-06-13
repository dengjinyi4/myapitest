#!/usr/bin/env python
# encoding: utf-8
import os,time,datetime
from selenium import webdriver

def gouwukecomptime(hour,minute,tseconds):
    timedangqian=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    print timedangqian
    strshijian=timedangqian.split('-')
    d1=datetime.datetime(year=int(strshijian[0]),month=int(strshijian[1]),day=int(strshijian[2]),hour=int(hour),minute=int(minute),second=00)
    d2=datetime.datetime.now()
    seconds=int((d2-d1).seconds)
    print '购物客中的最新商品的时间：%s'%d1
    print '当前时间：%s'%d2
    print '购物客最新商品与当前时间间隔的秒数：%s'%seconds
    if seconds>tseconds:
        return False
    else:
        return True
def getgouwuke_haitao():
    chromedriver = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver =  webdriver.Chrome(chromedriver)
    # driver.maximize_window()
    driver.get("http://gouwuke.com/")
    # driver.refresh()
    mytime=driver.find_element_by_class_name('time').text
    driver.quit()
    return mytime

if __name__ == '__main__':
    mytime=getgouwuke_haitao()
    print mytime
    mytime=mytime.split(':')
    t=gouwukecomptime(int(mytime[0]),int(mytime[1]),3000)
    print t