"""

"""
from __future__ import unicode_literals, division


def part1(lines):
    """Run solution for Part 1."""
    instructions = list(lines)
    table = {'a': 0, 'b': 0, 'c': 1, 'd': 0}

    idx = 0
    while idx < len(instructions):
        cmd, *args = instructions[idx].split()
        idx += globals()[cmd](table, *args)
    print(table['a'])


def cpy(table, val, reg):
    try:
        val = table[val]
    except KeyError:
        pass
    table[reg] = int(val)
    return 1


def inc(table, reg):
    table[reg] += 1
    return 1


def dec(table, reg):
    table[reg] -= 1
    return 1

def jnz(table, reg, val):
    try:
        zero_val = table[reg]
    except KeyError:
        zero_val = int(reg)
    if zero_val == 0:
        return 1
    return int(val)


def part2(lines):
    """Run solution for Part 2."""
