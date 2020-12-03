#!/usr/bin/python

arr = []

with open('input.txt', 'r') as fin:
    for num in fin.readlines():
        arr.append(int(num.strip()))

arr = set(arr)

for i in arr:
    if 2020 - i in arr:
        print((2020 - i) * i)

