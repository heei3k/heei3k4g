#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/6 12:10
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : scrapy_audio.py
# @Software: PyCharm
import json
import os
import time

import requests

from common.debug_talk import DebugTalk
from common.setting import ensure_path_sep, fix_full_path
from logging_tool.log_control import LogHandler
from utils.request_util import RequestUtil
from utils.yaml_util import read_yaml


class ScrapyAudio:

    def __init__(self,
                 save_file=None,
                 save_path=None,
                 index=None
                 ):
        log_file = fix_full_path("audio_download.log")
        self.scrapy_yaml = "scrapy_audio.yaml"
        self.log_handler = LogHandler(log_file, level='info')
        self.save_file = ensure_path_sep(
            save_file if save_file else read_yaml(self.scrapy_yaml, key="save_file", index=index))
        self.save_path = ensure_path_sep(
            save_path if save_path else read_yaml(self.scrapy_yaml, key="save_path", index=index))
        self.save_id = read_yaml(self.scrapy_yaml, key="save_id", index=index)

        if not os.path.isdir(self.save_path):
            os.makedirs(self.save_path)

    def request_ximalaya(self):
        headers = read_yaml(self.scrapy_yaml, key="headers", index=0)
        url = read_yaml(self.scrapy_yaml, key="url", index=0)
        params = read_yaml(self.scrapy_yaml, key="params", index=0)

        session = requests.session()
        resp = RequestUtil().send_request(method="get", url=url, headers=headers, params=params, is_save=True)

        tracks_list = []
        audio_url = []
        try:
            resp_list = resp['data']['tracksAudioPlay']

            for i in range(0, len(resp_list)):
                tracks_list.append(resp_list[i]['trackId'])
        except TypeError as e:
            self.log_handler.logger.error(f"错误打印为{e}")

        self.log_handler.logger.info(f"track id list is :{tracks_list}")

        for i in range(0, len(tracks_list)):
            time_id = str(round(time.time() * 1000))
            uri = "https://www.ximalaya.com/mobile-playpage/track/v3/baseInfo/" + time_id + "?device=www2&trackId=" + str(
                tracks_list[i]) + "&trackQualityLevel=1"
            try:
                res = session.request(method="get", url=uri, headers=headers)
                res_json = json.loads(res.text)
                audio_url.append(res_json["trackInfo"]["playUrlList"][0]["url"])
            except Exception as e:
                self.log_handler.logger.error(f"错误打印为{e}")

        self.log_handler.logger.info(f"audio url list is :{audio_url}")

        # re_expression = read_yaml(self.scrapy_yaml, key="re_expression", index=0)
        #
        # if re_expression is None:
        #     re_expression = r'(.*ts.*)'
        # self.log_handler.logger.info(f"正则表达式为{re_expression}")
        # indexs_list = []
        # try:
        #     indexs_list = re.findall(re_expression, resp)
        # except TypeError as e:
        #     self.log_handler.logger.error("正则匹配错误为{e}")
        #     return

        # f = open('./音频文件/' +name, 'ab' ) #文件路径  文件读写方式 a文件追加（不存在新建） b进制文件
        # f.write(mp3.content)
        # f.close()

    def request_kugou(self):

        headers = read_yaml(self.scrapy_yaml, key="headers", index=1)
        url = read_yaml(self.scrapy_yaml, key="url", index=1)
        params = read_yaml(self.scrapy_yaml, key="params", index=1)

        # clienttime = params["clienttime"]
        #
        # if clienttime is None:
        #     clienttime = DebugTalk.get_milliseconds()
        #     params["clienttime"]=clienttime

        key = str(params["appid"])

        # print(params)

        param_list = []
        for key, value in params.items():
            param_list.append(str(value))
        param_list.sort()
        print(param_list)
        a = ""
        for i in range(0, len(param_list)):
            a += param_list[i]
        print(f"\n\n a is {a}")

        signature = DebugTalk.gen_md5(key + a + key)

        print(f"\nsignature is {signature}")

        session = requests.session()
        resp = RequestUtil().send_request(method="get", url=url, headers=headers, params=params)


if __name__ == '__main__':
    sa = ScrapyAudio(index=1)
    sa.request_kugou()
