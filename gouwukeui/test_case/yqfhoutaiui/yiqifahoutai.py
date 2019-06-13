#!/usr/bin/env python
# encoding: utf-8
import os,time,requests,datetime
from selenium import webdriver
def yesterday():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=7)
    print type(yesterday)
    return yesterday
def getweek():
    d = datetime.datetime.now()
    dayscount = datetime.timedelta(days=d.isoweekday())
    dayto = d - dayscount
    sixdays = datetime.timedelta(days=6)
    dayfrom = dayto - sixdays
    date_from = datetime.datetime(dayfrom.year, dayfrom.month, dayfrom.day, 0, 0, 0)
    date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23, 59, 59)
    # date_from = datetime.datetime(dayfrom.year, dayfrom.month, dayfrom.day, 0, 0, 0)
    # date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23, 59, 59)
    # return str(date_from)[0:10],str(date_to)[0:10]
    return date_from
def getweeknew():
    d = datetime.datetime.now()
    dayscount = datetime.timedelta(days=d.isoweekday())
    dayto = d - dayscount
    sixdays = datetime.timedelta(days=6)
    dayfrom = dayto - sixdays
    date_from = datetime.datetime(dayfrom.year, dayfrom.month, dayfrom.day, 0, 0, 0)
    tmplist=[]
    for i in range(0,7,1):
        tmpdate_from=date_from+datetime.timedelta(days=i)
        tmplist.append(str(tmpdate_from)[0:10])
        print tmplist[i]
    return tmplist
def mywebdriver():
    chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver =  webdriver.Chrome(chromedriver)
    driver.get("https://admin.yiqifa.com/mgrLoginForm.do")
    driver.set_page_load_timeout(5)
    driver.find_element_by_id('userName').clear()
    driver.find_element_by_id('userName').send_keys('dengjinyi')
    driver.find_element_by_name('password').clear()
    driver.find_element_by_name('password').send_keys('123456')
    driver.find_element_by_id('loginbtn').click()
    return driver
def yqfcpsordershishihuizong(campaignId):
    driver=mywebdriver()
    driver.set_page_load_timeout(30)
    listweek=getweeknew()
    cpshuizonglist=[]
    cpsmingxilist=[]
    for fr in listweek:
        try:
            driver.get('https://admin.yiqifa.com/mgrSimpleCpsReport.do')
            time.sleep(5)
            # 查找前一个自然周的数据,查询当天的时间
            endDatejs="$(\"input[name='endDate']\").removeAttr('readonly');$(\"input[name='endDate']\").attr('value','"+fr+"')"
            startDatejs="$(\"input[name='startDate']\").removeAttr('readonly');$(\"input[name='startDate']\").attr('value','"+fr+"')"
            driver.execute_script(startDatejs)
            driver.execute_script(endDatejs)
            driver.find_element_by_id('campaignId').clear()
            driver.find_element_by_id('campaignId').send_keys(campaignId)
            driver.find_element_by_name('Submit2').click()
            time.sleep(3)
            # cps汇总页面  收订订单额
            cpsmingxi=driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[2]/td[10]').text
            driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[1]/td[24]/a').click()
            time.sleep(2)
            # CPS订单明细页面  收订订单额
            cpshuizong=driver.find_element_by_xpath('/html/body/center/div/table/tbody/tr[21]/td[14]').text
            time.sleep(2)
        except Exception,e:
            print "访问url找不到指定的元素:%s"%e.message
        print(driver.current_url)

        # print '活动:%s，CPS订单实时汇总页面 收订订单额是:%sCPS订单明细页面 收订订单额是:%s'%(campaignId,cpshuizong,cpsmingxi)
        print '查询开始日期：',fr,'查询结束日期：',fr,'活动: ',campaignId,'\n汇总数据转换前 CPS订单实时汇总页面 收订订单额是:',cpshuizong,'\nCPS订单明细页面 收订订单额是:',cpsmingxi
        # ￥2,355,303.07 转换成 2355303
        cpshuizong=cpshuizong[1:]
        cpshuizong=cpshuizong.split('.')[0]
        cpshuizong=cpshuizong.replace(',','')
        cpshuizonglist.append(cpshuizong)
        # ￥2355303.30 转换成 2355303
        cpsmingxi=cpsmingxi[1:].split('.')[0]
        cpsmingxilist.append(cpsmingxi)
        chae=int(cpshuizong)-int(cpsmingxi)
        print '活动: ',campaignId,'\n汇总数据转换后 CPS订单实时汇总页面 收订订单额是:',cpshuizong,'CPS订单明细页面 收订订单额是:',cpsmingxi,'\n数据相差:',chae,'\n\n'
    driver.close()
    return cpshuizonglist,cpsmingxilist

if __name__ == '__main__':
    # (cpshuizong,cpsmingxi)=yqfcpsordershishihuizong(254)
    # rrr=￥2263476.06
    # print cpsmingxi,cpshuizong
    # if (cpshuizong==cpsmingxi):
    #     print 111111100000000000
    week=getweeknew()
    print week



