#!/usr/bin/python3

with open('input.txt', 'r') as fin:
  group = []
  ans = 0
  for line in fin.readlines():
    line = line.strip()
    if line == '':
      ans += len(set(group))
      group = []
      continue
    for c in line:
      group.append(c)
    
print(ans)
