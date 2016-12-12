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
    found_states = {make_hashable_state(orig_state), }
    to_do = deque((orig_state, move, 0) for move in find_moves(orig_state))
    while to_do:
        # print('{} moves to evaluate'.format(len(to_do)))
        state, move, moves_so_far = to_do.pop()

        if is_complete(state):
            print('Solution found in {} moves'.format(moves_so_far))
            return moves_so_far

        if moves_so_far > MAX_MOVES:
            print('Solution not found within {} moves'.format(MAX_MOVES))
            continue

        if is_invalid(state):
            # print('Invalid state found.')
            continue

        new_state = make_move(state, *move)
        hashable_state = make_hashable_state(new_state)
        if hashable_state in found_states:
            print('State already found.')
            continue
        found_states.add(hashable_state)

        for next_move in find_moves(new_state):
            if is_great_move(new_state, *next_move):
                to_do.append((new_state, move, moves_so_far + 1))
            if is_bad_move(new_state, *next_move):
                continue
            to_do.appendleft((new_state, move, moves_so_far + 1))
    print('Failed to find')
    return inf


def is_great_move(state, destination, cargos):
    if destination < state['elevator']:
        return False
    if len(cargos) < 2:
        return False
    return cargos[0][1] == cargos[1][1]


def is_bad_move(state, destination, cargos):
    start = state['elevator']
    if destination > start:
        return False
    objects_below = 0
    for n in range(start - 1, 0, -1):
        objects_below += len(state[n]['generators'])
        objects_below += len(state[n]['microchips'])
    return objects_below == 0


def make_hashable_state(state):
    hashable_state = []
    elevator = state.pop('elevator')
    for n, floor in sorted(state.items()):
        for obj_type, elements in sorted(floor.items()):
            for element in sorted(elements):
                hashable_state.append(' '.join((str(n), element, obj_type)))
    hashable_state.append(' '.join(('elevator', str(elevator))))
    state['elevator'] = elevator
    return ' '.join(hashable_state)


def make_move(state, destination, cargos):
    start = state['elevator']
    new_state = deepcopy(state)
    new_state['elevator'] = destination
    for obj_type, element in cargos:
        new_state[start][obj_type].remove(element)
        new_state[destination][obj_type].add(element)
    return new_state


def parse_line(line):
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

    singles = ((obj, ) for obj in objects_on_floor(state, current_floor))
    pairs = combinations(objects_on_floor(state, current_floor), 2)
    cargos = chain(pairs, singles)

    return product(destinations, cargos)


def objects_on_floor(state, floor):
    for obj_type, elements in state[floor].items():
        for element in elements:
            yield (obj_type, element)


def find_elevator(state):
    return state['elevator']


def is_complete(state):
    return len(state[4]['generators']) == 5 and len(state[4]['microchips']) == 5


def is_invalid(state):
    for n in range(1, 5):
        for element in state[n]['microchips']:
            if state[n]['generators'] and element not in state[n]['generators']:
                return True
    return False
