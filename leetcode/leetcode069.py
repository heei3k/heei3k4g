#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/26 17:57
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode069.py
# @Software: PyCharm
"""
69. x 的平方根

给你一个非负整数 x ，计算并返回 x 的 算术平方根 。

由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。



示例 1：

输入：x = 4
输出：2

示例 2：

输入：x = 8
输出：2
解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。



提示：

    0 <= x <= 2147483647


"""
from jsonpath import xrange

from leetcode.costTime import cost_time


class Solution(object):
    @cost_time
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        length = len(str(x))
        div, mod = divmod(length, 2)
        # print(div,mod)
        lowBound, upBound = 1, 1
        if mod == 1:
            for _ in range(div):
                lowBound *= 10
        else:
            for _ in range(div - 1):
                lowBound *= 10
        upBound = lowBound * 10
        print(lowBound, upBound)
        for i in xrange(lowBound, upBound):
            if i * i > x:
                return i - 1
            elif i * i == x:
                return i
        return 0

    @cost_time
    def mySqrt2(self, x):
        if x == 0:
            return 0
        res, s = 0.0, float(x)
        while abs(res - s) >= 1e-1:
            res = (s + x / s) / 2
            s = (res + x / res) / 2
            # print(res)
            # print(s)
        return int(s)


if __name__ == '__main__':
    solution = Solution()
    print(solution.mySqrt(2147483647))
    print(solution.mySqrt2(2147483647))
