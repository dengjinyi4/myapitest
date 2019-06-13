#!/usr/bin/env python
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os,time,datetime
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import requests as r
# 获取最终的地址
def geturlnew(url):
    # url='''http://p.yiqifa.com/c?s=8a74e411&w=880012&c=139&i=802&l=0&a=151&pf=y&e=123456&t=http://www.yhd.com/'''
    # url='''http://click.yhd.com/?ut=6258&s=ZmRjMTAzMjIxMDZlOWFkZDA3ZTQwNTQzNGQ0Y2I3MTIyMDFkOWY2M2ZlMzRmZTljZjQ3MTgyZjQzZjQxYmJlOQ==&cv=1&website_id=880012&uid=00qtb8a52666271433d6'''
    # resp=r.get(url,verify=False,allow_redirects=False)
    resp=r.get(url,allow_redirects=True)
    print resp.url
    return
# 返回L跳url，并把p.yiqifa.com替换成生产机器ip
def geturl(shengchanip,url):
    # url='''http://p.yiqifa.com/c?s=8a74e411&w=880012&c=139&i=802&l=0&a=151&pf=y&e=123456&t=http://www.yhd.com/'''
    # url='''http://click.yhd.com/?ut=6258&s=ZmRjMTAzMjIxMDZlOWFkZDA3ZTQwNTQzNGQ0Y2I3MTIyMDFkOWY2M2ZlMzRmZTljZjQ3MTgyZjQzZjQxYmJlOQ==&cv=1&website_id=880012&uid=00qtb8a52666271433d6'''
    resp=r.get(url,verify=False,allow_redirects=False)
    location=resp.headers['location']
    # 返回L跳url，并把p.yiqifa.com替换成生产机器ip
    url=location.replace('p.yiqifa.com',shengchanip)
    print url
    return url
# 滑动屏幕
def scrollTop(driver,step):
    js = "var q=document.body.scrollTop=%d"%step
    print js
    driver.execute_script(js)
    return
# 一号店成单，并返回订单。
def getyihaodianorder(url):
    chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver =  webdriver.Chrome(chromedriver)
    # driver.add_cookie({'name':'seus', 'value':'419U6D1VS16948UKD7GBA3D','domain':'.yhd.com'})
    driver.get(url)
    driver.maximize_window()
    # time.sleep(3)
    WebDriverWait(driver,20).until(lambda the_driver: the_driver.find_element_by_id("keyword").is_displayed())
    # 检查登录控件是否存在
    WebDriverWait(driver,20).until(lambda the_driver: the_driver.find_element_by_xpath('''//*[@id="global_top_bar_loginLink"]''').is_displayed())
    driver.find_element_by_xpath('''//*[@id="global_top_bar_loginLink"]''').click()
    # 检查登录框是否存在
    WebDriverWait(driver,30).until(lambda  t:t.find_element_by_xpath('''//*[@id="un"]''').is_displayed())
    driver.find_element_by_xpath('''//*[@id="un"]''').send_keys('13811501646')
    driver.find_element_by_xpath('//*[@id="pwd"]').send_keys('1111111')
    driver.find_element_by_id('login_button').click()
    # 再次等待搜索框加载完成
    WebDriverWait(driver,20).until(lambda the_driver: the_driver.find_element_by_id("keyword").is_displayed())
    # 登录后查询
    driver.find_element_by_id('keyword').send_keys(u'0')
    # 查询按钮
    driver.find_element_by_id('hdSearchBtn').click()
    time.sleep(3)
    # target=driver.find_element_by_id('buyButton_1055229')
    # driver.execute_script("arguments[0].scrollIntoView();", target)
    # js = "var q=document.body.scrollTop=500"
    # driver.execute_script(js)
    # 滑动页面
    scrollTop(driver,500)
    # 点击购买 选择第一个商品进行预订，进入商品详情页
    driver.find_elements_by_class_name('img')[0].click()
    # 立即抢购
    time.sleep(3)
    # 滑动页面
    scrollTop(driver,500)
    # 跳转到详情页”
    driver.switch_to_window(driver.window_handles[1])
    title=str(driver.title)
    print '购买到的商品是 %s'%title
    # 在详情页点击“加入购物车”
    # driver.find_element_by_class_name('buy_btn6').click()
    driver.find_element_by_id('buyButton').click()
    # 去购物车结算
    # WebDriverWait(driver,30).until(lambda the_driver: the_driver.find_element_by_class_name('settlement').is_displayed())
    # driver.find_element_by_class_name('settlement').click()
    # 去结算
    WebDriverWait(driver,30).until(lambda the_driver: the_driver.find_element_by_class_name('checkout_btn').is_displayed())
    driver.find_element_by_class_name('checkout_btn').click()
    # 提交订单
    WebDriverWait(driver,30).until(lambda the_driver: the_driver.find_element_by_xpath('//*[@id="SellCountFixBox"]/div[2]/button').is_displayed())
    # driver.find_element_by_class_name('btSubOrder1').click()
    driver.find_element_by_xpath('//*[@id="SellCountFixBox"]/div[2]/button').click()
    # 获取订单
    WebDriverWait(driver,30).until(lambda the_driver: the_driver.find_element_by_xpath('//*[@id="comParamId"]/div[4]/div[1]/div[1]/p[1]/a').is_displayed())
    yhdorder=str(driver.find_element_by_xpath('//*[@id="comParamId"]/div[4]/div[1]/div[1]/p[1]/a').text)
    print '函数内部打印，一号店订单为:%s'%yhdorder
    driver.close()
    driver.quit()
    return yhdorder

if __name__ == '__main__':
    url='''http://p.yiqifa.com/c?s=8a74e411&w=880012&c=139&i=802&l=0&a=151&pf=y&e=123456&t=http://www.yhd.com/'''
    url=geturl('123.59.17.77:19200',url)
    # print url
    # geturlnew()
    getyihaodianorder(url)