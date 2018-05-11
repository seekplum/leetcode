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
    from add_two_numbers import string_to_node, node_to_string, add_two_numbers
    l1 = string_to_node(line1)
    l2 = string_to_node(line2)

    node = add_two_numbers(l1, l2)

    assert list(result) == list(node_to_string(node))
