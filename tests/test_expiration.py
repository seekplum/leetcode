# -*- coding: utf-8 -*-

import pytest

from src.expiration import is_it_leap_year
from src.expiration import getExpirationDate


@pytest.mark.parametrize("year, result", [
    (1, False),
    (4, True),
    (5, False),
    (8, True),
    (9, False),
    (10, False),
    (11, False),
    (12, True),
    (100, False),
    (200, False),
    (300, False),
    (400, True),
])
def test_is_it_leap_year(year, result):
    """测试判断闰年函数
    """
    assert is_it_leap_year(year) == result


@pytest.mark.parametrize("year, month, day, result", [
    (2016, 1, 28, [2016, 2, 28]),
    (2016, 1, 29, [2016, 2, 29]),
    (2016, 1, 30, [2016, 2, 29]),
    (2016, 1, 31, [2016, 2, 29]),

    (2016, 11, 10, [2016, 12, 10]),
    (2016, 12, 10, [2017, 1, 10]),

    (2017, 1, 28, [2017, 2, 28]),
    (2017, 1, 29, [2017, 2, 28]),
    (2017, 1, 30, [2017, 2, 28]),
    (2017, 1, 31, [2017, 2, 28]),

    (2017, 11, 30, [2017, 12, 30]),
    (2017, 10, 30, [2017, 11, 30]),
    (2017, 10, 31, [2017, 11, 30]),

    (2017, 12, 31, [2018, 1, 31]),
])
def test_getExpirationDate(year, month, day, result):
    """测试获取一个月到期日函数
    """
    assert getExpirationDate(year, month, day) == result
