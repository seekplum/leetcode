# -*- coding: utf-8 -*-

import pytest

from src.zig_zag_conversion import Solution


@pytest.mark.parametrize("s, numRows", [
    ("LEETCODEISHIRING", "")
])
def test_convert(s, numRows):
    sol = Solution()
    assert not sol.convert(s, numRows)
