#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/8 18:11
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode172.py
# @Software: PyCharm
"""
172. 阶乘后的零

给定一个整数 n ，返回 n! 结果中尾随零的数量。

提示 n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1



示例 1：

输入：n = 3
输出：0
解释：3! = 6 ，不含尾随 0

示例 2：

输入：n = 5
输出：1
解释：5! = 120 ，有一个尾随 0

示例 3：

输入：n = 0
输出：0



提示：

    0 <= n <= 104

"""


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # result = 0
        return n // 5 + n // 25 + n // 125 + n // 625 + n // 3125

    def trailingZeroes2(self, n):
        count = 0
        while n // 5 > 0:
            count += n // 5
            n //= 5
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.trailingZeroes(125))
    print(s.trailingZeroes(20000))
    print(s.trailingZeroes2(125))
    print(s.trailingZeroes2(20000))
