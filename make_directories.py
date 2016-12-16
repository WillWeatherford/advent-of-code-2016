"""Setup for Advent of Code by making git branches and directories."""
from __future__ import unicode_literals, division
from subprocess import call
from run_aoc import FILENAMES
import sys
import os


HERE = os.path.abspath(os.path.dirname(__file__))
RETURN_TO = 'master'


def main(start=1, end=26):
    """Run program creating git branches, directories and files for AoC."""
    for day_num in range(start, end):
        day_name = 'day{}'.format(day_num)
        call(['git', 'checkout', '-b', day_name])
        path = os.path.join(HERE, day_name)
        os.mkdir(path)

        for fmt in FILENAMES:
            dest_filename = fmt.format(day_name)
            dest_filepath = os.path.join(path, dest_filename)
            template_filename = fmt.format('template')
            template_filepath = os.path.join(HERE, 'templates', template_filename)
            call(['cp', template_filepath, dest_filepath])
            call(['git', 'add', dest_filepath])
        call(['touch', os.path.join(path, '__init__.py')])
        call(['git', 'add', os.path.join(path, '__init__.py')])
        call(['git', 'commit', '-m', 'Committing {} files.'.format(day_name)])
        call(['git', 'checkout', RETURN_TO])


if __name__ == '__main__':
    main(*map(int, sys.argv[1:]))
