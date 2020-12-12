#!/usr/bin/python3

with open('input.txt') as fin:
    instructions = fin.read().splitlines()


class Navigation:
    def __init__(self, head, xdir, ydir, xpos, ypos):
        self.head = head

        self.xdir = xdir
        self.ydir = ydir
        self.xpos = xpos
        self.ypos = ypos

        self.compass = ['N', 'E', 'S', 'W']

    def execute(self, command):
        if command[0] == 'L' or command[0] == 'R':
            self._turn(command)
        elif command[0] == 'F':
            self._move_forward(command)
        else:
            self._move_compass(command)

    def _move_forward(self, command):
        value = command[1:]
        self._move_compass(self.head + value)

    def _move_compass(self, command):
        direction, value = command[0], int(command[1:])

        if direction == 'N' or direction == 'S':
            self.xpos += value if self.xdir == direction else -value

            if self.xpos < 0:
                self.xdir = direction
                self.xpos = -self.xpos
        elif direction == 'W' or direction == 'E':
            self.ypos += value if self.ydir == direction else -value

            if self.ypos < 0:
                self.ydir = direction
                self.ypos = -self.ypos

    def _turn(self, command):
        direction, degrees = command[0], int(command[1:])
        ix = self.compass.index(self.head)

        if direction == 'L':
            self.head = self.compass[(ix - degrees // 90) % len(self.compass)]
        elif direction == 'R':
            self.head = self.compass[(ix + degrees // 90) % len(self.compass)]


navigation = Navigation('E', 'E', 'N', 0, 0)

for instruction in instructions:
    navigation.execute(instruction)

print(navigation.xpos + navigation.ypos)

