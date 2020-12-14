#!/usr/bin/python3

# https://cp-algorithms.com/algebra/chinese-remainder-theorem.html
# https://cp-algorithms.com/algebra/module-inverse.html

with open('input.txt', 'r') as fin:
    _, arr = fin.read().splitlines()
    arr = arr.split(',')

a, p = [], []

for ix, add in enumerate(arr):
    if add == 'x':
        continue

    add = int(add)
    norm = add - ix
    while norm < 0:
        norm += add
    a.append(norm)
    p.append(add)

x = [0] * len(a)

r = [[0] * len(p)] * len(p)
for i in range(len(x)):
    for j in range(i):
        r[j][i] = pow(p[i], p[j] - 2)

for i in range(len(x)):
    x[i] = a[i]
    for j in range(i):
        x[i] = pow(p[j], p[i] - 2) * (x[i] - x[j])
        x[i] %= p[i]
        if x[i] < 0:
            x[i] += p[i]

ans = 0
for i in range(1, len(x)):
    term = x[i]
    for j in range(i):
        term *= p[j]
    ans += term

print(ans + a[0])
