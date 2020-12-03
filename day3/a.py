#!/usr/bin/python

slopes = []
with open('input.txt', 'r') as fin:
    for line in fin.readlines():
        slopes.append(line.strip())

ans = 0
row, col = 0, 0
while row < len(slopes):
    if slopes[row][col] == '#':
        ans += 1
    col += 3
    col %= len(slopes[0])
    row += 1

print(ans)
