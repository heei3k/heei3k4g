#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/5 22:18
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode061.py
# @Software: PyCharm
"""
61. 旋转链表

给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。



示例 1：

输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]

示例 2：

输入：head = [0,1,2], k = 4
输出：[2,0,1]



提示：

    链表中节点的数目在范围 [0, 500] 内
    -100 <= Node.val <= 100
    0 <= k <= 2 * 109


"""
from typing import Optional


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class SingleLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_node(self, node: ListNode):
        self.length += 1
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node


def printNodeAsList(node):
    result = []
    while node is not None:
        result.append(node.val)
        node = node.next
    print(result)


def transferListAsSingleLinkedList(lst):
    result = SingleLinkedList()
    for val in lst:
        node = ListNode(val)
        result.add_node(node)
    return result


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    cls_v = 1

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = Solution.getLength(head)
        if n == 0:
            return None
        if k == 0:
            return head
        k = n - k % n
        if k == n:
            return head
        temp = head
        for i in range(k - 1):
            temp = temp.next
        node2 = temp.next
        temp.next = None
        return Solution.merge(node2, head)

    @staticmethod
    def merge(node1, node2):
        temp = node1
        while temp.next is not None:
            temp = temp.next
            if temp is None:
                break
        temp.next = node2
        return node1

    @classmethod
    def getLength(cls, node):
        # 类方法和静态方法的唯一区别就是类变量可以访问类变量
        if cls.cls_v == 1:
            print("hhh")
        if node is None:
            return 0
        else:
            res = 1
            temp = node
            while temp.next is not None:
                res += 1
                temp = temp.next
            return res


if __name__ == '__main__':
    sol = Solution()
    head = [1, 2, 3, 4, 5]
    k = 2
    sl = transferListAsSingleLinkedList(head)
    printNodeAsList(sol.rotateRight(sl.head, k))
