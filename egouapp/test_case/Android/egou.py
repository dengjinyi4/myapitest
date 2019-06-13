#coding=utf-8
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
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
# desired_caps['app']=PATH(r'D:\work\auto\sc\app-auto.apk')
# desired_caps['deviceName'] = 'emulator-5554'
desired_caps['deviceName'] = '81GEBN3222JX'
desired_caps['appPackage'] = 'com.emar.egou'
desired_caps['appActivity'] = 'com.egou.activity.SplashActivity'
# desired_caps['appActivity'] = 'com.egou.activity.activity.MainActivity'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
WebDriverWait(driver,20).until(lambda the_driver: the_driver.find_element_by_id("com.emar.egou:id/ad_icon1").is_displayed())
driver.find_element_by_id('com.emar.egou:id/ad_icon1').click()
WebDriverWait(driver,20).until(lambda the_driver: the_driver.find_element_by_id("com.emar.egou:id/rrtab_left").is_displayed())
strtitle=driver.find_element_by_id('com.emar.egou:id/rrtab_left').text
print strtitle
if(strtitle==u'淘宝返利'):
    print 'find is ok'
driver.quit()


 