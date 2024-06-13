#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/12 15:25
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode045.py
# @Software: PyCharm
"""
45. 跳跃游戏 II


给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。

每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:

    0 <= j <= nums[i]
    i + j < n

返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。



示例 1:

输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

示例 2:

输入: nums = [2,3,0,1,4]
输出: 2

"""


class Solution(object):
    def jump(self, nums):
        n = len(nums)
        last = n - 1
        i = 0
        jump = 0
        while i < last:
            if i + nums[i] >= last:
                jump += 1
                last = i
                i = -1
            i += 1
        return jump


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    solution = Solution()
    print(solution.jump(nums))
