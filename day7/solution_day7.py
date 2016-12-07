"""

"""
from __future__ import unicode_literals, division


def part1(lines):
    count = 0
    for line in lines:
        outers, inners = collect_matches(line, abba)
        count += bool(outers) and not bool(inners)
    print('{} IP addresses support Transport Layer Snooping.'.format(count))


def part2(lines):
    """Run solution for Part 2."""
    count = 0
    for line in lines:
        outers, inners = collect_matches(line, aba)
        for found in outers:
            if invert(found) in inners:
                count += 1
                break
    print('{} IP addresses support Super-Secret Listening'.format(count))


def collect_matches(line, match_check):
    outers = set()
    inners = set()
    location = outers
    for idx in range(len(line)):
        if idx >= len(line) - 4:
            break
        if line[idx] == '[':
            location = inners
        if line[idx] == ']':
            location = outers
        found = match_check(idx, line)
        if found:
            location.add(found)
    return outers, inners


def abba(idx, chars):
    a, b, c, d = chars[idx:idx + 4]
    return all((a == d, a != b, b == c)) and chars[idx:idx + 4]


def aba(idx, chars):
    a, b, c = chars[idx:idx + 3]
    return all((a == c, a != b)) and chars[idx:idx + 3]


def invert(aba):
    return aba[1] + aba[:2]
