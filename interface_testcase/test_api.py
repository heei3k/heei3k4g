#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/20 15:04
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : test_api.py
# @Software: PyCharm
import json

import pytest
from interface_testcase.common.request_util import RequestUtil
from interface_testcase.common.yaml_util import read_news_yaml, read_extract_yaml


class TestApi:

    @pytest.mark.parametrize('args',read_news_yaml())
    def test_01_api(self,args):
        url = args['api_request']['url']
        method = args['api_request']['method']
        headers = args['api_request']['headers']
        params = args['api_request']['params']
        validate = args['api_validate']
        # print(validate)
        res = RequestUtil().send_request(method=method,url=url, headers=headers,params=params)
        # print(res.json())

    def test_02_login(self):
        """
        测试登录接口
        :return:
        """
    #     url='http://127.0.0.1:5000/get_tokens'
    #     username=hashlib.md5('admin'.encode('utf-8')).hexdigest()
    #     password = hashlib.md5('123'.encode('utf-8')).hexdigest()
    #     data={'username':str(username).upper(),
    #           'password':str(password).upper()}
    #     headers={
    #         'Content-Type':'application/json'
    #     }
    #     res=requests.post(url,json=data,headers=headers)
    #     result=res.json()
    #     self.assertEqual(res.status_code,200)
    #     self.assertEqual(result['error_code'],'0')
    #     self.assertEqual(result['message'], '登录成功')
    pass

if __name__=='__main__':
    pytest.main(['test_api.py::TestApi'])