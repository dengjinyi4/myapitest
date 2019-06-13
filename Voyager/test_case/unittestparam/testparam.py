# encoding: utf-8
import unittest,hdtapi,sys
import logging
from parameterized import  parameterized,param
from test_case.hdtapi_business.utils.common_log import *
reload(sys)
sys.setdefaultencoding('utf8')


# def custom_name_func(testcase_func, param_num, param):
#     x = parameterized.to_safe_name("_".join(str(x) for x in param.args))
#     print("%s_%s_%s" % (
#         testcase_func.__name__,
#         parameterized.to_safe_name(str(param.args[0])),
#         parameterized.to_safe_name('sss')
#     )
#           )
#     return "%s_%s_%s" %(
#         testcase_func.__name__,
#         parameterized.to_safe_name(str(param.args[0])),
#         parameterized.to_safe_name('sss')
#     )


# class TestAdd(unittest.TestCase):
#     @parameterized.expand(hdtapi.initparam())
#     def test_demand(self, casename, expected, param_type, Actual):
#         # '''点击抽奖接口：验证返回字段是否正确'''
#         if str(param_type)=='A':
#             # print(Actual, expected)
#             #预期结果, 实际结果
#             self.assertEqual(str(expected), str(Actual))
#
#         elif str(param_type) == 'B':
#             expected_re = expected.split(',')
#             for item in Actual:
#                 self.assertIn(item, expected_re)
#
#         elif str(param_type) == 'C':
#             self.assertEqual(int(expected), int(Actual))
class adreport(unittest.TestCase):
    @parameterized.expand(hdtapi.cmp_cases(1))
    def test_cmp_cases(self,casename, expected, param_type, Actual):
        self.assertLessEqual(int(Actual), int(expected))




if __name__ == '__main__':
    unittest.main()
    # TestAdd.test_demand.__doc__
