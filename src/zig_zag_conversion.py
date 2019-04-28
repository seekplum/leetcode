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


class Solution(object):
    """转换字符串
    """

    def convert(self, s, numRows):
        """转换字符串

        解题思路:
            由描述可知，在 (2 * numRows) - 1 后会有一次循环。第一行的元素位置对应原下标未 0, ((2 * numRows) - 1 -1 ) * n
        :type s: str
        :type numRows: int
        :rtype: str
        """
        pass
