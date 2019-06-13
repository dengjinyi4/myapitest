#encoding:utf-8

"Combine tests for gnosis.xml.objectify package (req 2.3+)"

import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append("test_case")
import unittest, doctest
#这里需要导入测试文件

import HTMLTestRunner
import allcase_list
import Emar_SendMail_Attachments


#将用例组建成数组
alltestnames = allcase_list.caselist()

suite = unittest.TestSuite()

if __name__ == '__main__':
	# 这里我们可以使用defaultTestLoader.loadTestsFromNames(),
	# 但如果不提供一个良好的错误消息时，它无法加载测试
	# 所以我们加载所有单独的测试，这样将会提高脚本错误的确定。
	for test in alltestnames:
		try:
			#最关键的就是这一句，循环执行数据行中的用例。
			# suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test))
			suite.addTests(unittest.TestLoader().loadTestsFromName(test))
		except Exception , e:
			print 'ERROR: Skipping tests from "%s".' %test
			print 1111111111111
			print e.message
			print 222222222222

			try:
				__import__(test)
			except ImportError as e1:
				print 'Could not import the test moudle.'
				print e1.message
			else:
				print 'Could not load the test suite.'
			from traceback import print_exc
			print_exc()
	print
	print 'Runnint the tests...'

# suite = doctest.DocTestSuite()
# suite.addTest(unittest.makeSuite(demotest.Test))
# suite.addTest(unittest.makeSuite(test_Cridetcard.Testcard))

t = time.strftime('%Y-%m-%d-%H-%M',time.localtime(time.time()))
filename = 'D:/work/auto/Voyager/report/Report%s.html' %(t)
fp = file(filename, 'wb')

runner = HTMLTestRunner.HTMLTestRunner(
	stream=fp,
	title='Report_title',
	description='Report_description')
myresult=runner.run(suite)

# print myresult.__dict__
# print myresult.success_count
# print myresult.failure_count
# print myresult.error_count
# print myresult._previousTestClass
# tmp=str(myresult._previousTestClass)[8:]
# print tmp.replace('\'>','')


fp.close()
sendfilename='D:/work/auto/Voyager/report/Report%s.html'%t
to_list=['dengjinyi@emar.com','aidinghua@emar.com','wanglanqing@emar.com','zhaoyu1@emar.com','wangzhanyu@emar.com','chaobin@emar.com','jishenghui@emar.com']
# to_list=['dengjinyi@emar.com']
if myresult.failure_count>1:
	Emar_SendMail_Attachments.sendTestreport(sendfilename,to_list,'互动推线上接口检查自动化测试报告','测试报告')

































