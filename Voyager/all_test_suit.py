#encoding:utf-8
"Combine tests for gnosis.xml.objectify package (req 2.3+)"
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append("test_case")
import unittest, doctest
import test_case.unittestparamnew.addun as addun
#这里需要导入测试文件
import HTMLTestRunner
import allcase_list
import Emar_SendMail_Attachments
def autosuite(method):
    tmpsuite=unittest.TestSuite()
    tmpsuite.addTest(addun.myclass(method))
    print type(tmpsuite)
    return tmpsuite
def runtestcase(suite):
    t = time.strftime('%Y-%m-%d-%H-%M',time.localtime(time.time()))
    filename = 'D:/work/auto/Voyager/report/Report%s.html' %(t)
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='Report_title',
        description='Report_description')
    myresult=runner.run(suite)
    fp.close()
    sendfilename='D:/work/auto/Voyager/report/Report%s.html'%t
    # to_list=['dengjinyi@emar.com','aidinghua@emar.com','wangzhanyu@emar.com','mashilong@emar.com','chaobin@emar.com','jishenghui@emar.com']
    to_list=['dengjinyi@emar.com']
    Emar_SendMail_Attachments.sendTestreport(sendfilename,to_list,'egouapp自动化测试报告','测试报告')
if __name__ == '__main__':
    x=autosuite('testadd2')
    # print type(x)
    runtestcase(x)
    # suite = unittest.TestSuite()
    # suite.addTest(addun.myclass('testadd2'))
    # t = time.strftime('%Y-%m-%d-%H-%M',time.localtime(time.time()))
    # filename = 'D:/work/auto/Voyager/report/Report%s.html' %(t)
    # fp = file(filename, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     title='Report_title',
    #     description='Report_description')
    # myresult=runner.run(suite)
    # fp.close()
    # sendfilename='D:/work/auto/Voyager/report/Report%s.html'%t
    # # to_list=['dengjinyi@emar.com','aidinghua@emar.com','wangzhanyu@emar.com','mashilong@emar.com','chaobin@emar.com','jishenghui@emar.com']
    # to_list=['dengjinyi@emar.com']
    # Emar_SendMail_Attachments.sendTestreport(sendfilename,to_list,'egouapp自动化测试报告','测试报告')
































