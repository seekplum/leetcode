# -*- coding: utf-8 -*-
"""兼容Python2和Python3
"""
import sys

PY3 = sys.version_info[0] == 3
if PY3:
    xrange = range
else:
    xrange = xrange
