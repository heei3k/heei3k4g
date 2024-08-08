#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/8 21:18
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode021.py
# @Software: PyCharm
"""

21. 合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组
成的。



示例 1：

输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

示例 2：

输入：l1 = [], l2 = []
输出：[]

示例 3：

输入：l1 = [], l2 = [0]
输出：[0]



提示：

    两个链表的节点数目范围是 [0, 50]
    -100 <= Node.val <= 100
    l1 和 l2 均按 非递减顺序 排列

"""
from typing import Optional

from leetcode.ListNode import ListNode
from leetcode.SingleLinkedList import transferListAsSingleLinkedList


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        if list1.val > list2.val:
            temp = list1
            list1 = list2
            list2 = temp
        list1_cur = list1
        list2_cur = list2
        while list2_cur is not None:
            while list1_cur.next is not None and list1_cur.val == list1_cur.next.val:
                list1_cur = list1_cur.next
            if list1_cur.val <= list2_cur.val and list1_cur.next is None:
                list1_cur.next = list2_cur
                break
            elif list1_cur.val <= list2_cur.val <= list1_cur.next.val:
                temp1 = list2_cur.next
                temp2 = list1_cur.next
                list1_cur.next = list2_cur
                list2_cur.next = temp2
                list1_cur = list1_cur.next
                list2_cur = temp1
            else:
                list1_cur = list1_cur.next
        return list1


if __name__ == '__main__':
    sol = Solution()
    # l1 = [2]
    # l2 = [1]
    l1 = [-9, -5, -3, -2, -2, 3, 7]
    l2 = [-10, -8, -4, -3, -1, 3]
    sl = transferListAsSingleLinkedList(l1)
    sl2 = transferListAsSingleLinkedList(l2)
    print(sol.mergeTwoLists(sl.head, sl2.head))
