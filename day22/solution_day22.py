"""

"""
from __future__ import unicode_literals, division
import re
from itertools import permutations
from heapq import heappop, heappush
from itertools import count


def part1(lines):
    """Run solution for Part 1."""
    _, _ = next(lines), next(lines)
    lines = map(line_to_dict, lines)
    combos = permutations(lines, 2)
    result = sum(map(is_viable_combo, combos))
    print(result)


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


WIDTH = 38
HEIGHT = 28
TOO_LARGE = 100
USABLE = '.'
UNUSABLE = '#'


def part2(lines):
    """Run solution for Part 2."""
    _, _ = next(lines), next(lines)
    fewest_moves = find_shortest_path(lines)
    print('{} moves to get data to goal.'.format(fewest_moves))


def find_shortest_path(lines):
    grid = [[None, ] * WIDTH for _ in range(HEIGHT)]
    for line in lines:
        line_dict = line_to_dict(line)
        x, y = line_dict['pos']
        if line_dict['size'] < TOO_LARGE:
            grid[y][x] = USABLE
        else:
            grid[y][x] = UNUSABLE
        if line_dict['used'] == 0:
            empty_pos = (y, x)

    unique = count()
    data_pos = (0, WIDTH - 1)
    goal_pos = (0, 0)

    start_state = (empty_pos, data_pos)
    start_move = (
        0,
        distance_between(data_pos, goal_pos),
        next(unique),
        start_state
    )
    found_states = {start_state, }
    to_do = [start_move, ]

    while to_do:
        total_distance, _, _, current_state = heappop(to_do)

        empty_pos, data_pos = current_state

        if data_pos == goal_pos:
            return total_distance

        for neighbor_state in neighbor_states(grid, *current_state):

            if neighbor_state in found_states:
                continue

            found_states.add(neighbor_state)
            move = (
                total_distance + 1,
                distance_between(data_pos, goal_pos),
                next(unique),
                neighbor_state,
            )
            heappush(to_do, move)


def distance_between(pos1, pos2):
    """Return total distance to goal_pos from the current data position."""
    return sum(abs(xy1 - xy2) for xy1, xy2 in zip(pos1, pos2))


def neighbor_states(grid, empty_pos, data_pos):
    for neighbor_pos in usable_neighbors(empty_pos, grid):
        if neighbor_pos == data_pos:
            yield (neighbor_pos, empty_pos)
        else:
            yield (neighbor_pos, data_pos)


def usable_neighbors(pos, grid):
    """Return generator of only valid neighbor positions."""
    for y, x in find_neighbors(pos):
        try:
            val = grid[y][x]
        except IndexError:
            continue
        else:
            if val == USABLE:
                yield (y, x)


def find_neighbors(pos):
    """Return generator of all neighbor positions."""
    y, x = pos
    # up
    if y > 0:
        yield y - 1, x
    # left
    if x > 0:
        yield y, x - 1
    # down
    yield y + 1, x
    # right
    yield y, x + 1
