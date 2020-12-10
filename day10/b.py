#!/usr/bin/python3

import math
from collections import defaultdict

with open('input.txt') as fin:
  jolts = [int(i) for i in fin.read().splitlines()]

dist = defaultdict(lambda: 0)

jolts.append(0)
jolts.append(max(jolts) + 3)
jolts.sort()

poss = [0] * len(jolts)

for i in range(len(jolts)):
  if i + 2 < len(jolts) and jolts[i + 2] - jolts[i] <= 3:
    poss[i] += 1
  if i + 3 < len(jolts) and jolts[i + 3] - jolts[i] <= 3:
    poss[i] += 1

chunks = []
acc = 0
for i in range(len(poss)):
  if poss[i] == 0 and acc != 0:
    chunks.append(acc)
    acc = 0
  else:
    acc += poss[i]

table = {
  0: 1,
  1: 2,
  3: 4,
  5: 7
}

ans = math.prod([table[i] for i in chunks])
print(ans)
