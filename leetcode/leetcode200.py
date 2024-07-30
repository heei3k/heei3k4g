#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/27 23:14
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode200.py
# @Software: PyCharm
"""
200. 岛屿数量

给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。



示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1

示例 2：

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3



提示：

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] 的值为 '0' 或 '1'


"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        grid_ = [[0 for _ in range(n)] for _ in range(m)]
        new_grid = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                grid_[i][j] = int(grid[i][j])

        for i in range(m):
            for j in range(n):
                if grid_[i][j] != 0:
                    if i >= 1:
                        new_grid[i][j] += grid_[i - 1][j]
                    if i < m - 1:
                        new_grid[i][j] += grid_[i + 1][j]
                    if j >= 1:
                        new_grid[i][j] += grid_[i][j - 1]
                    if j < n - 1:
                        new_grid[i][j] += grid_[i][j + 1]
                    if new_grid[i][j] == 0:
                        new_grid[i][j] = 1
        print(new_grid)

        for i in range(m):
            for j in range(n):
                if new_grid[i][j] == 1:
                    if (i >= 1 and new_grid[i][j] < new_grid[i - 1][j]) or (
                            i < m - 1 and new_grid[i][j] < new_grid[i + 1][j]) or (
                            j >= 1 and new_grid[i][j] < new_grid[i][j - 1]) or (
                            j < n - 1 and new_grid[i][j] < new_grid[i][j + 1]):
                        new_grid[i][j] = 0
        print(new_grid)

        for i in range(m):
            left_point = 0
            right_point = n - 1
            while left_point <= right_point and left_point < n - 1 and right_point > 1:
                if new_grid[i][left_point] <= new_grid[i][left_point + 1] and new_grid[i][left_point] > 0:
                    new_grid[i][left_point] = 0
                if new_grid[i][right_point] <= new_grid[i][right_point - 1] and new_grid[i][right_point] > 0:
                    new_grid[i][right_point] = 0
                left_point += 1
                right_point -= 1
            if left_point == right_point - 1:
                if new_grid[i][left_point] > 0 and new_grid[i][left_point] <= new_grid[i][left_point + 1]:
                    new_grid[i][left_point] = 0
        print(new_grid)

        for i in range(n):
            up_point = 0
            down_point = m - 1
            while up_point <= down_point and up_point < m - 1 and down_point > 1:
                if new_grid[up_point][i] <= new_grid[up_point + 1][i] and new_grid[up_point][i] > 0:
                    new_grid[up_point][i] = 0
                if new_grid[down_point][i] <= new_grid[down_point - 1][i] and new_grid[down_point][i] > 0:
                    new_grid[down_point][i] = 0
                up_point += 1
                down_point -= 1
            if up_point == down_point - 1:
                if new_grid[up_point][i] > 0 and new_grid[up_point][i] <= new_grid[up_point + 1][i]:
                    new_grid[up_point][i] = 0
        print(new_grid)
        sum = 0
        for i in range(m):
            for j in range(n):
                if new_grid[i][j] > 0:
                    sum += 1
        return sum

    def numIslandsOffice(self, grid: List[List[str]]) -> int:
        nr, nc = len(grid), len(grid[0])
        sum = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == "1":
                    sum += 1
                    self.dfs(grid, i, j)
        print(grid)
        return sum

    def dfs(self, grid, i, j):
        grid[i][j] = "0"
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1":
                self.dfs(grid, x, y)


if __name__ == '__main__':
    s = Solution()
    #     grid=[
    #   ["1","1","0","0","0"],
    #   ["1","1","0","0","0"],
    #   ["0","0","1","0","0"],
    #   ["0","0","0","1","1"]
    # ]
    #     print(s.numIslands(grid))
    grid = [["1", "1", "1"], ["1", "0", "1"], ["1", "1", "1"]]
    print(s.numIslandsOffice(grid))
