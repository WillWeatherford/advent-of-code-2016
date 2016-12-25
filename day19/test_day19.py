"""Tests for Advent of Code solution."""
from __future__ import unicode_literals, division
import pytest
from .solution_day19 import (
    rotate_remove,
    rotate_pop,
    rotate_pop_rotate,
    # divide_and_join,
    alternate,
)


CASES = [
    (),
]


FUNCS = (
    # divide_and_join,
    rotate_remove,
    rotate_pop,
    rotate_pop_rotate,
    alternate,
)

# @pytest.mark.parametrize('', CASES)
# def test_part1():
#     """Test that part1 function returns expected result."""


@pytest.mark.parametrize('func', FUNCS)
def test_part2(func):
    """Test that part1 function returns expected result."""
    assert func(5) == 2
    assert func(8) == 7
