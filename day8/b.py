#!/usr/bin/python


with open('input.txt', 'r') as fin:
  instructions = fin.read().splitlines()


def find_loop():
  acc = 0
  ir = 0
  run = {}
  loop = []

  while ir < len(instructions):
    opcode, arg = instructions[ir].split()
    arg = int(arg)

    prev_ir = ir

    if opcode == 'nop':
      ir += 1
    elif opcode == 'jmp':
      ir += arg
    elif opcode == 'acc':
      acc += arg
      ir += 1

    if prev_ir not in run:
      run[prev_ir] = ir
    else:
      loop.append(prev_ir)
    
      while ir != prev_ir:
        loop.append(ir)
        ir = run[ir]

      break
      
  return loop, acc


loop, acc = find_loop()

for i in range(len(instructions)):
  prev = instructions[i]
  opcode, arg = instructions[i].split()

  if opcode == 'jmp':
    instructions[i] = 'nop +0'
    loop, acc = find_loop()
    instructions[i] = prev
  elif opcode == 'nop':
    instructions[i] = 'nop {}'.format(arg)
    loop, acc = find_loop()
    instructions[i] = prev

  if loop == []:
    print(acc)
    break
