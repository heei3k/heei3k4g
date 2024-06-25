#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/20 19:38
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode014.py
# @Software: PyCharm
"""
14. 最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。



示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"

示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。



提示：

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] 仅由小写英文字母组成



"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        index = 0
        length = len(strs[0])
        prefix = ""
        while index < length:
            jump_outerloop = False
            prefix_same = 1
            prefix_c = strs[0][index]
            for i in range(1, len(strs)):
                if len(strs[i]) == index or strs[i][index] != prefix_c:
                    jump_outerloop = True
                    break
                elif strs[i][index] == prefix_c:
                    prefix_same += 1
            if prefix_same == len(strs):
                prefix += prefix_c
            if jump_outerloop:
                break

            index += 1
        return prefix


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
    print(solution.longestCommonPrefix(["dog", "racecar", "car"]))
    print(solution.longestCommonPrefix(["a", "b", "c"]))
    print(solution.longestCommonPrefix(["ab", "a"]))
