#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/26 13:39
# @Author  : Lihua
# @Version : 1.0
# @Contact : heei3k@hotmail.com
# @File    : test_fixture.py
# @Software: PyCharm


import pytest


@pytest.fixture()
def fixture_demo():
    a = 'leo'
    return a


def test2(fixture_demo):
    assert fixture_demo == 'leo'


@pytest.fixture(scope='function', params=['成龙', '甄子丹', '李连杰'])
def my_fixture(request):
    print('前置')
    yield
    print('后置')
    return request.param


get_data = [(3, 4), (10, 20), (5, 15), (8, 12)]


class TestFixture:

    def test_case(self):
        print("ceshi1")

    def test_02_case(self, my_fixture):
        print("ceshi2")
        print("---------" + str(my_fixture))

    def test_allure(self):
        '''
        第一种allure报告提供测试title标题的方式:直接使用 '{a}'，带上我们的参数名称,记住不能使用‘f’
        :param a:
        :param b:
        :return:
        '''
        a, b = 3, 4
        assert a + b > 6
        print(a + b)


if __name__ == '__main__':
    pytest.main(['test_fixture.py'])
