#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: leetcode
#     FileName: test_longest_substring_without_repeating_characters
#         Desc: 测试查找字符串中的最长子串
#       Author: seekplum
#        Email: 1131909224m@sina.cn
#     HomePage: seekplum.github.io
#       Create: 2018-05-11 13:18
#=============================================================================
"""
import pytest

from src.longest_substring_without_repeating_characters import length_of_longest_substring

@pytest.mark.parametrize("s, max_length", [
    ("a", 1),
    ("aaa", 1),
    ("abcd", 4),
    ("abcdderf", 4),
    ("abcabca", 3),
    ("abac", 3),
    ("abcdafg", 6)
])
def test_length_of_long_substring(s, max_length):
    """测试查找最长子串长度

    :param s: 被查找的字符串
    :type s str

    :param max_length: 预期结果
    :type max_length int
    """
    assert max_length == length_of_longest_substring(s)
