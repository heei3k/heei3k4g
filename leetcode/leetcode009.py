#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/26 20:05
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode009.py
# @Software: PyCharm
"""
9. 回文数
已解答
简单
相关标签
相关企业
提示

给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数
是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

    例如，121 是回文，而 123 不是。



示例 1：

输入：x = 121
输出：true

示例 2：

输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3：

输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数。



提示：

    -231 <= x <= 231 - 1



进阶：你能不将整数转为字符串来解决这个问题吗？

"""
from leetcode.costTime import cost_time


class Solution(object):
    @cost_time
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        length = len(str_x)
        haf = length // 2
        for i in range(haf):
            if str_x[i] != str_x[length - 1 - i]:
                return False
        return True

    @cost_time
    def isPalindromeOffice(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        revertedNumber = 0
        while revertedNumber < x:
            revertedNumber = revertedNumber * 10 + x % 10
            x = x // 10
        return x == revertedNumber or x == revertedNumber // 10


if __name__ == '__main__':
    solution = Solution()
    # print(solution.isPalindrome(121))
    # print(solution.isPalindrome(-121))
    # print(solution.isPalindrome(10))
    # print(solution.isPalindrome(10002001))
    print(solution.isPalindrome(12344321))
    print(solution.isPalindromeOffice(12344321))
