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
    *func_words, _ = line.split(maxsplit=2)

    func_name = '_'.join(func_words)
    func = globals()[func_name]

    args = tuple(map(int, re.findall(r'\d+', line)))
    if not args:
        letters = re.findall(r'letter\s\w', line)
        args = [letter.split()[1] for letter in letters]
    return func(string, *args)


def swap_position(string, idx_1, idx_2):
    as_list = list(string)
    as_list[idx_1], as_list[idx_2] = as_list[idx_2], as_list[idx_1]
    return ''.join(as_list)


def swap_letter(string, letter_1, letter_2):
    idx_1 = string.find(letter_1)
    idx_2 = string.find(letter_2)
    return swap_position(string, idx_1, idx_2)


def rotate_left(string, steps):
    steps %= len(string)
    return string[steps:] + string[:steps]


def rotate_right(string, steps):
    steps %= len(string)
    return string[-steps:] + string[:-steps]


def rotate_based(string, letter):
    steps = string.find(letter)
    return rotate_right(string, 1 + steps + (steps >= 4))


def reverse_positions(string, start, end):
    reverse = ''.join(reversed(string[start:end + 1]))
    return string[:start] + reverse + string[end + 1:]


def move_position(string, from_idx, to_idx):
    letter = string[from_idx]
    string = string[:from_idx] + string[from_idx + 1:]
    return string[:to_idx] + letter + string[to_idx:]
