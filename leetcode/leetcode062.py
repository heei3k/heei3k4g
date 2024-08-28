#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/18 9:21
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode062.py
# @Software: PyCharm

"""
62. 不同路径

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

输入：m = 3, n = 7
输出：28

示例 2：

输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下

示例 3：

输入：m = 7, n = 3
输出：28

示例 4：

输入：m = 3, n = 3
输出：6



提示：

    1 <= m, n <= 100
    题目数据保证答案小于等于 2 * 109

"""


def custom_cache(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.combination(m + n - 2, m - 1)

    @custom_cache
    def combination(self, n, k):
        if (k == 0 or k == n):
            return 1
        else:
            return self.combination(n - 1, k) + self.combination(n - 1, k - 1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.uniquePaths(3, 7))
    assert solution.uniquePaths(3, 7) == 28
    assert solution.uniquePaths(3, 2) == 3
    assert solution.uniquePaths(7, 3) == 28
    assert solution.uniquePaths(3, 3) == 6
