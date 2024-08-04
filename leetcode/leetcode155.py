#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/4 20:17
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode155.py
# @Software: PyCharm
"""
155. 最小栈

设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

实现 MinStack 类:

    MinStack() 初始化堆栈对象。
    void push(int val) 将元素val推入堆栈。
    void pop() 删除堆栈顶部的元素。
    int top() 获取堆栈顶部的元素。
    int getMin() 获取堆栈中的最小元素。



示例 1:

输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.



提示：

    -231 <= val <= 231 - 1
    pop、top 和 getMin 操作总是在 非空栈 上调用
    push, pop, top, and getMin最多被调用 3 * 104 次


"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) == 1:
            self.minStack.append(val)
        else:
            self.minStack.append(min(self.getMin(), val))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


if __name__ == '__main__':
    MinStack = MinStack()
    MinStack.push(-2)
    MinStack.push(0)
    MinStack.push(-3)
    print(MinStack.getMin())
    MinStack.pop()
    print(MinStack.top())
    print(MinStack.getMin())
