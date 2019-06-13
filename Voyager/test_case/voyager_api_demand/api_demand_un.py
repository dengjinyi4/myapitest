# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 16:09
# @Author  : wanglanqing

import unittest
from parameterized import parameterized
from .api_demand import initparam


class DemandSuite(unittest.TestCase):
    @parameterized.expand(initparam())
    def test_demand(self, casename, expected, param_type, Actual):
        # '''点击抽奖接口：验证返回字段是否正确'''
        if str(param_type)=='A':
            # print(Actual, expected)
            #预期结果, 实际结果
            self.assertEqual(str(expected), str(Actual))

        elif str(param_type) == 'B':
            expected_re = expected.split(',')
            for item in Actual:
                self.assertIn(item, expected_re)

        elif str(param_type) == 'C':
            self.assertEqual(int(expected), int(Actual))