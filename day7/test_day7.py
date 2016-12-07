"""Tests for Advent of Code solution."""
from __future__ import unicode_literals, division
import pytest

CASES = [
    (),
]


PARTS_CASES = [
    ('a[b]c', {'a', 'c'}, {'b'}),
    ('asd[vbnm]xc', {'asd', 'xc'}, {'vbnm'}),
    ('a[b]x[y]c', {'a', 'x', 'c'}, {'b', 'y'}),
    ('out1[in1]out2[in2]out3[in3]out4[in4]out5',
     {'out1', 'out2', 'out3', 'out4', 'out5'},
     {'in1', 'in2', 'in3', 'in4'}
     ),
]


@pytest.mark.parametrize('line, outsides, insides', PARTS_CASES)
def test_parse_parts(line, outsides, insides):
    """Test that parse_parts returns sets of inside and outside parts."""
    from .solution_day7 import parse_parts
    assert parse_parts(line) == (outsides, insides)


@pytest.mark.parametrize('', CASES)
def test_part1():
    """Test that part1 function returns expected result."""


@pytest.mark.parametrize('', CASES)
def test_part2():
    """Test that part1 function returns expected result."""
