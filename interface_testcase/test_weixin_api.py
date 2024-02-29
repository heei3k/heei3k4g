#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/21 14:43
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : test_weixin_api.py
# @Software: PyCharm

"""
接口1

获取 Access token

接口调用请求说明

https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET

接口2

获取微信API接口 IP地址

使用固定IP访问api.weixin.qq.com时，请开发者注意运营商适配，跨运营商访问可能会存在高峰期丢包问题。

API接口IP即api.weixin.qq.com的解析地址，由开发者调用微信侧的接入IP。

接口调用请求说明

http请求方式: GET https://api.weixin.qq.com/cgi-bin/get_api_domain_ip?access_token=ACCESS_TOKEN

接口3
获取客服基本信息

调用说明

http请求方式: GET https://api.weixin.qq.com/cgi-bin/customservice/getkflist?access_token=ACCESS_TOKEN


接口4

接口调用请求说明

HTTP请求方式: POST/FROMURL:https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token=ACCESS_TOKEN

https://developers.weixin.qq.com/doc/offiaccount/Cards_and_Offer/Create_a_Coupon_Voucher_or_Card.html#4

"""

import json

import allure
import pytest

# sys.path.append(os.path.dirname(sys.path[0]))
from interface_testcase.common.request_util import RequestUtil
from interface_testcase.common.yaml_util import read_login_yaml, read_yaml, write_yaml
from interface_testcase.logging_tool.log_control import INFO


@allure.epic("微信小程序接口")
@allure.feature("基础模块")
class TestWeixinApi:
    access_token=''

    @allure.story("登录接口")
    @pytest.mark.parametrize('args',read_yaml("weixin.yaml",index=0))
    def test_01_login(self,args):
        method = args['method']
        url = args['url']
        params = args['params']
        RequestUtil().send_request(method=method, url=url,params=params,is_save_yaml=True)


    @allure.story("获取ip接口")
    @pytest.mark.parametrize('args',read_yaml("weixin.yaml",index=1))
    @pytest.mark.smoke
    def test_02_get_ip(self,args):
        method = args['method']
        url = args['url']
        params = args['params']
        RequestUtil().send_request(method=method, url=url,params=params)

    @allure.story("获取客服列表")
    @pytest.mark.parametrize('args',read_yaml("weixin.yaml",index=2))
    def test_03_getkflist(self,args):
        method = args['method']
        url = args['url']
        params = args['params']
        RequestUtil().send_request(method=method, url=url,params=params)

    @allure.story("上传文件")
    @pytest.mark.parametrize('args',read_yaml("weixin.yaml",index=3))
    def test_04_upload(self,args):
        method = args['method']
        url = args['url']
        params = args['params']
        files = args['files']
        RequestUtil().send_request(method=method, url=url,params=params,files=files)


if __name__=='__main__':
    pytest.main(['test_weixin_api.py::TestWeixinApi'])
    # pytest.main()

