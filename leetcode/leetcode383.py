#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/1 21:43
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode383.py
# @Software: PyCharm
"""
383. 赎金信

给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。

如果可以，返回 true ；否则返回 false 。

magazine 中的每个字符只能在 ransomNote 中使用一次。



示例 1：

输入：ransomNote = "a", magazine = "b"
输出：false

示例 2：

输入：ransomNote = "aa", magazine = "ab"
输出：false

示例 3：

输入：ransomNote = "aa", magazine = "aab"
输出：true



提示：

    1 <= ransomNote.length, magazine.length <= 105
    ransomNote 和 magazine 由小写英文字母组成


"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic_r, dic_m = self.str_dict(ransomNote), self.str_dict(magazine)
        for key, value in dic_r.items():
            if key in dic_m.keys():
                if dic_r[key] > dic_m[key]:
                    return False
            else:
                return False
        return True

    def str_dict(self, s: str) -> dict:
        dic = {}
        for i in range(len(s)):
            if s[i] in dic.keys():
                dic[s[i]] += 1
            else:
                dic[s[i]] = 0
        return dic


if __name__ == '__main__':
    solution = Solution()
    print(solution.canConstruct("aa", "aab"))
