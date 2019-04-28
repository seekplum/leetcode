# -*- coding: utf-8 -*-
import pytest

from src.expression import ExpressionEvaluator


@pytest.mark.parametrize("express, result", [
    ("2 + 3", 5),
    ("2 - 3", -1),
    ("2 * 3", 6),
    ("6 / 3", 2),
    ("4 + (14 + 7 - 3 * 5) / 6", 5),
    ("2 + (3 + 4 * 5) * 6", 140),
])
def test_parse(express, result):
    e = ExpressionEvaluator()
    assert e.parse(express) == result


@pytest.mark.parametrize("express", [
    "1 - - 2",
    "1 - + 2",
    "1 -",
    "-",
    "1 + (1 +"
    "1 + (1 + 1"
    "1 + 1 + 1)"
])
def test_parse_raise(express):
    with pytest.raises(SyntaxError):
        e = ExpressionEvaluator()
        e.parse(express)
