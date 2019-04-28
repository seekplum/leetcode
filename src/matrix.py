#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
题目：转圈打印一个矩阵
思路：利用两个斜对角坐标确定一个矩阵，每次打印最外层的一圈，打印结束后，两坐标向中心移动
结果：顺时针、逆时针打印出矩阵
"""

from __future__ import print_function


def print_clockwise_circle(matrix, tc, tr, dc, dr):
    """
    顺时针打印一圈内容
    :param matrix:
    :param tc: 起始点横坐标
    :param tr: 起始点纵坐标
    :param dc: 结束点横坐标
    :param dr: 结束点纵坐标
    :return:
    """
    i = tc  # 打印值的横坐标
    j = tr  # 要打印值的纵坐标
    if tr > dr or tc > dc:
        # 打印结束
        return None
    # 横着打印，横坐标增加，纵坐标不变
    while j <= dc:
        print(matrix[i][j], " ", end="")
        j += 1
    if tr == dr:
        return None
    j -= 1
    i += 1
    # 竖着打印，纵坐标减少，横坐标不变
    while i <= dr:
        print(matrix[i][j], " ", end="")
        i += 1
    if tc == dc:
        return None
    i -= 1
    j -= 1
    # 横着打印，横坐标减少，纵坐标不变
    while j >= tc:
        print(matrix[i][j], " ", end="")
        j -= 1
    j += 1
    i -= 1
    # 竖着打印，横坐标增加，纵坐标不变
    while i > tr:
        print(matrix[i][j], " ", end="")
        i -= 1
    return print_clockwise_circle(matrix, i + 1, j + 1, dc - 1, dr - 1)


def print_anticlockwise_circle(matrix, tc, tr, dc, dr):
    """
    逆时针打印一圈内容
    :param matrix:
    :param tc: 起始点横坐标
    :param tr: 起始点纵坐标
    :param dc: 结束点横坐标
    :param dr: 结束点纵坐标
    :return:
    """
    i = tc  # 打印值的横坐标
    j = tr  # 要打印值的纵坐标
    if tr > dr or tc > dc:
        # 打印结束
        return None
    # 竖着打印，纵坐标不变，横坐标增加
    while i <= dr:
        print(matrix[i][j], " ", end="")
        i += 1
    if tc == dc:
        return None
    i -= 1
    j += 1
    # 横着打印，横坐标不变，纵坐标增加
    while j <= dc:
        print(matrix[i][j], " ", end="")
        j += 1
    if tr == dr:
        return None
    j -= 1
    i -= 1
    # 竖着打印，横坐标减少，纵坐标不变
    while i >= tc:
        print(matrix[i][j], " ", end="")
        i -= 1
    i += 1
    j -= 1
    # 横着打印，横坐标不变，纵坐标减少
    while j > tr:
        print(matrix[i][j], " ", end="")
        j -= 1
    return print_anticlockwise_circle(matrix, i + 1, j + 1, dc - 1, dr - 1)


def get_matrix(m, n):
    """生成一个 m * n 的矩阵
    :param m: 行
    :param n: 列

    :return: m * n 的矩阵
    :rtype list
    """
    if m <= 0 or n <= 0:
        print("参数错误")
        return None
    matrix = []
    number = m * n
    res = []
    for i in range(1, number + 1):
        res.append(i)
        print(i, end="")
        if len(res) == m:
            print()
            matrix.append(res)
            res = []
    return matrix


def main():
    """
    主函数
    :return:
    """
    matrix = get_matrix(5, 5)
    tc = 0
    tr = 0
    dc = len(matrix[0]) - 1
    dr = len(matrix) - 1
    print("\n============= 顺时针转圈打印结果 =============")
    print_clockwise_circle(matrix, tc, tr, dc, dr)
    print("\n============= 逆时针转圈打印结果 =============")
    print_anticlockwise_circle(matrix, tc, tr, dc, dr)


if __name__ == '__main__':
    main()
