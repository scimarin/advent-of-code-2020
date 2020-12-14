#!/usr/bin/python3

with open('input.txt', 'r') as fin:
    input_lines = fin.read().splitlines()


def apply(mask, value):
    value = list('{0:b}'.format(value))
    padding = ['0'] * (36 - len(value))

    value = padding + value

    for ix, bit in enumerate(mask):
        if bit == '0':
            pass
        elif bit == '1':
            value[ix] = '1'
        elif bit == 'X':
            value[ix] = 'X'

    return ''.join(value)

def generate(ref_address):
    bits = int(ref_address.count('X'))
    limit = 1 << bits

    addresses = []

    for i in range(limit):
        last_ix = 0
        address = list(ref_address)
        for j in range(bits):
            ix = address.index('X', last_ix)
            last_ix = ix + 1

            if (i & (1 << j)) > 0:
                address[ix] = '1'
            else:
                address[ix] = '0'
        addresses.append(''.join(address))

    return [''.join(address) for address in addresses]

memory = {}

mask = ''
for line in input_lines:
    if 'mask' in line:
        mask = line[line.index('=')+1:].strip()
    else:
        address = int(line[line.index('[')+1:line.index(']')])
        value = int(line[line.index('=')+1:])

        address = apply(mask, address)

        addresses = generate(address)
        for addr in addresses:
            memory[addr] = value

print(sum(memory.values()))
