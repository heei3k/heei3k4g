#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/25 15:33
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : leetcode068.py
# @Software: PyCharm
"""
68. 文本左右对齐
给定一个单词数组 words 和一个长度 maxWidth ，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用 “贪心算法” 来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

注意:

    单词是指由非空格字符组成的字符序列。
    每个单词的长度大于 0，小于等于 maxWidth。
    输入单词数组 words 至少包含一个单词。



示例 1:

输入: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

示例 2:

输入:words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
输出:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
     因为最后一行应为左对齐，而不是左右两端对齐。
     第二行同样为左对齐，这是因为这行只包含一个单词。

示例 3:

输入:words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]，maxWidth = 20
输出:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]



提示:

    1 <= words.length <= 300
    1 <= words[i].length <= 20
    words[i] 由小写英文字母和符号组成
    1 <= maxWidth <= 100
    words[i].length <= maxWidth


"""


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        length = len(words)
        # str_len_list = [len(words[i]) for i in range(length)]
        # print(str_len_list)
        result = []
        # str_ele_length = 0
        index = 0
        leftWords = length
        while leftWords > 0:
            current_index = 0
            usedWords = 0
            str_ele = []
            nex_str_ele = []
            while current_index < leftWords and len(" ".join(nex_str_ele)) <= maxWidth:
                nex_str_ele.append(words[index])
                if len(" ".join(nex_str_ele)) <= maxWidth:
                    str_ele.append(words[index])
                    current_index += 1
                    index += 1
                    usedWords += 1
            # print(" ".join(str_ele))
            leftWords -= usedWords
            str_out = ""
            if leftWords == 0:
                str_out += " ".join(str_ele)
                str_out += " " * (maxWidth - len(str_out))
            else:
                if current_index - 1 != 0:
                    div, mod = divmod(maxWidth - len("".join(str_ele)), current_index - 1)
                    for i in range(len(str_ele) - 1):
                        str_out += str_ele[i] + " " * div
                        if mod > 0:
                            str_out += " "
                            mod -= 1
                    str_out += str_ele[-1]
                    print(str_out)
                else:
                    str_out += str_ele[0] + " " * (maxWidth - len(str_ele[0]))
                    print(str_out)
            result.append(str_out)
        return result

    def fullJustify2(self, words, maxWidth):
        res, line, str_num = [], [], 0
        for word in words:
            # line中所有单词加一起的长度 + line中单词(单词与单词之间原生需要1个空格)之间的间距数 + 当前需要判断的单词长度
            # 上述之和大于等于maxWidth时会溢出，为什么等于时也会溢出？因为若新加入Word，会新增加1个间距(即空格长度)
            if str_num + len(line) - 1 + len(word) >= maxWidth:
                for i in range(maxWidth - str_num):
                    line[i % max(len(line) - 1, 1)] += ' '  # 循环将每个空格依次加到每个单词之间的间距上
                res.append(''.join(line))
                line, str_num = [], 0
            line.append(word)
            str_num += len(word)
        return res + [' '.join(line).ljust(maxWidth)]


if __name__ == '__main__':
    s = Solution()
    words = ["What", "must", "be", "acknowledgment", "shall", "be"]
    maxWidth = 16
    print(s.fullJustify2(words, maxWidth))
