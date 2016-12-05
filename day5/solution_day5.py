"""
--- Day 5: How About a Nice Game of Chess? ---

You are faced with a security door designed by Easter Bunny engineers that seem to have acquired most of their security knowledge by watching hacking movies.

The eight-character password for the door is generated one character at a time by finding the MD5 hash of some Door ID (your puzzle input) and an increasing integer index (starting with 0).

A hash indicates the next character in the password if its hexadecimal representation starts with five zeroes. If it does, the sixth character in the hash is the next character of the password.

For example, if the Door ID is abc:

    The first index which produces a hash that starts with five zeroes is 3231929, which we find by hashing abc3231929; the sixth character of the hash, and thus the first character of the password, is 1.
    5017308 produces the next interesting hash, which starts with 000008f82..., so the second character of the password is 8.
    The third time a hash starts with five zeroes is for abc5278568, discovering the character f.

In this example, after continuing this search a total of eight times, the password is 18f47a30.

Given the actual Door ID, what is the password?

--- Part Two ---

As the door slides open, you are presented with a second door that uses a slightly more inspired security mechanism. Clearly unimpressed by the last version (in what movie is the password decrypted in order?!), the Easter Bunny engineers have worked out a better solution.

Instead of simply filling in the password from left to right, the hash now also indicates the position within the password to fill. You still look for hashes that begin with five zeroes; however, now, the sixth character represents the position (0-7), and the seventh character is the character to put in that position.

A hash result of 000001f means that f is the second character in the password. Use only the first result for each position, and ignore invalid positions.

For example, if the Door ID is abc:

    The first interesting hash is from abc3231929, which produces 0000015...; so, 5 goes in position 1: _5______.
    In the previous method, 5017308 produced an interesting hash; however, it is ignored, because it specifies an invalid position (8).
    The second interesting hash is at index 5357525, which produces 000004e...; so, e goes in position 4: _5__e___.

You almost choke on your popcorn as the final character falls into place, producing the password 05ace8e3.

Given the actual Door ID and this new method, what is the password? Be extra proud of your solution if it uses a cinematic "decrypting" animation.

"""
from __future__ import unicode_literals, division
from itertools import count
from hashlib import md5

PASSWORD_LEN = 8
FIVE_ZEROES = '0' * 5


def part1(lines):
    """Run solution for Part 1."""
    line = next(lines)
    result = decode_password1(line)
    print('The first door code for door ID {} is {}'.format(line, result))


def part2(lines):
    """Run solution for Part 2."""
    line = next(lines)
    result = decode_password2(line)
    print('The second door code for door ID {} is {}'.format(line, result))


def get_bytes_val(door_id, n):
    """Return a bytestring concatenation of door_id and index n."""
    return '{}{}'.format(door_id, n).encode('ascii')


def get_hashed_hex(bytes_val):
    """Return a single string character; the 6th char in a md5 hash of val.

    If the hashed does not start with five zeroes, returns empty string.
    """
    hashed = md5(bytes_val)
    return hashed.hexdigest()


def gen_valid_hexes(door_id):
    """Return a generator of all valid iterative hashed hexes of door ID.

    These are the hexidecimal value of the md5 hash of the door ID concatenated
    with sequence of integers starting with 0.
    """
    for n in count():
        bytes_val = get_bytes_val(door_id, n)
        hashed_hex = get_hashed_hex(bytes_val)
        if hashed_hex.startswith(FIVE_ZEROES):
            yield hashed_hex


def decode_password1(door_id):
    """Return decoded password for part 1."""
    hexes = gen_valid_hexes(door_id)
    result = [next(hexes)[5] for _ in range(PASSWORD_LEN)]
    return ''.join(result)


def decode_password2(door_id):
    """Return decoded password for part 2."""
    result = ['_'] * PASSWORD_LEN
    hexes = gen_valid_hexes(door_id)

    for _ in range(PASSWORD_LEN):
        while True:
            hashed_hex = next(hexes)

            try:
                position = int(hashed_hex[5])
            except ValueError:
                continue

            try:
                if result[position] != '_':
                    continue
            except IndexError:
                continue

            char = hashed_hex[6]
            result[position] = char
            break
    return ''.join(result)
