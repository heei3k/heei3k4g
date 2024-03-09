#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/26 15:04
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : request_util.py
# @Software: PyCharm
import json as json_module
from json import JSONDecodeError

import requests

from common.replace_load import replace_load
from logging_tool.log_control import INFO, ERROR
from utils.fiddler_util import FiddlerUtil
from utils.text_util import write_text
from utils.yaml_util import read_extract_yaml, read_config_yaml, write_yaml, read_yaml


class RequestUtil:
    session = requests.session()

    def __init__(self):
        self.last_method = None
        self.base_url = read_config_yaml('base_url')
        self.last_headers = None
        self.last_url = None
        self.last_data = None
        self.last_params = None
        self.last_json = None
        self.last_files = None

    def send_request(self, method, url, headers=None, data=None, params=None, json=None, files=None, verify=True,
                     proxies=None, is_save=None):
        # method参数转化为小写
        if isinstance(method, dict):
            method = str(method.get('method'))
        self.last_method = str(method).lower()

        # 如果url包含${和}则需要进行参数提取
        for cs in range(1, str(url).count('${') + 1):
            if '${' in str(url) and '}' in str(url):
                startIndex = str(url).find('${')
                endIndex = str(url).find('}')
                oldValue = str(url)[int(startIndex):int(endIndex) + 1]
                newValue = read_extract_yaml(str(oldValue[2:-1]))
                url = eval(str(url).replace(str(oldValue), str(newValue)))
                url = str(url['url'])
            # 接口路径=基本路径+接口路径
        if isinstance(url, dict):
            url = str(url['url'])
        if url and ":" in url:
            self.last_url = url
        else:
            self.last_url = self.base_url + url

        for each_json in [a for a in [params, headers, json, data] if a is not None]:
            for key, value in each_json.items():
                for cs in range(1, str(value).count('${') + 1):
                    if "${" in str(value) and "}" in str(value):
                        if "(" in str(value) and ")" in str(value):
                            value = replace_load(value)
                        else:
                            startIndex = str(value).find('${')
                            endIndex = str(value).find('}')
                            header_value = str(value)[:int(startIndex)] if startIndex != 0 else ""
                            end_value = str(value)[int(endIndex) + 1:] if endIndex != len(value) else ""
                            oldValue = str(value)[int(startIndex):int(endIndex) + 1]
                            try:
                                value = header_value + read_extract_yaml(str(oldValue)[2:-1]) + end_value
                            except Exception as e:
                                ERROR.logger.error(e)
                each_json[key] = value

        self.last_headers = headers
        self.last_params = params
        self.last_data = data
        self.last_json = json

        if files:
            for key, path in files.items():
                files[key] = open(path, 'rb')
        self.last_files = files

        INFO.logger.info(f"https请求地址：{self.last_url}")
        INFO.logger.info(f"https请求方式：{self.last_method}")
        if self.last_headers:
            INFO.logger.info(f"https请求头：{self.last_headers}")
        if self.last_data:
            INFO.logger.info(f"https请求数据：{self.last_data}")
        if self.last_params:
            INFO.logger.info(f"https请求参数：{self.last_params}")
        if self.last_json:
            INFO.logger.info(f"https请求json：{self.last_json}")
        if self.last_files:
            INFO.logger.info(f"https请求文件：{self.last_files}")

        # 判断是否开启fiddler抓包，开启时需要打开代理
        if proxies:
            if FiddlerUtil.is_fiddler_enabled():
                proxies = {
                    'http': '127.0.0.1:8888',
                    'https': '127.0.0.1:8888'
                }
            response = RequestUtil().session.request(method=self.last_method,
                                                     url=self.last_url,
                                                     headers=self.last_headers,
                                                     data=self.last_data,
                                                     json=self.last_json,
                                                     params=self.last_params,
                                                     files=self.last_files,
                                                     verify=False,
                                                     proxies=proxies)
        else:
            response = RequestUtil().session.request(method=self.last_method,
                                                     url=self.last_url,
                                                     headers=self.last_headers,
                                                     data=self.last_data,
                                                     json=self.last_json,
                                                     params=self.last_params,
                                                     files=self.last_files)

        res_json = None
        res_text = None

        # INFO.logger.info(f"response is {response.text}")

        if response.status_code == 200:
            if response.text:
                # 因为json模块名被参数json同名了，所以重命名模块的json
                # 如何返回的不是json格式的，则保存text值
                try:
                    res_json = json_module.loads(response.text)
                except JSONDecodeError as e:
                    res_text = response.text
                if 'errcode' not in response.text:
                    INFO.logger.info("https返回正常，返回消息：" + response.text)
                    if is_save:
                        if res_json:
                            # 使用文件保存中间变量
                            write_yaml(data=res_json)
                        else:
                            write_text(data=res_text)
                # 根据业务返回json增加的判断代码
                elif 'statusCode' in res_json and res_json['statusCode'] != 200:
                    # DEBUG.logger.debug("错误响应：" + response.text)
                    pass
                else:
                    ERROR.logger.error("https返回错误，返回消息：" + response.text)
            else:
                ERROR.logger.error("https返回为空")
        else:
            ERROR.logger.error("https返回异常，错误码：" + str(response.status_code))

        if res_json:
            return res_json
        else:
            return res_text


if __name__ == '__main__':
    request_str = read_yaml("weixin.yaml", index=2)
    # headers = read_config_yaml(key="headers")
    headers = request_str[0]["headers"]
    method = request_str[0]["method"]
    # data = read_config_yaml('data')
    url = request_str[0]["url"]
    params = request_str[0]["params"]
    # files = request_str[0]["files"]
    print(f"第一次打印method{method}")
    print(f"第一次打印url{url}")
    # print(f"第一次打印params{params}")
    # print(f"第一次打印files{files}")
    # print(f"第一次打印data{data}")
    print(f"第一次打印headers{headers}")
    # req = RequestUtil().send_request(method, url,headers=headers,params=params,is_save_yaml=True)
    # req = RequestUtil().send_request(method, url, headers=headers, params=params, files=files)
    req = RequestUtil().send_request(method, url, headers=headers, params=params)
