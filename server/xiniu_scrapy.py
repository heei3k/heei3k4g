#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/12/8 12:04
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : xiniu_scrapy.py
# @Software: PyCharm

import execjs
import requests

cookies = {
    'btoken': '5KMYQOHNBOVEY8R9VBT9YCPX912260AF',
    'Hm_lvt_42317524c1662a500d12d3784dbea0f8': '1733626505',
    'HMACCOUNT': '4588BDFCE42D6B53',
    'hy_data_2020_id': '193a431267be33-0f6f444745d8df-26011851-1327104-193a431267c122c',
    'hy_data_2020_js_sdk': '%7B%22distinct_id%22%3A%22193a431267be33-0f6f444745d8df-26011851-1327104-193a431267c122c%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%22193a431267be33-0f6f444745d8df-26011851-1327104-193a431267c122c%22%7D',
    'sajssdk_2020_cross_new_user': '1',
    'utoken': '1YKPTP5Q52YTXDPEBLP6X9A9QN2OB02B',
    'username': '%E6%9C%A8%E5%87%BA%E5%B9%BD%E6%9E%97',
    'export_notice': 'true',
    'Hm_lpvt_42317524c1662a500d12d3784dbea0f8': '1733633220',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': 'btoken=5KMYQOHNBOVEY8R9VBT9YCPX912260AF; Hm_lvt_42317524c1662a500d12d3784dbea0f8=1733626505; HMACCOUNT=4588BDFCE42D6B53; hy_data_2020_id=193a431267be33-0f6f444745d8df-26011851-1327104-193a431267c122c; hy_data_2020_js_sdk=%7B%22distinct_id%22%3A%22193a431267be33-0f6f444745d8df-26011851-1327104-193a431267c122c%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%22193a431267be33-0f6f444745d8df-26011851-1327104-193a431267c122c%22%7D; sajssdk_2020_cross_new_user=1; utoken=1YKPTP5Q52YTXDPEBLP6X9A9QN2OB02B; username=%E6%9C%A8%E5%87%BA%E5%B9%BD%E6%9E%97; export_notice=true; Hm_lpvt_42317524c1662a500d12d3784dbea0f8=1733633220',
    'origin': 'https://www.xiniudata.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.xiniudata.com/project/lib',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

json_data = {
    'payload': 'LBcnV1QrNXhyGnsLewQEDHMRBBYVcBN6GwhmCmcMEGN1ZAwICXZ2CR1jdWB9BmEAeR90Bht+dkokOTckZ3MQY3VRIUFZNy82ISA2cA1neWtAIV9ZXDwzUCwgNiw5MVttexcoWV4pIjsnOzErTCo7LhB4FFhQPDNIJSE8KjosAH91GWZPRTQuPyYmIypRKzAnVT5fR1Endh5vJjU+Pj9YPD9SIhocbBISfQMAAXASd2UQPExcUzA3Wik9Oi90aRA8P10+UEMgLC4wJipgFGciLFs8U0xQPCxbb2JwKyMtRy45Ui5NXioneGRjMyxSPz0tSD9cTF4hdh5vLCElOi5VNzBGZhQSJiIuKykoKl8jLS5BdhoWUic1SzgrITgvMFxtCkg=',
    'sig': '9B1A798BF1DF8455A1B89FF4F2D41A5C',
    'v': 1,
}

response = requests.post(
    'https://www.xiniudata.com/api2/service/x_service/person_company4_list/list_companies4_list_by_codes',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
# data = '{"payload":"LBcnV1QrNXhyGnsLewQEDHMRBBYVcBN6GwhmCmcMEGN1ZAwICXZ2CR1jdWB9BmEAeR90Bht+dkokOTckZ3MQY3VRIUFZNy82ISA2cA1neWtAIV9ZXDwzUCwgNiw5MVttexcoWV4pIjsnOzErTCo7LhB4FFhQPDNIJSE8KjosAH91GWZPRTQuPyYmIypRKzAnVT5fR1Endh5vJjU+Pj9YPD9SIhocbBISfQMAAXASd2UQPExcUzA3Wik9Oi90aRA8P10+UEMgLC4wJipgFGciLFs8U0xQPCxbb2JwKyMtRy45Ui5NXioneGRjMyxSPz0tSD9cTF4hdh5vLCElOi5VNzBGZhQSJiIuKykoKl8jLS5BdhoWUic1SzgrITgvMFxtCkg=","sig":"9B1A798BF1DF8455A1B89FF4F2D41A5C","v":1}'
# response = requests.post(
#    'https://www.xiniudata.com/api2/service/x_service/person_company4_list/list_companies4_list_by_codes',
#    cookies=cookies,
#    headers=headers,
#    data=data,
# )

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
# data = '{"payload":"LEg=","sig":"4DA6328ED82E464C7C1A9735C490F9E0","v":1}'
# response = requests.post(
#    'https://www.xiniudata.com/api2/service/x_service/person_user/get_user_info',
#    cookies=cookies,
#    headers=headers,
#    data=data,
# )
# print(response.text)
# print(response.json().get('d'))

encrypt_data = response.json().get('d')

print(encrypt_data)

with open('./heei3k/js/xiniushuju.js', 'r', encoding='utf-8') as f:
    js_code = f.read()

decode_data = execjs.compile(js_code).call('decrypt', encrypt_data)

print(decode_data)
