"""

"""
from __future__ import unicode_literals, division
from heapq import heappop, heappush
from itertools import count


WALL = '#'

def part1(lines):
    """Run solution for Part 1."""
    num_moves = find_shortest_path(lines, False)
    print('It takes at least {} moves to visit every position.'.format(num_moves))


def part2(lines):
    """Run solution for Part 2."""
    num_moves = find_shortest_path(lines, True)
    print('It takes at least {} moves to visit every position, then return home.'.format(num_moves))


def find_shortest_path(lines, return_home):
    unique = count()
    grid = []
    goals = set()
    for y, line in enumerate(lines):
        row = []
        for x, char in enumerate(line):
            if char.isdigit():
                if char == '0':
                    start_pos = (y, x)
                else:
                    goals.add((y, x))
            row.append(char)
        grid.append(row)

    # (total_distance, closest_target, num_unfound, _, pos, un_found)
    goals = tuple(sorted(goals))

    start_move = (
        0,
        len(goals),
        return_home,
        next(unique),
        start_pos,
        goals,
    )
    start_state = (start_pos, goals)
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
