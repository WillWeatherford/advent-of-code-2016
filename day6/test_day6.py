"""Tests for Advent of Code solution."""
from __future__ import unicode_literals, division
import pytest

CASES = [
    (['easy'], 'easy', 'easy'),
    (['easy', 'hard', 'etsy'], 'easy', 'htrd'),
    (['eedadn',
      'drvtee',
      'eandsr',
      'raavrd',
      'atevrs',
      'tsrnev',
      'sdttsa',
      'rasrtv',
      'nssdts',
      'ntnada',
      'svetve',
      'tesnvt',
      'vntsnd',
      'vrdear',
      'dvrsen',
      'enarar'], 'easter', 'advent'),
]


@pytest.mark.parametrize('lines, normal, modified', CASES)
def test_most_common_normal(lines, normal, modified):
    """Test that most_common_per_index function returns expected result."""
    from .solution_day6 import most_common_per_index
    assert most_common_per_index(lines, reverse=False) == normal


@pytest.mark.parametrize('lines, normal, modified', CASES)
def test_most_common_modified(lines, normal, modified):
    """Test that most_common_per_index function returns expected result."""
    from .solution_day6 import most_common_per_index
    assert most_common_per_index(lines, reverse=True) == modified
