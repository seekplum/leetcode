#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import pytest


def main():
    # parametrize 中需要对每个测试用例指定id,对应不上会导致整个test文件无法运行
    curr_path = os.path.dirname(os.path.abspath(__file__))

    file_path = os.path.join(curr_path, "tests",
                             "test_longest_palindromic_substring.py::test_longest_palindrome")

    if len(sys.argv) > 1:
        args = " ".join(sys.argv[1:])
    elif (file_path.endswith(".py") and os.path.exists(file_path)) or (not file_path.endswith(".py")):
        args = file_path
    else:
        args = curr_path
    print("*" * 100)
    print("测试文件: %s" % args)
    print("*" * 100)

    pytest.main(args)


if __name__ == '__main__':
    main()
