# -*- coding: utf-8 -*-
# @Time : 2021/5/26 10:49 PM
# @Author: lixiaomeng_someday
# @Email : 131xxxx119@163.com
# @File : test_ci.py


def sum(a, b):
    return a + b


def test_sum():
    assert 3 == sum(1, 2)

