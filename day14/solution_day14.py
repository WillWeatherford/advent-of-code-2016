"""
Inspired by this solution: https://github.com/bpeel/advent2016/blob/master/day14.py

"""
from __future__ import unicode_literals, division
from itertools import count
from hashlib import md5
from collections import deque


def part1(lines):
    """Run solution for Part 1."""
    salt = next(lines)
    n = 64
    result = find_nth_key_index(salt, 64)
    print('{}th key found at the {} index.'.format(n, result))


def part2(lines):
    """Run solution for Part 2."""
    salt = next(lines)
    n = 64
    result = find_nth_key_index(salt, 64, stretch=True)
    print('{}th key found at the {} index.'.format(n, result))


def find_nth_key_index(salt, n, stretch=False):
    found = 0
    hashes = deque(get_hashed_hex(salt, idx, stretch) for idx in range(1001))

    for idx in count():
        current = hashes.popleft()

        triplet = get_repeat(current, 3)
        if triplet:
            for other_hash in hashes:
                quint = get_repeat(other_hash, 5)
                if triplet == quint[:3]:
                    found += 1
                    break
        if found == 64:
            break
        hashes.append(get_hashed_hex(salt, idx + 1001, stretch))

    return idx


def get_repeat(chars, num):
    for idx, char in enumerate(chars):
        if chars[idx:idx + num] == char * num:
            return chars[idx:idx + num]
    return ''


def get_hashed_hex(salt, idx, stretch):
    """."""
    bytes_val = '{}{}'.format(salt, idx).encode('ascii')
    hashed = md5(bytes_val).hexdigest()
    if stretch:
        for _ in range(2016):
            hashed = md5(hashed.encode('ascii')).hexdigest()
    return hashed
