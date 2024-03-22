#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/21 16:12
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : kuwo.py
# @Software: PyCharm
import os
import urllib

import requests

from setting import clean_filename


class Kuwo:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
            'Secret': '4e02e59620092e668769a6f2409a7a761c14442138d3a6f99f8604172070ba390025541f',
        }
        self.cookies = {
            'Hm_lvt_cdb524f42f0ce19b169a8071123a4797': '1710839732,1711007963',
            '_ga': 'GA1.2.1545164685.1705456225',
            '_ga_ETPBRPM9ML': 'GS1.2.1711007963.3.1.1711008255.10.0.0',
            'Hm_Iuvt_cdb524f42f23cer9b268564v7y735ewrq2324': 'mDGrTpZ7Bcj8CEbd2Gbz4SFZRxTKGTRj',
            'Hm_lpvt_cdb524f42f0ce19b169a8071123a4797': '1711007982',
            '_gid': 'GA1.2.1849104302.1711007963',
            '_gat': '1',
        }

        # self.url = 'https://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&page=1&pagesize=30&httpsStatus=1&reqId=a29544b-265d-4f72-952b-25014b754567&userId=-1&realIP=117.136.84.139&host=kuwo.cn&ip=117.136.84'
        self.url = 'http://www.kuwo.cn/api/v1/www/music/playUrl'

        self.save_path = 'D:/Download/export_data/kuwo/'

        self.success = 0

    def crawl_music(self, mid, save_name=None):

        params = {
            # 'mid': '284892811',
            'mid': mid,
            # 'type': 'music',
            # 'httpsStatus': '1',
            # 'reqId': '9db42ac1-e759-11ee-a77c-8791fd11a5f8',
            # 'plat': 'web_www',
            # 'from': '',
        }

        response = requests.get(self.url, params=params, cookies=self.cookies, headers=self.headers)
        if response and response.json() and 'data' in response.json():
            song_actual_url = response.json()['data']['url']
            print(song_actual_url)
        else:
            print(f"{save_name}歌曲下载失败，可能是因为该歌曲为VIP歌曲，或者该歌曲不存在")
            return

        response = requests.get(song_actual_url)
        if save_name is None:
            save_name = str(mid)

        save_file = self.save_path + save_name + ".mp3"

        if not os.path.exists(save_file):
            with open(save_file, mode="ab") as f:
                f.write(response.content)
            print("歌曲 " + save_name + " 已完成下载！")
            self.success += 1
        else:
            print("歌曲 " + save_name + " 已经下载过，无需重复下载！")

    def crawl_kuwo(self, keywords):
        encoded_string = urllib.parse.quote(keywords)

        self.save_path += keywords + "/"

        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

        # abslist = response.json()['abslist']

        music_list = []
        files_list = []

        for page in range(0, 20):
            url = 'http://www.kuwo.cn/search/searchMusicBykeyWord?vipver=1&client=kt&ft=music&cluster=0&strategy=2012&encoding=utf8&rformat=json&mobi=1&issubtitle=1&show_copyright_off=1&pn=' + str(
                page) + '&rn=20&all=' + encoded_string

            response = requests.get(url, cookies=self.cookies, headers=self.headers)
            if response and response.json() and 'abslist' in response.json():
                abslist = response.json()['abslist']
            else:
                continue

            for song in abslist:
                album_id = song['ALBUMID']
                music_id = song['MUSICRID'].replace('MUSIC_', '')
                song_name = clean_filename(song['NAME'])
                song_artist = song['ARTIST']
                music_list.append(music_id)
                files_list.append(album_id + '_' + music_id + '_' + song_name + '_' + song_artist)
                print(album_id, music_id, song_name, song_artist)

        for music_id in music_list:
            self.crawl_music(mid=music_id, save_name=files_list[music_list.index(music_id)])

        print(f'本次一共完成{self.success}首有关{keywords}的歌曲下载！')


if __name__ == '__main__':
    kw = Kuwo()
    kw.crawl_kuwo('邓紫棋')
    # kw.crawl_music(mid=355459295)
