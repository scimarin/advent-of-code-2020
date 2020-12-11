#!/usr/bin/python3

with open('input.txt', 'r') as fin:
  igrid = fin.read().splitlines()

  # pad the grid
  igrid.insert(0, '.' * len(igrid[0]))
  igrid.append('.' * len(igrid[0]))

  grid = []
  for row in igrid:
    row = '.' + row + '.'
    grid.append(row)


directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def get_adj_seats(cur_state, x, y):
  adj = []
  for direction in directions:
    for i in range(1, max(len(grid), len(grid[0]))):
      nx, ny = x + direction[0] * i, y + direction[1] * i

      if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]):
        if grid[nx][ny] == '#' or grid[nx][ny] == 'L':
          adj.append(grid[nx][ny])
          break # once an empty/occupied seat found, stop searching in this direction

  return adj

def get_next_state(cur_state):
  next_state = []
  for i in range(0, len(cur_state)):
    next_row = []
    for j in range(0, len(cur_state[i])):
      if cur_state[i][j] == '.':
        next_cell = '.'
      else:
        adj = get_adj_seats(cur_state, i, j) # look from (i, j) in all directions for free/occupied seats

        next_cell = cur_state[i][j]

        if cur_state[i][j] == 'L' and '#' not in adj:
          next_cell = '#'
        elif cur_state[i][j] == '#' and adj.count('#') >= 5:
          next_cell = 'L'

      next_row.append(next_cell)
    next_state.append(''.join(next_row))

  return next_state

# simulate
while True:
  next_grid = get_next_state(grid)
  if grid == next_grid:
    break
  grid = next_grid


ans = 0
for row in grid:
  for seat in row:
    if seat == '#':
      ans += 1

print(ans)
