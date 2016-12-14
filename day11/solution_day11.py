"""
--- Day 11: Radioisotope Thermoelectric Generators ---

You come upon a column of four floors that have been entirely sealed off from the rest of the building except for a small dedicated lobby. There are some radiation warnings and a big sign which reads "Radioisotope Testing Facility".

According to the project status board, this facility is currently being used to experiment with Radioisotope Thermoelectric Generators (RTGs, or simply "generators") that are designed to be paired with specially-constructed microchips. Basically, an RTG is a highly radioactive rock that generates electricity through heat.

The experimental RTGs have poor radiation containment, so they're dangerously radioactive. The chips are prototypes and don't have normal radiation shielding, but they do have the ability to generate an electromagnetic radiation shield when powered. Unfortunately, they can only be powered by their corresponding RTG. An RTG powering a microchip is still dangerous to other microchips.

In other words, if a chip is ever left in the same area as another RTG, and it's not connected to its own RTG, the chip will be fried. Therefore, it is assumed that you will follow procedure and keep chips connected to their corresponding RTG when they're in the same room, and away from other RTGs otherwise.

These microchips sound very interesting and useful to your current activities, and you'd like to try to retrieve them. The fourth floor of the facility has an assembling machine which can make a self-contained, shielded computer for you to take with you - that is, if you can bring it all of the RTGs and microchips.

Within the radiation-shielded part of the facility (in which it's safe to have these pre-assembly RTGs), there is an elevator that can move between the four floors. Its capacity rating means it can carry at most yourself and two RTGs or microchips in any combination. (They're rigged to some heavy diagnostic equipment - the assembling machine will detach it for you.) As a security measure, the elevator will only function if it contains at least one RTG or microchip. The elevator always stops on each floor to recharge, and this takes long enough that the items within it and the items on that floor can irradiate each other. (You can prevent this if a Microchip and its Generator end up on the same floor in this way, as they can be connected while the elevator is recharging.)

You make some notes of the locations of each component of interest (your puzzle input). Before you don a hazmat suit and start moving things around, you'd like to have an idea of what you need to do.

When you enter the containment area, you and the elevator will start on the first floor.

For example, suppose the isolated area has the following arrangement:

The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.

As a diagram (F# for a Floor number, E for Elevator, H for Hydrogen, L for Lithium, M for Microchip, and G for Generator), the initial state looks like this:

F4 .  .  .  .  .  
F3 .  .  .  LG .  
F2 .  HG .  .  .  
F1 E  .  HM .  LM 

Then, to get everything up to the assembling machine on the fourth floor, the following steps could be taken:

    Bring the Hydrogen-compatible Microchip to the second floor, which is safe because it can get power from the Hydrogen Generator:

    F4 .  .  .  .  .  
    F3 .  .  .  LG .  
    F2 E  HG HM .  .  
    F1 .  .  .  .  LM 

    Bring both Hydrogen-related items to the third floor, which is safe because the Hydrogen-compatible microchip is getting power from its generator:

    F4 .  .  .  .  .  
    F3 E  HG HM LG .  
    F2 .  .  .  .  .  
    F1 .  .  .  .  LM 

    Leave the Hydrogen Generator on floor three, but bring the Hydrogen-compatible Microchip back down with you so you can still use the elevator:

    F4 .  .  .  .  .  
    F3 .  HG .  LG .  
    F2 E  .  HM .  .  
    F1 .  .  .  .  LM 

    At the first floor, grab the Lithium-compatible Microchip, which is safe because Microchips don't affect each other:

    F4 .  .  .  .  .  
    F3 .  HG .  LG .  
    F2 .  .  .  .  .  
    F1 E  .  HM .  LM 

    Bring both Microchips up one floor, where there is nothing to fry them:

    F4 .  .  .  .  .  
    F3 .  HG .  LG .  
    F2 E  .  HM .  LM 
    F1 .  .  .  .  .  

    Bring both Microchips up again to floor three, where they can be temporarily connected to their corresponding generators while the elevator recharges, preventing either of them from being fried:

    F4 .  .  .  .  .  
    F3 E  HG HM LG LM 
    F2 .  .  .  .  .  
    F1 .  .  .  .  .  

    Bring both Microchips to the fourth floor:

    F4 E  .  HM .  LM 
    F3 .  HG .  LG .  
    F2 .  .  .  .  .  
    F1 .  .  .  .  .  

    Leave the Lithium-compatible microchip on the fourth floor, but bring the Hydrogen-compatible one so you can still use the elevator; this is safe because although the Lithium Generator is on the destination floor, you can connect Hydrogen-compatible microchip to the Hydrogen Generator there:

    F4 .  .  .  .  LM 
    F3 E  HG HM LG .  
    F2 .  .  .  .  .  
    F1 .  .  .  .  .  

    Bring both Generators up to the fourth floor, which is safe because you can connect the Lithium-compatible Microchip to the Lithium Generator upon arrival:

    F4 E  HG .  LG LM 
    F3 .  .  HM .  .  
    F2 .  .  .  .  .  
    F1 .  .  .  .  .  

    Bring the Lithium Microchip with you to the third floor so you can use the elevator:

    F4 .  HG .  LG .  
    F3 E  .  HM .  LM 
    F2 .  .  .  .  .  
    F1 .  .  .  .  .  

    Bring both Microchips to the fourth floor:

    F4 E  HG HM LG LM 
    F3 .  .  .  .  .  
    F2 .  .  .  .  .  
    F1 .  .  .  .  .  

In this arrangement, it takes 11 steps to collect all of the objects at the fourth floor for assembly. (Each elevator stop counts as one step, even if nothing is added to or removed from it.)

In your situation, what is the minimum number of steps required to bring all of the objects to the fourth floor?


--- Part Two ---

You step into the cleanroom separating the lobby from the isolated area and put on the hazmat suit.

Upon entering the isolated containment area, however, you notice some extra parts on the first floor that weren't listed on the record outside:

    An elerium generator.
    An elerium-compatible microchip.
    A dilithium generator.
    A dilithium-compatible microchip.

These work just like the other generators and microchips. You'll have to get them up to assembly as well.

What is the minimum number of steps required to bring all of the objects, including these four new ones, to the fourth floor?

"""
from __future__ import unicode_literals, division
from itertools import chain, combinations, product
from collections import deque
from operator import itemgetter
import re

