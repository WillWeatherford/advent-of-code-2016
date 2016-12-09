"""Tests for Advent of Code solution."""
from __future__ import unicode_literals, division
import pytest

PART2_CASES = [
    ('(3x3)XYZ', len('XYZXYZXYZ')),
    ('X(8x2)(3x3)ABCY', len('XABCABCABCABCABCABCY')),
    ('(27x12)(20x12)(13x14)(7x10)(1x12)A', 241920),
    ('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', 445),
]


# @pytest.mark.parametrize('', CASES)
# def test_part1():
#     """Test that part1 function returns expected result."""


@pytest.mark.parametrize('string, result', PART2_CASES)
def test_part2(string, result):
    """Test that part1 function returns expected result."""
    from .solution_day9 import decompress
    assert sum(decompress(string, True)) == result


def test_specific():
    pass