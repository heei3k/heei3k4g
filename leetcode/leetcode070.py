#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/26 19:13
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode070.py
# @Software: PyCharm
"""
70. 爬楼梯
已解答
简单
相关标签
相关企业
提示

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？



示例 1：

输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶

示例 2：

输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶



提示：

    1 <= n <= 45


"""
from leetcode.costTime import cost_time


class Solution(object):
    @cost_time
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        result = [0 for _ in range(n)]
        result[0] = 1
        result[1] = 2
        for i in range(2, n):
            result[i] = result[i - 1] + result[i - 2]
        return result[-1]

    @cost_time
    def climbStairs2(self, n):
        square = 5 ** 0.5
        fibN = pow((1 + square) / 2, n + 1) - pow((1 - square) / 2, n + 1)
        return round(fibN / square)


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(44))
    print(s.climbStairs2(44))
