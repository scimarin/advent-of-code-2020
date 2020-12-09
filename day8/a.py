#!/usr/bin/python


with open('input.txt', 'r') as fin:
  instructions = fin.read().splitlines()

acc = 0

freq = [0] * len(instructions)
ir = 0

while freq[ir] < 1:
  opcode, arg = instructions[ir].split()
  arg = int(arg)

  freq[ir] += 1

  if opcode == 'nop':
    ir += 1
  elif opcode == 'jmp':
    ir += arg
  elif opcode == 'acc':
    acc += arg
    ir += 1

print(acc)
