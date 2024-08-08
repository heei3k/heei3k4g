#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/8 21:21
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : ListNode.py
# @Software: PyCharm
from copy import copy


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

    def __str__(self):
        if self:
            return "{} -> {}".format(self.val, str(self.next))

    def __len__(self):
        if self.next is None:
            return 1
        return 1 + len(self.next)

    def __getitem__(self, index):
        if index == 0:
            return self.val
        if self.next is None:
            raise IndexError
        return self.next[index - 1]

    def __setitem__(self, index, value):
        if index == 0:
            self.val = value
        elif self.next is None:
            raise IndexError
        else:
            self.next[index - 1] = value

    def __delitem__(self, index):
        if index == 0:
            self.val = self.next
        elif self.next is None:
            raise IndexError
        else:
            del self.next[index - 1]

    def __iter__(self):
        yield self.val
        if self.next is not None:
            yield from self.next

    def __reversed__(self):
        if self.next is None:
            yield self.val
        else:
            yield from reversed(self.next)

    def __iadd__(self, other):
        if self.next is None:
            self.next = other
        else:
            self.next += other
        return self

    def __add__(self, other):
        result = copy(self)
        result += other
        return result

    def __radd__(self, other):
        result = copy(other)
        result += self
        return result


if __name__ == '__main__':

    # 示例用法
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)

    a += b + c

    for item in a:
        print(item)  # 输出：1 2 3

    for item in reversed(a):
        print(item)
