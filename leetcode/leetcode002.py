#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/27 19:49
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode002.py
# @Software: PyCharm
"""
2. 两数相加

给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]

示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]



提示：

    每个链表中的节点数在范围 [1, 100] 内
    0 <= Node.val <= 9
    题目数据保证列表表示的数字不含前导零

"""


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


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum_ = carry + x + y
            carry = sum_ // 10
            curr.next = ListNode(sum_ % 10)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            curr.next = ListNode(carry)
        return dummy.next


if __name__ == '__main__':
    # node1=ListNode(2)
    # node2=ListNode(4)
    # node3=ListNode(3)
    # sl=SingleLinkedList()
    # sl.add_node(node1)
    # sl.add_node(node2)
    # sl.add_node(node3)
    #
    # node4=ListNode(5)
    # node5=ListNode(6)
    # node6=ListNode(4)
    # sl2=SingleLinkedList()
    # sl2.add_node(node4)
    # sl2.add_node(node5)
    # sl2.add_node(node6)

    l1 = [9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]
    sl = transferListAsSingleLinkedList(l1)
    sl2 = transferListAsSingleLinkedList(l2)

    solution = Solution()
    result = solution.addTwoNumbers(sl.head, sl2.head)
    printNodeAsList(result)
