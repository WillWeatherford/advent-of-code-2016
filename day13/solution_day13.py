"""

"""
from __future__ import unicode_literals, division
from collections import deque
from itertools import product

inf = float('inf')

MAGIC_NUM = 1362


def part1(lines):
    """Run solution for Part 1."""
    start = {'x': 1, 'y': 1}
    exit = {'x': 31, 'y': 39}
    path = solve(start, exit)
    print(len(path))


def part2(lines):
    """Run solution for Part 2."""
    start = {'x': 1, 'y': 1}
    exit = {'x': 31, 'y': 39}
    num_found = solve2(start, exit)
    print(num_found)


def is_wall(x, y):
    val = x * x + 3 * x + 2 * x * y + y + y * y
    val += MAGIC_NUM
    return bin(val)[2:].count('1') % 2


DIRECTIONS = [
    ('up', 0, -1),
    ('down', 0, 1),
    ('left', -1, 0),
    ('right', 1, 0),
]


def solve2(start, exit):
    start_pos = (start['x'], start['y'])
    exit_pos = (exit['x'], exit['y'])
    to_do = deque([start_pos])
    found = {start_pos: None}

    for _ in range(49):
        x, y = to_do.pop()
        # if (x, y) == exit_pos:
        #     return make_path(found, start_pos, exit_pos)

        for move, n_pos in get_passable_neighbors(x, y, ):
            if n_pos not in found:
                to_do.appendleft(n_pos)
                found[n_pos] = {'move': move, 'prev': (x, y)}
    return len(found)


def solve(start, exit):
    start_pos = (start['x'], start['y'])
    exit_pos = (exit['x'], exit['y'])
    to_do = deque([start_pos])
    found = {start_pos: None}

    while to_do:
        x, y = to_do.pop()
        if (x, y) == exit_pos:
            return make_path(found, start_pos, exit_pos)

        for move, n_pos in get_passable_neighbors(x, y, ):
            if n_pos not in found:
                to_do.appendleft(n_pos)
                found[n_pos] = {'move': move, 'prev': (x, y)}


def get_passable_neighbors(x, y, ):
    for move, x_mod, y_mod in DIRECTIONS:
        n_x = x + x_mod
        n_y = y + y_mod
        if n_x < 0 or n_y < 0:
            continue
        if not is_wall(x, y):
            yield move, (n_x, n_y)


def make_path(found, start_pos, tile):
    path = []
    while tile != start_pos:
        path.append(found[tile]['move'])
        tile = found[tile]['prev']
    return path[::-1]
