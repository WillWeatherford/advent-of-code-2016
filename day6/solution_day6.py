"""

"""
from __future__ import unicode_literals, division
from collections import Counter

INPUT_LEN = 8


def part1(lines):
    """Run solution for Part 1."""
    table = {n: Counter() for n in range(INPUT_LEN)}
    for line in lines:
        for idx, char in enumerate(line):
            table[idx].update(char)

    result = [table[idx].most_common()[0][0] for idx in range(INPUT_LEN)]
    print(''.join(result))


def part2(lines):
    """Run solution for Part 2."""
    table = {n: Counter() for n in range(INPUT_LEN)}
    for line in lines:
        for idx, char in enumerate(line):
            table[idx].update(char)
    result = [next(reversed(table[idx].most_common()))[0] for idx in range(INPUT_LEN)]
    print(''.join(result))
