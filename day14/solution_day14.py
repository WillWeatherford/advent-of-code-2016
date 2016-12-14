"""

"""
from __future__ import unicode_literals, division
from itertools import count
from hashlib import md5


def part1(lines):
    """Run solution for Part 1."""
    found = 0
    salt = 'ihaygndm'
    candidates = {}
    for n in count():
        bytes_val = get_bytes_val(salt, n)
        hashed_hex = get_hashed_hex(bytes_val)
        triplet = get_triple(hashed_hex)
        if triplet:
            candidates[triplet] = 1000

        quint = get_quint(hashed_hex)
        if quint and quint[:3] in candidates:
            found += 1

        candidates = update_candidates(candidates)


def update_candidates(candidates):
    candidates_copy = {}
    for cand, countdown in candidates.items():
        new_count = countdown - 1
        if new_count > 0:
            candidates_copy[cand] = new_count
    return candidates_copy


def part2(lines):
    """Run solution for Part 2."""


def get_bytes_val(door_id, n):
    """Return a bytestring concatenation of door_id and index n."""
    return '{}{}'.format(door_id, n).encode('ascii')


def get_hashed_hex(bytes_val):
    """Return a single string character; the 6th char in a md5 hash of val.

    If the hashed does not start with five zeroes, returns empty string.
    """
    hashed = md5(bytes_val)
    return hashed.hexdigest()

