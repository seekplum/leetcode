#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: leetcode
#     FileName: add_two_numbers
#         Desc: 测试两个树相加
#       Author: seekplum
#        Email: 1131909224m@sina.cn
#     HomePage: seekplum.github.io
#       Create: 2018-05-11 09:32
#=============================================================================
"""

import pytest


@pytest.mark.parametrize("line1, line2, result", [
    ("[1, 1]", "[1, 1]", "[2, 2]"),
    ("[1, 2, 3, 4, 9]", "[1, 1]", "[2, 3, 3, 4, 9]"),
    ("[5, 4, 3]", "[7, 8, 9]", "[2, 3, 3, 1]")
])
def test_add_two_numbers(line1, line2, result):
    """测试两数相加

    :param line1: 输入的字符串数组1
    :type line1 str

    :param line2: 输入的字符串数组2
    :type line2 str

    :param result: 预期结果
    :type result str
    """
    from add_two_numbers import string_to_node, node_to_string, add_two_numbers
    node1 = string_to_node(line1)
    node2 = string_to_node(line2)

    node = add_two_numbers(node1, node2)

    assert list(result) == list(node_to_string(node))
