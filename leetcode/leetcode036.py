#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/4 11:51
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode036.py
# @Software: PyCharm
import collections
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        # 将每个小九宫格里面的数存入到matrix的列表中
        matrix = [[] for _ in range(row)]
        for i in range(row):
            for j in range(row):
                matrix[i // 3 * 3 + j // 3].append(board[i][j])

        for i in range(row):
            # row_counter = collections.Counter(board[i])
            # col_counter = collections.Counter([board[j][i] for j in range(row)])
            # matrix_counter = collections.Counter(matrix[i])
            combined_list = list(collections.Counter(board[i]).items()) + list(
                collections.Counter([board[j][i] for j in range(row)]).items()) + list(
                collections.Counter(matrix[i]).items())
            for k, v in combined_list:
                if k != "." and v > 1:
                    return False
        return True


if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", "2", "8", ".", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    s = Solution()
    print(s.isValidSudoku(board))
