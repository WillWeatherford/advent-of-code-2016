"""

"""
from __future__ import unicode_literals, division
from itertools import count
from hashlib import md5


def part1(lines):
    """Run solution for Part 1."""
    found = 0
    salt = 'ihaygndm'
    candidates = []
    for n in count():
        bytes_val = get_bytes_val(salt, n)
        hashed_hex = get_hashed_hex(bytes_val)

        quint = get_repeat(hashed_hex, 5)
        if quint:
            match_index = match_quint(quint, candidates)
            if match_index is not None:
                found += 1
                if found == 64:
                    print(match_index)
                    break
        else:
            triplet = get_repeat(hashed_hex, 3)
            if triplet:
                candidates.append((triplet, 1000, n))

        candidates = update_candidates(candidates)


def match_quint(quint, candidates):
    match_index = None
    candidates_copy = []
    for triplet, coundown, n in candidates:
        if match_index is None and triplet == quint[:3]:
            match_index = n
        else:
            candidates_copy.append((triplet, coundown, n))
    return match_index


def get_repeat(chars, num):
    for idx, char in enumerate(chars):
        if chars[idx:idx + num] == char * num:
            return chars[idx:idx + num]
    return ''


def update_candidates(candidates):
    candidates_copy = []
    for triplet, countdown, n in candidates:
        new_count = countdown - 1
        if new_count > 0:
            candidates_copy.append((triplet, new_count, n))
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

