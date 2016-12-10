"""

"""
from __future__ import unicode_literals, division
from collections import deque
from functools import reduce
from operator import mul
import re

IN_PAT = r'^value (\d+) goes to bot (\d+)'
GIVE_PAT = r'^bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)'


def part1(lines):
    """Run solution for Part 1."""
    target = (17, 61)
    result = process_instructions(lines, target)
    print('Bot # {} is the target.'.format(result))


def part2(lines):
    """Run solution for Part 2."""
    outputs = process_instructions(lines)
    result = reduce(mul, (outputs[chip].pop() for chip in '012'))
    print('The product of chips in outputs 0, 1 and 2 = {}'.format(result))


def process_instructions(lines, target=None):
    """Return final output dict after processing robot instructions."""
    bots = {}
    outputs = {}
    to_do = deque(lines)
    while to_do:
        line = to_do.pop()
        if line.startswith('value'):
            chip, getter = re.match(IN_PAT, line).groups()
            bots.setdefault(getter, []).append(int(chip))

        elif line.startswith('bot'):
            match = re.match(GIVE_PAT, line)
            giver, low_type, low_dest, high_type, high_dest = match.groups()

            if len(bots.get(giver, [])) < 2:
                to_do.appendleft(line)
                continue

            low, high = sorted(bots[giver])
            if target and (low, high) == target:
                return giver

            locals()[low_type + 's'].setdefault(low_dest, []).append(low)
            locals()[high_type + 's'].setdefault(high_dest, []).append(high)
            bots[giver] = []
    return outputs
