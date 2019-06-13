#!/usr/bin/env python
#encoding: utf-8
# from appium import webdriver
import os
import time
import unittest
# from selenium import webdriver
from time import sleep
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
PATH=lambda p:os.path.abspath(
os.path.join(os.path.dirname(__file__),p)
)


class mytest(unittest.TestCase):
    
    ##初始化工作
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'
        # desired_caps['app']=PATH(r'D:\work\auto\sc\app-auto.apk')
        # desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['deviceName'] = '81GEBN3222JX'
        desired_caps['appPackage'] = 'com.emar.egou'
        desired_caps['appActivity'] = 'com.egou.activity.SplashActivity'
        # desired_caps['appActivity'] = 'com.egou.activity.activity.MainActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        pass
    
    #退出清理工作
    def tearDown(self):
        self.driver.quit()
        pass
    '''获取屏幕xy值'''
    def getSize(self):
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        return (x, y)
    '''滑动'''
    def swipeUp(self,t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)    #x坐标
        y1 = int(l[1] * 0.75)   #起始y坐标
        y2 = int(l[1] * 0.05)   #终点y坐标
        self.driver.swipe(x1, y1, x1, y2,t)
    #具体的测试用例，一定要以test开头
    def testegouapptaobaofanli(self):
    	'''点击淘宝返利后跳转'''
        WebDriverWait(self.driver,20).until(lambda the_driver: the_driver.find_element_by_id("com.emar.egou:id/ad_icon1").is_displayed())
        self.driver.find_element_by_id('com.emar.egou:id/ad_icon1').click()
        WebDriverWait(self.driver,20).until(lambda the_driver: the_driver.find_element_by_id("com.emar.egou:id/rrtab_left").is_displayed())
        strtitle=self.driver.find_element_by_id('com.emar.egou:id/rrtab_left').text
        print strtitle+'\n'
        self.assertEqual(strtitle, u'淘宝返利')
    def testegouappshangchengfanli(self):
    	'''点击淘宝返利后跳转'''
        WebDriverWait(self.driver,20).until(lambda the_driver: the_driver.find_element_by_id("com.emar.egou:id/ad_icon2").is_displayed())
        self.driver.find_element_by_id('com.emar.egou:id/ad_icon2').click()
        WebDriverWait(self.driver,20).until(lambda the_driver: the_driver.find_element_by_id("com.emar.egou:id/rrtab_right").is_displayed())
        strtitle=self.driver.find_element_by_id('com.emar.egou:id/rrtab_right').text
        print strtitle+'\n'
        self.assertEqual(strtitle, u'商城返利')
    def testegouappshangchengfanlijingdong(self):
    	'''点击淘宝返利后跳转'''
        WebDriverWait(self.driver,20).until(lambda the_driver: the_driver.find_element_by_id("com.emar.egou:id/ad_icon2").is_displayed())
        self.driver.find_element_by_id('com.emar.egou:id/ad_icon2').click()
        WebDriverWait(self.driver,20).until(lambda the_driver: the_driver.find_element_by_id("com.emar.egou:id/rrtab_right").is_displayed())
        strtitle=self.driver.find_element_by_id('com.emar.egou:id/rrtab_right').text
        print strtitle+'\n'
        # self.driver.find_element_by_partial_link_text('返利可达5.6%').click()
        # WebDriverWait(self.driver,20).until(lambda the_driver: the_driver.find_element_by_id("com.emar.egou:id/h_top_title").is_displayed())

        # self.driver.find_element_by_xpath("//android.support.v4.view.ViewPager[3]/android.widget.FrameLayout[0]/android.widget.LinearLayout[0]/android.widget.FrameLayout[0]/android.widget.ScrollView[0]/android.widget.RelativeLayout[0]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[0]/android.widget.TextView[1]").click()

        self.driver.find_element_by_name('返利可达5.6%').click()
        # print el
        strtitle=self.driver.find_element_by_id('com.emar.egou:id/h_top_title').text
        print strtitle+'\n'
        self.assertEqual(strtitle, u'京东商城')
    def testegouappyouhuiquan(self):
    	'''点击优惠券后跳转'''
        WebDriverWait(self.driver,20).until(lambda the_driver: the_driver.find_element_by_id("com.emar.egou:id/ad_icon3").is_displayed())
        self.driver.find_element_by_id('com.emar.egou:id/ad_icon3').click()
        WebDriverWait(self.driver,20).until(lambda the_driver: the_driver.find_element_by_id("com.emar.egou:id/head_title").is_displayed())
        strtitle=self.driver.find_element_by_id('com.emar.egou:id/head_title').text
        print strtitle+'\n'
        self.assertEqual(strtitle, u'超级优惠券')
    def testegouappyizhemiaosha(self):
    	'''点击一折秒杀后跳转'''
        WebDriverWait(self.driver,20).until(lambda the_driver: the_driver.find_element_by_id("com.emar.egou:id/ad_icon4").is_displayed())
        self.driver.find_element_by_id('com.emar.egou:id/ad_icon4').click()
        WebDriverWait(self.driver,20).until(lambda the_driver: the_driver.find_element_by_id("com.emar.egou:id/head_title").is_displayed())
        strtitle=self.driver.find_element_by_id('com.emar.egou:id/head_title').text
        print strtitle+'\n'
        self.assertEqual(strtitle, u'1折秒杀')
    def testegouappxianshiqiang(self):
    	'''点击限时抢后跳转'''
        WebDriverWait(self.driver,20).until(lambda the_driver: the_driver.find_element_by_id("com.emar.egou:id/ll_home_ad_timer").is_displayed())
        self.driver.find_element_by_id('com.emar.egou:id/ll_home_ad_timer').click()
        WebDriverWait(self.driver,20).until(lambda the_driver: the_driver.find_element_by_id("com.emar.egou:id/head_title").is_displayed())
        strtitle=self.driver.find_element_by_id('com.emar.egou:id/head_title').text
        print strtitle+'\n'
        self.assertEqual(strtitle, u'限时抢购')
    def testegouappjiujiu(self):
    	'''点击9.9包邮后跳转'''
        WebDriverWait(self.driver,20).until(lambda the_driver: the_driver.find_element_by_id("com.emar.egou:id/img_ad_0").is_displayed())
        self.driver.find_element_by_id('com.emar.egou:id/img_ad_0').click()
        WebDriverWait(self.driver,20).until(lambda the_driver: the_driver.find_element_by_id("com.emar.egou:id/head_title").is_displayed())
        strtitle=self.driver.find_element_by_id('com.emar.egou:id/head_title').text
        print strtitle+'\n'
        self.assertEqual(strtitle, u'9.9包邮')
    def testegouapplingyuanchou(self):
    	'''点击0元抽后跳转'''
        WebDriverWait(self.driver,20).until(lambda the_driver: the_driver.find_element_by_id("com.emar.egou:id/img_ad_1").is_displayed())
        self.driver.find_element_by_id('com.emar.egou:id/img_ad_1').click()
        WebDriverWait(self.driver,20).until(lambda the_driver: the_driver.find_element_by_id("com.emar.egou:id/head_title").is_displayed())
        strtitle=self.driver.find_element_by_id('com.emar.egou:id/head_title').text
        strtitle=strtitle[:3]
        print strtitle[:3]+'\n'
        self.assertEqual(strtitle, u'0元抽')
        # self.assertTrue('true')
    def testegouappchaojiyouhuiqquan(self):
    	'''点击0元抽后跳转'''
        WebDriverWait(self.driver,20).until(lambda the_driver: the_driver.find_element_by_id("com.emar.egou:id/img_ad_2").is_displayed())
        self.driver.find_element_by_id('com.emar.egou:id/img_ad_2').click()
        WebDriverWait(self.driver,20).until(lambda the_driver: the_driver.find_element_by_id("com.emar.egou:id/head_title").is_displayed())
        strtitle=self.driver.find_element_by_id('com.emar.egou:id/head_title').text
        print strtitle+'\n'
        self.assertEqual(strtitle, u'超级优惠券')
    def testegouappzhupinghuadong(self):
    	'''滑动效果'''
        # 到达主屏，检查出现淘宝返利
        WebDriverWait(self.driver,20).until(lambda the_driver: the_driver.find_element_by_id("com.emar.egou:id/ad_icon1").is_displayed())
        # 向上滑动
        self.swipeUp(1000)
        WebDriverWait(self.driver,20).until(lambda the_driver: the_driver.find_element_by_id("com.emar.egou:id/item_name").is_displayed())
        strtitle=self.driver.find_element_by_id('com.emar.egou:id/item_name').text
        print strtitle+'\n'
        self.assertTrue(len(strtitle)>0)

if __name__ =='__main__':

    unittest.main()
	#testunit = unittest.TestSuite()