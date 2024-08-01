#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/1 21:35
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode067.py
# @Software: PyCharm
"""
67. 二进制求和

给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。



示例 1：

输入:a = "11", b = "1"
输出："100"

示例 2：

输入：a = "1010", b = "1011"
输出："10101"



提示：

    1 <= a.length, b.length <= 104
    a 和 b 仅由字符 '0' 或 '1' 组成
    字符串如果不是 "0" ，就不含前导零


"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)
        sum = ""
        list_a = list(a)
        list_b = list(b)
        list_a.reverse()
        list_b.reverse()
        a = ''.join(list_a)
        b = ''.join(list_b)
        res = 0
        for i in range(max(len_a, len_b)):
            x = int(a[i]) if i < len_a else 0
            y = int(b[i]) if i < len_b else 0
            res = res + x + y
            sum = str(res % 2) + sum
            res = res // 2
        if res == 1:
            return "1" + ''.join(sum)
        else:
            return ''.join(sum)


if __name__ == '__main__':
    s = Solution()
    print(s.addBinary("11", "1"))
    print(s.addBinary("1010", "1011"))
