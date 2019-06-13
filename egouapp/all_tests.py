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
			suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test))
		except Exception:
			print 'ERROR: Skipping tests from "%s".' %test

			try:
				__import__(test)
			except ImportError:
				print 'Could not import the test moudle.'
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
filename = 'report/Report%s.html' %(t)
fp = file(filename, 'wb')

runner = HTMLTestRunner.HTMLTestRunner(
	stream=fp,
	title='Report_title',
	description='Report_description')
runner.run(suite)
fp.close()
sendfilename='./report/Report%s.html'%t
to_list=['dengjinyi@emar.com']
Emar_SendMail_Attachments.sendTestreport(sendfilename,to_list,'egouapp自动化测试报告','测试报告')
































