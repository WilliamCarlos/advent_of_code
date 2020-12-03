from functools import reduce

# Build toboggan land grid.
grid = []
with open("data/day3.txt") as f:
    for line in f:
        grid.append(line)

num_rows, num_cols = len(grid), len(grid[0])
print('rows, cols: {} {}'.format(num_rows, num_cols))

# Slope as (drow, dcol)
slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

# For each candidate slope
num_trees_list = []
for dr, dc in slopes:
    r = 0
    c = 0
    num_trees = 0

    # How many trees will I hit?
    while r < num_rows:

        # print('{:2} {:2}'.format(r, c))

        if grid[r][c] == "#":
            num_trees += 1

        r += dr
        c += dc

        c = c % (num_cols-1)
    num_trees_list.append(num_trees)

    # Answer for part 1.
    if ((dr, dc) == (1, 3)): print('\nPart 1: {}'.format(num_trees))

slopes_and_trees = sorted(zip(slopes, num_trees_list), key=lambda x: x[1])
print('You should probably take slope {}... {} trees :o\n'.format(*slopes_and_trees[0]))

for slope, trees in list(slopes_and_trees):
    print('slope {}: {} trees'.format(slope, trees))

# Answer for part 2.
print('\nPart2:')
print(reduce(lambda x, y: x*y, num_trees_list))
