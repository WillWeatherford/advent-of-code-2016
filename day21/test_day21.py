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


def test_reverse_positions():
    from .solution_day21 import reverse_positions
    assert reverse_positions('edcba', 0, 4) == 'abcde'


def test_move_position():
    from .solution_day21 import move_position
    assert move_position('bcdea', 1, 4) == 'bdeac'
    assert move_position('bdeac', 3, 0) == 'abdec'
