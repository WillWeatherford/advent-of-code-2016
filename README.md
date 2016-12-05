# advent-of-code-2016
Solutions and tools for Advent of Code 2016. http://adventofcode.com/2016

To set up git branches and directories for each day in the Advent of Code, use
the `make_directories` Python script from the command line:

`>>> python make_directories.py`

It can take two positional arguments, which are the start and end of the range
of days. Defaults are `1` and `26`, i.e. by default, running
`python make_directories.py` will create branches and folders for days 1 through
25.

Each folder will have this structure commited the branch of the same name:
```
dayN/
- __init__.py
- input_dayN.txt
- solution_dayN.py
- test_dayN.py
```

Each `solution_dayN.py` file has boilerplate functions `part1()` and `part2()`.
These can be executed on any branch by running the `run_aoc` Python script,
giving it the day number as a command line argument, e.g.:
`>>> python run_aoc.py 14` will execute `part1()` and `part2` in `solution_day14.py`.

Be sure to paste your text input for each day into your `input_dayN.txt` for
that day. `run_aoc.py` passes a generator of all lines from input text file
into `part1()` and `part2()`.