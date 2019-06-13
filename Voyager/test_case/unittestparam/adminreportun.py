# encoding: utf-8
import unittest,hdtapi,sys
import logging
from parameterized import  parameterized,param
from test_case.hdtapi_business.utils.common_log import *
reload(sys)
sys.setdefaultencoding('utf8')

class daminreport(unittest.TestCase):
    @parameterized.expand(hdtapi.cmp_cases(1))
    def test_cmp_cases(self,casename, expected, param_type, Actual):
        self.assertLessEqual(int(Actual), int(expected))


if __name__ == '__main__':
    unittest.main()
    # TestAdd.test_demand.__doc__
