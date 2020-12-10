#!/usr/bin/python3

with open('input.txt', 'r') as fin:
  data = [int(i) for i in fin.read().splitlines()]

for ix in range(25, len(data)):
  before = data[ix-25:ix]
  no = data[ix]

  valid = False
  for ij in range(len(before)):
    if no - before[ij] in before:
      valid = True

  if not valid:
    print(no)
    break

