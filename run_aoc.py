"""Utilities for Advent of Code challenges."""
from __future__ import unicode_literals, division
from importlib import import_module
from time import time
import sys
import re
import os


DAY_NAME_MATCH = r'day\d{1,2}'

SOLUTION_MODULE = 'solution_{}'
SOLUTION_NAME = 'solution_{}.py'
TEST_NAME = 'test_{}.py'
INPUT_NAME = 'input_{}.txt'
FILENAMES = (SOLUTION_NAME, TEST_NAME, INPUT_NAME)


def main(day_num, split=False):
    """Run the main function from a specified day."""
    day_name = 'day{}'.format(day_num)
    if not re.match(DAY_NAME_MATCH, day_name):
        raise ValueError('Bad day_name.')

    input_func = split_input_lines if split else input_lines
    input_filename = INPUT_NAME.format(day_name)
    input_filepath = os.path.join(day_name, input_filename)
    solution_modulename = SOLUTION_MODULE.format(day_name)
    solution_module = import_module('.'.join((day_name, solution_modulename)))

    for n in ('1', '2'):
        lines = input_func(input_filepath)
        solution_func = getattr(solution_module, 'part' + n)
        before = time()
        solution_func(lines)
        after = time()
        print('Part {} ran in {}.'.format(n, after - before))


def input_lines(filepath):
    """Return generator of lines from input file."""
    with open(filepath, 'r') as input_file:
        for line in input_file:
            yield line.strip()


def split_input_lines(filepath):
    """Return generator of lines from input file which have been split."""
    for line in input_lines(filepath):
        yield line.split()

if __name__ == '__main__':
    main(*sys.argv[1:])
