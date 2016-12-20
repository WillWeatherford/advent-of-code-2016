"""

"""
from __future__ import unicode_literals, division
from itertools import count


MIN = 16777216
# MAX = 2147483647
MAX = 4294967295


def part1(lines):
    """Run solution for Part 1."""
    lines = map(intify, lines)
    lines = iter(sorted(lines))
    lowest_range = next(simplify_ranges(lines))
    print(lowest_range[1] + 1)


def part2(lines):
    """Run solution for Part 2."""
    lines = map(intify, lines)
    lines = iter(sorted(lines))
    ranges = simplify_ranges(lines)
    total_valid = range_gaps(ranges)
    print(total_valid)


def intify(line):
    return tuple(map(int, line.split('-')))


def range_size(tup):
    smaller, larger = tup
    assert larger > smaller
    return abs(larger - smaller) + 1


def simplify_ranges(lines):
    lowest_range = list(next(lines))
    for low, high in lines:
        if low <= lowest_range[1] + 1 and high > lowest_range[1]:
            lowest_range[1] = high
        elif low > lowest_range[1] + 1:
            yield tuple(lowest_range)
            lowest_range = [low, high]
    yield tuple(lowest_range)


def range_gaps(ranges):
    total = 0
    prev_low, prev_high = next(ranges)
    for low, high in ranges:
        total += low - (prev_high + 1)
        prev_low, prev_high = low, high
    total += (MAX - prev_high)
    return total
