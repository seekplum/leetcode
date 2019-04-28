#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: leetcode
#     FileName: zig_zag_conversion
#         Desc: 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
#
#               比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
#
#               L   C   I   R
#               E T O E S I I G
#               E   D   H   N
#
#               之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
#       Author: seekplum
#        Email: 1131909224m@sina.cn
#     HomePage: seekplum.github.io
#       Create: 2019-03-05 20:39
#=============================================================================
"""

from .compat import xrange


class Solution(object):
    """转换字符串
    """

    def convert(self, s, numRows):
        """转换字符串

        解题思路:
            记 k = 2 * (numRows - 1)
            由描述可知，每k个字符有一次循环。
            第一行: 0, k, 2k, ..., n * k
            第二行: 1, 2k - 1, 2k + 1, 3k -1, 3k + 2..., n * k
            第三行: 2, k, 2k, ..., n * k
            第numRow -1行: numRow - 1, k + numRow - 1, 2k + numRow - 1, ..., n * k + numRow - 1

        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = []
        if numRows <= 1:
            return s
        n = numRows * 2 - 2
        length = len(s)
        for i in xrange(numRows):
            for j in xrange(0, length, n):
                if i + j < length:
                    result.append(s[i + j])
                if i % (n / 2) != 0 and j + n - i < length:
                    result.append(s[j + n - i])
        return "".join(result)
