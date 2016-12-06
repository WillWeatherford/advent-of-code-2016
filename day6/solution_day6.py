"""
--- Day 6: Signals and Noise ---

Something is jamming your communications with Santa. Fortunately, your signal is only partially jammed, and protocol in situations like this is to switch to a simple repetition code to get the message through.

In this model, the same message is sent repeatedly. You've recorded the repeating message signal (your puzzle input), but the data seems quite corrupted - almost too badly to recover. Almost.

All you need to do is figure out which character is most frequent for each position. For example, suppose you had recorded the following messages:

eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar

The most common character in the first column is e; in the second, a; in the third, s, and so on. Combining these characters returns the error-corrected message, easter.

Given the recording in your puzzle input, what is the error-corrected version of the message being sent?

--- Part Two ---

Of course, that would be the message - if you hadn't agreed to use a modified repetition code instead.

In this modified code, the sender instead transmits what looks like random data, but for each character, the character they actually want to send is slightly less likely than the others. Even after signal-jamming noise, you can look at the letter distributions in each column and choose the least common letter to reconstruct the original message.

In the above example, the least common character in the first column is a; in the second, d, and so on. Repeating this process for the remaining characters produces the original message, advent.

Given the recording in your puzzle input and this new decoding methodology, what is the original message that Santa is trying to send?

"""
from __future__ import unicode_literals, division
from collections import Counter

INPUT_LEN = 8


def part1(lines):
    """Run solution for Part 1."""
    result = most_common_per_index(lines)
    print('The decoded message is: {}'.format(result))


def part2(lines):
    """Run solution for Part 2."""
    result = most_common_per_index(lines, reverse=True)
    print('The modified decoded message is: {}'.format(result))


def most_common_per_index(lines, reverse=False):
    """Find the most common letter in each index position across many lines."""
    gen = reversed if reverse else iter
    table = {}
    for line in lines:
        for idx, char in enumerate(line):
            counter = table.setdefault(idx, Counter())
            counter.update(char)
    results = [next(gen(table[idx].most_common()))[0] for idx in range(len(table))]
    return ''.join(results)
