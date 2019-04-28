# -*- coding: utf-8 -*-


"""
#=============================================================================
#  ProjectName: leetcode
#     FileName: the_difference_between_two_sorted_arrays
#         Desc: 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2
#               请找出这 存在nums1数组中，但是不存在nums2数组中的所有数字,要求算法的时间复杂度为 O(log (m+n))
#               示例 1:
#                   nums1 = [1, 3]
#                   nums2 = [2, 3]
#                   结果是 [1]
#       Author: seekplum
#        Email: 1131909224m@sina.cn
#     HomePage: seekplum.github.io
#       Create: 2019-04-26 19:03
#=============================================================================
"""


# def check(num, pos):
#     return 1 if num >= b[pos] else 0
#
#
# # l = 0
# # r = len(b)
# def divide(l, r, num):
#     while l <= r:
#         mid = (l + r) / 2
#         result = check(num, mid)
#         if result == 1:
#             r = mid - 1
#         elif result == 0:
#             l = mid + 1
#
#     return num == b[l]


def divide(nums1, nums2):
    """查存在nums1但不存在nums2的所有元素
    """
    result = []
    i = 0
    j = 0
    length1 = len(nums1)
    length2 = len(nums2)
    while i < length1 and j < length2:
        num1 = nums1[i]
        num2 = nums2[j]
        if num1 < num2:
            result.append(num1)
            i += 1
        elif num1 > num2:
            j += 1
        else:
            i += 1
            j += 1
    # 处理 nums1 数组中还有元素未对比的情况
    result.extend(nums1[i:])
    return result
