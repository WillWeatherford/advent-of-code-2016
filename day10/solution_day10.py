"""

"""
from __future__ import unicode_literals, division
from collections import deque
import re

IN_PAT = r'^value (\d+) goes to bot (\d+)'
GIVE_PAT = r'^bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)'


def part1(lines):
    """Run solution for Part 1."""
    bots = {}
    outputs = {}
    to_do = deque(lines)
    while to_do:
        line = to_do.pop()
        if line.startswith('value'):
            chip, getter = re.match(IN_PAT, line).groups()
            bots.setdefault(getter, []).append(int(chip))
        elif line.startswith('bot'):
            giver, low_type, low_dest, high_type, high_dest = re.match(GIVE_PAT, line).groups()
            if len(bots.get(giver, [])) < 2:
                to_do.appendleft(line)
                continue
            low, high = sorted(bots[giver])
            if low == 17 and high == 61:
                print('TARGET FOUND')
                print(giver)
            locals()[low_type + 's'].setdefault(low_dest, []).append(low)
            locals()[high_type + 's'].setdefault(high_dest, []).append(high)
            bots[giver] = []
    prod = 1
    for n in range(3):
        prod *= outputs[str(n)].pop()
    print(prod)



def part2(lines):
    """Run solution for Part 2."""


