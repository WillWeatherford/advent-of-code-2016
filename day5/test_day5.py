"""Tests for Advent of Code solution."""
from __future__ import unicode_literals, division
import pytest

CASES = [
    ('abc', '18f47a30', '05ace8e3'),
]


SINGLE_CHAR_CASES = [
    (b'abc3231929', '1'),
    (b'abc5017308', '8'),
    (b'abc5357525', '4'),
]


@pytest.mark.parametrize('door_id, result1, result2', CASES)
def test_decode_password1(door_id, result1, result2):
    """Test that decode_password function returns expected result."""
    from .solution_day5 import decode_password1
    assert decode_password1(door_id) == result1


@pytest.mark.parametrize('door_id, result1, result2', CASES)
def test_decode_password2(door_id, result1, result2):
    """Test that decode_password function returns expected result."""
    from .solution_day5 import decode_password2
    assert decode_password2(door_id) == result2


@pytest.mark.parametrize('bytes_val, result', SINGLE_CHAR_CASES)
def test_get_hashed_hex(bytes_val, result):
    """Test that get_password_char function returns expected char."""
    from .solution_day5 import get_hashed_hex
    assert get_hashed_hex(bytes_val)[5] == result
