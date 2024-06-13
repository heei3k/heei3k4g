#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/6 19:45
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode071.py
# @Software: PyCharm
"""
71. 简化路径

给你一个字符串 path ，表示指向某一文件或目录的 Unix 风格 绝对路径 （以 '/' 开头），请你将其转化为更加简洁的规范路径。

在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。任意多个连续的斜杠（即，'//'）都被视为单个斜杠 '/' 。 对于此问题，任何其他格式的点（例如，'...'）均被视为文件/目录名称。

请注意，返回的 规范路径 必须遵循下述格式：

    始终以斜杠 '/' 开头。
    两个目录名之间必须只有一个斜杠 '/' 。
    最后一个目录名（如果存在）不能 以 '/' 结尾。
    此外，路径仅包含从根目录到目标文件或目录的路径上的目录（即，不含 '.' 或 '..'）。

返回简化后得到的 规范路径 。



示例 1：

输入：path = "/home/"
输出："/home"
解释：注意，最后一个目录名后面没有斜杠。

示例 2：

输入：path = "/../"
输出："/"
解释：从根目录向上一级是不可行的，因为根目录是你可以到达的最高级。

示例 3：

输入：path = "/home//foo/"
输出："/home/foo"
解释：在规范路径中，多个连续斜杠需要用一个斜杠替换。

示例 4：

输入：path = "/a/./b/../../c/"
输出："/c"

"""
import re


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        # while "//" in path:
        #     path = path.replace("//", "/")
        while "/.." in path or "/./" in path or "//" in path:
            if ("/..." in path and "/../" not in path and "//" not in path) or path.startswith("/..hidden"):
                break
            if "//" in path:
                path = path.replace("//", "/")
            if "/./" in path:
                path = path.replace("/./", "/")
            if path.startswith("/..") and not path.startswith("/...") and not path.startswith("/..hidden"):
                path = path.replace("/..", "/", 1)
            path = re.sub("(\w+)(/\.{2})", "", path)
            print(path)

        if not path.endswith("/../") and path != "/" and not path.endswith("/..."):
            # print(path)
            if path.endswith("/"):
                path = path[:-1]
            if path.endswith("/."):
                path = path[:-2]
            # print(path)
        if not path:
            path = "/"

        return path

    def simplifyPathOffice(self, path):
        names = path.split("/")
        stack = list()
        for name in names:
            if name == "..":
                if stack:
                    stack.pop()
            elif name and name != ".":
                stack.append(name)
        return "/" + "/".join(stack)


if __name__ == '__main__':
    s = Solution()
    path = "/../..ga/b/.f..d/..../e.baaeeh./.a"
    print(s.simplifyPathOffice(path))
