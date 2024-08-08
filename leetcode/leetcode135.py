#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/18 18:51
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode135.py
# @Software: PyCharm
"""

135. 分发糖果
困难
相关标签
相关企业

n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。

你需要按照以下要求，给这些孩子分发糖果：

    每个孩子至少分配到 1 个糖果。
    相邻两个孩子评分更高的孩子会获得更多的糖果。

请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。



示例 1：

输入：ratings = [1,0,2]
输出：5
解释：你可以分别给第一个、第二个、第三个孩子分发 2、1、2 颗糖果。

示例 2：

输入：ratings = [1,2,2]
输出：4
解释：你可以分别给第一个、第二个、第三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这满足题面中的两个条件。
"""


class Solution(object):
    def candy(self, ratings):
        length = len(ratings)
        candy = [1] * length
        for i in range(1, length):
            if ratings[i - 1] < ratings[i] and candy[i - 1] >= candy[i]:
                candy[i] = candy[i - 1] + 1
            elif ratings[i - 1] > ratings[i] and candy[i - 1] <= candy[i]:
                candy[i - 1] = candy[i] + 1

        for i in reversed(range(1, length)):
            if ratings[i - 1] < ratings[i] and candy[i - 1] >= candy[i]:
                candy[i] = candy[i - 1] + 1
            elif ratings[i - 1] > ratings[i] and candy[i - 1] <= candy[i]:
                candy[i - 1] = candy[i] + 1

        return sum(candy)


s = Solution()
print(s.candy([1, 0, 2]))
print(s.candy([1, 2, 2]))
