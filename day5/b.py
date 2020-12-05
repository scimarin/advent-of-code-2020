#!/usr/bin/python3

import numpy as np

ids = []

def decode_row(part):
  start , end = 0, 127
  for c in part:
    mid = (start + end) // 2
    if c == 'F':
      end = mid
    elif c == 'B':
      start = mid + 1
  return start

def decode_col(part):
  start , end = 0, 7
  for c in part:
    mid = (start + end) // 2
    if c == 'L':
      end = mid
    elif c == 'R':
      start = mid + 1
  return start

with open('input.txt', 'r') as fin:
  for line in fin.readlines():
    line = line.strip()
    row = decode_row(line[:7])
    if line == '':
      break
    column = decode_col(line[7:])
    ids.append(row * 8 + column)

complete = set(np.arange(1, np.max(ids, axis=0) + 1).tolist())
ids = set(ids)
potential = complete.difference(ids)
print(list(potential)[-1])
