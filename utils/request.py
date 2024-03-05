#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/1 15:54
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : request.py
# @Software: PyCharm

import json
import re
from builtins import str

import jsonpath
import requests

from utils.send_request import YamlUtil


class RequestUtil_:

    def __init__(self, two_node, obj):
        self.base_url = YamlUtil().read_config('base', two_node)
        self.obj = obj

    # 替换值的方法
    # #(替换url，params,data,json,headers)
    # #(string，int,float,list,dict)
    def replace_value(self, data):
        if data:
            # 保存数据类型
            data_type = type(data)
            # 判断数据类型转换成str
            if isinstance(data, dict) or isinstance(data, list):
                str_data = json.dumps(data)
            else:
                str_data = str(data)
            for cs in range(1, str_data.count('${') + 1):
                # 替换
                if "${" in str_data and "}" in str_data:
                    start_index = str_data.index("${")
                    end_index = str_data.index("}", start_index)
                    old_value = str_data[start_index:end_index + 1]
                    print("old_value:" + old_value)
                    # 反射：通过类的对象和方法字符串调用方法
                    func_name = old_value[2:old_value.index('(')]
                    args_value1 = old_value[old_value.index('(') + 1:old_value.index(')')]
                    new_value = ""
                    if args_value1 != "":
                        args_value2 = args_value1.split(',')
                        new_value = getattr(self.obj, func_name)(*args_value2)
                    else:
                        new_value = getattr(self.obj, func_name)()
                    str_data = str_data.replace(old_value, str(new_value))
            # 还原数据类型
            if isinstance(data, dict) or isinstance(data, list):
                data = json.loads(str_data)
            else:
                data = data_type(str_data)
        return data

    # 规范yaml测试用例
    def standard_yaml(self, caseinfo):
        caseinfo_keys = caseinfo.keys()
        # 判断一级关键字是否包含：name，request，validate
        if "name" in caseinfo_keys and "request" in caseinfo_keys and "validate" in caseinfo_keys:
            # 判断request下面是否包含：method、url
            request_keys = caseinfo["request"].keys()
            if "method" in request_keys and "url" in request_keys:
                print("yaml基本架构检查通过")
                method = caseinfo['request'].pop("method")  # pop() 函数用于移除列表中的一个元素，并且返回该元素的值。
                url = caseinfo['request'].pop("url")
                res = self.send_request(method, url, **caseinfo['request'])  # caseinfo需要解包加**
                return_text = res.text
                return_code = res.status_code
                return_json = ""
                try:
                    return_json = res.json()
                except Exception as e:
                    print("extract返回的结果不是JSON格式")

                # 提取值并写入extract.yaml文件
                if "extract" in caseinfo.keys():
                    for key, value in caseinfo["extract"].items():
                        if "(.*?)" in value or "(.+?)" in value:  # 正则表达式
                            zz_value = re.search(value, return_text)
                            if zz_value:
                                extract_value = {key: zz_value.group(1)}
                                YamlUtil().write_yaml(extract_value)
                        else:  # jsonpath
                            js_value = jsonpath.jsonpath(return_json, value)
                            if js_value:
                                extract_value = {key: js_value[0]}
                                YamlUtil().write_yaml(extract_value)
            else:
                print("在request下必须包含method,url")
        else:
            print("一级关键字必须包含name,request,validate")

    sess = requests.session()

    # 统一请求封装

    def send_request(self, method, url, **kwargs):
        method = str(method).lower()  # 转换小写
        # 基础路径的拼接和替换
        url = self.base_url + self.replace_value(url)
        print(url)
        # 参数替换
        for key, value in kwargs.items():
            if key in ['params', 'data', 'json', 'headers']:
                kwargs[key] = self.replace_value(value)
            elif key == "files":
                for file_key, file_path in value.items():
                    value[file_key] = open(file_path, 'rb')
        res = RequestUtil.sess.request(method, url, **kwargs)
        print(res.text)
        return res
