# -*- coding: utf-8 -*-
"""
#=============================================================================
#  ProjectName: expiration
#     FileName: __init__.py
#       Author: seekplum
#        Email: huangjiandong95@sina.com
#         Desc: 计算订单到期时间
#     HomePage: seekplum.github.io
#       Create: 2019-04-23 21:25
#=============================================================================
"""

from __future__ import division, unicode_literals

from enum import IntEnum
from enum import unique


@unique
class DateMonth(IntEnum):
    """所有月份
    """
    Jan = 1
    Feb = 2
    Mar = 3
    Apr = 4
    May = 5
    Jun = 6
    Jul = 7
    Aug = 8
    Sep = 9
    Oct = 10
    Nov = 11
    Dec = 12


class DateDay(IntEnum):
    """月份对应的天数
    """
    Jan = 31
    Feb = 28
    Mar = 31
    Apr = 30
    May = 31
    Jun = 30
    Jul = 31
    Aug = 31
    Sep = 30
    Oct = 31
    Nov = 30
    Dec = 31


def is_it_leap_year(year):
    """判断年份是否为闰年

    判断标准：
        1.能整除4且不能整除100
        2.能整除400
    :param year: 年份
    :type year int

    :rtype bool
    :return:
        True: 该年份是闰年
        False: 该年份不是闰年，是平年
    """
    return True if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else False


def getExpirationDate(year, month, day):
    """计算订单的到期日，订购时长为一个月

    :param year: 年份
    :type year int

    :param month: 月份
    :type month int

    :param day: 日期号
    :type day int

    :rtype list
        [年, 月, 日]
    :return: 到期的时间
    """
    # 12月份的下一个月是一年
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1

    # 获取下一个月的天数
    next_month_day = getattr(DateDay, DateMonth(month).name).value

    # 闰年 2 月会多一天，天数是 29
    if month == DateMonth.Feb and is_it_leap_year(year):
        next_month_day += 1

    # 当前日期号大于下一个月的，不能超过下一个月天数
    if day >= next_month_day:
        day = next_month_day
    return [year, month, day]
