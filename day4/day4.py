"""
--- Day 4: Security Through Obscurity ---

Finally, you come across an information kiosk with a list of rooms. Of course, the list is encrypted and full of decoy data, but the instructions to decode the list are barely hidden nearby. Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order, with ties broken by alphabetization. For example:

    aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between x, y, and z, which are listed alphabetically.
    a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each), the first five are listed alphabetically.
    not-a-real-room-404[oarel] is a real room.
    totally-real-room-200[decoy] is not.

Of the real rooms from the list above, the sum of their sector IDs is 1514.

What is the sum of the sector IDs of the real rooms?
"""

from __future__ import unicode_literals, division
from collections import Counter
from operator import itemgetter
import re


ROOM_PAT = re.compile(r'(?P<name>[a-z\-]+)\-(?P<sector>\d+)\[(?P<checksum>[a-z]+)\]')


def input_lines(filename):
    """Return generator of lines from input file."""
    with open(filename, 'r') as input_file:
        for line in input_file:
            yield line.strip()


def sum_real_sectors(rooms):
    """Return total sum of all real room sectors."""
    return sum(is_real_room(room) for room in rooms)


def is_real_room(room):
    """Return int of sector if room is real; else return 0."""
    parts = parse_room(room)
    if order_name(parts['name']) == parts['checksum']:
        return int(parts['sector'])
    return 0


def parse_room(room):
    """Return regex match group dict of room string segments."""
    match = ROOM_PAT.match(room)
    try:
        return match.groupdict()
    except AttributeError:
        return {}


def order_name(name):
    """Return a string of letters representing the letters in a room name."""
    counts = Counter(name)
    counts.pop('-')
    by_alpha = sorted(counts.items())
    by_count = sorted(by_alpha, key=itemgetter(1), reverse=True)
    return ''.join(map(itemgetter(0), by_count))[:5]


if __name__ == '__main__':
    rooms = input_lines('input.txt')
    result1 = sum_real_sectors(rooms)
    print('Sum of all sector IDs is {}'.format(result1))
