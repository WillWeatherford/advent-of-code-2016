"""

"""
from __future__ import unicode_literals, division
from collections import OrderedDict


START_ELVES = 3001330

def part1(lines):
    """Run solution for Part 1."""

    elves = OrderedDict.fromkeys(range(1, START_ELVES + 1), 1)

    while len(elves) > 1:
        dead = set()

        stolen_from = False
        for elf_num, presents in elves.items():
            if stolen_from:
                # print('{} steals {} presents from {}'.format(stealer_num, presents, elf_num))
                elves[stealer_num] += presents
                dead.add(elf_num)
                stolen_from = False
            else:
                stealer_num = elf_num
                stolen_from = True
        if len(elves) % 2:
            elves.move_to_end(stealer_num, last=False)

        for elf in dead:
            elves.pop(elf)
        dead = set()

        print('{} elves left'.format(len(elves)))

    print(elves.popitem()[0])


def part2(lines):
    """Run solution for Part 2."""
