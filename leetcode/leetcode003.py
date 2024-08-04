#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/3 9:05
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode003.py
# @Software: PyCharm
"""
3. 无重复字符的最长子串

给定一个字符串 s ，请你找出其中不含有重复字符的 最长
子串
 的长度。



示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。



提示：

    0 <= s.length <= 5 * 104
    s 由英文字母、数字、符号和空格组成


"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        if l < 2:
            return l
        i, j, res = 0, 0, 1
        while i < l - res:
            j = i + res
            while j < l:
                j += 1
                if len(s[i:j]) > len(set(s[i:j])):
                    i += 1
                    break
                else:
                    res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))
    print(s.lengthOfLongestSubstring(" "))
    print(s.lengthOfLongestSubstring("au"))
    print(s.lengthOfLongestSubstring("dvdf"))
