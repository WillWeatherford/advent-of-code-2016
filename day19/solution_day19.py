"""

"""
from __future__ import unicode_literals, division
from collections import OrderedDict, deque
from itertools import chain

START_ELVES = 5


def part1(lines):
    """Run solution for Part 1."""




def part2(lines):
    """Run solution for Part 2."""
    num_elves = int(next(lines))
    result = remove_halfway(num_elves)
    print('Elf #{} is left with all the presents!'.format(result))


def remove_halfway(num_elves):
    """Return the elf remaining when stealing from elf across the circle."""
    elves = deque(range(1, num_elves + 1))
    elves.rotate(-((len(elves) - 1) >> 1))
    while len(elves) > 1:
        if len(elves) % 2 == 0:
            elves.rotate(-1)
        elves.popleft()
    return elves[0]
