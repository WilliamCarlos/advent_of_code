#!/usr/bin/env python

''' --- Day 1: Report Repair --- After saving Christmas five years in a row,
you've decided to take a vacation at a nice resort on a tropical island. Surely,
Christmas will go on without you.


The tropical island has its own currency and is entirely cash-only. The gold
coins used there have a little picture of a starfish; the locals just call them
stars. None of the currency exchanges seem to have heard of them, but somehow,
you'll need to find fifty of these coins by the time you arrive so you can pay
the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day
in the Advent calendar; the second puzzle is unlocked when you complete the
first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense
report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then
multiply those two numbers together.

For example, suppose your expense report contained the following:

1721 979 366 299 675 1456

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying
them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to
2020; what do you get if you multiply them together? '''

# TODO(williamylee): How do we auto-return at 80 chars?

print('hello world!')
entries = []
with open("day1.txt") as file:
    for line in file:
        entries.append(int(line))

# Part 1, naive
for i in range(len(entries)):
    for j in range(i, len(entries)):
        if entries[i] + entries[j] == 2020:
            print("{:15} Hurray, we found it! The numbers are {} and {} and"\
                  "their product is {}.".format('Part 1:', entries[i],
                                                entries[j],
                                                entries[i]*entries[j]))

# Part 1, but faster
memo = set()
for entry in entries:
    memo.add(entry)

for entry in entries:
    if 2020-entry in memo:
        print("{:15} Hurray, we found it! The numbers are {} and {} and "\
              "their product is {}.".format('Part 1 Linear:', entry, 2020-entry,
                                           2020*entry-entry**2))
        break

# Part 2: The elves need 3
# Idea: A 3-sum has a complement that is a valid 2-sum.
# First, we generalize part 1 in a function:
def two_sum(number):
    for entry in entries:
        if number - entry in memo:
            return (entry, number-entry)
    return (None, None)

# Find the number whose complement is a valid 2-sum.
for entry in entries:
    x, y = two_sum(2020-entry)
    if (x != None) and (x!=y and y!=entry and entry!=x):
        print("{:15} Hurray, we found it! The numbers are {}, {}, and {} and "\
              "their product is {}.".format('Part 2:', entry, x, y, entry*x*y))
        break
