"""

"""
from __future__ import unicode_literals, division
from itertools import chain, combinations, product
from copy import deepcopy
from math import inf
import re

LINE_PAT = r'(\w+ium)(\sgenerator|\-compatible\smicrochip)'
MAX_MOVES = 30


def part1(lines):
    """Run solution for Part 1."""
    state = create_state(lines)
    result = simulate(state, 0)
    print('Lowest number of moves: {}'.format(result))


def part2(lines):
    """Run solution for Part 2."""


def create_state(lines):
    state = dict(zip(range(1, 5), map(parse_line, lines)))
    state['elevator'] = 1
    return state


def simulate(state, moves_so_far):
    if is_complete(state):
        print('Solution found in {} moves'.format(moves_so_far))
        return moves_so_far
    if moves_so_far > MAX_MOVES:
        print('Solution not found within {} moves'.format(MAX_MOVES))
        return inf
    if is_invalid(state):
        print('Invalid state found.')
        return inf
    moves_counts = []
    for start, destination, cargos in find_moves(state):
        new_state = make_move(state, start, destination, cargos)
        moves_count = simulate(new_state, moves_so_far + 1)
        moves_counts.append(moves_count)
    return min(moves_counts)


def make_move(state, start, destination, cargos):
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

    return product((current_floor, ), destinations, cargos)


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
