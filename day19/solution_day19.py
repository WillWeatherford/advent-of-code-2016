"""

"""
from __future__ import unicode_literals, division
from collections import OrderedDict, deque
from itertools import chain

START_ELVES = 5


def part1(lines):
    """Run solution for Part 1."""
    num_elves = int(next(lines))
    result = steal_presents(num_elves, False)
    print('Elf #{} is left with all the presents!'.format(result))


def part2(lines):
    """Run solution for Part 2."""
    num_elves = int(next(lines))
    result = steal_presents(num_elves, True)
    print('Elf #{} is left with all the presents!'.format(result))


def steal_presents(num_elves, steal_across):
    """Return the elf remaining when stealing from the next elf."""
    elves = deque(range(1, num_elves + 1))
    if steal_across:
        elves.rotate(-((len(elves) - 1) >> 1))
    while len(elves) > 1:
        if not steal_across or (len(elves) % 2 == 0):
            elves.rotate(-1)
        elves.popleft()
    return elves[0]
