"""
--- Day 5: How About a Nice Game of Chess? ---

You are faced with a security door designed by Easter Bunny engineers that seem to have acquired most of their security knowledge by watching hacking movies.

The eight-character password for the door is generated one character at a time by finding the MD5 hash of some Door ID (your puzzle input) and an increasing integer index (starting with 0).

A hash indicates the next character in the password if its hexadecimal representation starts with five zeroes. If it does, the sixth character in the hash is the next character of the password.

For example, if the Door ID is abc:

    The first index which produces a hash that starts with five zeroes is 3231929, which we find by hashing abc3231929; the sixth character of the hash, and thus the first character of the password, is 1.
    5017308 produces the next interesting hash, which starts with 000008f82..., so the second character of the password is 8.
    The third time a hash starts with five zeroes is for abc5278568, discovering the character f.

In this example, after continuing this search a total of eight times, the password is 18f47a30.

Given the actual Door ID, what is the password?
"""
from __future__ import unicode_literals, division
from itertools import count
from hashlib import md5

FIVE_ZEROES = '0' * 5


def part1(lines):
    """Run solution for Part 1."""


def part2(lines):
    """Run solution for Part 2."""


def get_password_char(bytes_val):
    """Return a single string character; the 6th char in a md5 hash of val.

    If the hashed does not start with five zeroes, returns empty string.
    """
    hashed = md5(bytes_val)
    hexed = hashed.hexdigest()
    if hexed.startswith(FIVE_ZEROES):
        return hexed[5]
    return ''


def decode_password(door_id):
    """Return decoded password."""
    result = ''
    for n in count():
        bytes_val = '{}{}'.format(door_id, n).encode('ascii')
        result += get_password_char(bytes_val)
        if len(result) >= 8:
            break
    return result
