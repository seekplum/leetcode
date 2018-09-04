#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: leetcode
#     FileName: test_character_combination
#         Desc: 测试字符串解码后有多少种可能
#       Author: seekplum
#        Email: 1131909224m@sina.cn
#     HomePage: seekplum.github.io
#       Create: 2018-09-04 23:55
#=============================================================================
"""

import pytest


@pytest.mark.parametrize("s, result", [
    ("12345", 3),
    ("1234510", 3),
    ("1234520", 3),
    ("1234526", 6),
])
def test_add_two_numbers(s, result):
    """测试两数相加

    :param s:  数字字符串
    :type s: str
    :example s: "1234567"

    :param result: 解码次数
    :type result int
    :example 3
    """
    from character_combination import num_decoding
    assert num_decoding(s) == result
