#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: leetcode
#     FileName: test_longest_palindromic_substring
#         Desc: 测试查找最长回文字符串
#       Author: seekplum
#        Email: 1131909224m@sina.cn
#     HomePage: seekplum.github.io
#       Create: 2018-05-13 12:09
#=============================================================================
"""

import pytest


@pytest.mark.parametrize("s, result", [
    ("a", "a"),
    ("ab", "b"),
    ("aa", "aa"),
    ("aaa", "aaa"),
    ("aaaa", "aaaa"),
    ("aba", "aba"),
    ("aab", "aa"),
    ("abb", "bb"),
    ("abbd", "bb"),
    ("abbba", "abbba"),
    ("abbbag", "abbba"),
    ("abbbbag", "abbbba"),
    ("abaaba", "abaaba"),
    ("abccac", "cac"),
    ("abccacc", "ccacc"),
    ("abcdcba", "abcdcba"),
    ("abcddcba", "abcddcba"),
    ("abcdddcba", "abcdddcba"),
    ("ababababa", "ababababa"),
])
def test_longest_palindrome(s, result):
    """测试查找最长回文字符串

    :param s 要被查找的字符串
    :type s str

    :param result 预期结果
    :type result str
    """
    from longest_palindromic_substring import longest_palindrome
    assert result == longest_palindrome(s)
