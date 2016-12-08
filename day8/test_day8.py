"""Tests for Advent of Code solution."""
from __future__ import unicode_literals, division
import pytest

RECT_CASES = [
    (
        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]],
        1, 1,
        [[1, 0, 0],
         [0, 0, 0],
         [0, 0, 0]],
    ),
    (
        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]],
        2, 2,
        [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 0]],
    ),
]


ROTATE_ROW_CASES = [
    (
        [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 0]],
        1, 1,
        [[1, 1, 0],
         [0, 1, 1],
         [0, 0, 0]],
    ),
    (
        [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 0]],
        1, 2,
        [[1, 1, 0],
         [1, 0, 1],
         [0, 0, 0]],
    ),
]


ROTATE_COL_CASES = [
    (
        [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 0]],
        1, 1,
        [[1, 0, 0],
         [1, 1, 0],
         [0, 1, 0]],
    ),
    (
        [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 0]],
        1, 2,
        [[1, 1, 0],
         [1, 0, 0],
         [0, 1, 0]],
    ),
]


@pytest.mark.parametrize('start, cols, rows, result', RECT_CASES)
def test_rect(start, cols, rows, result):
    """Test that part1 function returns expected result."""
    from .solution_day8 import TinyDisplay
    dis = TinyDisplay()
    dis.grid = start
    dis.rect(cols, rows)
    assert dis.grid == result


@pytest.mark.parametrize('start, row, shifts, result', ROTATE_ROW_CASES)
def test_rotate_row(start, row, shifts, result):
    """Test that part1 function returns expected result."""
    from .solution_day8 import TinyDisplay
    dis = TinyDisplay()
    dis.height = len(start)
    dis.width = len(start[0])
    dis.grid = start
    dis.rotate_row(row, shifts)
    assert dis.grid == result


@pytest.mark.parametrize('start, col, shifts, result', ROTATE_COL_CASES)
def test_rotate_col(start, col, shifts, result):
    """Test that part1 function returns expected result."""
    from .solution_day8 import TinyDisplay
    dis = TinyDisplay()
    dis.height = len(start)
    dis.width = len(start[0])
    dis.grid = start
    dis.rotate_column(col, shifts)
    assert dis.grid == result

# @pytest.mark.parametrize('', )
# def test_part2():
#     """Test that part1 function returns expected result."""
