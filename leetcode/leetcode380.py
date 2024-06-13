#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/12 16:20
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode380.py
# @Software: PyCharm
"""
380. O(1) 时间插入、删除和获取随机元素
实现RandomizedSet 类：

    RandomizedSet() 初始化 RandomizedSet 对象
    bool insert(int val) 当元素 val 不存在时，向集合中插入该项，并返回 true ；否则，返回 false 。
    bool remove(int val) 当元素 val 存在时，从集合中移除该项，并返回 true ；否则，返回 false 。
    int getRandom() 随机返回现有集合中的一项（测试用例保证调用此方法时集合中至少存在一个元素）。每个元素应该有 相同的概率 被返回。

你必须实现类的所有函数，并满足每个函数的 平均 时间复杂度为 O(1) 。
示例：

输入
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
输出
[null, true, false, true, 2, true, false, 2]

解释
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // 向集合中插入 1 。返回 true 表示 1 被成功地插入。
randomizedSet.remove(2); // 返回 false ，表示集合中不存在 2 。
randomizedSet.insert(2); // 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
randomizedSet.getRandom(); // getRandom 应随机返回 1 或 2 。
randomizedSet.remove(1); // 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
randomizedSet.insert(2); // 2 已在集合中，所以返回 false 。
randomizedSet.getRandom(); // 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。

"""
import random


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


class RandomizedSet(object):

    def __init__(self):
        self.set = set()

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.set:
            self.set.add(val)
            return True
        else:
            return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.set:
            self.set.remove(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        length = len(self.set)
        for i in self.set:
            return random.choice(list(self.set))


if __name__ == '__main__':
    s = RandomizedSet()
    print(s.insert(1))
    print(s.remove(2))
    print(s.insert(2))
    print(s.insert(3))
    print(s.getRandom())
    print(s.getRandom())
    print(s.getRandom())
