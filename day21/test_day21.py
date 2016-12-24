"""Tests for Advent of Code solution."""
from __future__ import unicode_literals, division
import pytest

CASES = [
    (),
]


def test_swap_position():
    from .solution_day21 import swap_position
    assert swap_position('abcde', 4, 0) == 'ebcda'


def test_swap_letter():
    from .solution_day21 import swap_letter
    assert swap_letter('ebcda', 'd', 'b') == 'edcba'


def test_rotate_left():
    from .solution_day21 import rotate_left
    assert rotate_left('abcde', 1) == 'bcdea'


def test_rotate_right():
    from .solution_day21 import rotate_right
    assert rotate_right('abcde', 1) == 'eabcd'
    assert rotate_right('ecabd', 6) == 'decab'


def test_rotate_based():
    from .solution_day21 import rotate_based
    assert rotate_based('abdec', 'b') == 'ecabd'
    assert rotate_based('ecabd', 'd') == 'decab'
    assert rotate_based('0123456789', '4') == '4567890123'


def test_rotate_based_reverse():
    from .solution_day21 import rotate_based
    assert rotate_based('bca', 'b', reverse=True) == 'abc'
    assert rotate_based('abc', 'c', reverse=True) == 'abc'
    assert rotate_based('cab', 'a', reverse=True) == 'abc'
    assert rotate_based('ecabd', 'b', reverse=True) == 'abdec'
    assert rotate_based('4567890123', '4', reverse=True) == '0123456789'
    assert rotate_based('decab', 'd', reverse=True) == 'ecabd'


def test_reverse_positions():
    from .solution_day21 import reverse_positions
    assert reverse_positions('edcba', 0, 4) == 'abcde'


def test_move_position():
    from .solution_day21 import move_position
    assert move_position('bcdea', 1, 4) == 'bdeac'
    assert move_position('bdeac', 3, 0) == 'abdec'


def test_move_position_reverse():
    from .solution_day21 import move_position
    assert move_position('bdeac', 1, 4, reverse=True) == 'bcdea'
    assert move_position('abdec', 3, 0, reverse=True) == 'bdeac'
