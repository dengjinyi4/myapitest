#!/usr/bin/env python
#encoding: utf-8
import unittest,add
class addtest(unittest.TestCase):


    #具体的测试用例，一定要以test开头
    def test_add01(self):
        '''1+3=4'''
        print 'abcdE'
        self.assertEqual(add.add(1,113), 14)

    def test_add02(self):
        '''1+2=3'''
        self.assertEqual(add.add(1,2),3)
if __name__ =='__main__':
    unittest.main()
