"""

"""
from __future__ import unicode_literals, division
from itertools import chain, combinations, product
from copy import deepcopy
from math import inf
from collections import deque, namedtuple
from operator import itemgetter
import re

LINE_PAT = r'(\w+ium)(\sgenerator|\-compatible\smicrochip)'
MAX_MOVES = 30


State = namedtuple('State', ('moves_so_far', 'elevator', 'pairs'))
State.__eq__ = lambda self, other: set(self) == set(other)


def part1(lines):
    """Run solution for Part 1."""
    initial_state = create_initial_state(lines)
    result = simulate(initial_state)
    print('Lowest number of moves: {}'.format(result))


def part2(lines):
    """Run solution for Part 2."""


def parse_line(line):
    output = {'generators': set(), 'microchips': set()}
    for element, obj_type in re.findall(LINE_PAT, line):
        if obj_type.endswith('chip'):
            output['microchips'].add(element)
        elif obj_type.endswith('tor'):
            output['generators'].add(element)
    return output


def create_initial_state(lines):
    microchips = {}
    generators = {}
    for floor, line in enumerate(lines):
        for element, obj_type in re.findall(LINE_PAT, line):
            if obj_type.endswith('chip'):
                microchips[element] = floor
            elif obj_type.endswith('tor'):
                generators[element] = floor
    chips_pos = map(itemgetter(1), sorted(microchips.items()))
    gens_pos = map(itemgetter(1), sorted(generators.items()))
    return State(0, 1, tuple(zip(chips_pos, gens_pos)))


def simulate(initial_state):
    found_states = {initial_state}
    to_do = deque([initial_state])
    while to_do:
        current_state = to_do.pop()
        for next_move in find_moves(current_state):
            # trim out based on move -- don't move down
            state = make_move(current_state, *next_move)
            if is_complete(state):
                print('Solution found in {} moves'.format(state.moves_so_far))
                return state.moves_so_far

            if state in found_states:
                print('State already found.')
                continue

            if is_invalid(state):
                continue

            to_do.appendleft(state)

# single chip
# single generator
# 2x generator
# 2x chip
# chip and gen of same element
    # don't move down
# NOT chip and gen of different elements


def find_moves(state):
    singles = ((obj, ) for obj in objects_at_elevator(state))
    doubles = doubles_at_elevator(state)
    cargos = chain(singles, doubles)
    moves = product(destinations(state), cargos)
    return moves


def destinations(state):
    if state.elevator > 0:
        yield state.elevator - 1
    if state.elevator < 3:
        yield state.elevator + 1


def doubles_at_elevator(state):
    # Discrete combinations, no duplicates or repeats
    for obj1, obj2 in combinations(objects_at_elevator(state), 2):
        # If they are different types AND different elements
        if obj1[0] != obj2[0] and obj1[1] != obj1[1]:
            continue
        yield obj1, obj2


def objects_at_elevator(state):
    for pair, obj_type in product(range(len(state.pairs)), range(2)):
        # Check if object is on the same floor as the elevator
        if state.pairs[pair][obj_type] == state.elevator:
            yield pair, obj_type


def make_move(state, destinations, cargos):
    new_pairs = state.pairs
    for pair, obj_type in cargos:
        pass

    return new_state


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
