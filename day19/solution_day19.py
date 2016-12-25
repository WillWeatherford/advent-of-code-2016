"""

"""
from __future__ import unicode_literals, division
from collections import OrderedDict, deque
from itertools import chain

START_ELVES = 5


def part1(lines):
    """Run solution for Part 1."""

    # elves = OrderedDict.fromkeys(range(1, START_ELVES + 1), 1)

    # while len(elves) > 1:
    #     dead = set()

    #     stolen_from = False
    #     for elf_num, presents in elves.items():
    #         if elf_num in dead:
    #             continue
    #         target = (elf_num + len(elves)) // 2
    #     if len(elves) % 2:
    #         elves.move_to_end(stealer_num, last=False)

    #     for elf in dead:
    #         elves.pop(elf)
    #     dead = set()

    #     print('{} elves left'.format(len(elves)))

    # print(elves.popitem()[0])


START_ELVES = 3001330


def part2(lines):
    """Run solution for Part 2."""
    func = alternate
    print(func(START_ELVES))


# def divide_and_join(num_elves):
#     elves = deque(range(1, num_elves + 1))
#     while len(elves) > 1:
#         half = (len(elves) - 1) >> 1
#         elves = deque(chain(elves[:half], elves[half + 1:]))
#     return elves[0]


def alternate(num_elves):
    elves = deque(range(1, num_elves + 1))
    elves.rotate(-((len(elves) - 1) >> 1))
    while len(elves) > 1:
        if len(elves) % 2 == 0:
            elves.rotate(-1)
        elves.popleft()
    return elves[0]


def rotate_remove(num_elves):
    elves = deque(range(1, num_elves + 1))
    while len(elves) > 1:
        print('elf {} steals from elf {} out'.format(elves[0], elves[len(elves) // 2]))
        elves.remove(elves[len(elves) // 2])
        elves.rotate(-1)
    return elves[0]


def rotate_pop(num_elves):
    """Run solution for Part 2."""
    elves = deque(range(1, num_elves + 1))
    elves.rotate(-(len(elves) >> 1))
    while len(elves) > 1:
        print(elves[0])
        elves.popleft()
        elves.rotate(-1)
    return elves[0]


def rotate_pop_rotate(num_elves):
    """Run solution for Part 2."""
    elves = deque(range(1, num_elves + 1))
    while len(elves) > 1:
        # print('elf {} steals from elf {} out'.format(elves[0], elves[len(elves) // 2]))
        elves.rotate(-(len(elves) // 2))
        print('elf {} is out'.format(elves[0]))
        elves.popleft()
        elves.rotate((len(elves) // 2) - 1)
    return elves[0]
