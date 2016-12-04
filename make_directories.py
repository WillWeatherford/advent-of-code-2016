"""Setup for Advent of Code by making git branches and directories."""
from __future__ import unicode_literals, division
from subprocess import call
from run_aoc import FILENAMES
import os


HERE = os.path.abspath(os.path.dirname(__file__))
RETURN_TO = 'master'


def main(day_range):
    """."""
    for day_num in day_range:
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
    main(range(5, 26))
