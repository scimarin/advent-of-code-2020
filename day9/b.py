#!/usr/bin/python3

with open('input.txt', 'r') as fin:
  data = [int(i) for i in fin.read().splitlines()]

def find_first_invalid():
  for ix in range(25, len(data)):
    before = data[ix-25:ix]
    no = data[ix]

    valid = False
    for ij in range(len(before)):
      if no - before[ij] in before:
        valid = True

    if not valid:
      break

  return no

target = find_first_invalid()

prefix_sum = [0] * len(data)
prefix_sum[0] = data[0]

for i in range(1, len(data)):
  prefix_sum[i] = prefix_sum[i - 1] + data[i]

head, tail = 0, -1
while head < len(prefix_sum):
  if tail == -1:
    cur_sum = prefix_sum[head]
  else:
    cur_sum = prefix_sum[head] - prefix_sum[tail]

  if cur_sum > target:
    tail += 1
  elif cur_sum < target:
    head += 1
  else:
    print(max(data[tail+1:head]) + min(data[tail+1:head]))
    break