LINE_PAT = r'(\w+ium)(\sgenerator|\-compatible\smicrochip)'
MAX_MOVES = 30

PART2_EXTRA_INPUT = [
    'An elerium generator.',
    'An elerium-compatible microchip.',
    'A dilithium generator.',
    'A dilithium-compatible microchip.',
]


def part1(lines):
    """Run solution for Part 1."""
    initial_state = create_initial_state(lines)
    result = simulate(initial_state)
    print('Fewest moves for part 1: {}'.format(result))


def part2(lines):
    """Run solution for Part 2."""
    lines = list(lines)
    lines[0] += ' '.join(PART2_EXTRA_INPUT)
    initial_state = create_initial_state(lines)
    result = simulate(initial_state)
    print('Fewest moves for part 2: {}'.format(result))


def create_initial_state(lines):
    """Return a state-tuple of the initial state from text input.

    State is represented as a tuple: (e, ((c1, g2), (c4, g1), (c2, g4), ...))
    Where e is the floor where the elevator is located, and each paired tuple
    are the curent floors of the corresponding chip and generator for each
    element.
    """
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
    """Return the fewest number of steps for all pairs to reach 4th floor.

    Breadth first search keeping track of already found states to avoid
    repeated steps.
    No heuristic.
    """
    found_states = {initial_state: 0}
    to_do = deque([initial_state])
    while to_do:
        print('{} states found so far'.format(len(found_states)))
        current_state = to_do.pop()
        for new_state in find_new_states(current_state):
            # trim out based on move -- don't move down
            if is_complete(new_state):
                moves = found_states[current_state] + 1
                print('Solution found in {} moves'.format(moves))
                return moves

            if new_state in found_states:
                continue
            found_states[new_state] = found_states[current_state] + 1

            if is_invalid(new_state):
                continue

            to_do.appendleft(new_state)

# single chip
# single generator
# 2x generator
# 2x chip
# chip and gen of same element
    # don't move down
# NOT chip and gen of different elements


def find_new_states(state):
    """Return generator of all adjacent states."""
    singles = ((obj, ) for obj in objects_at_elevator(state))
    doubles = doubles_at_elevator(state)
    cargos = chain(doubles, singles)
    for destination, cargos in product(destinations(state), cargos):
        yield make_move(state, destination, cargos)


def destinations(state):
    """Return generator of up to 2 valid destinations to move (up/down)."""
    elevator = state[0]
    if elevator > 0:
        yield elevator - 1
    if elevator < 3:
        yield elevator + 1


def objects_at_elevator(state):
    """Return generator of indices of objects on same floor as elevator ."""
    elevator, pairs = state
    for pair, obj_type in product(range(len(pairs)), range(2)):
        # Check if object is on the same floor as the elevator
        if pairs[pair][obj_type] == elevator:
            yield pair, obj_type


def doubles_at_elevator(state):
    """Return generator of 2-object combinations at same floor as elevator."""
    # Discrete combinations, no duplicates or repeats
    for obj1, obj2 in combinations(objects_at_elevator(state), 2):
        # Don't carry a chip and a generator of different elements
        if obj1[0] != obj2[0] and obj1[1] != obj1[1]:
            continue
        yield obj1, obj2


def make_move(state, destination, cargos):
    """Return a new state by moving the objects to destination."""
    pairs = state[1]
    new_pairs = [list(pair) for pair in pairs]
    for pair, obj_type in cargos:
        new_pairs[pair][obj_type] = destination
    new_pairs = tuple(sorted(tuple(pair) for pair in new_pairs))
    return (destination, new_pairs)


def is_complete(state):
    """Return boolean of whether all objects are on top floor."""
    return all(pair == (3, 3) for pair in state[1])


def is_invalid(state):
    """Return True if microchip is on same floor as an un-matched generator."""
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
