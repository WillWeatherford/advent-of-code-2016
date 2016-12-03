"""
--- Day 3: Squares With Three Sides ---

Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for triangles.

Or are they?

The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these aren't triangles. You can't help but mark the impossible ones.

In a valid triangle, the sum of any two sides must be larger than or equal to the remaining side. For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.

In your puzzle input, how many of the listed triangles are possible?

--- Part Two ---

Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of three vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated.

For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:

101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603

In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?

"""

INPUT_FILE = 'day3_input.txt'


def input_lines(filename):
    """Return a generator of all lines in given file."""
    with open(filename, 'r') as text_file:
        for line in text_file:
            yield line.strip()


def is_valid_triangle(numbers):
    """Return boolean of whether a set of integers is a valid triangle."""
    numbers = sorted(numbers)
    return sum(numbers[:2]) > numbers[-1]


def count_valid_triangles_by_line(lines):
    """Return an integer of the number of valid triangles found in input."""
    count = 0
    for line in lines:
        numbers = map(int, line.split())
        count += is_valid_triangle(numbers)
    return count


def count_valid_triangles_by_column(lines):
    """Return an integer of the number of valid triangles found in input."""
    count = 0
    while True:
        try:
            three_lines = [map(int, next(lines).split()) for _ in range(3)]
        except StopIteration:
            break
        rotated = zip(*reversed(three_lines))
        count += sum(map(is_valid_triangle, rotated))
    return count


if __name__ == '__main__':
    lines = input_lines(INPUT_FILE)
    result1 = count_valid_triangles_by_line(lines)
    print('There are {} valid triangles, looking at each line as a triangle.'
          ''.format(result1))

    lines = input_lines(INPUT_FILE)
    result2 = count_valid_triangles_by_column(lines)
    print('There are {} valid triangles, looking at 3 numbers in each column '
          'as a triangle.'.format(result2))
