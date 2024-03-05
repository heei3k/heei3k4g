#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/3 22:00
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : proxy_util.py
# @Software: PyCharm
import parsel
import requests


class ProxyUtil:

    def get_proxy(self):
        url = "https://www.89ip.cn/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"
        }

        res = requests.get(url=url, headers=headers)

        sel = parsel.Selector(res.text)

        ips = sel.xpath('//table[@class="layui-table"]/tbody/tr/td[1]/text()').getall()
        ports = sel.xpath('//table[@class="layui-table"]/tbody/tr/td[2]/text()').getall()

        ips = [i.replace("\n", "").replace("\t", "") for i in ips]
        ports = [i.replace("\n", "").replace("\t", "") for i in ports]

        a = []

        for ip, port in zip(ips, ports):
            a.append(ip + ":" + port)
        return a


if __name__ == '__main__':
    print(ProxyUtil().get_proxy())
