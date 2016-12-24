"""

"""
from __future__ import unicode_literals, division


def part1(lines):
    """Run solution for Part 1."""
    table = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
    result = process_instructions(lines, table)
    print('Value of register "a" after execution: {}'.format(result))


def part2(lines):
    """Run solution for Part 2."""
    table = {'a': 12, 'b': 0, 'c': 1, 'd': 0}
    result = process_instructions(lines, table)
    print('Value of register "a" after execution: {}'.format(result))


def process_instructions(lines, table):
    """Return value of table register "a" after executing instruction lines."""
    instructions = list(lines)
    idx = 0
    while idx < len(instructions):
        print(instructions[idx])
        cmd, *args = instructions[idx].split()
        if cmd == 'tgl':
            args.extend([idx, instructions])

        idx += globals()[cmd](table, *args)
    return table['a']


def tgl(table, register, idx, instructions):
    """Toggle the instruction at distance determined by value of register."""
    target_idx = idx + table[register]
    if target_idx < 0:
        return 1
    try:
        cmd, *args = instructions[target_idx].split()
    except IndexError:
        return 1

    if len(args) == 1:
        cmd = 'dec' if cmd == 'inc' else 'inc'
    elif len(args) == 2:
        cmd = 'cpy' if cmd == 'jnz' else 'jnz'

    instructions[target_idx] = ' '.join([cmd] + args)
    return 1


def cpy(table, val, register):
    """Copy val (either an integer or value of a register) into register y."""
    try:
        val = table[val]
    except KeyError:
        pass
    table[register] = int(val)
    return 1


def inc(table, register):
    """Increase the value of given register by 1."""
    table[register] += 1
    return 1


def dec(table, register):
    """Decrease the value of given register by 1."""
    table[register] -= 1
    return 1


def jnz(table, val, jump_distance):
    """Jump the given distance/direction in the instructions list."""
    try:
        zero_val = table[val]  # Check if the given val is a register.
    except KeyError:
        zero_val = int(val)  # Otherwise, it's just an integer.
    if zero_val == 0:
        return 1
    try:
        return table[jump_distance]  # Check if the given distance is a register.
    except KeyError:
        return int(jump_distance)  # Otherwise, it's just an integer.
