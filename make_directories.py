"""Setup for Advent of Code by making git branches and directories."""
from __future__ import unicode_literals, division
from subprocess import call
import os

HERE = os.path.abspath(os.path.dirname(__file__))


def test_names():
    """."""
    for n in range(2):
        yield 'test{}'.format(n)


def main(names):
    """."""
    for name in names:
        call(['git', 'checkout', '-b', name])
        path = os.path.join(HERE, name)
        os.mkdir(path)
        call(['touch', '.'.join((name, 'txt'))], cwd=path)
        call(['git', 'add', '.'.join((name, 'txt'))], cwd=path)
        call(['git', 'commit', '-m', 'Committing new {} file.'])
        call(['git', 'checkout', 'automate-setup'])


if __name__ == '__main__':
    names = test_names()
    main(names)
