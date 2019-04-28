#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: leetcode
#     FileName: two_sum
#         Desc: 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数
#               你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用
#               示例:
#               给定 nums = [2, 7, 11, 15], target = 9
#               因为 nums[0] + nums[1] = 2 + 7 = 9
#               所以返回 [0, 1]
#       Author: seekplum
#        Email: 1131909224m@sina.cn
#     HomePage: seekplum.github.io
#       Create: 2018-05-09 23:07
#=============================================================================
"""


def two_sum1(nums, target):
    """通过暴力的两层循环查询两数之和

    :param nums 被查找的列表
    :type nums: list [int]

    :param target 要找到的目标数字
    :type target: int

    :rtype: List[int]
    :return 两个数字的下标列表
    """
    # 第一层循环遍历的从第 1 个数到倒数第 2 数
    # 第二层循环中从第 2 个数开始遍历，依次对当前下标值前的所有值进行对比，看是否符合要求
    length = len(nums)
    for i in range(length - 1):
        for j in range(1, length):
            # 找到了符合要求的数据
            if (nums[i] + nums[j]) == target:
                return [i, j]
    return None


def two_sum2(nums, target):
    """通过hash，把遍历过的数据存在字典中，对比时从字典取值

    :param nums 被查找的列表
    :type nums: list [int]

    :param target 要找到的目标数字
    :type target: int

    :rtype: List[int]
    :return 两个数字的下标列表
    """
    hash_data = {}
    for val in nums:
        interval = target - val
        index = nums.index(val)
        if interval in hash_data:
            return [hash_data[interval], index]
        hash_data[val] = index
    return None
