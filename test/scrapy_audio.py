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
from common.setting import ensure_path_sep, fix_full_path, clean_filename
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

    def request_kugou(self, type=None):

        headers = read_yaml(self.scrapy_yaml, key="headers", index=1)
        if type in ['主页歌单', None]:
            url = read_yaml(self.scrapy_yaml, key="url", index=1)
        elif type == 'TOP500':
            url = "https://www.kugou.com/yy/rank/home/1-8888.html?from=rank"

        # sjoin = 'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwtappid=1014clienttime=1710569658618clientver=20000dfid=34cfyK0OUOqA2L0DLT4EBTtmencode_album_audio_id=6hc50e62from=111mid=103cd3fcda7117a575067d21c185b075platid=4srcappid=2919token=userid=0uuid=103cd3fcda7117a575067d21c185b075NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt'

        resp = requests.get(url=url, headers=headers)

        soup = BeautifulSoup(resp.text, "lxml")
        # self.log_handler.logger.info(soup)
        if type in ['主页歌单', None]:
            song_list = soup.find_all("li", class_="homep_d1_d1_d3_li1")
        elif type == 'TOP500':
            song_list = soup.find_all("div", class_="pc_temp_songlist")[0]
            # self.log_handler.logger.info(song_list)
            song_list = song_list.find_all("li", class_="")

        song_album_list = []
        song_name_list = []
        singer_name_list = []

        for song in song_list:
            if type in ['主页歌单', None]:
                song_url = song.find("a").get("href")
                song_info = song.find("a").get("dataobj")
                song_name = re.findall('"songname":"(.*?)"', song_info)[0]
                singer_name = re.findall('"author_name":"(.*?)"', song_info)[0]

            elif type == 'TOP500':
                song_a = song.find("a", class_="pc_temp_songname")
                song_url = song_a.get("href")
                song_title = song_a.get("title")
                singer_name = song_title.split(" - ")[0]
                song_name = song_title.split(" - ")[1]
            album_id = re.findall('mixsong/(.*?).html', song_url)[0]
            song_album_list.append(album_id)
            song_name_list.append(song_name)
            singer_name_list.append(singer_name)

        # self.log_handler.logger.info("歌曲列表长度 " + str(len(song_album_list) ))
        # self.log_handler.logger.info("歌曲名列表长度 " + str(len(song_name_list)))
        # self.log_handler.logger.info("歌曲演唱者列表长度 " + str(len(singer_name_list)))

        loop_lenght = len(song_album_list)
        # loop_lenght = 2
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
            # self.log_handler.logger.info(song_album_list[i])
            encode_string = "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwtappid=1014clienttime=" + str(
                clienttime) + "clientver=20000dfid=34cfyK0OUOqA2L0DLT4EBTtmencode_album_audio_id=" + song_album_list[
                                i] + "mid=103cd3fcda7117a575067d21c185b075platid=4srcappid=2919token=userid=0uuid=103cd3fcda7117a575067d21c185b075NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt"
            # self.log_handler.logger.info(encode_string)
            with open(r"D:\PycharmProjects\heei3k\js\decrypto.js", encoding='UTF-8') as f:
                js_code = f.read()
            js_com = execjs.compile(js_code)
            signature = js_com.call('exports', encode_string)
            # self.log_handler.logger.info(signature)
            request_song_url = "https://wwwapi.kugou.com/play/songinfo?srcappid=2919&clientver=20000&clienttime=" + str(
                clienttime) + "&mid=103cd3fcda7117a575067d21c185b075&uuid=103cd3fcda7117a575067d21c185b075&dfid=34cfyK0OUOqA2L0DLT4EBTtm&appid=1014&platid=4&encode_album_audio_id=" + \
                               song_album_list[i] + "&token=&userid=0&signature=" + signature

            # self.log_handler.logger.info(request_song_url)



            res = requests.get(request_song_url, headers=headers)
            song_actual_url = res.json()['data']['play_url']
            singer_name = singer_name_list[i]
            song_name = song_name_list[i]
            self.log_handler.logger.info(
                "正在下载歌曲," + song_name + ",演唱者" + singer_name + ",下载地址" + song_actual_url)
            # 因为酷狗是分段下载 ，使用迅雷下载可以直接避开这个问题
            # os.system(r'"D:\Program Files (x86)\Thunder Network\Thunder\Program\ThunderStart.exe" {url}'.format(
            #     url=song_actual_url))

            res = requests.get(song_actual_url, headers=headers)
            with open(save_path + singer_name + "_" + song_name + ".mp3", mode="ab") as f:
                f.write(res.content)
                self.log_handler.logger.info("歌曲 " + song_name + " 已完成下载！")
                # while res.status_code == 200:
                #     res = requests.get(song_actual_url, headers=headers)
                #     f.write(res.content)
                # if res.status_code == 206:
                #     for chunk in res.iter_content(chunk_size=1024):
                #         if chunk:
                #             f.write(chunk)

    def request_netease(self):
        url = "https://music.163.com/weapi/discovery/recommend/resource?csrf_token=0184df3f4bb5f9bec3c84ab0e4baa157"
        crypto_string = '{"userId":"532767234","csrf_token":"0184df3f4bb5f9bec3c84ab0e4baa157"}'
        headers = read_yaml(self.scrapy_yaml, key="headers", index=5)
        res_text = self.exec_js(crypto_string, url, headers)

        self.log_handler.logger.info(res_text)

        music_id_list = re.findall(r'"id":(\d+),', res_text)
        self.log_handler.logger.info(music_id_list)

        headers = read_yaml(self.scrapy_yaml, key="headers", index=7)
        params = {'csrf_token': '0184df3f4bb5f9bec3c84ab0e4baa157'
                  }
        song_list = []
        for album in music_id_list:
            url = "https://music.163.com/playlist?id=" + album
            self.log_handler.logger.info(url)
            resp = requests.get(url, headers=headers)
            soup = BeautifulSoup(resp.text, "lxml")
            ul = soup.find("ul", class_="f-hide")
            song_a_list = ul.find_all("a")
            self.log_handler.logger.info(song_a_list)
            for song in song_a_list:
                song_id = re.findall(r"song\?id=(\d+)", song.get("href"))
                song_name = song.text
                song_list.append({"song_id": song_id, "song_name": song_name})
        self.log_handler.logger.info(song_list)

        for i in range(0, len(song_list)):
            url = "https://music.163.com/weapi/song/enhance/player/url/v1"
            headers = read_yaml(self.scrapy_yaml, key="headers", index=2)
            params = {'csrf_token': '0184df3f4bb5f9bec3c84ab0e4baa157'}
            song_id = song_list[i]["song_id"]

            res = self.exec_js(song_id, url, headers, params)

            song_actual_url = json.loads(res)['data'][0]['url']

            song_name = clean_filename(str(song_list[i]["song_name"]))

            # headers2 = read_yaml(self.scrapy_yaml, key="headers", index=3)
            if song_actual_url:
                self.log_handler.logger.info("歌曲 " + song_name + " 真实下载地址为 " + song_actual_url)
                # 这里不需要加headers，加了有些歌曲反而会下载失败
                res = requests.get(song_actual_url)
                with open(self.save_path + song_name + "_" + str(song_id) + ".m4a", mode="ab") as f:
                    f.write(res.content)
                    self.log_handler.logger.info("歌曲 " + song_name + " 已完成下载！")

            else:
                # 部分歌曲下载失败原因是歌曲为VIP歌曲，响应不会给出歌曲的下载url
                self.log_handler.logger.info(f"歌曲 {song_name} song_id {song_id}下载失败！，失败原因  {res}")

    def exec_js(self, crypto_string, url, headers=None, params=None):
        with open(r"D:\PycharmProjects\heei3k\js\netease.js", encoding='UTF-8') as f:
            js_code = f.read()
        js_com = execjs.compile(js_code)
        text_seckey = js_com.call('asrseaDict2', crypto_string)

        data = {
            'params': text_seckey['encText'],
            'encSecKey': text_seckey['encSecKey']
        }
        if headers is None:
            headers = read_yaml(self.scrapy_yaml, key="headers", index=2)
        if params is None:
            params = {'csrf_token': '0184df3f4bb5f9bec3c84ab0e4baa157'
                      }
        # res = requests.post(url,  data=data)
        res = requests.post(url, headers=headers, params=params, data=data)
        return res.text

    def request_netease_song(self, music_list):

        headers = read_yaml(self.scrapy_yaml, key="headers", index=2)
        url = "https://music.163.com/weapi/song/enhance/player/url/v1"

        params = {'csrf_token': '0184df3f4bb5f9bec3c84ab0e4baa157'
                  }

        with open(r"D:\PycharmProjects\heei3k\js\netease.js", encoding='UTF-8') as f:
            js_code = f.read()
        js_com = execjs.compile(js_code)
        text_seckey = js_com.call('asrseaDict2', music_list)

        print(text_seckey)

        data = {
            'params': text_seckey['encText'],
            'encSecKey': text_seckey['encSecKey']
        }

        res = requests.post(url, data=data)
        # res=requests.post(url,headers=headers,params=params,data=data)
        # res.encoding = res.apparent_encoding
        # res.encoding = 'ANSI'
        print(res.text)
        song_actual_url = res.json()['data'][0]['url']
        print(song_actual_url)

        song_name = str(music_list[0])

        headers2 = read_yaml(self.scrapy_yaml, key="headers", index=3)

        # 这个地方可能不需要请求头
        res = requests.get(song_actual_url)
        # print(res)
        with open(self.save_path + "_" + song_name + ".m4a", mode="ab") as f:
            f.write(res.content)
            print("歌曲 " + song_name + " 已完成下载！")



if __name__ == '__main__':
    sa = ScrapyAudio(index=2)
    sa.request_netease()
    # sa.request_netease_song([571861425])
