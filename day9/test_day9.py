"""Tests for Advent of Code solution."""
from __future__ import unicode_literals, division
import pytest

CASES = [
    ('', 0, 0),
    ('A', 1, 1),
    ('ABC', 3, 3),
    ('(3x3)XYZ', 9, 9),
    ('X(8x2)(3x3)ABCY', 18, 20),
    ('(27x12)(20x12)(13x14)(7x10)(1x12)A', 324, 241920),
    ('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', 238, 445),
    ('(5x3)(8x2)abcdefgh', 23, 8),
]


@pytest.mark.parametrize('string, shallow, recursive', CASES)
def test_part1(string, shallow, recursive):
    """Test that part1 function returns expected result."""
    from .solution_day9 import decompress
    assert sum(decompress(string, False)) == shallow


@pytest.mark.parametrize('string, shallow, recursive', CASES)
def test_part2(string, shallow, recursive):
    """Test that part1 function returns expected result."""
    from .solution_day9 import decompress
    assert sum(decompress(string, True)) == recursive
