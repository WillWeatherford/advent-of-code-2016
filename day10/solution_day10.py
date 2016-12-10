"""

"""
from __future__ import unicode_literals, division
from itertools import tee
import re

IN_PAT = r'value (\d+) goes to bot (\d+)'
GIVE_PAT = r'bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)'


def part1(lines):
    """Run solution for Part 1."""
    run1, run2 = tee(lines, 2)
    inputs = (line for line in run1 if line.startswith('value'))
    moves = (line for line in run2 if line.startswith('bot'))

    outputs = {}
    bots = {}
    for inp in inputs:
        match = re.match(IN_PAT, inp)
        chip, bot = match.groups()
        bots.setdefault(bot, []).append(int(chip))
        assert len(bots[bot]) < 3

    for move in moves:
        match = re.match(GIVE_PAT, move)
        from_bot, low_to_type, low_to, high_to_type, high_to = match.groups()

        try:
            low, high = sorted(bots[from_bot])
        except (KeyError, ValueError):
            continue
        if low == 17 and high == 61:
            print('TARGET FOUND')
            print('Bot # {}'.format(from_bot))
            return
        if low_to_type == 'bot':
            bots.setdefault(low_to, []).append(low)
        else:
            outputs.setdefault(low_to, []).append(low)
        if high_to_type == 'bot':
            bots.setdefault(high_to, []).append(high)
        else:
            outputs.setdefault(high_to, []).append(high)


def part2(lines):
    """Run solution for Part 2."""


