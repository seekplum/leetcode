#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: leetcode
#     FileName: character_combination
#         Desc: 计算数字字符串可能的组合
#               假设有小写字母 a-z 分别对应 1-26，比如1->a 12-> ab 或者 l, 那么给定一串数字字符串，问其原来的字母串有多少种可能？
#       Author: seekplum
#        Email: 1131909224m@sina.cn
#     HomePage: seekplum.github.io
#       Create: 2018-05-10 22:45
#=============================================================================
"""


def num_decoding(s):
    """计算数字字符串解码次数

    :param s:  数字字符串
    :type s: str
    :example s: "1234567"

    :rtype int
    :return 解码次数
    :example 3
    """
    if s is None or s == "" or s[0] == "0":
        return 0

    n = len(s)
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        first = int(s[i - 1])
        second = int(s[i - 2: i])
        if first > 0:
            dp[i] += dp[i - 1]
        if 10 <= second <= 26:
            dp[i] += dp[i - 2]
    return dp[n]
