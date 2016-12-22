"""

"""
from __future__ import unicode_literals, division
import re
from itertools import permutations


def part1(lines):
    """Run solution for Part 1."""
    _, _ = next(lines), next(lines)
    lines = map(line_to_dict, lines)
    combos = permutations(lines, 2)
    result = sum(map(is_viable_combo, combos))
    print(result)


def part2(lines):
    """Run solution for Part 2."""


def line_to_dict(line):
    name, size, used, avail, use_percent = line.split()
    return {
        'pos': tuple(map(int, re.match(r'.*-x(\d+)-y(\d+)', name).groups())),
        'size': int(size[:-1]),
        'used': int(used[:-1]),
        'avail': int(avail[:-1]),
        'use_percent': int(use_percent[:-1]),
    }


def is_viable_combo(nodes):
    node1, node2 = nodes
    if node1['used'] <= 0:
        return False
    if node1['pos'] == node2['pos']:
        return False
    return node1['used'] <= node2['avail']
