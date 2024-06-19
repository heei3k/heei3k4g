#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/19 15:51
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode042.py
# @Software: PyCharm
"""

42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



示例 1：

输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

示例 2：

输入：height = [4,2,0,3,2,5]
输出：9



提示：

    n == height.length
    1 <= n <= 2 * 104
    0 <= height[i] <= 105


"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        left_bound, right_bound = [0] * length, [0] * length
        for i in range(1, length):
            left_bound[i] = max(height[i - 1], left_bound[i - 1])
        for i in reversed(range(1, length)):
            right_bound[i - 1] = max(height[i], right_bound[i])
        # print(left_bound)
        # print(right_bound)
        rain_trapped = [max(0, min(left_bound[i], right_bound[i]) - height[i]) for i in range(length)]
        return sum(rain_trapped)


if __name__ == '__main__':
    solution = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(solution.trap(height))
