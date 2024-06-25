#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/24 17:56
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode006.py
# @Software: PyCharm
"""
6. Z 字形变换

将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R

之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);



示例 1：

输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"

示例 2：

输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I

示例 3：

输入：s = "A", numRows = 1
输出："A"



提示：

    1 <= s.length <= 1000
    s 由英文字母（小写和大写）、',' 和 '.' 组成
    1 <= numRows <= 1000


"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)
        z_num = 2 * numRows - 2
        if z_num == 0:
            return s
        # print(z_num)
        result = [[] for _ in range(numRows)]
        # result = [[]] * numRows
        print(result)
        for i in range(length):

            # print(mod_num1)
            mod_num2 = i % z_num
            # print(mod_num2)
            if mod_num2 < numRows:
                result[mod_num2].append(s[i])
            else:
                middle = z_num - mod_num2
                print(middle)
                result[middle].append(s[i])
        # print(result)
        res = ""
        for i in range(numRows):
            res += "".join(result[i])
        return res


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    print(Solution().convert(s, numRows))

    s = "PAYPALISHIRING"
    numRows = 4
    print(Solution().convert(s, numRows))
