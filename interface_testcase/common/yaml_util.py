#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/20 15:49
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : yaml_util.py
# @Software: PyCharm
import yaml
import os

from interface_testcase.logging_tool.log_control import INFO, WARNING, ERROR

current_file = __file__  # 获取当前执行的文件名（包括后缀）
current_dir = os.path.dirname(os.path.dirname(current_file))  # 获取当前执行的文件所在目录的上级目录
default_filepath=os.path.join(current_dir, 'extract.yaml')


def read_yaml(file_path=default_filepath,key=None, is_dict=False, index=None):
    if ":" not in file_path:
        file_path = os.path.join(current_dir,file_path)
    if os.path.exists(file_path):
        with open(file_path, encoding='utf-8') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        if isinstance(data,dict):
            if key and key in data:
                if is_dict:
                    return {key:data[key]}
                else:
                    return data[key]
            elif key and key not in data:
                # print(f"没有这个key:{key}")
                pass
        elif isinstance(data,list):
            if index is not None and isinstance(index,int) and index>=0 and index<len(data):
                # 这里如果列表元素是字典的话，返回的元素要转换成列表，则能被pytest.mark.parametrize作为参数调用
                return [{key:value for key,value in data[index].items()}]
            elif index is None:
                return data
            else:
                ERROR.logger.error("索引无效")
        else:
            return data
    else:
        return None



def write_yaml(file_path=default_filepath,data=None):
    if os.path.exists(file_path):
        if data:
            with open(file_path, encoding='utf-8',mode="a+") as f:
                yaml.dump(data,stream=f,allow_unicode=True)
        else:
            WARNING.logger.warning("写入数据为空")
    else:
        ERROR.logger.error("文件不存在")

def read_config_yaml(key=None,is_dict=None):
    file_path = os.path.join(current_dir , 'config.yaml')
    return read_yaml(file_path,key,is_dict=is_dict)


def read_news_yaml(key=None,is_dict=None):
    file_path = os.path.join(current_dir , 'get_news.yaml')
    return read_yaml(file_path,is_dict=is_dict)


def read_testcase_yaml(key=None,is_dict=None):
    file_path = os.path.join(current_dir , 'test_case.yaml')
    return read_yaml(file_path,is_dict=is_dict)

def read_login_yaml(key=None,is_dict=None):
    file_path = os.path.join(current_dir ,'logins.yaml')
    # print(file_path)
    return read_yaml(file_path,is_dict=is_dict)

def clear_yaml(file_path=default_filepath):
    # print("file path 为%s" % file_path)
    if os.path.exists(file_path):
        with open(file_path, encoding='utf-8',mode="w") as f:
            # print("开始清除yaml文件")
            f.truncate()

def read_extract_yaml(key=None,is_dict=None):
    return read_yaml(file_path=default_filepath,key=key,is_dict=is_dict)


if __name__=='__main__':
    print(read_extract_yaml("access_token"))