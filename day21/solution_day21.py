"""

"""
from __future__ import unicode_literals, division
import re

INITIAL = 'abcdefgh'


def part1(lines):
    """Run solution for Part 1."""
    string = INITIAL
    for line in lines:
        string = execute(line, string)
    print(string)


def part2(lines):
    """Run solution for Part 2."""


def execute(line, string):
    """Return a partialed function with arguments from line."""
    for pat, func in INSTRUCTIONS.items():
        match = re.match(pat, line)
        if match is not None:
            try:
                return func(string, *map(int, match.groups()))
            except ValueError:
                return func(string, *match.groups())

    raise AssertionError('No match found in line: {}.'.format(line))


def swap_position(string, idx_1, idx_2):
    as_list = list(string)
    as_list[idx_1], as_list[idx_2] = as_list[idx_2], as_list[idx_1]
    return ''.join(as_list)


def swap_letter(string, letter_1, letter_2):
    idx_1 = string.find(letter_1)
    idx_2 = string.find(letter_2)
    return swap_position(string, idx_1, idx_2)


def rotate_left(string, steps):
    return string[steps:] + string[:steps]


def rotate_right(string, steps):
    return string[-steps:] + string[:-steps]


def rotate_based_on_index(string, letter):
    steps = string.find(letter)
    if steps >= 4:
        steps += 1
    return rotate_right(string, steps + 1)


def reverse_slice(string, start, end):
    return string[:start] + string[end:start - 1: -1] + string[end + 1:]


def move(string, from_idx, to_idx):
    letter = string[from_idx]
    string = string[:from_idx] + string[from_idx + 1:]
    return string[:to_idx] + letter + string[to_idx:]


SWAP_POS = r'^swap\sposition\s(\d+)\swith\sposition\s(\d+)$'
SWAP_LETTER = r'^swap\sletter\s(\w)\swith\sletter\s(\w)$'
ROTATE_LEFT = r'^rotate left\s(\d+)\sstep'
ROTATE_RIGHT = r'^rotate right\s(\d+)\sstep'
ROTATE_ON_IDX = r'^rotate based on position of letter\s(\w)$'
REVERSE_SLICE = r'^reverse positions\s(\d+)\sthrough\s(\d+)$'
MOVE = r'^move position\s(\d+)\sto position\s(\d+)$'

INSTRUCTIONS = {
    SWAP_POS: swap_position,
    SWAP_LETTER: swap_letter,
    ROTATE_LEFT: rotate_left,
    ROTATE_RIGHT: rotate_right,
    ROTATE_ON_IDX: rotate_based_on_index,
    REVERSE_SLICE: reverse_slice,
    MOVE: move,
}
