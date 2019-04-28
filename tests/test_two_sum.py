#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: leetcode
#     FileName: test_two_sum
#         Desc: 测试查找两数之和
#       Author: seekplum
#        Email: 1131909224m@sina.cn
#     HomePage: seekplum.github.io
#       Create: 2018-05-11 09:14
#=============================================================================
"""

import pytest

from src.two_sum import two_sum1
from src.two_sum import two_sum2


@pytest.mark.parametrize("nums, target, result", [
    ([1, 2, 3, 4, 5], 5, [0, 3]),
    ([1, 2, 3, 4, 5], 10, None),
])
def test_two_sum1(nums, target, result):
    """测试查找两数之和

    :param nums 被查找的列表
    :type nums: list [int]

    :param target 要找到的目标数字
    :type target: int

    :param result 预期结果
    :type result int
    """
    assert two_sum1(nums, target) == result


@pytest.mark.parametrize("nums, target, result", [
    ([1, 2, 3, 4, 5], 5, [1, 2]),
    ([1, 2, 3, 4, 5], 10, None),
])
def test_two_sum2(nums, target, result):
    """测试查找两数之和

    :param nums 被查找的列表
    :type nums: list [int]

    :param target 要找到的目标数字
    :type target: int

    :param result 预期结果
    :type result int
    """
    assert two_sum2(nums, target) == result
