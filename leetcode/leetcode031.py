#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/9 22:42
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode031.py
# @Software: PyCharm
"""
31. 下一个排列

整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。

    例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。

整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。

    例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
    类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
    而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。

给你一个整数数组 nums ，找出 nums 的下一个排列。

必须 原地 修改，只允许使用额外常数空间。



示例 1：

输入：nums = [1,2,3]
输出：[1,3,2]

示例 2：

输入：nums = [3,2,1]
输出：[1,2,3]

示例 3：

输入：nums = [1,1,5]
输出：[1,5,1]



提示：

    1 <= nums.length <= 100
    0 <= nums[i] <= 100


"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if (len(nums) == 2):
            nums[0], nums[1] = nums[1], nums[0]
        elif len(nums) == 3:
            if nums[1] < nums[2]:
                nums[1], nums[2] = nums[2], nums[1]
            else:
                if nums[1] > nums[0] > nums[2]:
                    nums[0], nums[1], nums[2] = nums[1], nums[2], nums[0]
                elif nums[1] > nums[2] > nums[0]:
                    nums[2], nums[0], nums[1] = nums[1], nums[2], nums[0]
                else:
                    nums[0], nums[2] = nums[2], nums[0]
        else:
            if self.isLargest(nums):
                self.getMinimum(nums)
            else:
                if self.isLargest(nums[1:]):
                    for i in range(len(nums) - 1, 0, -1):
                        if nums[0] == nums[i] - 1:
                            nums[0], nums[i] = nums[i], nums[0]
                            break
                    self.getMinimum(nums[1:])
                else:
                    self.nextPermutation(nums[1:])

    def isLargest(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                return False
        return True

    def getMinimum(self, nums):
        n = len(nums)
        ptr = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        for i in range(ptr, n):
            if nums[i] == 1:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3]
    sol.nextPermutation(nums)
    print(nums)

    nums = [3, 2, 1]
    sol.nextPermutation(nums)
    print(nums)

    nums = [1, 1, 5]
    sol.nextPermutation(nums)
    print(nums)

    nums = [1, 3, 2]
    sol.nextPermutation(nums)
    print(nums)

    nums = [2, 3, 1]
    sol.nextPermutation(nums)
    print(nums)

    nums = [1, 1, 0]
    sol.nextPermutation(nums)
    print(nums)

    nums = [1, 0, 2]
    sol.nextPermutation(nums)
    print(nums)
