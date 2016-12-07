"""

"""
from __future__ import unicode_literals, division


def part1(lines):
    """Run solution for Part 1."""
    count = 0
    for line in lines:
        outsides, insides = parse_parts(line)
        for part in insides:
            if has_abba(part):
                break
        else:
            for part in outsides:
                if has_abba(part):
                    count += 1
                    break
    print(count)


def parse_parts(line):
    outsides = set()
    insides = set()
    while True:
        try:
            outside, line = line.split('[', 1)
        except ValueError:
            outsides.add(line)
            break
        inside, line = line.split(']', 1)
        outsides.add(outside)
        insides.add(inside)
    return outsides, insides


def has_abba(part):
    for idx, char in enumerate(part[:-3]):
        if char == part[idx + 3] and part[idx + 1] == part[idx + 2] and char != part[idx + 1]:
            return True
    return False


def get_abas(part):
    for idx, char in enumerate(part[:-2]):
        if char == part[idx + 2] and char != part[idx + 1]:
            yield part[idx:idx + 3]


def has_bab(part, a, b):
    for idx, char in enumerate(part[:-2]):
        if char == b and part[idx + 2] == b and part[idx + 1] == a:
            return True
    return False


def part2(lines):
    """Run solution for Part 2."""
    count = 0
    for line in lines:
        outsides, insides = parse_parts(line)
        abas = set()
        for part in outsides:
            abas.update(get_abas(part))
        for aba in abas:
            for part in insides:
                if has_bab(part, *aba[:2]):
                    count += 1
                    break
            else:
                continue
            break
    print(count)
