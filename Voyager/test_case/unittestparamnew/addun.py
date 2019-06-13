#!/usr/bin/env python
# encoding: utf-8
import unittest
import add
newid=None
class myclass(unittest.TestCase):
    # def __init__(self):
    #     globals()['newid']=11
    def testadd1(self):
        global newid
        print newid
        self.assertEqual(int(add.myadd(1,3)),4)
    def testadd2(self):
        self.assertEqual(int(add.myadd(1,3)),4)
# if __name__ == '__main__':
#     testsuite=unittest.TestSuite()
#     testsuite.addTest(myclass('testadd2'))
#     # testsuite.addTest(myclass('testadd1'))
#     runner=unittest.TextTestRunner(verbosity=2)
#     runner.run(testsuite)
    # unittest.main()