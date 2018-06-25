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

    思路：
        在遍历点的位置，左右发散向两边找，如果是回文字符串则继续，不是则遍历下一个位置
    """
    length = len(s)
    if length == 1:
        return s
    elif length > 1000:
        raise ValueError
    max_length = 1  # 子串最大长度
    result = s[0]  # 默认值为第一个元素
    for i in range(1, length):
        # 往左移元素起始点
        left_begin = i - 1

        # 往右移元素起始点
        right_begin = min(i + 1, length - 1)

        # 连续三个元素相等，取前两个再向两边移动
        if s[left_begin] == s[i] == s[right_begin]:
            sub_len, sub = find_palindrome(s, left_begin, right_begin)
            if sub_len > max_length:
                max_length, result = sub_len, sub

            sub_len, sub = find_palindrome(s, left_begin, i)
            if sub_len > max_length:
                max_length, result = sub_len, sub

            # sub_len, sub = find_palindrome(s, i, right_begin)
            # if sub_len > max_length:
            #     max_length, result = sub_len, sub
        else:
            # 和左边元素相等，右边开始位左移 1 位
            if s[left_begin] == s[i]:
                right_begin -= 1
            # 和右边元素相等，左边开始位再左移 1 位
            elif s[right_begin] == s[i]:
                left_begin += 1

            sub_len, sub = find_palindrome(s, left_begin, right_begin)
            if sub_len > max_length:
                max_length, result = sub_len, sub
    return result


def find_palindrome(s, left_begin, right_begin):
    """查找指定范围内字符串中的回文字符串

    :param s: 被查找的字符串
    :type s str

    :param left_begin: 左边开始查找的下标
    :type left_begin int

    :param right_begin: 右边开始查找的下标
    :type right_begin int

    :return: max_length 回文字符串长度
    :rtype max_length int

    :return: result 回文字符串内容
    :rtype result str
    """
    max_length = 1
    result = s[0]
    length = len(s)
    # 从遍历点位置分别往左右移动
    while 0 <= left_begin <= right_begin <= length - 1:
        sub = s[left_begin: right_begin + 1]
        # 遍历点左右的字符加起来是回文
        if check_is_palindrome(sub):
            # 记录结果
            sub_len = len(sub)
        else:
            break
        # 检查结果是否需要更新
        if sub_len > max_length:
            max_length = sub_len
            result = sub
        left_begin -= 1
        right_begin += 1
    return max_length, result


def check_is_palindrome(sub):
    """检查列表中存储的是否是回文字符串

    :param sub 要检查字符串内容
    :type sub str | list

    :rtype bool
    :return
        True: sub中的内容是回文字符串
        False: sub中的内容不是回文字符串
    """
    length = len(sub)
    if length == 1:
        return True
    elif length == 0:
        raise ValueError
    i_min, i_max = 0, length - 1
    # 从两边开始往中间移动，对比两个元素是否一致
    while i_min < i_max:
        if sub[i_min] != sub[i_max]:
            return False
        i_min += 1
        i_max -= 1
    return True


def longest_palindrome1(s):
    """查找字符串中最长的回文字符串
    """
    start = 0
    end = 0
    for i in range(len(s)):
        len1 = expand_around_center(s, i, i)
        len2 = expand_around_center(s, i, i + 1)
        length = max(len1, len2)
        if length > (end - start):
            start = i - (length - 1) / 2
            end = i + length / 2
    return s[start: end + 1]


def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        right -= 1
        left -= 1
    return right - left - 1


def test():
    """测试入口函数
    """
    s = "abbd"
    result = longest_palindrome(s)
    print result


if __name__ == '__main__':
    test()
