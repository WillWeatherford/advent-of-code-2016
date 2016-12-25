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


def line_to_tup(line):
    name, *rest = line.split()
    pos = tuple(map(int, re.match(r'.*-x(\d+)-y(\d+)', name).groups()))
    return pos + tuple(map(lambda x: int(x[:-1], rest)))


def is_viable_combo(nodes):
    node1, node2 = nodes
    if node1['used'] <= 0:
        return False
    if node1['pos'] == node2['pos']:
        return False
    return node1['used'] <= node2['avail']


WIDTH = 38
HEIGHT = 28


def part2(lines):
    """Run solution for Part 2."""
    _, _ = next(lines), next(lines)
    fewest_moves = find_shortest_path(lines)


def find_shortest_path(lines):
    grid = [[None, ] * WIDTH for _ in range(HEIGHT)]
    for line in lines:
        line_tup = line_to_tup(line)
        x, y = line_tup[:2]
        grid[y][x] = line_tup[2:]
        if line_tup[2] == 0:
            empty_pos = (y, x)

    unique = count()
    data_pos = (0, WIDTH - 1)
    goal_pos = (0, 0)

    start_move = (
        0,
        # heuristic?
        next(unique),
        data_pos,
        goal_pos,
    )
    start_state = str(grid)
    found_states = {start_state, }
    to_do = [start_move]

    while True:
        total_distance, num_unfound, return_home, _, pos, unfound = heappop(to_do)

        if pos in unfound:
            unfound = tuple(g_pos for g_pos in unfound if g_pos != pos)
            num_unfound = len(unfound)

        if num_unfound == 0:
            if return_home:
                unfound = (start_pos, )
                num_unfound = 1
                return_home = False
            else:
                return total_distance

        for neighbor_pos in passable_neighbors(pos, grid):

            neighbor_state = (neighbor_pos, unfound)
            if neighbor_state in found_states:
                continue

            found_states.add(neighbor_state)
            move = (
                total_distance + 1,
                num_unfound,
                return_home,
                next(unique),
                neighbor_pos,
                unfound,
            )
            heappush(to_do, move)


def passable_neighbors(pos, grid):
    """Return generator of only valid neighbor positions."""
    for y, x in find_neighbors(pos):
        try:
            val = grid[y][x]
        except IndexError:
            continue
        else:
            if val != WALL:
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
