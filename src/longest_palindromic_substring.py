#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: leetcode
#     FileName: longest_palindromic_substring
#         Desc: 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。
#               示例 1：
#               输入: "babad"
#               输出: "bab"
#               注意: "aba"也是一个有效答案。
#               示例 2：
#               输入: "cbbd"
#               输出: "bb"
#       Author: seekplum
#        Email: 1131909224m@sina.cn
#     HomePage: seekplum.github.io
#       Create: 2018-05-13 12:08
#=============================================================================
"""


def longest_palindrome(s):
    """查找字符串中最长的回文字符串
    """
    if not s:
        return ""
    start = 0
    end = 0
    for i in xrange(len(s)):
        len1 = expand_around_center(s, i, i)
        len2 = expand_around_center(s, i, i + 1)
        length = max(len1, len2)
        if length > (end - start):
            start = i - (length - 1) / 2
            end = i + length / 2
    return s[start: end + 1]


def expand_around_center(s, left, right):
    """计算回文长度
    """
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1
