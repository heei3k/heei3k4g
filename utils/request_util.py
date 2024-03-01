#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/26 15:04
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : request_util.py
# @Software: PyCharm
import json as json_module

import requests

from common.replace_load import replace_load
from logging_tool.log_control import DEBUG, INFO, ERROR
from utils.fiddler_util import FiddlerUtil
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
                     proxies=None, is_save_yaml=None):
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
        self.last_url = self.base_url + url

        # 处理yaml文件中对headers的引用
        if headers:
            if headers.get('headers'):
                headers = headers.get('headers')
            if isinstance(headers, dict):
                for key, value in headers.items():
                    if str(value).startswith("${") and str(value).endswith("}"):
                        if "(" in str(value) and ")" in str(value):
                            headers[key] = replace_load(value)
                        else:
                            headers[key] = read_extract_yaml(str(value)[2:-1])
                    else:
                        headers[key] = str(value)
        self.last_headers = headers

        # if self.last_headers:
        #     headers_json = json_module.loads(json_module.dumps(self.last_headers))
        #     for key, value in headers_json.items():
        #         headers_json[key] = replace_load(value)
        #     self.last_headers = headers_json

        # 处理yaml文件中对params的引用
        if params and isinstance(params, dict):
            if params.get('params'):
                params = params.get('params')
            if isinstance(params, dict):
                for key, value in params.items():
                    if str(value).startswith("${") and str(value).endswith("}"):
                        if "(" in str(value) and ")" in str(value):
                            params[key] = replace_load(value)
                        else:
                            params[key] = read_extract_yaml(str(value)[2:-1])
                    else:
                        params[key] = str(value)
        self.last_params = params

        # 如果data不为None,并且为字典类型，则转换成json字符串，因为get和post方式都支持传入json
        # 处理yaml文件中对data的引用
        if data and isinstance(data, dict):
            if data.get('data'):
                data = data.get('data')
            if isinstance(data, dict):
                for key, value in data.items():
                    if str(value).startswith("${") and str(value).endswith("}"):
                        if "(" in str(value) and ")" in str(value):
                            data[key] = replace_load(value)
                        else:
                            data[key] = read_extract_yaml(str(value)[2:-1])
                    else:
                        data[key] = str(value)
        self.last_data = data

        if json and isinstance(json, dict):
            if json.get('json'):
                json = json.get('json')
            if isinstance(json, dict):
                for key, value in json.items():
                    if str(value).startswith("${") and str(value).endswith("}"):
                        if "(" in str(value) and ")" in str(value):
                            json[key] = replace_load(value)
                        else:
                            json[key] = read_extract_yaml(str(value)[2:-1])
                    else:
                        json[key] = str(value)
        self.last_json = json

        if files:
            for key, path in files.items():
                files[key] = open(path, 'rb')
        self.last_files = files

        # for each_json in all_json:
        #     for key, value in each_json.items():
        #         if key in ['params', 'data', 'json', 'headers']:
        #             each_json[key] = replace_load(value)
        #         elif key == "files":
        #             for file_key, file_path in value.items():
        #                 value[file_key] = open(file_path, 'rb')
        # if headers_json:
        #     self.last_headers = headers_json
        # if data_json:
        #     self.last_data = data_json
        # self.last_json = json_json if json_json else None
        # self.last_files = files_json if json_json else None

        INFO.logger.info("\n")
        INFO.logger.info("---------接口测试开始----------")
        INFO.logger.info(f"接口请求地址：{self.last_url}")
        INFO.logger.info(f"接口请求方式：{self.last_method}")
        if self.last_headers:
            INFO.logger.info(f"接口请求头：{self.last_headers}")
        if self.last_data:
            INFO.logger.info(f"接口请求数据：{self.last_data}")
        if self.last_params:
            INFO.logger.info(f"接口请求参数：{self.last_params}")
        if self.last_json:
            INFO.logger.info(f"接口请求json：{self.last_json}")
        if self.last_files:
            INFO.logger.info(f"接口请求文件：{self.last_files}")

        # 判断是否开启fiddler抓包，开启时需要打开代理
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

        if response.status_code == 200:
            if response.text:
                # 因为json模块名被参数json同名了，所以重命名模块的json
                res_json = json_module.loads(response.text)
                if 'errcode' not in response.text:
                    INFO.logger.info("接口返回正常，返回消息：" + response.text)
                    if is_save_yaml:
                        # 使用文件保存中间变量
                        write_yaml(data=res_json)
                # 根据业务返回json增加的判断代码
                elif 'statusCode' in res_json and res_json['statusCode'] != 200:
                    DEBUG.logger.debug("错误响应：" + response.text)
                else:
                    ERROR.logger.error("接口返回错误，返回消息：" + response.text)
            else:
                ERROR.logger.error("接口返回为空")
        else:
            ERROR.logger.error("接口返回异常，错误码：" + str(response.status_code))

        INFO.logger.info("---------接口测试结束----------")
        INFO.logger.info("\n")

        return res_json


if __name__ == '__main__':
    request_str = read_yaml("weixin.yaml", index=3)
    headers = read_config_yaml(key="headers")
    method = request_str[0]["method"]
    # data = read_config_yaml('data')
    url = request_str[0]["url"]
    params = request_str[0]["params"]
    files = request_str[0]["files"]
    print(f"第一次打印method{method}")
    print(f"第一次打印url{url}")
    # print(f"第一次打印params{params}")
    print(f"第一次打印files{files}")
    # print(f"第一次打印data{data}")
    print(f"第一次打印headers{headers}")
    # req = RequestUtil().send_request(method, url,headers=headers,params=params,is_save_yaml=True)
    req = RequestUtil().send_request(method, url, headers=headers, params=params, files=files)
