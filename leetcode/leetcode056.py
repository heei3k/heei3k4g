#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/29 16:25
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode056.py
# @Software: PyCharm
"""
56. 合并区间

以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

示例 1：

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2：

输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""
from typing import List


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        all_set = set()
        for interval in intervals:
            for i in range(interval[0], interval[1] + 1):
                if i not in all_set:
                    # print(i)
                    all_set.add(i)

        summary = []
        for i, num in enumerate(all_set):
            if i == 0:
                if num + 1 not in all_set:
                    summary.append(str(num))
                else:
                    current_num = num
                    start_num = current_num
                    while current_num + 1 in all_set:
                        current_num += 1
                    end_num = current_num
                    summary.append([start_num, end_num])

            elif i == len(all_set) - 1:
                if num - 1 not in all_set:
                    summary.append(str(num))
            else:
                if num + 1 not in all_set and num - 1 not in all_set:
                    summary.append(str(num))
                if num - 1 not in all_set and num + 1 in all_set:
                    current_num = num
                    start_num = current_num
                    while current_num + 1 in all_set:
                        current_num += 1
                    end_num = current_num
                    summary.append([start_num, end_num])
        return summary

    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print(intervals)

        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


if __name__ == '__main__':
    solution = Solution()
    intervals = [[1, 4], [2, 3], [5, 6]]
    print(solution.merge2(intervals))
