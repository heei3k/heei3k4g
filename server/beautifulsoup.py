#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/2 11:13
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : beautifulsoup.py
# @Software: PyCharm


import urllib.request

import requests
from bs4 import BeautifulSoup

# 1. 获取目标网页的URL
url = "https://shfront.wxwork.qq.com/downloadobject?fileid=08011204313330332210313638383835353535303436313830372a0131322432383730396134342d633561372d343636612d623161392d62336134643737326564316338d6d8e99e014214880e5ee946424e4f7a6986884b388dd30cd1496548015802600768b8177207333030303030309001b0bad8a5069a0100a0018fe002&filename=Python实战训练营第一天.mp4"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0'
}
response = requests.get(url, headers=headers)

# 2. 解析HTML源代码
soup = BeautifulSoup(response.text, 'html.parser')
video_tag = soup.find('video')
video_url = video_tag['src']

# 3. 下载视频文件
urllib.request.urlretrieve(video_url, 'video.mp4')
