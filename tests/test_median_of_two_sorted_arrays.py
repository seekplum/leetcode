#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: leetcode
#     FileName: test_median_of_two_sorted_arrays
#         Desc: 测试查找两个数组的中位数
#       Author: seekplum
#        Email: 1131909224m@sina.cn
#     HomePage: seekplum.github.io
#       Create: 2018-05-11 14:17
#=============================================================================
"""

import pytest


@pytest.mark.parametrize("nums1, nums2, result", [
    ([1], [2], 1.5),
    ([1], [2, 3], 2),
    ([1], [1, 2, 3], 1.5),
    ([1], [2, 3, 4, 5, 6, 7], 4),
    ([1], [1, 2, 3, 4, 5, 6, 7], 3.5),
    ([1, 2], [1, 2, 3, 4, 5, 6, 7], 3),
    ([1, 2, 3], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4),
    ([4], [1, 2, 3, 5, 6], 3.5),
    ([4], [1, 2, 3, 5, 6, 7], 4),
    ([1, 4], [3], 3),
    ([3], [1, 4], 3),
    ([1, 2], [3, 4], 2.5),
    ([1, 2, 3, 4, 5], [1, 4], 3),
    ([1, 2, 3, 4], [1, 2, 3, 4], 2.5),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 3)
])
def test_find_median_sorted_arrays(nums1, nums2, result):
    from median_of_two_sorted_arrays import find_median_sorted_arrays
    assert result == find_median_sorted_arrays(nums1, nums2)
