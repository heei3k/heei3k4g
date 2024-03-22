#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/14 14:03
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : string2byte.py
# @Software: PyCharm

# def string_to_binary(s):
#     return ''.join([bin(ord(c)).replace('0b', '') for c in s])

def string_to_bytes(t):
    n = []

    for r in range(len(t)):
        n.append(t[r].encode('utf-8')[0])

    return n


def bytes_to_string(t):
    n = [chr(byte_value) for byte_value in t]
    return ''.join(n)


def bytes_to_words(t):
    n = []
    e = 0  # 当前要处理的位的位置
    for r in range(0, len(t)):
        # 如果e是32的倍数，则添加一个新整数到结果列表中
        if e % 32 == 0:
            n.append(0)
        # 将当前字节左移，并添加到结果列表中对应的整数中
        n[e // 32] |= t[r] << (24 - e % 32)
        e += 8  # 移动到下一个字节的位位置
    return n


def transform_words(s):
    # 假设 s 是一个整数数组，即之前通过 bytesToWords 函数转换得到的
    for g in range(len(s)):
        # JavaScript 中的位操作需要转换为 Python 的等效操作
        # 16711935 & (s[g] << 8 | s[g] >>> 24)
        # 这个表达式对 s[g] 左移 8 位，然后和右移 24 位（无符号右移）后的 s[g] 做按位或操作
        # 然后将结果与 16711935 做按位与操作
        # 在 Python 中，右移 24 位（无符号右移）等价于右移 24 位然后取模 2**32
        temp1 = (s[g] << 8) | (s[g] >> 24) & 0xFFFFFFFF  # 保证结果仍然是 32 位
        temp1 &= 0xFF00FF  # 16711935 in hex is 0xFF00FF

        # 4278255360 & (s[g] << 24 | s[g] >>> 8)
        # 这个表达式对 s[g] 左移 24 位，然后和右移 8 位后的 s[g] 做按位或操作
        # 然后将结果与 4278255360 做按位与操作
        temp2 = (s[g] << 24) | (s[g] >> 8)
        temp2 &= 0xFF000000  # 4278255360 in hex is 0xFF000000

        # 最后，将两个结果通过按位或操作合并，并赋值回 s[g]
        s[g] = temp1 | temp2

    return s


def words_to_bytes(t):
    n = []
    r = 0
    while r < 32 * len(t):
        # 获取当前字节在“词”数组中的索引
        word_index = r >> 5
        # 计算当前字节在“词”中的偏移量
        bit_offset = 24 - (r % 32)
        # 从“词”中提取出当前字节
        byte_value = (t[word_index] >> bit_offset) & 0xFF
        # 将提取出的字节添加到结果列表中
        n.append(byte_value)
        # 移动到下一个字节
        r += 8
    return n


# 假设 t 是原始字节数组，n.bytesToWords(t) 已经将 t 转换为整数数组 s
# 这里假设我们已经有了一个函数 bytes_to_words(t) 来完成这个转换
# s = bytes_to_words(t)
# a = 8 * len(t)
# 以下是固定的初始化值，根据算法而定
l = 1732584193
u = -271733879
f = -1732584194
d = 271733878


# 调用转换函数
# s = transform_words(s)

def bytes_to_hex(t):
    n = []

    for byte in t:
        # 提取高4位并转换为十六进制

        high_nibble = (byte >> 4) & 0x0F

        n.append(hex(high_nibble)[2:])

        # 提取低4位并转换为十六进制

        low_nibble = byte & 0x0F

        n.append(hex(low_nibble)[2:])

        # 将列表中的元素拼接成一个字符串

    return ''.join(n)


t = 'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwtappid=1014clienttime=1710404971clientver=1000dfid=34cfyK0OUOqA2L0DLT4EBTtmmid=103cd3fcda7117a575067d21c185b075srcappid=2919uuid=1710404971260{"userid":0,"plat":103,"m_type":0,"vip_type":0,"own_ads":{}}NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt'
t1 = 'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwtappid=1014clienttime=1710403244clientver=1000dfid=34cfyK0OUOqA2L0DLT4EBTtmmid=103cd3fcda7117a575067d21c185b075srcappid=2919uuid=1710403243949{"userid":0,"plat":103,"m_type":0,"vip_type":0,"own_ads":{}}NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt'
sb = string_to_bytes(t)
bw = bytes_to_words(sb)
ts = transform_words(bw)
#
s = [363678169, 1850966388, -533646285, -990498492]
wb = words_to_bytes(s)
print(sb)
print(len(sb))
print(bw)
print(ts)
print(wb)
# print(bw)

# print("N".encode('utf-8')[0])
#
# print(64//32)

# e=[26, 70, 184, 32, 126, 136, 153, 143, 239, 151, 54, 173, 79, 1, 166, 183]
# print(e)
#
# print(bytes_to_hex(e))
