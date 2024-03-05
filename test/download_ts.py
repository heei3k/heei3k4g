#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/3 14:39
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : download_ts.py
# @Software: PyCharm
import datetime
import os
import re

import requests
from Crypto.Cipher import AES

from common.debug_talk import DebugTalk
from common.setting import ensure_path_sep, fix_full_path
from logging_tool.log_control import LogHandler
from utils.request_util import RequestUtil
from utils.yaml_util import read_yaml, write_yaml, clear_yaml


class DownloadAndCombineTs:
    """
    dowmload ts and combine all the ts to a mp4
    """

    def __init__(self,
                 save_file=None,
                 save_path=None
                 ):
        log_file = fix_full_path("ts_download.log")
        self.log_handler = LogHandler(log_file, level='info')
        self.save_file = ensure_path_sep(save_file if save_file else read_yaml("scrapy.yaml", key="save_file", index=0))
        self.save_path = ensure_path_sep(save_path if save_path else read_yaml("scrapy.yaml", key="save_path", index=0))
        self.save_id = read_yaml("scrapy.yaml", key="save_id", index=0)

        if not os.path.isdir(self.save_path):
            os.makedirs(self.save_path)

    def download(self):
        headers = read_yaml("scrapy.yaml", key="headers", index=0)
        url = read_yaml("scrapy.yaml", key="url", index=0)
        params = read_yaml("scrapy.yaml", key="params", index=0)

        session = requests.session()
        resp = RequestUtil().send_request(method="get", url=url, headers=headers, params=params, is_save=True)

        self.log_handler.logger.info(f"response is :{resp}")

        re_expression = read_yaml("scrapy.yaml", key="re_expression", index=0)
        if re_expression is None:
            re_expression = r'(.*ts.*)'
        self.log_handler.logger.info(f"正则表达式为{re_expression}")
        indexs_list = []
        try:
            indexs_list = re.findall(re_expression, resp)
        except TypeError as e:
            self.log_handler.logger.error("正则匹配错误为{e}")
            return

        self.log_handler.logger.info(f"返回消息的ts数量为{len(indexs_list)}")
        yaml_path = fix_full_path(self.save_id + "ts_number.yaml", self.save_path)
        clear_yaml(yaml_path)
        write_yaml(yaml_path, data={"ts_number": len(indexs_list)})
        split_chars = read_yaml("scrapy.yaml", key="split_chars", index=0)
        if split_chars:
            url = url.split(split_chars)[0]
        if not url.endswith("/"):
            url += "/"
        self.log_handler.logger.info(f"URL为{url}")
        key = read_yaml("scrapy.yaml", key="encrypt_key", index=0)
        if key:
            key = key.encode()
            cryptor = AES.new(key, AES.MODE_CBC, key)
        self.log_handler.logger.info(f"加密码为{key}")

        for i in range(0, len(indexs_list)):
            uri = url + indexs_list[i]
            self.log_handler.logger.info(f"开始下载链接{uri}的ts文件")
            res = session.request(method="get", url=uri, headers=headers)
            ts_data = res.content
            with open(f'{self.save_path}/{i}.ts', 'wb') as fp:
                if key:
                    fp.write(cryptor.decrypt(ts_data))
                else:
                    fp.write(ts_data)
                self.log_handler.logger.info(f'{i}.ts下载完成！！')

    def write_text(self):
        file_names = os.listdir(self.save_path)
        if self.save_id:
            self.list_file = self.save_id + 'file_list.txt'
        else:
            self.list_file = 'file_list.txt'
        if self.list_file in file_names:
            os.remove(fix_full_path(self.list_file, self.save_path))
        file_list = open(os.path.join(self.save_path, self.list_file), 'w+')
        yaml_path = fix_full_path(self.save_id + "ts_number.yaml", self.save_path)
        ts_number = read_yaml(yaml_path, key="ts_number")
        for i in range(0, ts_number):
            file_list.write("file '" + self.save_path + "\\" + str(i) + ".ts'\n")
        file_list.close()
        self.log_handler.logger.info("生成txt文件成功!")

    def combine_ts(self):
        if self.save_file is None:
            self.save_file = DebugTalk.rand_chars() + 'output.mp4'
        start = datetime.datetime.now()
        self.log_handler.logger.info(f'开始合成，初始时间为:{start}')
        ffmpeg_bin_dic = r"D:/PROGRA~1/ffmpeg/bin/"
        save_file = fix_full_path(self.save_file, self.save_path)
        self.log_handler.logger.info(f'保存文件名为:{save_file}')
        if self.save_id:
            self.list_file = self.save_id + 'file_list.txt'
        else:
            self.list_file = 'file_list.txt'
        self.save_file = fix_full_path(self.save_file.replace(" ", ""), self.save_path)
        command = ffmpeg_bin_dic + 'ffmpeg -f concat -safe 0 -i ' + fix_full_path(self.list_file,
                                                                                  self.save_path) + ' -c ' + ' copy ' + self.save_file
        self.log_handler.logger.info(f'开始执行命令:{command}')
        os.system(command)
        end = datetime.datetime.now()
        spend_time = str(end - start)
        self.log_handler.logger.info(f'合成后的当前时间为：{end}')
        self.log_handler.logger.info(f'合成视频完成！用时：{spend_time}')


if __name__ == '__main__':
    dact = DownloadAndCombineTs()
    dact.download()
    dact.write_text()
    dact.combine_ts()
