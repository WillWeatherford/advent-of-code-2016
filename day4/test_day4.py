"""Tests for Day 4."""
from __future__ import unicode_literals
import pytest

ROOM_CASES = [
    (
        'aaaaa-bbb-z-y-x-123[abxyz]',
        ('aaaaa-bbb-z-y-x', '123', 'abxyz'),
        123,
    ),
    (
        'a-b-c-d-e-f-g-h-987[abcde]',
        ('a-b-c-d-e-f-g-h', '987', 'abcde'),
        987,
    ),
    (
        'not-a-real-room-404[oarel]',
        ('not-a-real-room', '404', 'oarel'),
        404,
    ),
    (
        'totally-real-room-200[decoy]',
        ('totally-real-room', '200', 'decoy'),
        0,
    ),
]


NAME_CASES = [
    ('aaaaa-bbb-z-y-x', 'abxyz'),
    ('a-b-c-d-e-f-g-h', 'abcde'),
    ('not-a-real-room', 'oarel'),
]

ROTATE_NAME_CASES = [
    ('qzmt-zixmtkozy-ivhz-343', 'very encrypted name'),
]


@pytest.mark.parametrize('room, groups, real', ROOM_CASES)
def test_parse_room(room, groups, real):
    """Test that room is parsed correctly by regex."""
    from day4 import parse_room
    assert parse_room(room) == groups


@pytest.mark.parametrize('name, result', NAME_CASES)
def test_order_name(name, result):
    """Test that letters in a name are ordered correctly."""
    from day4 import order_name
    assert order_name(name) == result


@pytest.mark.parametrize('room, groups, real', ROOM_CASES)
def test_is_real_room(room, groups, real):
    """Test if a room represents a real room or not."""
    from day4 import is_real_room
    assert is_real_room(*groups) == real


@pytest.mark.parametrize('name, real_name', ROTATE_NAME_CASES)
def test_rotate_name(name, real_name):
    """Test that name is rotated correctly."""
    from day4 import rotate_name
    name, sector = name.rsplit('-', 1)
    assert rotate_name(name, sector) == real_name
