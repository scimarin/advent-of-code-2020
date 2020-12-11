#!/usr/bin/python3

import numpy as np

with open('input.txt', 'r') as fin:
  igrid = fin.read().splitlines()

  igrid.insert(0, '.' * len(igrid[0]))
  igrid.append('.' * len(igrid[0]))

  grid = []
  for row in igrid:
    row = '.' + row + '.'
    grid.append(row)

def get_next_state(cur_state):
  next_state = []
  for i in range(0, len(cur_state)):
    next_row = []
    for j in range(0, len(cur_state[i])):
      if cur_state[i][j] == '.':
        next_cell = '.'
      else:
        adj = [
          cur_state[i][j - 1], cur_state[i][j + 1], cur_state[i - 1][j], cur_state[i + 1][j],
          cur_state[i - 1][j - 1], cur_state[i + 1][j + 1], cur_state[i - 1][j + 1], cur_state[i + 1][j - 1],
        ]

        next_cell = cur_state[i][j]

        if cur_state[i][j] == 'L' and '#' not in adj:
          next_cell = '#'
        elif cur_state[i][j] == '#' and adj.count('#') >= 4:
          next_cell = 'L'

      next_row.append(next_cell)
    next_state.append(''.join(next_row))

  return next_state

while True:
  next_grid = get_next_state(grid)
  if grid == next_grid:
    break
  grid = next_grid

ans = 0
for line in grid:
  ans += line.count('#')

print(ans)
