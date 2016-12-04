"""Setup for Advent of Code by making git branches and directories."""
from __future__ import unicode_literals, division
from subprocess import call
import os

# Add dayname.py file
#   Import unicode_literals, empty docstring
#   def part1 and part2 functions
# Add test_dayname.py file
# Import unicode_literals, Docstring

SOLUTION_TEMPLATE = [
    '"""',
    '"""',
    'from __future__ import unicode_literals, division',
    '',
    '',
    'def part1(lines):',
    '   """Run solution for Part 1."""',
    '',
    '',
    'def part1(lines):',
    '   """Run solution for Part 1."""',
    '',
]

HERE = os.path.abspath(os.path.dirname(__file__))

RETURN_TO = 'automate-setup'


def test_names():
    """."""
    for n in range(2):
        yield 'test{}'.format(n)


def main(names):
    """."""
    for name in names:
        path = os.path.join(HERE, name)
        txt_filename = '.'.join((name, 'txt'))
        txt_filepath = os.path.join(path, txt_filename)
        solution_filename = '.'.join((name, 'py'))
        solution_filepath = os.path.join(path, solution_filename)

        call(['git', 'checkout', '-b', name])
        os.mkdir(path)
        call(['touch', txt_filepath])
        call(['git', 'add', txt_filepath])
        with open(solution_filepath, 'w') as solution_file:
            solution_file.writelines(SOLUTION_TEMPLATE)
        call(['git', 'add', solution_filepath])
        call(['git', 'commit', '-m', 'Committing {}.'.format(txt_filename)])
        call(['git', 'checkout', RETURN_TO])


if __name__ == '__main__':
    names = test_names()
    main(names)
