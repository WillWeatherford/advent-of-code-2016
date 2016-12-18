"""

"""
from __future__ import unicode_literals, division


TRAP = '^'
SAFE = '.'
TRAP_2 = (TRAP, TRAP)
SAFE_2 = (SAFE, SAFE)
ROWS = 400000

def part1(lines):
    """Run solution for Part 1."""
    start_row = next(lines)
    prev_row = start_row
    total_safe = start_row.count(SAFE)
    for _ in range(ROWS - 1):
        prev_row = make_new_row(prev_row)
        total_safe += prev_row.count(SAFE)
    print(total_safe)



def part2(lines):
    """Run solution for Part 2."""


def make_new_row(prev_row):
    new_row = []
    for idx, c in enumerate(prev_row):
        if idx == 0:
            l = '.'
        else:
            l = prev_row[idx - 1]
        if idx == len(prev_row) - 1:
            r = '.'
        else:
            r = prev_row[idx + 1]

        new_row.append(is_trap(l, c, r))

    return ''.join(new_row)



def is_trap(l, c, r):
    return '^' if any((
        (l, c) == TRAP_2 and r == SAFE,
        (c, r) == TRAP_2 and l == SAFE,
        (l, c) == SAFE_2 and r == TRAP,
        (c, r) == SAFE_2 and l == TRAP,
    )) else '.'


