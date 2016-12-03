"""
--- Day 3: Squares With Three Sides ---

Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for triangles.

Or are they?

The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these aren't triangles. You can't help but mark the impossible ones.

In a valid triangle, the sum of any two sides must be larger than or equal to the remaining side. For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.

In your puzzle input, how many of the listed triangles are possible?
"""

INPUT_FILE = 'day3_input.txt'


def input_lines(filename):
    """Return a generator of all lines in given file."""
    with open(filename, 'r') as text_file:
        for line in text_file:
            yield line.strip()


def count_valid_triangles(lines):
    """Return an integer of the number of valid triangles found in input."""
    count = 0
    for line in lines:
        numbers = set(map(int, line.split()))
        largest = max(numbers)
        numbers.remove(largest)
        count += sum(numbers) >= largest
    return count


if __name__ == '__main__':
    lines = input_lines(INPUT_FILE)
    result = count_valid_triangles(lines)
    print('There are {} valid triangles.'.format(result))
