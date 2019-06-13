#coding:utf-8
print "########################新轮盘抽奖##########################"
import os 
import sys
import time 
import datetime
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from common import  mysql
from selenium.webdriver.common.keys import Keys

def xinlunpan():
    chromedriver="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    driver = webdriver.Chrome(chromedriver)
    mobile_emulation = {"deviceName":"iPhone 6"}  
    chrome_options = Options()  
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)  
    driver = webdriver.Chrome(chromedriver,chrome_options = chrome_options) 
    driver.get('https://display.adhudong.com/site_login_ijf.htm?app_key=adhu6fdc510f87524780&user_id=not_login&sign=fa2aff9c0dcb3d007e5343330c66d917')
    driver.maximize_window()    
    time.sleep(1)    
    driver.find_element_by_xpath('/html/body/section/div[2]/div[2]/div/div[3]').click()
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/section/div[6]/div/div/div[3]/div[3]/div/button').click()
    time.sleep(2)
    driver.back()
    print"抽奖流程正常"
    
    logid=driver.current_url[61:79]
    driver.find_element_by_xpath('/html/body/section/div[1]/a[1]').click()
    WebDriverWait(driver,20).until(lambda the_driver: the_driver.find_element_by_xpath('/html/body/section/div/ul/li[1]/a/div[2]/p').is_displayed())
    print "我的奖品信息展示正常"
    driver.back()
    
    time.sleep(3)
    def expectdata1(host,database,user,password,port,sql):
       mysql.connectdb(host,database,user,password,port)
       result=mysql.selete(sql)
       mysql.closeconnect()
       return result[0][0]
    def expectdata2(host,database,user,password,port,sql):
       mysql.connectdb(host,database,user,password,port)
       result=mysql.insertdb(sql)
       mysql.closeconnect()
    host = '221.122.127.183'
    port = 5701
    database = 'voyager'
    user = 'voyager'
    password = 'voyager'
    date=datetime.datetime.now().strftime("%Y%m%d")
    sql1= "SELECT count(1) FROM voyagerlog.ad_click_log"+date+" where adzone_click_id ='"+logid+"'"
    sql2= "SELECT count(1) FROM voyagerlog.ad_show_log"+date+" where adzone_click_id ='"+logid+"'"
    sql3= "SELECT count(1) FROM voyagerlog.adzone_click_log"+date+" where adzone_click_id ='"+logid+"'"
    sql4= "SELECT count(1) FROM voyagerlog.lottery_click_log"+date+" where adzone_click_id ='"+logid+"'"
    sql5= "insert into `tmp_activity` (`id`, `act_type`, `act_name`, `status`, `create_time`) values('6','6','新轮盘抽奖','1',current_time);"
    sql6= "insert into `tmp_activity` (`id`, `act_type`, `act_name`, `status`, `create_time`) values('6','6','新轮盘抽奖','0',current_time);"
        
    adclick=expectdata1(host,database,user,password,port,sql1) 
    adshow=expectdata1(host,database,user,password,port,sql2)
    adzone_click=expectdata1(host,database,user,password,port,sql3)
    lottery_click=expectdata1(host,database,user,password,port,sql4) 
    
    if adclick==1 and adshow==1 and adzone_click==1 and lottery_click==1:
       print"新轮盘抽奖活动日志正常"
       expectdata2(host,database,user,password,port,sql5)
    else:
       print "新轮盘抽奖活动日志异常"
       expectdata2(host,database,user,password,port,sql6)
    driver.quit()     

xinlunpan()    
