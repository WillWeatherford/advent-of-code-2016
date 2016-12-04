"""Utilities for Advent of Code challenges."""
from __future__ import unicode_literals, division
from itertools import tee
import sys
import re
import os


DAYNAME_MATCH = r'day\d{1,2}'


def main(dayname, split=False):
    """Run the main function from a specified day."""
    if not re.match(DAYNAME_MATCH, dayname):
        raise ValueError('Bad dayname.')

    input_filename = os.path.join(dayname, 'input.txt')
    if split:
        lines = split_input_lines(input_filename)
    else:
        lines = input_lines(input_filename)
    lines1, lines2 = tee(lines, 2)

    day_module = __import__(dayname)
    day_module.part1(lines1)
    day_module.part2(lines2)


def input_lines(filename):
    """Return generator of lines from input file."""
    with open(filename, 'r') as input_file:
        for line in input_file:
            yield line.strip()


def split_input_lines(filename):
    """Return generator of lines from input file which have been split."""
    for line in input_lines(filename):
        yield line.split()

if __name__ == '__main__':
    main(*sys.argv[1:])
