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

import allure
import pytest

# sys.path.append(os.path.dirname(sys.path[0]))
from logging_tool.log_control import ERROR
from utils.request_util import RequestUtil
from utils.yaml_util import read_yaml


@allure.epic("微信公众号接口")
@allure.feature("基础模块")
class TestWeixinApi:
    access_token = ''

    # _feature = "基础模块"
    # story_a="登录接口"
    # story_b="获取ip接口"
    # story_c = "获取客服列表"
    # story_d = "上传文件"

    # @allure.story("登录接口")
    # @allure.story("测试登录接口")
    @pytest.mark.parametrize('args', read_yaml("weixin.yaml", index=0))
    def test_01_login(self, args):
        allure.dynamic.epic(args['epic'])
        allure.dynamic.feature(args['feature'])
        allure.dynamic.story(args['story'])
        method = args['method']
        url = args['url']
        params = args['params']
        RequestUtil().send_request(method=method, url=url, params=params, is_save_yaml=True)

    @allure.story("获取ip接口")
    @pytest.mark.parametrize('args', read_yaml("weixin.yaml", index=1))
    @pytest.mark.smoke
    def test_02_get_ip(self, args):
        allure.dynamic.epic(args['epic'])
        allure.dynamic.feature(args['feature'])
        allure.dynamic.story(args['story'])
        allure.dynamic.description("动态描述")
        allure.dynamic.link("https://www.cnblogs.com/longronglang/category/1859053.html", '动态Link')
        allure.dynamic.issue("https://www.cnblogs.com/longronglang/category/1859053.html", '动态Issue')
        allure.dynamic.testcase("https://www.cnblogs.com/longronglang/category/1859053.html", '动态testcase')
        method = args['method']
        url = args['url']
        params = args['params']
        RequestUtil().send_request(method=method, url=url, params=params)

    # @allure.story(story_c)
    # @allure.story("获取客服列表")
    @pytest.mark.parametrize('args', read_yaml("weixin.yaml", index=2))
    def test_03_getkflist(self, args):
        allure.dynamic.epic(args['epic'])
        allure.dynamic.feature(args['feature'])
        allure.dynamic.story(args['story'])
        method = args['method']
        url = args['url']
        params = args['params']
        RequestUtil().send_request(method=method, url=url, params=params)

    # @allure.story("上传文件")
    # @allure.story(story_d)
    @pytest.mark.parametrize('args', read_yaml("weixin.yaml", index=3))
    def test_04_upload(self, args):
        allure.dynamic.epic(args['epic'])
        allure.dynamic.feature(args['feature'])
        allure.dynamic.story(args['story'])
        method = args['method']
        url = args['url']
        params = args['params']
        files = args['files']
        response = RequestUtil().send_request(method=method, url=url, params=params, files=files)

        if response:
            if 'eq' in args['validate']:
                validate = args['validate']['eq']['message']
                assert response['message'] == validate
            elif 'contains' in args['validate']:
                validate = args['validate']['contains']['message']
                assert validate in response
            else:
                ERROR.logger.error("不支持该断言")
                assert 1 == 0
        else:
            ERROR.logger.error("响应消息为空")
            assert 1 == 0


if __name__ == '__main__':
    pytest.main(['test_weixin_api.py::TestWeixinApi'])
    # pytest.main()
