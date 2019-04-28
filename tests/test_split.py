# -*- coding: utf-8 -*-

import pytest

from src.split import split


@pytest.mark.parametrize("s, sep, maxsplit", [
    ("aaaaaaaa", "a", 0),
    ("aaaaaaaa", "a", None),
    ("aaaaaaaa", "a", 0),
    ("aaaaaaaa", "a", 3),
    ("abcdef", "a", None),
    ("bcdefa", "bc", None),
    ("a b c d e f", " ", 3),
    ("a b c d e f", " ", 300),
    ("a b c d e f", " ", None),
    ("a b c d e f", None, None),
    ("abcdefgf", "f", None),
    ("abcdefg", "AA", None),
    ("aaaafffffaaaa", "aaaa", None),
    ("aaaafffffaaaa", "ffff", None),
    ("a", "abcdef", None),
    ("", "abcdef", None),
    # TODO: 还有测试场景未覆盖
    # ("a b  c d    e f ", None, None),
])
def test_split(s, sep, maxsplit):
    if maxsplit is not None:
        assert s.split(sep, maxsplit) == split(s, sep, maxsplit)
    else:
        assert s.split(sep) == split(s, sep)
