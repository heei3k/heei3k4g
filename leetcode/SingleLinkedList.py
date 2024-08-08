#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/8 21:25
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : SingleLinkedList.py
# @Software: PyCharm
from leetcode.ListNode import ListNode


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
