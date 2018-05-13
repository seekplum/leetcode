#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: leetcode
#     FileName: test_main
#         Desc: 测试主函数，可以直接通过python调用，进行debug，其他测试文件需要由pytest运行
#       Author: seekplum
#        Email: 1131909224m@sina.cn
#     HomePage: seekplum.github.io
#       Create: 2018-05-10 22:45
#=============================================================================
"""

import os

import pytest


def main():
    """测试文件主函数
    """
    # parametrize 中需要对每个测试用例指定id,对应不上会导致整个test文件无法运行
    curr_path = os.path.dirname(os.path.abspath(__file__))

    file_path = os.path.join(curr_path, "test.py")
    if os.path.exists(file_path):
        print "测试文件: {}".format(file_path)
        # 测试单个文件
        pytest.main(file_path)
    else:
        print "文件: {} 不存在".format(file_path)
        print "测试目录: {}".format(curr_path)
        # 测试整个目录下的文件
        pytest.main(curr_path)


if __name__ == '__main__':
    main()
