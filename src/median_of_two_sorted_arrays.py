#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: leetcode
#     FileName: median_of_two_sorted_arrays
#         Desc: 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2
#               请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n))
#               示例 1:
#                   nums1 = [1, 3]
#                   nums2 = [2]
#                   中位数是 2.0
#               示例 2:
#                   nums1 = [1, 2]
#                   nums2 = [3, 4]
#                   中位数是 (2 + 3)/2 = 2.5
#       Author: seekplum
#        Email: 1131909224m@sina.cn
#     HomePage: seekplum.github.io
#       Create: 2018-05-11 14:17
#=============================================================================
"""


def _check_even(number):
    """检查数字是否为偶数

    :param number 要检查的数字
    :type number int

    :rtype bool
    :return
        True: 数字是偶数
        False: 数字是奇数
    """
    result = False
    if number % 2 == 0:
        result = True
    return result


def find_median_sorted_arrays(nums1, nums2):
    """查找两个有序数组的中位数

    对于两个数组长度之和是偶数，那么中位数就会有两个，需要取两个数的平均值

    :param nums1 有序数组1
    :type nums1: List[int]

    :param nums2 有序数组2
    :type nums2: List[int]
    :rtype: float
    """
    m = len(nums1)
    n = len(nums2)
    if m == 0 and n == 0:
        return 0

    total = m + n

    # 数组长度之和为偶数
    if _check_even(total):
        return (_find_median(nums1, 0, nums2, 0, total / 2) + _find_median(nums1, 0, nums2, 0, total / 2 + 1)) / 2.0
    # 数组长度之和为奇数
    else:
        return _find_median(nums1, 0, nums2, 0, total / 2 + 1)


def _find_median(nums1, i, nums2, j, k):
    """查两个人有序数组中的第 k 位数

    :param nums1 有序数组1
    :type nums1: List[int]

    :param i 数组 1 当前指针所在下标
    :type i int

    :param nums2 有序数组2
    :type nums2: List[int]

    :param j 数组 2 当前指针所在下标
    :type j int

    :param k 两个数组归并排序后的第k位
    :type k int


    :rtype int
    :return 第 k 位数的值
    """
    m = len(nums1)
    n = len(nums2)

    # 首先确保数组1的长度小于等于数组2长度
    if (m - i) > (n - j):
        return _find_median(nums2, j, nums1, i, k)

    # 1 数组为空，直接在 2 数组中进行查找
    if m == i:
        return nums2[j + k - 1]

    # 如果 k = 1, 那么说明是找第一个值
    if k == 1:
        return min(nums1[i], nums2[j])

    # 因为数组有序，那么进行二分查找
    # 注意数组 1 的长度，不要越界
    p1 = min(m, i + k / 2)
    p2 = j + k - p1 + i

    # 如果 1 的 目标 小于 2 中的目标，那么在 1 的后面和 2 的前面开始查找
    if nums1[p1 - 1] < nums2[p2 - 1]:
        return _find_median(nums1, p1, nums2, j, k - p1 + i)
    # 如果 1 的 目标 大于 2 中的目标，那么在 1 的前面和 2 的后面开始查找
    elif nums1[p1 - 1] > nums2[p2 - 1]:
        return _find_median(nums1, i, nums2, p2, k - p2 + j)
    # 如果 1 的 目标 刚好在 2 的目录和 2 的目标前一位中间，那么这就是要找的 k
    else:
        return nums1[p1 - 1]


def test():
    # nums1, nums2 = [1, 2, 3, 4, 5], [1, 4]
    # nums1, nums2 = [4], [1, 4]
    nums1, nums2 = [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]
    # nums1, nums2 = [1, 2], [3, 4]
    # nums1, nums2 = [1], [2]
    # result = _find_median(nums1, nums2, 3, True)
    result = find_median_sorted_arrays(nums1, nums2)
    print result


if __name__ == '__main__':
    test()
