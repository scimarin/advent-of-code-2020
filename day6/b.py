#!/usr/bin/python3

with open('input.txt', 'r') as fin:
  group = {}
  no = 0
  ans = 0
  for line in fin.readlines():
    line = line.strip()
    if line == '':
      for key, value in group.items():
        if value == no:
          ans += 1
      no = 0
      group = {}
      continue

    for c in line:
      if c not in group:
        group[c] = 1
      else:
        group[c] += 1
    no += 1
    
print(ans)
