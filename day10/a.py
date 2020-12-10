#!/usr/bin/python3

from collections import defaultdict

with open('example1.txt') as fin:
  jolts = [int(i) for i in fin.read().splitlines()]

dist = defaultdict(lambda: 0)

jolts.sort()
dist[3] += 1

o = 0
for j in jolts:
  dist[j - o] += 1
  o = j

print(dist[1] * dist[3])
print(dist)
