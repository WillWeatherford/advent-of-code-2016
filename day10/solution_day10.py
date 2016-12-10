"""
--- Day 10: Balance Bots ---

You come upon a factory in which many robots are zooming around handing small microchips to each other.

Upon closer examination, you notice that each bot only proceeds when it has two microchips, and once it does, it gives each one to a different bot or puts it in a marked "output" bin. Sometimes, bots take microchips from "input" bins, too.

Inspecting one of the microchips, it seems like they each contain a single number; the bots must use some logic to decide what to do with each chip. You access the local control computer and download the bots' instructions (your puzzle input).

Some of the instructions specify that a specific-valued microchip should be given to a specific bot; the rest of the instructions indicate what a given bot should do with its lower-value or higher-value chip.

For example, consider the following instructions:

value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2

    Initially, bot 1 starts with a value-3 chip, and bot 2 starts with a value-2 chip and a value-5 chip.
    Because bot 2 has two microchips, it gives its lower one (2) to bot 1 and its higher one (5) to bot 0.
    Then, bot 1 has two microchips; it puts the value-2 chip in output 1 and gives the value-3 chip to bot 0.
    Finally, bot 0 has two microchips; it puts the 3 in output 2 and the 5 in output 0.

In the end, output bin 0 contains a value-5 microchip, output bin 1 contains a value-2 microchip, and output bin 2 contains a value-3 microchip. In this configuration, bot number 2 is responsible for comparing value-5 microchips with value-2 microchips.

Based on your instructions, what is the number of the bot that is responsible for comparing value-61 microchips with value-17 microchips?

--- Part Two ---

What do you get if you multiply together the values of one chip in each of outputs 0, 1, and 2?

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
    print('Bot {} processes chips {} and {}.'.format(result, *target))


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
