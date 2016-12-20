"""

"""
from __future__ import unicode_literals, division
from itertools import count


MIN = 16777216


def part1(lines):
    """Run solution for Part 1."""
    lines = map(intify, lines)
    lines = iter(sorted(lines))
    lowest_range = find_lowest_range(lines)
    print(lowest_range[1] + 1)


def intify(line):
    return tuple(map(int, line.split('-')))


def range_size(tup):
    smaller, larger = tup
    assert larger > smaller
    return abs(larger - smaller) + 1


def find_lowest_range(lines):
    lowest_range = list(next(lines))
    for low, high in lines:
        if low <= lowest_range[1] + 1 and high > lowest_range[1]:
            lowest_range[1] = high
    return lowest_range



def part2(lines):
    """Run solution for Part 2."""
