#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/30 21:50
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode083.py
# @Software: PyCharm
"""
83. 删除排序链表中的重复元素
给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。

示例 1：

输入：head = [1,1,2]
输出：[1,2]

示例 2：

输入：head = [1,1,2,3,3]
输出：[1,2,3]

提示：

    链表中节点数目在范围 [0, 300] 内
    -100 <= Node.val <= 100
    题目数据保证链表已经按升序 排列


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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        cur = head
        next_ = head.next
        while next_ is not None:
            if cur.val == next_.val:
                cur.next = next_.next
            else:
                cur = cur.next
            next_ = cur.next
        return head


if __name__ == '__main__':
    solu = Solution()
    head = [1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]
    sl = transferListAsSingleLinkedList(head)
    printNodeAsList(solu.deleteDuplicates(sl.head))
