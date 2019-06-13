# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
 
 
mobileEmulation = {'deviceName': 'Apple iPhone 4'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)
chromedriver="C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chromedriver, chrome_options=options)
 
driver.get('https://m.baidu.com')
 
sleep(3)
driver.close()