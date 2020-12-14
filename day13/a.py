#!/usr/bin/python3

with open('input.txt', 'r') as fin:
    time, buses = fin.read().splitlines()
    time = int(time)
    buses = [int(x) for x in buses.split(',') if x != 'x']


ans_time = 1e9
ans_bus = 0

for bus in buses:
    mul = time // bus
    cur = bus * (mul + 1) - time

    if cur < ans_time:
        ans_time = cur
        ans_bus = bus

print(ans_time * ans_bus)
