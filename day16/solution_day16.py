"""

"""
from __future__ import unicode_literals, division




def part1(lines):
    """Run solution for Part 1."""
    data, disc_size, _ = lines
    expanded_data = expand_data(data, disc_size)
    checksum = make_checksum(expanded_data)
    print('The final checksum from initial data {} on disc size {} is {}.'
          ''.format(data, disc_size, checksum))


def part2(lines):
    """Run solution for Part 2."""
    data, _, max_size = lines



def expand_data(data, max_size):
    while len(data) < max_size:
        inverse = ''.join('0' if c == '1' else '1' for c in reversed(data))
        data = '0'.join((data, inverse))
    return data[:max_size]


def make_checksum(data):
    while not len(data) % 2:
        data = ''.join(generate_checksum(iter(data)))
    return data


def generate_checksum(iter_data):
    for char in iter_data:
        yield '1'if next(iter_data) == char else '0'
