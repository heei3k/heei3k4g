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
import re
import time

import execjs
import requests
from bs4 import BeautifulSoup

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

        sjoin = 'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwtappid=1014clienttime=1710569658618clientver=20000dfid=34cfyK0OUOqA2L0DLT4EBTtmencode_album_audio_id=6hc50e62from=111mid=103cd3fcda7117a575067d21c185b075platid=4srcappid=2919token=userid=0uuid=103cd3fcda7117a575067d21c185b075NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt'

        resp = requests.get(url=url, headers=headers)

        soup = BeautifulSoup(resp.text, "lxml")

        song_list = soup.find_all("li", class_="homep_d1_d1_d3_li1")

        song_album_list = []
        song_name_list = []
        singer_name_list = []

        for song in song_list:
            song_url = song.find("a").get("href")
            album_id = re.findall('mixsong/(.*?).html', song_url)[0]
            song_album_list.append(album_id)

            song_info = song.find("a").get("dataobj")
            song_name = re.findall('"songname":"(.*?)"', song_info)[0]
            singer_name = re.findall('"author_name":"(.*?)"', song_info)[0]
            song_name_list.append(song_name)
            singer_name_list.append(singer_name)

        # loop_lenght=len(song_url)
        loop_lenght = 2
        # u = "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt"
        # appid=1014
        # srcappid="2919"
        # clientver="20000"
        # # clienttime=n
        # dfid = "34cfyK0OUOqA2L0DLT4EBTtm"
        # # encode_album_audio_id =
        # mid = "084a8e74c44d3bd8d38d958c2ffe278b"
        # srcappid = 2919
        # uuid = "103cd3fcda7117a575067d21c185b075"
        # token =""
        # userid = 0
        # from = 111
        # platid = 4
        save_path = "D:\\Download\\export_data\\song\\"

        for i in range(0, loop_lenght):
            clienttime = DebugTalk.get_milliseconds()
            # print(song_album_list[i])
            encode_string = "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwtappid=1014clienttime=" + str(
                clienttime) + "clientver=20000dfid=34cfyK0OUOqA2L0DLT4EBTtmencode_album_audio_id=" + song_album_list[
                                i] + "mid=103cd3fcda7117a575067d21c185b075platid=4srcappid=2919token=userid=0uuid=103cd3fcda7117a575067d21c185b075NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt"
            # encode_string=encode_string.replace("\u200b","")
            # print(encode_string)
            with open(r"D:\PycharmProjects\heei3k\js\decrypto.js", encoding='UTF-8') as f:
                js_code = f.read()
            js_com = execjs.compile(js_code)
            signature = js_com.call('exports', encode_string)
            # print(signature)
            request_song_url = "https://wwwapi.kugou.com/play/songinfo?srcappid=2919&clientver=20000&clienttime=" + str(
                clienttime) + "&mid=103cd3fcda7117a575067d21c185b075&uuid=103cd3fcda7117a575067d21c185b075&dfid=34cfyK0OUOqA2L0DLT4EBTtm&appid=1014&platid=4&encode_album_audio_id=" + \
                               song_album_list[i] + "&token=&userid=0&signature=" + signature

            # print(request_song_url)

            res = requests.get(request_song_url, headers=headers)
            song_actual_url = res.json()['data']['play_url']
            print(song_actual_url)
            # 因为酷狗是分段下载 ，使用迅雷下载可以直接避开这个问题
            # os.system(r'"D:\Program Files (x86)\Thunder Network\Thunder\Program\ThunderStart.exe" {url}'.format(
            #     url=song_actual_url))

            res = requests.get(song_actual_url, headers=headers)
            with open(save_path + singer_name_list[i] + "_" + song_name_list[i] + ".mp3", mode="ab") as f:
                while res.status_code == 200:
                    res = requests.get(song_actual_url, headers=headers)
                if res.status_code == 206:
                    for chunk in res.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)

                    # f.write(res.content)



if __name__ == '__main__':
    sa = ScrapyAudio(index=1)
    sa.request_kugou()
