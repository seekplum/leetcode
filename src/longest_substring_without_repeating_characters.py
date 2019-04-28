#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: leetcode
#     FileName: longest_substring_without_repeating_characters
#         Desc: 给定一个字符串，找出不含有重复字符的最长子串的长度
#               示例：
#                   给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。
#                   给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。
#                   给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。
#       Author: seekplum
#        Email: 1131909224m@sina.cn
#     HomePage: seekplum.github.io
#       Create: 2018-05-11 13:18
#=============================================================================
"""


def length_of_longest_substring(s):
    """查找不包含重复字符串的最长子串

    :param s 被查找的字符串
    :type s: str
    :rtype: int
    """
    sub = []  # 记录遍历过的自创
    max_length = 0  # 子串最大长度
    # 依次遍历整个字符串
    for c in s:
        # 字符串如果已经重复，则比较长度，初始化子串
        if c in sub:
            # 记录最长的子串长度
            max_length = max(max_length, len(sub))
            # 针对已经重复的情况，需要找到最开始重复的位置，不重复的字符串需要保留
            sub = sub[sub.index(c) + 1:]
        sub.append(c)

    # 处理可能出现没有重复字符串情况
    max_length = max(max_length, len(sub))
    return max_length
