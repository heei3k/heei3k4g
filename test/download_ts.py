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
import urllib3
from Crypto.Cipher import AES

from common.debug_talk import DebugTalk
from common.setting import ensure_path_sep, fix_full_path
from logging_tool.log_control import LogHandler
from utils.request_util import RequestUtil
from utils.yaml_util import read_yaml, update_yaml


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

        with open(f'{self.save_path}/m3u.txt', 'w+', encoding='utf-8') as fp:
            fp.write(resp)

        # self.log_handler.logger.info(f"response is :{resp}")

        re_expression = read_yaml("scrapy.yaml", key="re_expression", index=0)
        if re_expression is None:
            re_expression = r'(.*ts.*)'
        # self.log_handler.logger.info(f"正则表达式为{re_expression}")
        indexs_list = []
        try:
            indexs_list = re.findall(re_expression, resp)
            # key_url = re.findall('URI="(.+)"', resp)[0]
            # iv = re.findall('IV=0x(\w+)', resp)[0]
            # self.log_handler.logger.info(f"加密码url为{key_url},偏移为{iv}")
            # key=requests.get(key_url, headers=headers).content
            # key=key.decode()
            # self.log_handler.logger.info(f"密码为{key}")
            # key=bytes(key)
            # self.log_handler.logger.info(f"加密码为{key}")
            # key=base64.b64decode(key)
            # self.log_handler.logger.info(f"base64密码为{key}")

        except TypeError as e:
            self.log_handler.logger.error("正则匹配错误为{e}")
            return

        index_number = len(indexs_list)
        self.log_handler.logger.info(f"返回消息的ts数量为{index_number}")
        yaml_path = fix_full_path(self.save_id + "ts_number.yaml", self.save_path)
        update_yaml(yaml_path, key="ts_number", value=index_number)
        split_chars = read_yaml("scrapy.yaml", key="split_chars", index=0)
        if split_chars:
            url = url.split(split_chars)[0]
        if not url.endswith("/"):
            url += "/"
        # self.log_handler.logger.info(f"URL为{url}")

        key = b'D7569A5E6EB34E10DD5FF664B8C9BD48'
        iv = b'fce466ebfd3233d688ae6a67092e3147'

        # if key:
        #     # key = key.encode()
        #     # 替换为实际的IV
        #     iv = 'fce466ebfd3233d688ae6a67092e3147'
        #     iv =bytes.fromhex(iv)
        #     # key = b64decode(key)  # 替换为实际的KEY
        #     # iv = format(int(iv, 16), 'b')
        #     self.log_handler.logger.info(f"key长度为{len(key)},偏移长度为{len(iv)}")
        #     self.log_handler.logger.info(f"加密秘钥为{key},偏移为{iv}")
        #     cryptor = AES.new(key, AES.MODE_CBC, iv)

        cryptor = AES.new(key, AES.MODE_CBC, iv)
        downloaded_number = read_yaml(yaml_path, "downloaded")

        self.log_handler.logger.info(f"已下载了{downloaded_number}个文件")

        if downloaded_number is None:
            downloaded_number = 0

        # key = None

        while downloaded_number < index_number:
            for i in range(downloaded_number, len(indexs_list)):
                uri = url + indexs_list[i]
                self.log_handler.logger.info(f"开始下载链接{uri}的ts文件")
                try:
                    res = session.request(method="get", url=uri, headers=headers)
                    ts_data = res.content
                    with open(f'{self.save_path}/{i}.ts', 'wb') as fp:
                        if key:
                            fp.write(cryptor.decrypt(ts_data))
                        else:
                            fp.write(ts_data)
                        downloaded_number += 1
                        update_yaml(yaml_path, key="downloaded", value=downloaded_number)
                        self.log_handler.logger.info(f'{i}.ts下载完成！！')
                except ConnectionResetError as e:
                    self.log_handler.logger.error(f'下载中断，服务器返回错误{e}')
                    break
                except requests.exceptions.ChunkedEncodingError as e:
                    self.log_handler.logger.error(f'下载中断，服务器返回错误{e}')
                    break
                except urllib3.exceptions.ProtocolError as e:
                    self.log_handler.logger.error(f'下载中断，服务器返回错误{e}')
                    break


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

    def legth(self, value):
        l = len(value)
        flag = l % 16
        if flag != 0:
            add = 16 - (l % 16)
            value = value + ('\0' * add).encode('utf-8')
        return value



if __name__ == '__main__':
    dact = DownloadAndCombineTs()
    dact.download()
    dact.write_text()
    dact.combine_ts()

    # hex_str = "fce466ebfd3233d688ae6a67092e3147"  # 示例十六进制字符串
    # binary_str = bin(int(hex_str, 16))  # 转换为二进制字符串，并去除前面的 '0b'
    # key = b'D7569A5E6EB34E10DD5FF664B8C9BD48'
    # print(len(key))
