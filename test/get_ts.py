#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/22 17:10
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : get_ts.py
# @Software: PyCharm

import os
import re
import requests
import shutil
import time
from concurrent.futures import ThreadPoolExecutor
# from fake_useragent import UserAgent
from urllib.parse import urljoin

from Crypto.Cipher import AES

from yaml_util import read_yaml

video_download_path = 'D:/Download/export_data/d0e4b7101397757886434752212'
save_mp4_path = 'D:/Download/export_data/d0e4b7101397757886434752212/testVideo'
save_temporary_ts_path = 'D:/Download/export_data/d0e4b7101397757886434752212/temporary_ts'
if not os.path.exists(video_download_path):
    os.makedirs(save_mp4_path)
    os.mkdir(save_temporary_ts_path)
if not os.path.exists(save_temporary_ts_path):
    os.mkdir(save_temporary_ts_path)


# 先定义一个发送请求方法，方便后面的重复调用
def send_request(url):
    headers = read_yaml("scrapy.yaml", key="headers", index=0)
    try:
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return response
        else:
            print(response, '响应异常！')
            exit()
    except Exception as e:
        print('m3u8链接请求异常！！！')
        print(e)


# 这里先发送m3u8链接请求，得到返回的响应数据
def get_m3u8_response_data():
    m3u8_data = send_request(m3u8_url).text
    return m3u8_data


# 然后对得到的m3u8数据进行解析，得到每一个ts_url链接，和视频的时长，有加密则提取出
def parse_m3u8_data():
    m3u8_data = get_m3u8_response_data()
    each_line_list = m3u8_data.strip('\n').split('\n')  # 对m3u8里面的内容提取出每一行数据
    all_ts_list = []
    video_time = []
    AES_decode_data = None
    if '#EXTM3U' in each_line_list:
        for i in each_line_list:
            if '#EXT-X-KEY' in i:  # 判断是否加密
                encryption_method, key_url, iv = parse_AES_encryption(i)
                print('加密方法：', encryption_method)
                # key_url = urljoin(m3u8_url,key_url)
                AES_decode_data = AES_decode(key_url, iv)
            if not i.startswith('#') or i.startswith('http') or i.endswith('.ts'):
                each_ts_url = urljoin(m3u8_url, i)
                all_ts_list.append(each_ts_url)
            if i.startswith('#EXTINF'):
                time_ = float(i.strip().split(':')[1][:-1])
                video_time.append(time_)
    print('视频时长约为：{:.2f}分钟'.format(sum(video_time) / 60))
    return all_ts_list, AES_decode_data


# 再对每一个ts_url链接发送请求（用线程池）
def get_each_ts_response_data():
    print('开始下载视频……')
    all_ts_list, AES_decode_data = parse_m3u8_data()
    ###初始化一个线程池，并设置最大线程数为30
    with ThreadPoolExecutor(max_workers=30) as executor:
        for i, ts_url in enumerate(all_ts_list):
            executor.submit(download_ts, i, ts_url, AES_decode_data)
    '''这里可以使用单线程来下载3个ts文件做测试'''
    # i = 0
    # for ts_url in all_ts_list:
    #     download_ts(i,ts_url,AES_decode_data)
    #     i += 1
    #     if i > 3:
    #         break
    print('视频下载结束！')
    return True


# 下载并保存ts
def download_ts(i, ts_url, AES_decode_data):
    if AES_decode_data:
        ts_data = send_request(ts_url).content
        ts_data = AES_decode_data.decrypt(ts_data)
    else:
        ts_data = send_request(ts_url).content
    with open(f'{save_temporary_ts_path}/{i}.ts', mode='wb+') as f:
        f.write(ts_data)
        print(f'{i}.ts下载完成！')


# 解析加密内容
def parse_AES_encryption(key_content):
    if 'IV' in key_content or 'iv' in key_content:
        parse_result = key_content.split('=')
        encryption_method = parse_result[1].split(',')[0]
        key_url = re.findall('URI="(.+)"', key_content)[0]
        iv = re.findall('IV=0x(\w+)', key_content)[0]
        iv = iv.encode()
    else:
        parse_result = key_content.split('=')
        encryption_method = parse_result[1].split(',')[0]
        key_url = re.findall('URI="(.+)"', key_content)[0]
        iv = None
    return encryption_method, key_url, iv


