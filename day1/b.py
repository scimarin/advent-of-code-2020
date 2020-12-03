#!/usr/bin/python

arr = []

with open('input.txt', 'r') as fin:
    for num in fin.readlines():
        arr.append(int(num.strip()))

for a in arr[:-2]:
    for b in arr[:-1]:
        for c in arr:
            if a + b + c == 2020:
                print(a * b * c)
