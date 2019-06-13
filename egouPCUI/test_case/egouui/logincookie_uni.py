#!/usr/bin/env python
#encoding: utf-8
# from appium import webdriver

import unittest
import os,time,requests
from selenium import webdriver

class mytest(unittest.TestCase):
    
    ##初始化工作
    def mywebdriver(self):
        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        driver =  webdriver.Chrome(chromedriver)
        driver.get("http://www.egou.com/")
        driver.set_page_load_timeout(5)
        driver.delete_all_cookies()
        driver.add_cookie({'name':'egouUser', 'value':'dTE0Njg1NDMzNzg2MzcvLzg0NmRiMDViZmMwOTZkN2YwODYzMDZhZDBiOTQ2NTBhLy85NTg5NDI4Ly8vLzFlYzAwNjM%3D','domain':'.egou.com'})
        return driver
    def myegou_order(self,url,elementxpath):
        driver=self.mywebdriver()
        driver.set_page_load_timeout(20)
        try:
            driver.get(url)
            time.sleep(5)
            tmp=driver.find_element_by_xpath(elementxpath).text
        except Exception,e:
            print "访问url找不到指定的元素:%s"%e.message
        print(driver.current_url)
        driver.close()
        return tmp

    #退出清理工作
    def tearDown(self):
        pass
    #具体的测试用例，一定要以test开头
    def testmyegouorder(self):
    	'''进入http://my.egou.com/order.htm 页面检查订单列表中返利详情是否显示'''
        gouwufanli=self.myegou_order('http://my.egou.com/order.htm','/html/body/div[5]/div[4]/div[6]/div[1]/div[2]/div[1]/p[5]/a')
        self.assertEqual(gouwufanli, u'返利详情')


if __name__ =='__main__':

    unittest.main()
	#testunit = unittest.TestSuite()