# encoding: utf-8
# coding=gbk
import os,time,datetime,re
import mydriverpath
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
def mywebdriver():
    chromedriver = mydriverpath.drvierpath()
    # chromedriver = r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver =  webdriver.Chrome(chromedriver)
    driver.get("http://172.16.17.213:19100/mgrLoginForm.do")
    # driver.set_page_load_timeout(5)
    WebDriverWait(driver,30).until(lambda the_driver: the_driver.find_element_by_id('userName').is_displayed())
    WebDriverWait(driver,30).until(lambda the_driver: the_driver.find_element_by_name('password').is_displayed())

    driver.find_element_by_id('userName').clear()
    driver.find_element_by_id('userName').send_keys('admin')
    driver.find_element_by_name('password').clear()
    driver.find_element_by_name('password').send_keys('123456')
    time.sleep(3)
    driver.find_element_by_id('loginbtn').click()
    return driver
def jifeilianjiemi(driver,yiqifaurl):
    time.sleep(3)
    driver.get('http://172.16.17.213/mgrMonitorLinkDecode.do')
    WebDriverWait(driver,30).until(lambda the_driver: the_driver.find_element_by_name('linkName').is_displayed())
    driver.find_element_by_name('linkName').clear()
    driver.find_element_by_name('linkName').send_keys(yiqifaurl)
    driver.find_element_by_id('searchBtn').click()
    driver.switch_to_active_element()
    campainid=str(driver.find_element_by_xpath('''//*[@id="searchForm"]/table/tbody/tr/td/table[2]/tbody/tr[2]/td[1]''').text)
    websiteid=str(driver.find_element_by_xpath('''//*[@id="searchForm"]/table/tbody/tr/td/table[2]/tbody/tr[2]/td[2]''').text)
    linkid=str(driver.find_element_by_xpath('''//*[@id="searchForm"]/table/tbody/tr/td/table[2]/tbody/tr[2]/td[3]''').text)
    Advertiserid=str(driver.find_element_by_xpath('''//*[@id="searchForm"]/table/tbody/tr/td/table[2]/tbody/tr[2]/td[4]''').text)
    transactionid=str(driver.find_element_by_xpath('''//*[@id="searchForm"]/table/tbody/tr/td/table[2]/tbody/tr[2]/td[5]''').text)
    pingtaibiaoshi=str(driver.find_element_by_xpath('''//*[@id="searchForm"]/table/tbody/tr/td/table[2]/tbody/tr[2]/td[6]''').text)
    print '活动id：%s,站点id：%s,链接id：%s,广告主id:%s,交易id：%s，平台标识：%s'%(campainid,websiteid,linkid,Advertiserid,transactionid,pingtaibiaoshi)
    driver.close()
    driver.quit()
    return (campainid,websiteid,linkid,Advertiserid,transactionid,pingtaibiaoshi)
if __name__ == '__main__':
    mydriver=mywebdriver()
    (campainid,websiteid,linkid,Advertiserid,transactionid,pingtaibiaoshi)=jifeilianjiemi(mydriver,'https://p.yiqifa.com/n?k=UZMWD748rI6H1NW7WmLErI6H2mLErntl1QLF6ltl6EBHWNKqrI6H3cLErnDlWE276nb9rIW-&e=123456&t=https://www.yhd.com/product/index.do')
    print type(campainid)
    # print 1