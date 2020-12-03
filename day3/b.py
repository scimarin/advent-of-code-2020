#!/usr/bin/python

slopes = []
with open('input.txt', 'r') as fin:
    for line in fin.readlines():
        slopes.append(line.strip())


def sim(inc_row, inc_col):
    ans = 0
    row, col = 0, 0
    while row < len(slopes):
        if slopes[row][col] == '#':
            ans += 1
        col += inc_col
        col %= len(slopes[0])
        row += inc_row
    return ans

routes = [
    (1, 1),
    (1, 3),
    (1, 5),
    (1, 7),
    (2, 1),
]

ans = 1
for route in routes:
    ans *= sim(route[0], route[1])

print(ans)
