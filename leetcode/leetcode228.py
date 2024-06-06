#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/29 15:49
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode228.py
# @Software: PyCharm
"""
228. 汇总区间

给定一个  无重复元素 的 有序 整数数组 nums 。

返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表 。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。

列表中的每个区间范围 [a,b] 应该按如下格式输出：

    "a->b" ，如果 a != b
    "a" ，如果 a == b



示例 1：

输入：nums = [0,1,2,4,5,7]
输出：["0->2","4->5","7"]
解释：区间范围是：
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

示例 2：

输入：nums = [0,2,3,4,6,8,9]
输出：["0","2->4","6","8->9"]
解释：区间范围是：
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        summary = []
        for i, num in enumerate(nums):
            if i == 0:
                if num + 1 not in nums:
                    summary.append(str(num))
                else:
                    current_num = num
                    start_num = current_num
                    while current_num + 1 in nums:
                        current_num += 1
                    end_num = current_num
                    summary.append(str(start_num) + '->' + str(end_num))

            elif i == len(nums) - 1:
                if num - 1 not in nums:
                    summary.append(str(num))
            else:
                if num + 1 not in nums and num - 1 not in nums:
                    summary.append(str(num))
                if num - 1 not in nums and num + 1 in nums:
                    current_num = num
                    start_num = current_num
                    while current_num + 1 in nums:
                        current_num += 1
                    end_num = current_num
                    summary.append(str(start_num) + '->' + str(end_num))
        return summary


if __name__ == '__main__':
    nums = [0, 2, 3, 4, 6, 8, 9]
    s = Solution()
    print(s.summaryRanges(nums))
