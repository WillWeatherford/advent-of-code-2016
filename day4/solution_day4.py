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

--- Part Two ---

With all the decoy data out of the way, it's time to decrypt this list and get moving.

The room names are encrypted by a state-of-the-art shift cipher, which is nearly unbreakable without the right software. However, the information kiosk designers at Easter Bunny HQ were not expecting to deal with a master cryptographer like yourself.

To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's sector ID. A becomes B, B becomes C, Z becomes A, and so on. Dashes become spaces.

For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.

What is the sector ID of the room where North Pole objects are stored?
"""

from __future__ import unicode_literals, division
from string import ascii_lowercase
from collections import Counter
from operator import itemgetter
import re


ROOM_PAT = re.compile(r'(?P<name>[a-z\-]+)\-(?P<sector>\d+)\[(?P<checksum>[a-z]+)\]')

ORD_MAP = dict(zip(ascii_lowercase, range(26)))
CHR_MAP = dict(zip(range(26), ascii_lowercase))


def is_real_room(name, sector, checksum):
    """Return int of sector if room is real; else return 0."""
    if order_name(name) == checksum:
        return int(sector)
    return 0


def parse_room(room):
    """Return regex match group dict of room string segments."""
    match = ROOM_PAT.match(room)
    try:
        return match.groups()
    except AttributeError:
        return {}


def order_name(name):
    """Return a string of letters representing the letters in a room name."""
    counts = Counter(name)
    counts.pop('-')
    by_alpha = sorted(counts.items())
    by_count = sorted(by_alpha, key=itemgetter(1), reverse=True)
    return ''.join(map(itemgetter(0), by_count))[:5]


def decode_real_rooms(rooms):
    """Return generator of decoded names of real rooms."""
    for room in rooms:
        name, sector, checksum = parse_room(room)
        if is_real_room(name, sector, checksum):
            yield rotate_name(name, sector), sector


def rotate_name(name, sector):
    """Rotate name forward in alphabet number of spaces equal to its sector."""
    return ''.join([rotate_letter(letter, int(sector)) for letter in name])


def rotate_letter(letter, mod):
    """Move a letter forward mod number of spaces in the alphabet."""
    if letter == '-':
        return ' '
    moved = ORD_MAP[letter] + mod
    return CHR_MAP[moved % 26]


def part1(lines):
    """Return total sum of all real room sectors."""
    result = sum(is_real_room(*parse_room(room)) for room in lines)
    print('Sum of all sector IDs is {}'.format(result))


def part2(rooms):
    """Return the sector ID of room containing northpole object."""
    for name, sector in decode_real_rooms(rooms):
        if 'northpole object' in name:
            break
    print('The northpole objects are in sector {}'.format(sector))
