#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/8 11:35
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : download_pic.py
# @Software: PyCharm


import os
import time

# coding:utf-8
import requests
from bs4 import BeautifulSoup
# 移动鼠标到某个元素
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

from debug_talk import DebugTalk
from log_control import LogHandler
from setting import fix_full_path
from yaml_util import read_yaml


class downloadPic:

    def __init__(self,
                 save_path=None):
        scrapy_yaml = "scrapy_pic.yaml"
        self.url = read_yaml(scrapy_yaml, key="url")
        self.header = read_yaml(scrapy_yaml, key="headers")
        self.save_path = save_path if save_path else read_yaml(scrapy_yaml, key="save_path")
        # print(self.save_path)
        if not os.path.isdir(self.save_path):
            os.makedirs(self.save_path)
        log_file = fix_full_path("download_pic.log", self.save_path)
        self.log_handler = LogHandler(log_file, level='info')

    def get_pics_for_one(self, url):
        url = self.url
        header = self.header
        log_handler = self.log_handler

        pages_link = []

        try:
            web_data = requests.get(url, headers=header)

            soup = BeautifulSoup(web_data.text, 'lxml')
            title = soup.select('.main-title')[0].text
            save_path = str(self.save_path) + '\\' + title
            self.log_handler.logger.info("美图保存于：", save_path)
            pages_total = int(soup.select('.pagenavi a span')[-2].text)
            self.log_handler.logger.info("此美女图片总数：", pages_total)
            for i in range(pages_total):
                # log_handler.logger.info(url + str(i+1))
                # pic_detail_page = url + str(i+1)
                pages_link.append(url + str(i + 1))
        except:
            pass
        return pages_link

    def download_pics(self):
        url = self.url
        header = self.header
        log_handler = self.log_handler
        save_path = self.save_path
        try:
            resp = requests.get(url, headers=header)
            # print("page data is" + str(page_data))
            main_page = BeautifulSoup(resp.text, "html.parser")
            # print("soup data is"+soup_data)

            aList = main_page.find_all(class_="list")
            # aList = img_div.find_all("img")
            # log_handler.logger.info(f"img div is {aList}")
            img_header = read_yaml("scrapy_pic.yaml", key="headers", index=1)
            for i in aList:
                img_one = i.find("img")
                # log_handler.logger.info(f"image {i} is {img_one}")
                img_url = "https:"
                if img_one.get("data-original") is not None:
                    img_url += img_one.get("data-original")
                else:
                    img_url += img_one.get("src")

                img_name = img_one.get("title")
                if img_name is None:
                    img_name = DebugTalk.rand_chars()
                log_handler.logger.info(f"开始下载{img_url},标题为{img_name}")
                img_resp = requests.get(img_url, headers=img_header)

                with open(save_path + img_name + ".jpg", mode="wb") as f:
                    f.write(img_resp.content)  # 图片内容写入文件
        except Exception as e:
            log_handler.logger.error(e)

    # def get_pics_for_one_pages(self,pool_num):
    #     log_handler = self.log_handler
    #     header = self.header
    #     url=self.url
    #     try:
    #         res = requests.get(url,headers=header)
    #         web_data = res.text
    #         soup = BeautifulSoup(web_data,'lxml')
    #         pages_url = soup.select('#pins li span a')
    #         for page_url in pages_url:
    #             log_handler.logger.info('===============开始下载：',page_url.text+"==============")
    #             log_handler.logger.info("此美女美图链接",page_url.get('href'))
    #             url_list = self.get_pics_for_one(page_url.get('href')+"/")
    #             pool = Pool(pool_num)
    #             pool.map(self.download_pics,url_list)
    #             pool.close()
    #             pool.join()
    #             log_handler.logger.info("======================下载完成======================")
    #             log_handler.logger.info("")
    #     except:
    #         pass

    def download_with_selenium(self):
        log_handler = self.log_handler
        binary_path = (r'C:\Program Files\Mozilla Firefox\firefox.exe')
        ops = Options()
        ops.binary_location = binary_path
        wd = webdriver.Firefox(options=ops,
                               service=Service(executable_path='D:\\tools\\firefox_webdriver\\geckodriver.exe'))
        wd.implicitly_wait(5)

        time.sleep(5)

        wd.get(
            'https://joke.oupeng.com/home?first=off')
        elements = wd.find_elements(By.XPATH, "//div[contains(@class,'img-loader')]/img[contains(@src,'jpeg')]")

        log_handler.logger.info(f"一共有{len(elements)}个图片元素 {elements}")

        d = "D:\\download\\export_data\\meitu\\"

        i = 0

        for element in elements:
            i += 1
            print('----------------')
            t = element.get_attribute('src')
            name = element.get_attribute('alt')
            # print(t)
            path = "D:\Download\export_data\pic\meitu\{}.jpeg".format(name)

            r = requests.get(t)
            r.raise_for_status()
            with open(path, 'wb') as f:
                f.write(r.content)
                log_handler.logger.info(f"开始下载{t}")
                f.close()
                # print('保存成功')

        wd.quit()


if __name__ == '__main__':
    hello = "                     |--------------------------------- |\n" \
            "                     | 欢迎使用无界面多进程美图下载器！ |\n" \
            "                     | 此项目只供个人学习使用，请勿用于 |\n" \
            "                     |       其他商业用途，谢谢！       |\n" \
            "                     |       如若侵权，联系立删！       |\n" \
            "                     |----------------------------------|"
    downloadPic = downloadPic()
    downloadPic.download_with_selenium()
    # downloadPic.log_handler.logger.info(hello)
    #
    # try:
    #     downloadPic.download_pics()
    # except:
    #     downloadPic.log_handler.logger.info("网络连接错误...")
    # downloadPic.log_handler.logger.info("")
    # downloadPic.log_handler.logger.info("##################全部下载完成!##################")
