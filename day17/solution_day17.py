"""

"""
from __future__ import unicode_literals, division
from hashlib import md5
from collections import deque

OPENS = 'bcdef'

DIRECTIONS = [
    ('U', 0, -1),
    ('D', 0, 1),
    ('L', -1, 0),
    ('R', 1, 0),
]

SALT = 'pvhmgsws'

def part1(lines):
    """Run solution for Part 1."""
    result = solve((0, 0, ''), (3, 3))
    print(result)


def part2(lines):
    """Run solution for Part 2."""


def solve(start, exit):
    found_paths = set()
    to_do = deque([start])

    while to_do:
        x, y, path_so_far = to_do.pop()

        print('Examinging at {} {}'.format(x, y))

        if (x, y) == exit:
            found_paths.add(path_so_far)
            continue

        for move, n_x, n_y in get_passable_neighbors(x, y, path_so_far):
            to_do.appendleft((n_x, n_y, path_so_far + move))
            print('Found a passable neighbor: {} {}'.format(n_x, n_y))

    return len(max(found_paths, key=len))


def get_passable_neighbors(x, y, path):
    for n_pos, door in zip(get_neighbors(x, y), get_locked_status(path)):
        move, n_x, n_y = n_pos
        if n_x < 0 or n_y < 0 or n_x > 3 or n_y > 3:
            continue
        if door:
            yield move, n_x, n_y


def get_neighbors(x, y):
    for move, x_mod, y_mod in DIRECTIONS:
        n_x = x + x_mod
        n_y = y + y_mod
        yield move, n_x, n_y


# def make_path(found, start_pos, tile):
#     path = []
#     while tile != start_pos:
#         path.append(found[tile]['move'])
#         tile = found[tile]['prev']
#     return path[::-1]


def get_locked_status(path):
    hashed = md5((SALT + path).encode('ascii')).hexdigest()
    return map(lambda x: x in OPENS, hashed[:4])
