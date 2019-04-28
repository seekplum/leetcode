#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: leetcode
#     FileName: add_two_numbers
#         Desc: 给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表
#               你可以假设除了数字 0 之外，这两个数字都不会以零开头
#               示例：
#               输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
#               输出：7 -> 0 -> 8
#               原因：342 + 465 = 807
#       Author: seekplum
#        Email: 1131909224m@sina.cn
#     HomePage: seekplum.github.io
#       Create: 2018-05-09 23:07
#=============================================================================
"""

import json


class ListNode(object):
    """节点树
    """

    def __init__(self, val):
        """初始化参数

        :param val: 节点的值
        :type val int
        """
        self.val = val
        self.next_node = None


def add_two_numbers(node1, node2):
    """两个节点树进行相加

    :param node1: 节点树1
    :type node1: ListNode

    :param node2: 节点树2
    :type node2: ListNode

    :rtype: ListNode
    :return 相加后的节点树
    """
    carry = 0  # 需要进位的值
    root = node = ListNode(0)  # 初始化两个节点
    # 当两个树中任一树还有值或者还需要进位处理
    while node1 or node2 or carry:
        val1 = val2 = 0
        if node1:
            val1 = node1.val
            node1 = node1.next_node

        if node2:
            val2 = node2.val
            node2 = node2.next_node

        # 处理相加大于 10 需要进位的情况
        carry, value = divmod(val1 + val2 + carry, 10)

        # 把结果重新存入树中
        node.next_node = ListNode(value)
        node = node.next_node
    return root.next_node


def string_to_node(line):
    """把字符串转成节点树

    :param line 输入的数据
    :type line str

    :rtype ptr ListNode
    :return ptr 节点树
    """
    # 解析输入数据
    numbers = json.loads(line)

    # 根节点
    dummy_root = ListNode(0)
    ptr = dummy_root

    # 针对输入的每个值存放到树中
    for number in numbers:
        # 每次把下节点的信息存在当前节点
        ptr.next_node = ListNode(number)

        # 把下个节点信息中重新赋值给节点
        ptr = ptr.next_node

    ptr = dummy_root.next_node
    return ptr


def node_to_string(node):
    """把节点树转成平面数据

    :param node 节点树
    :type node ListNode
    """
    if not node:
        return "[]"

    result = []
    while node:
        result.append(node.val)
        node = node.next_node
    return str(result)