# AES解密
def AES_decode(key_url, iv):
    print("key_url：", key_url)
    print("iv：", iv)
    key = send_request(key_url).content
    if iv:
        AES_decode_data = AES.new(key, AES.MODE_CBC, iv)
    else:
        AES_decode_data = AES.new(key, AES.MODE_CBC, b'0000000000000000')
    return AES_decode_data


# 最后合并所有的ts文件
def merge_all_ts_file():
    print('开始合并视频……')
    ts_file_list = os.listdir(save_temporary_ts_path)
    ts_file_list.sort(key=lambda x: int(x[:-3]))
    with open(save_mp4_path + '/video.mp4', 'wb+') as fw:
        for i in range(len(ts_file_list)):
            fr = open(os.path.join(save_temporary_ts_path, ts_file_list[i]), 'rb')
            fw.write(fr.read())
            fr.close()
    shutil.rmtree(save_temporary_ts_path)  # 删除所有的ts文件
    print('视频合并完成！')


def begin():
    if get_each_ts_response_data():
        merge_all_ts_file()


if __name__ == '__main__':
    start_time = time.time()
    ###m3u8_url链接自己找哈！
    m3u8_url = 'https://video.gzfeice.com/b7554d95vodtranscq1254019786/d0e4b7101397757886434752212/voddrm.token.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9~eyJ0eXBlIjoiRHJtVG9rZW4iLCJhcHBJZCI6MTI1NDAxOTc4NiwiZmlsZUlkIjoiMTM5Nzc1Nzg4NjQzNDc1MjIxMiIsImN1cnJlbnRUaW1lU3RhbXAiOjAsImV4cGlyZVRpbWVTdGFtcCI6MjE0NzQ4MzY0NywicmFuZG9tIjowLCJvdmVybGF5S2V5IjoiIiwib3ZlcmxheUl2IjoiIiwiY2lwaGVyZWRPdmVybGF5S2V5IjoiMTViY2E4YzM0NTdmZDkxZTY3ODM0ZWE1NjM0MmFkMGRhNzczN2E0MDk1ZDlmMzEzMTVkZTI5YzEwYjkwMzJiYmU4YjZjOGI5ZTk3N2ZmZWRiMjEzMzI5OWYwZGExMjkzNzZjYzhjNGE4MzRiNTU4ODhkMDE4MTQxMmJmZTc2ZTJlMmViZDMwZDQyZjE2YjgwZWNlZjRjOGY0YzRmYjA5YjliNzZjODIxNjM4OTIwZDY3NGIzYTA3MDZmMzhlMzFmMzQ1NDQxOTY0ZTkzYWJkOGEwNzFiYTgyZmEyMzdmNGVmOWMwYTY3NzRjYzIzYTViMzVmZjg0NDJhOGNjZjU4NiIsImNpcGhlcmVkT3ZlcmxheUl2IjoiOGQ3N2E2MmQzZjA0Y2ZiZjNmMmQ0NmIwOTU5Yzc5ZDIzNTY4NDU2ZjEyM2M4MTZmMmU2ODA1Nzk5NTY0ODIxMTRlZGYyYTZiYjEzNzExNjkyODliMTkzZTc4ZmFlZjA4YmJmNjQ2MzQzMWI5ZTM1NDk5MGJlNDEwNWZkYzYwOGQ2ODBiMzVmZTkxNGFkMTVhODViNTMzMTEyZmViMWE2NjYxNjc5OWQyYTQ3NWEwYzViOGNjZTNjZDY1NTEzN2ZlMDQzMmU2MTIyMzAwNDQzNWZhODRkY2JlYjRjM2YxMjg5NzM0YWEwY2I5ODY3OTU5ZjM1ZThiMDE4M2MyYWIyMiIsImtleUlkIjoxLCJzdHJpY3RNb2RlIjowLCJwZXJzaXN0ZW50IjoiIiwicmVudGFsRHVyYXRpb24iOjAsImZvcmNlTDFUcmFja1R5cGVzIjpudWxsfQ~ZamwkZTKaIBH0s3pNt1Xu0vMy1FvZ2YHKu5kiyAp_wo.video_1444917_2.m3u8?sign=23c269a2a06f4568e7f8ce99eea9047e&t=65fdbc5d'
    begin()
    end_time = time.time()
    print(f'总共耗时：{end_time - start_time}秒')
