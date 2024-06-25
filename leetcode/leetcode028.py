#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/25 15:03
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode028.py
# @Software: PyCharm
"""
28. 找出字符串中第一个匹配项的下标

给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。



示例 1：

输入：haystack = "sadbutsad", needle = "sad"
输出：0
解释："sad" 在下标 0 和 6 处匹配。
第一个匹配项的下标是 0 ，所以返回 0 。

示例 2：

输入：haystack = "leetcode", needle = "leeto"
输出：-1
解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。



提示：

    1 <= haystack.length, needle.length <= 104
    haystack 和 needle 仅由小写英文字符组成


"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_h = len(haystack)
        len_n = len(needle)
        start = 0
        while start <= len_h - len_n:
            if haystack[start] == needle[0]:
                checked = 0
                for i in range(1, len_n):
                    if haystack[start + i] != needle[0 + i]:
                        break
                    else:
                        checked = i
                if checked == len_n - 1:
                    return start
            start += 1
        return -1


if __name__ == '__main__':
    haystack = "leetcode"
    needle = "leeto"
    print(Solution().strStr(haystack, needle))
