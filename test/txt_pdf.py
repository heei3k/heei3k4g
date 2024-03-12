#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/10 21:42
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : txt_pdf.py
# @Software: PyCharm
import os
import re

from fpdf import FPDF


def txtToPdf():
    i = 1
    # 以列表的方式打开所有txt文件的路径
    for filename in os.listdir("E:\\txt版"):
        print("第%d开始" % i)
        pdf = FPDF()
        # 读取字体文件
        pdf.add_font('fangzhengzhunyuan', '', 'fangzhengzhunyuan.TTF', True)
        pdf.add_page()
        # 设置pdf字体大小
        pdf.set_font("fangzhengzhunyuan", size=12)
        # 打开txt文本
        with open("E:\\txt版\\" + filename, encoding='utf-8') as f:
            ms = re.sub(r'.txt', '.pdf', filename)
            try:
                # 按行读取txt文本内容
                for line in f.readlines():
                    str = line
                    num = len(str)
                    temp = 45  # 判断标志，实现pdf文件每行最多村45个字符
                    for j in range(0, num, temp):
                        if (j + temp < num):
                            data = str[j:j + temp]
                        else:
                            data = str[j:num]
                        pdf.cell(0, 5, data, ln=1)
                    f.close()
            except Exception as e:
                print(e)
            print(ms)
            pdf.output("E:\\中转\\" + ms)
        print("第%d完成" % i)
        i = i + 1


txtToPdf()
