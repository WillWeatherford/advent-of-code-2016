"""

"""
from __future__ import unicode_literals, division


def part1(lines):
    """Run solution for Part 1."""
    count = 0
    for line in lines:
        outsides, insides = parse_out(line)
        for part in insides:
            if has_abba(part):
                break
        else:
            for part in outsides:
                if has_abba(part):
                    count += 1
                    break
    print(count)


def parse_out(line):
    outsides = []
    insides = []
    start = 0
    while True:
        try:
            brack_start = line.index('[', start)
        except ValueError:
            outsides.append(line[start:])
            break
        brack_end = line.index(']', brack_start)
        outsides.append(line[start:brack_start])
        insides.append(line[brack_start:brack_end])
        start = brack_end
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
        outsides, insides = parse_out(line)
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
