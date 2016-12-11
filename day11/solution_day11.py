"""

"""
from __future__ import unicode_literals, division
from itertools import chain, combinations, product
from copy import deepcopy
from math import inf
from collections import deque
import re

LINE_PAT = r'(\w+ium)(\sgenerator|\-compatible\smicrochip)'
MAX_MOVES = 30


def part1(lines):
    """Run solution for Part 1."""
    state = create_state(lines)
    result = simulate(state)
    print('Lowest number of moves: {}'.format(result))


def part2(lines):
    """Run solution for Part 2."""


def create_state(lines):
    state = dict(zip(range(1, 5), map(parse_line, lines)))
    state['elevator'] = 1
    return state


def simulate(orig_state):
    to_do = deque((orig_state, move, 0) for move in find_moves(orig_state))
    while to_do:
        state, move, moves_so_far = to_do.pop()

        if is_complete(state):
            print('Solution found in {} moves'.format(moves_so_far))
            return moves_so_far

        if moves_so_far > MAX_MOVES:
            print('Solution not found within {} moves'.format(MAX_MOVES))
            continue

        if is_invalid(state):
            print('Invalid state found.')
            continue

        new_state = make_move(state, *move)
        for move in find_moves(new_state):
            to_do.appendleft((new_state, move, moves_so_far + 1))
    print('Failed to find')
    return inf


def make_move(state, destination, cargos):
    start = state['elevator']
    new_state = deepcopy(state)
    new_state['elevator'] = destination
    if not cargos:
        return new_state
    for obj_type, element in cargos:
        new_state[start][obj_type].remove(element)
        new_state[destination][obj_type].add(element)
    return new_state


def parse_line(line):
    """Return a list of the abbreviations for each element object."""
    output = {'generators': set(), 'microchips': set()}
    for element, obj_type in re.findall(LINE_PAT, line):
        if obj_type.endswith('chip'):
            output['microchips'].add(element)
        elif obj_type.endswith('tor'):
            output['generators'].add(element)
        else:
            raise AssertionError
    return output


def find_moves(state):
    current_floor = find_elevator(state)
    destinations = []
    if current_floor < 4:
        destinations.append(current_floor + 1)
    if current_floor > 1:
        destinations.append(current_floor - 1)

    empty = ((), )
    singles = ((obj, ) for obj in objects_on_floor(state, current_floor))
    pairs = combinations(objects_on_floor(state, current_floor), 2)
    cargos = chain(pairs, singles, empty)

    return product(destinations, cargos)


def objects_on_floor(state, floor):
    for obj_type, elements in state[floor].items():
        for element in elements:
            yield (obj_type, element)


def find_elevator(state):
    return state['elevator']


def is_complete(state):
    return len(state[4]) > 10


def is_invalid(state):
    for n in range(1, 5):
        for element in state[n]['microchips']:
            if state[n]['generators'] and element not in state[n]['generators']:
                return True
    return False
