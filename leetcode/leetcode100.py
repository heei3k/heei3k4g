#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/2 22:02
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode100.py
# @Software: PyCharm

"""
100. 相同的树

给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。



示例 1：

输入：p = [1,2,3], q = [1,2,3]
输出：true

示例 2：

输入：p = [1,2], q = [1,null,2]
输出：false

示例 3：

输入：p = [1,2,1], q = [1,1,2]
输出：false



提示：

    两棵树上的节点数目都在范围 [0, 100] 内
    -104 <= Node.val <= 104


"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None and q is not None or q is None and p is not None:
            return False

        elif p.val == q.val and p.left is None and p.right is None and q.left is None and q.right is None:
            return True
        elif p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
