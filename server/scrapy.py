#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/2 10:58
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : scrapy.py
# @Software: PyCharm

import requests

url = "https://shfront.wxwork.qq.com/downloadobject?fileid=08011204313330332210313638383835353535303436313830372a0131322432383730396134342d633561372d343636612d623161392d62336134643737326564316338d6d8e99e014214880e5ee946424e4f7a6986884b388dd30cd1496548015802600768b8177207333030303030309001b0bad8a5069a0100a0018fe002&filename=Python实战训练营第一天.mp4"

headers = {
    'Cookie': 'RK=ORfNFu+ceK; ptcz=3a203f89a09bb27427b8f320730e5cac728b072b03dcf43ce21c965cab3b1134; pgv_pvid=852980667; ETCI=6641523bde97497bbd8ed1eec747c038; fqm_pvqid=0b11bb57-cdba-405c-87c3-cf719a6e42dc; _clck=j6ahur|1|fjo|0; authkey=700800100918702270bf15d661081a4fe89d368088ce59375f14e16bf8fb133f1705419d518ae7c81f2b90654bc29f2e0db570bc3aca29ff1d2fed0c1eb38bf34e7c8859436236ab3b000c5dea565d62c9cf1701a52729ea73e41da2a8d297c4d841146cac3ae86178e01d167b077c5da5238f3207262b9c9f&weixinnum=0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
}
res = requests.session().get(url, headers=headers)

if res.status_code == 200:
    with open("scrapy.mp4", "wb") as f:
        f.write(res.content)
    f.close()
else:
    print(f"消息响应错误，错误码{res.status_code}")
