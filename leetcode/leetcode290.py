#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/9 16:31
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode290.py
# @Software: PyCharm
"""
290. 单词规律

给定一种规律 pattern 和一个字符串 s ，判断 s 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 s 中的每个非空单词之间存在着双向连接的对应规律。



示例1:

输入: pattern = "abba", s = "dog cat cat dog"
输出: true

示例 2:

输入:pattern = "abba", s = "dog cat cat fish"
输出: false

示例 3:

输入: pattern = "aaaa", s = "dog cat cat dog"
输出: false



提示:

    1 <= pattern.length <= 300
    pattern 只包含小写英文字母
    1 <= s.length <= 3000
    s 只包含小写英文字母和 ' '
    s 不包含 任何前导或尾随对空格
    s 中每个单词都被 单个空格 分隔


"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_s = s.split(" ")
        list_s.reverse()
        dic1 = {}
        dic2 = {}
        n = len(list_s)
        m = len(pattern)
        if m != n:
            return False
        for c in pattern:
            word = list_s.pop()
            if c not in dic1:
                dic1[c] = word
                if word in dic2:
                    return False
                else:
                    dic2[word] = c
            else:
                if dic1[c] != word or dic2[word] != c:
                    return False
        return True

    def wordPattern2(self, pattern: str, s: str) -> bool:
        res = s.split()
        return [*map(pattern.index, pattern)] == [*map(res.index, res)]


if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat fish"
    solution = Solution()
    print(solution.wordPattern2(pattern, s))
