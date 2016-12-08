"""
--- Day 8: Two-Factor Authentication ---

You come across a door implementing what you can only assume is an implementation of two-factor authentication after a long game of requirements telephone.

To get past the door, you first swipe a keycard (no problem; there was one on a nearby desk). Then, it displays a code on a little screen, and you type that code on a keypad. Then, presumably, the door unlocks.

Unfortunately, the screen has been smashed. After a few minutes, you've taken everything apart and figured out how it works. Now you just have to work out what the screen would have displayed.

The magnetic strip on the card you swiped encodes a series of instructions for the screen; these instructions are your puzzle input. The screen is 50 pixels wide and 6 pixels tall, all of which start off, and is capable of three somewhat peculiar operations:

    rect AxB turns on all of the pixels in a rectangle at the top-left of the screen which is A wide and B tall.
    rotate row y=A by B shifts all of the pixels in row A (0 is the top row) right by B pixels. Pixels that would fall off the right end appear at the left end of the row.
    rotate column x=A by B shifts all of the pixels in column A (0 is the left column) down by B pixels. Pixels that would fall off the bottom appear at the top of the column.

For example, here is a simple sequence on a smaller screen:

    rect 3x2 creates a small rectangle in the top-left corner:

    ###....
    ###....
    .......

    rotate column x=1 by 1 rotates the second column down by one pixel:

    #.#....
    ###....
    .#.....

    rotate row y=0 by 4 rotates the top row right by four pixels:

    ....#.#
    ###....
    .#.....

    rotate row x=1 by 1 again rotates the second column down by one pixel, causing the bottom pixel to wrap back to the top:

    .#..#.#
    #.#....
    .#.....

As you can see, this display technology is extremely powerful, and will soon dominate the tiny-code-displaying-screen market. That's what the advertisement on the back of the display tries to convince you, anyway.

There seems to be an intermediate check of the voltage used by the display: after you swipe your card, if the screen did work, how many pixels should be lit?

"""
from __future__ import unicode_literals, division
from itertools import chain


HEIGHT = 6
WIDTH = 50


def part1(lines):
    """Run solution for Part 1."""
    display = TinyDisplay()
    for line in lines:
        display.parse_command(line)
    print('{} cells are lit.'.format(display.count_lit()))


def part2(lines):
    """Run solution for Part 2."""
    display = TinyDisplay()
    for line in lines:
        display.parse_command(line)
    display.print_code()


class TinyDisplay(object):
    """A Python class representation of the tiny display in the challenge."""

    def __init__(self, height, width):
        """Initialize a tiny display."""
        self.height = height
        self.width = width
        self.grid = [[0] * self.width for _ in range(self.height)]

    def parse_command(self, line):
        """Parse a text command."""
        # r'(?P<cmd>rect|rotate\srow|rotate\scolumn)\s()'
        if line.startswith('rect'):
            cmd, rest = line.split()
            args = rest.split('x')
        else:
            parts = line.split()
            cmd = '_'.join(parts[:2])
            _, pos = parts[2].split('=')
            args = (pos, parts[-1])
        method = getattr(self, cmd)
        method(*map(int, args))

    def rect(self, cols, rows):
        """Turn on all pixels in upper left corner of grid.

        Turns on all of the pixels in a rectangle at the top-left of the
        screen which is A wide and B tall.
        """
        for y in range(rows):
            for x in range(cols):
                self.grid[y][x] = 1

    def rotate_row(self, row, shifts):
        """Shift all pixels in row right by given number of shifts.

        0 is the top row.
        Pixels that would fall off the right end appear at the left end of
        the row.
        """
        new_row = [self.grid[row][x - shifts] for x in range(self.width)]
        self.grid[row] = new_row

    def rotate_column(self, col, shifts):
        """Shift all pixels in col down by given number of shifts.

        0 is the left column.
        Pixels that would fall off the bottom appear at the left end of
        the row.
        """
        current_col = [row[col] for row in self.grid]
        for y in range(self.height):
            self.grid[y][col] = current_col[y - shifts]

    def count_lit(self):
        """Return number of lit cells."""
        return sum(chain(*self.grid))

    def print_code(self):
        for topleft in range(0, self.width, 5):
            segments = [row[topleft:topleft + 5] for row in self.grid]
            segments = [''.join(map(lambda c: '#' if c else ' ', seg))
                        for seg in segments]
            print('\n'.join(segments))
            print('\n')
