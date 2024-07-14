#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/26 20:43
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode066.py
# @Software: PyCharm
"""
66. 加一

给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。



示例 1：

输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

示例 2：

输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。

示例 3：

输入：digits = [0]
输出：[1]



提示：

    1 <= digits.length <= 100
    0 <= digits[i] <= 9


"""
from typing import List


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        res = 0
        for i in range(length):
            res = res * 10 + digits[i]
        res += 1
        length_new = len(str(res))
        result = [0 for _ in range(length_new)]
        for i in range(length_new):
            res, mod = divmod(res, 10)
            result[i] = mod
        result.reverse()
        return result

    def plusOneOffice(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                for j in range(i + 1, n):
                    digits[j] = 0
                return digits

        # digits 中所有的元素均为 9
        return [1] + [0] * n


if __name__ == '__main__':
    digits = [1, 9, 4]
    s = Solution()
    print(s.plusOneOffice(digits))
