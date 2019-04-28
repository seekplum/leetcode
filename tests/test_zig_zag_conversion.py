# -*- coding: utf-8 -*-

import pytest

from src.zig_zag_conversion import Solution


@pytest.mark.parametrize("s, numRows, result", [
    ("LEETCODEISHIRING", 3, "LCIRETOESIIGEDHN"),
    ("", 3, ""),
    ("LEETCODEISHIRING", 0, "LEETCODEISHIRING")
])
def test_convert(s, numRows, result):
    sol = Solution()
    assert sol.convert(s, numRows) == result
