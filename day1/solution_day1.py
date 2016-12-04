"""
--- Day 1: No Time for a Taxicab ---
Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's oscillator is regulated by stars. Unfortunately, the stars have been stolen... by the Easter Bunny. To save Christmas, Santa needs you to retrieve all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.

The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?

For example:
Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
R5, L5, R5, R3 leaves you 12 blocks away.

How many blocks away is Easter Bunny HQ?
"""


# Transformation table to give appropriate new x, y values depending on facing.
MOVES = {
    'N': lambda x, y: (x, y + 1),
    'E': lambda x, y: (x + 1, y),
    'S': lambda x, y: (x, y - 1),
    'W': lambda x, y: (x - 1, y),
}


# Main transformation table to give appropriate new facing value.
TURNS = {
    'L': {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'},
    'R': {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'},
}


def parse_input(input_):
    """Parse a long input string of instructions."""
    for line in input_.strip().split('\n'):
        for instruction in line.split(', '):
            print(instruction)
            yield instruction[0], int(instruction[1:])


def calc_blocks_away(instructions):
    """Calculate the distance in blocks of the final position."""
    visited = set()
    x, y, facing = 0, 0, 'N'
    for turn, distance in instructions:
        facing = TURNS[turn][facing]
        for _ in range(distance):
            x, y = MOVES[facing](x, y)
            if (x, y) in visited:
                return abs(x) + abs(y)
            visited.add((x, y))
    return abs(x) + abs(y)


def step1(lines):
    """Process solution for Day 1 Step 1."""
    pass


def step2(lines):
    """Process solution for Day 1 Step 2."""
    pass
