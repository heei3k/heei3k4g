#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/24 19:32
# @Author  : Taoyuan
# @Version : 1.0
# @Contact : taoyuan0810@163.com
# @File    : replace_load.py.py
# @Software: PyCharm

import json
# replace_load.py
from typing import Text, Dict, Union

from common.debug_talk import DebugTalk


# 热加载
def replace_load(data: Union[Dict, Text]) -> Union[Dict, Text]:
    """

    :param data: 传入数据参数，可以是字典或文本类型
    :return: 对测试用例进行热加载
    """
    # 不管什么类型，统一转换为字符串格式

    if data and isinstance(data, dict):  # 如果data不为空，并且格式为字典,转换为字符串格式
        # ensure_ascii=False,避免将中文转换为Unicode编码，但是兼容可能会有问题
        # str_data = json.dumps(data, ensure_ascii=False)
        # 先将json字符串进行encode()编码，然后再使用unicode_escape编解码器将Unicode编码转换回中文字符
        str_data = json.dumps(data).encode().decode('unicode_escape')
    else:
        str_data = str(data)
    # 替换值
    if str_data is not None and "${" in str_data and "}" in str_data:
        for i in range(1, str_data.count("${") + 1):
            if "${" in str_data and "}" in str_data:
                start_index = str_data.index("${")
                end_index = str_data.index("}", start_index)
                # 字符串切片：切片从开始索引开始截取到结束索引，不包含结束索引（俗称含头不含尾），步长就是每几步取一个
                old_value = str_data[start_index:end_index + 1]
                func_name = old_value[2:old_value.index('(')]
                arg_value = old_value[old_value.index('(') + 1:old_value.index(')')]
                # 增加if条件语句，如果传入参数为""空字符串，则不传入，否则会报错
                if arg_value == "":
                    new_value = getattr(DebugTalk(), func_name)()
                else:
                    if "," in arg_value:
                        new_value = getattr(DebugTalk(), func_name)(*arg_value.split(','))
                    else:
                        new_value = getattr(DebugTalk(), func_name)(arg_value)
                # 这里replace只替换一次，否则会将所有满足条件的一次替换完
                str_data = str_data.replace(old_value, str(new_value), 1)
                # str_data = str_data.replace(old_value, str(new_value))
    # 还原数据类型
    if data and isinstance(data, dict):  # 如果data为字典，则将str_data还原为字典
        data = json.loads(str_data)
    else:
        data = str_data
    # 返回替换过后的data
    return data


if __name__ == '__main__':
    a = '1312a${get_random_str(1000,9999)}u${get_random_str(1000,9999)}trr'
    d = '3124413${read_extract_yaml(access_token)}1aty${read_extract_yaml(access_token)}ytnn${get_random_str(1000,9999)}rrttdf${get_random_str(1000,9999)}dsfst{access_token}yjjsdfsdf'
    print(replace_load(a))
    print(replace_load(d))
