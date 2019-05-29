#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: leetcode
#     FileName: test
#         Desc: 测试函数
#       Author: seekplum
#        Email: 1131909224m@sina.cn
#     HomePage: seekplum.github.io
#       Create: 2018-05-10 22:45
#=============================================================================
"""

from __future__ import print_function

from collections import deque


def count_down(n):
    while n > 0:
        x = yield n
        print("count down: %d" % x)
        n -= 1


def count_up(n):
    while n > 0:
        y = yield n
        print("count up: %d" % y)
        n -= 1


class Task(object):
    def __init__(self):
        self._queue = deque()

    def add_task(self, task):
        self._queue.append((task, None))

    def run(self):
        while self._queue:
            task, msg = self._queue.popleft()
            try:
                data = task.send(msg)
            except StopIteration:
                pass
            else:
                self._queue.append((task, data))


def multi_thread():
    t = Task()
    d = count_down(10)
    u = count_up(5)
    t.add_task(d)
    t.add_task(u)
    t.run()


def merge(nums1, nums2):
    m = len(nums1) - 1
    n = len(nums2) - 1

    result = [0 for _ in xrange(m + n + 2)]
    while m >= 0 and n >= 0:
        index = m + n + 1
        if nums1[m] > nums2[n]:
            result[index] = nums1[m]
            m -= 1
        else:
            result[index] = nums2[n]
            n -= 1
    while m >= 0:
        result[m] = nums1[m]
        m -= 1
    while n >= 0:
        result[n] = nums2[n]
        n -= 1
    return result


if __name__ == '__main__':
    print(merge([1, 3, 5, 7], [1, 3, 6, 8]))
