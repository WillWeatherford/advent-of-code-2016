"""

"""
from __future__ import unicode_literals, division
import re

PAT = r'\((?P<num>\d+)x(?P<mult>\d+)\)'


def part1(lines):
    """Run solution for Part 1."""
    line = next(lines)
    result = sum(decompress(line, False))
    print(result)


def part2(lines):
    """Run solution for Part 2."""
    line = next(lines)
    result = sum(decompress(line, True))
    print(result)


def decompress(chars, part2):
    while chars:
        match = re.search(PAT, chars)
        if match is None:
            yield len(chars)  # Any remaining chars outside a multiplied
            break

        yield len(chars[:match.start()])  # Any leading chars before (NxM) pattern
        chars = chars[match.end():]  # Snip off the (NxM) pattern
        num, mult = map(int, match.groups())
        to_multiply = chars[:num]  # The slice to be multplied
        chars = chars[num:]  # Truncate remaining chars

        if part2:
            yield sum(decompress(to_multiply, part2)) * mult
        else:
            yield num * mult
