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
            yield len(chars)
            break
        else:
            before = chars[:match.start()]
            yield len(before)
            chars = chars[match.end():]
            num, mult = map(int, match.groups())
            to_multipy = chars[:num]
            chars = chars[num:]  # remainder

            if not part2:
                yield num * mult
                continue

            for count in decompress(to_multipy * mult, part2):
                yield count
