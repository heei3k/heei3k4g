#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/10 20:01
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : scrapy_books.py
# @Software: PyCharm
import os
import re

import requests
from bs4 import BeautifulSoup
from common.setting import fix_full_path
from logging_tool.log_control import LogHandler


# from lxml import etree

# import sys
# sys.path.append("C:\\Python\\Python37\\Lib\\site-packages")


class ScrapyBooks:
    # 去掉文件名中非法字符
    @staticmethod
    def clean_filename(filename):
        illegal_chars = re.compile(r'[\\/:*?"<>|]')  # 正则表达式匹配不合法字符
        clean_name = re.sub(illegal_chars, '', filename)  # 替换非法字符为空
        return clean_name

    def download_zongheng(self, bookId, save_vip=False):

        bookId = str(bookId)

        url = "https://book.zongheng.com/showchapter/" + bookId + ".html"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Cookie": "zhffr=www.baidu.com; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218e282bbee26ba-0720e5dbda4a84-e565623-1327104-18e282bbee31014%22%2C%22%24device_id%22%3A%2218e282bbee26ba-0720e5dbda4a84-e565623-1327104-18e282bbee31014%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; sajssdk_2015_cross_new_user=1; ZHID=CEED747C90424891B71B63816082BE51; zh_visitTime=1710070955852; PassportCaptchaId=e18c0cfb7a418063e1afc0c0341414e1; Hm_lvt_c202865d524849216eea846069349eb9=1710070957; Hm_lpvt_c202865d524849216eea846069349eb9=1710071909; acw_tc=ac11000117100719075024794ea93a9df6611698a950b8b1ba2d587ecf8655; ver=2018",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1"
        }

        res = requests.get(url, headers=headers)

        soup = BeautifulSoup(res.text, "lxml")

        chapters = soup.find_all("li", class_="col-4")
        chapters_vip = soup.find_all("li", class_="vip col-4")
        chapters_normal = [i for i in chapters if i not in chapters_vip]

        save_dir = "D:\\Download\\export_data\\books\\" + bookId + "\\"

        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        log_file = fix_full_path("download_books.log", save_dir)
        log_handler = LogHandler(log_file, level='info')

        # 默认只保存非VIP的章节
        if not save_vip:
            chapters = chapters_normal

        for chapter in chapters:
            chapter_url = chapter.find("a").get("href")
            chapter_title = chapter.find("a").text
            save_file = save_dir + chapter_title + ".txt"
            if os.path.exists(save_file):
                log_handler.logger.info(f"{chapter_title}.txt已存在，跳过下载过程")
                continue
            # print(chapter_url,chapter_title)
            res = requests.get(chapter_url, headers=headers)
            soup_text = BeautifulSoup(res.text, "html.parser")
            content = soup_text.find_all("div", class_="content")[0]
            content = "\n".join(content.stripped_strings)

            if not os.path.exists(save_file):
                # 对文件名校验，去掉非法字符
                chapter_title = ScrapyBooks.clean_filename(chapter_title)
                save_file = save_dir + chapter_title + ".txt"
                with open(save_file, "w") as f:
                    f.write(content)
                    log_handler.logger.info(f"{chapter_title}已保存")

    def downlaod_books(self):
        # book_list=[189169,435710]
        # book_list=[547156,1190950]
        book_list = [435710]
        for i in book_list:
            self.download_zongheng(i)


if __name__ == '__main__':
    ScrapyBooks().downlaod_books()
