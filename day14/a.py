#!/usr/bin/python3


def apply(mask, value):
    for ix, bit in enumerate(mask[::-1]):
        if bit == '0':
            value &= ~(1 << ix)
        elif bit == '1':
            value |= (1 << ix)
    return value


memory = {}
with open('input.txt', 'r') as fin:
    mask = ''
    for line in fin.read().splitlines():
        if 'mask' in line:
            mask = line[line.index('=')+1:].strip()
        else:
            address = int(line[line.index('[')+1:line.index(']')])
            value = int(line[line.index('=')+1:].strip())

            memory[address] = apply(mask, value)

print(sum(memory.values()))
