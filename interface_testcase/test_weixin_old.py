#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/28 16:50
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : test_weixin_old.py
# @Software: PyCharm
import json

import allure
import pytest

# sys.path.append(os.path.dirname(sys.path[0]))
from interface_testcase.common.request_util import RequestUtil
from interface_testcase.common.send_request import SendRequest
from interface_testcase.common.yaml_util import read_login_yaml, read_yaml, write_yaml
from interface_testcase.logging_tool.log_control import INFO

@allure.epic("微信小程序接口")
@allure.feature("基础模块")
class TestWeixinApi:
    access_token=''

    @allure.story("登录接口")
    @pytest.mark.parametrize('args',read_login_yaml())
    def test_01_login(self,args):
        appid = args['testdata']['appid']
        secret = args['testdata']['secret']
        print(appid)
        print(secret)
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid='+appid+'&secret='+secret
        # headers = {
        #     'Content-Type': 'application/json',
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
        #     'Accept': '*/*'
        # }
        # response = requests.get(url=url,headers=headers)

        try:
            response = SendRequest().all_send_request(method='get',url=url)
            INFO.logger.info("响应报文为"+response.text)
            data = json.loads(response.text)

            # 使用文件保存中间变量
            write_yaml(data=data)

            # 使用全局变量保存中间变量，对于多个类之间相互调用存在问题
            # TestWeixinApi.access_token = data['access_token']
            # 使用正则表达式提取access_token
            # value=re.search('name="access_token" value="(.+?)"',response.text)
            # print(value)
            # print("获取到的access token为" + TestWeixinApi.access_token)
        except TypeError:
            print("获取失败")

        # result_dict = json.loads(response.text)
        # print(result_dict)

    @allure.story("获取ip接口")
    @pytest.mark.smoke
    def test_02_get_ip(self):
        # 使用全局变量保存中间变量，对于多个类之间相互调用存在问题
        # url='https://api.weixin.qq.com/cgi-bin/get_api_domain_ip?access_token=' + TestWeixinApi.access_token
        url = 'https://api.weixin.qq.com/cgi-bin/get_api_domain_ip?access_token=' + read_yaml(key="access_token")
        response = SendRequest().all_send_request(method='get',url=url)
        result_dict = json.loads(response.text)
        print(result_dict)

    @allure.story("获取客服列表")
    def test_03_getkflist(self):
        url='https://api.weixin.qq.com/cgi-bin/customservice/getkflist?access_token='+ read_yaml(key="access_token")
        response = SendRequest().all_send_request(method='get',url=url)
        result_dict = json.loads(response.text)
        print(result_dict)

    @allure.story("上传文件")
    def test_04_upload(self):
        url='https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token='+ read_yaml(key="access_token")
        datas={
            "media":open(r"D:\backup\489pm2.jpg",mode="rb")
        }
        res = SendRequest().all_send_request(method='post',url=url,files=datas)
        print(res.json())


if __name__=='__main__':
    pytest.main(['test_weixin_old.py::TestWeixinApi'])
    # pytest.main()

