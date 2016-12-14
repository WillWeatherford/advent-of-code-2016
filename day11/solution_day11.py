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


# State = namedtuple('State', ('elevator', 'pairs'))
# State.__eq__ = lambda self, other: set(self.pairs) == set(other.pairs)


def part1(lines):
    """Run solution for Part 1."""
    initial_state = create_initial_state(lines)
    result = simulate(initial_state)
    print('Lowest number of moves: {}'.format(result))


def part2(lines):
    """Run solution for Part 2."""


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
    return (0, tuple(sorted(zip(chips_pos, gens_pos))))


def simulate(initial_state):
    found_states = {initial_state: 0}
    to_do = deque([initial_state])
    while to_do:
        print('{} states found so far'.format(len(found_states)))
        current_state = to_do.pop()
        for next_move in find_moves(current_state):
            # trim out based on move -- don't move down
            state = make_move(current_state, *next_move)
            if is_complete(state):
                moves = found_states[current_state] + 1
                print('Solution found in {} moves'.format(moves))
                return moves

            if state in found_states:
                # print('State already found.')
                continue
            found_states[state] = found_states[current_state] + 1

            if is_invalid(state):
                # print('Invalid state.')
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
    cargos = chain(doubles, singles)
    moves = product(destinations(state), cargos)
    return moves


def destinations(state):
    elevator = state[0]
    if elevator > 0:
        yield elevator - 1
    if elevator < 3:
        yield elevator + 1


def doubles_at_elevator(state):
    # Discrete combinations, no duplicates or repeats
    for obj1, obj2 in combinations(objects_at_elevator(state), 2):
        # Don't carry a chip and a generator of different elements
        if obj1[0] != obj2[0] and obj1[1] != obj1[1]:
            continue
        yield obj1, obj2


def objects_at_elevator(state):
    elevator, pairs = state
    for pair, obj_type in product(range(len(pairs)), range(2)):
        # Check if object is on the same floor as the elevator
        if pairs[pair][obj_type] == elevator:
            yield pair, obj_type


def make_move(state, destination, cargos):
    new_pairs = [list(pair) for pair in state[1]]
    for pair, obj_type in cargos:
        new_pairs[pair][obj_type] = destination
    new_pairs = tuple(sorted(tuple(pair) for pair in new_pairs))
    return (destination, new_pairs)


def is_complete(state):
    return all(pair == (3, 3) for pair in state[1])


def is_invalid(state):
    pairs = state[1]
    for chip, gen in pairs:
        if chip != gen:
            for _, other_gen in pairs:
                if other_gen == chip:
                    return True
    return False


def is_great_move(state, destination, cargos):
    # moving matched pair up
    pass


def is_bad_move(state, destination, cargos):
    # moving matched pair down
    # moving down when down is empty
    pass
