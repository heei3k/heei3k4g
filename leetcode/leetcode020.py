#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/6 17:23
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode020.py
# @Software: PyCharm

"""
20. 有效的括号

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
    每个右括号都有一个对应的相同类型的左括号。



示例 1：

输入：s = "()"
输出：true

示例 2：

输入：s = "()[]{}"
输出：true

示例 3：

输入：s = "(]"
输出：false

"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.count("(") != s.count(")") or s.count("[") != s.count("]") or s.count("{") != s.count("}"):
            return False
        else:
            # s=s.replace(")","(").replace("]","[").replace("}","{")
            print(s)
            i = 0
            while s:
                if i == len(s) - 1:
                    break
                if (s[i] == "(" and s[i + 1] == ")") or (s[i] == "[" and s[i + 1] == "]") or (
                        s[i] == "{" and s[i + 1] == "}"):
                    s = s.replace(s[i] + s[i + 1], "")
                    i = max(0, i - 2)
                    print("s is " + s)
                    print("i is " + str(i))
                else:
                    i += 1
            print(s)
            if s:
                return False
            else:
                return True


if __name__ == '__main__':
    solution = Solution()
    s = "([)]"
    print(solution.isValid(s))
