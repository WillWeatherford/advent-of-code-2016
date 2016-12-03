"""Utilities for Advent of Code challenges."""


def input_lines(filename):
    """Return generator of lines from input file."""
    with open(filename, 'r') as input_file:
        for line in input_file:
            yield line.strip()


def split_input_lines(filename):
    """Return generator of lines from input file which have been split."""
    for line in input_lines(filename):
        yield line.split()
