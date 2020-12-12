#!/usr/bin/python3

with open('input.txt') as fin:
    instructions = fin.read().splitlines()


class CoordinateSystem:
    def __init__(self, head, xdir, ydir, xpos, ypos):
        self.head = head
        self.xdir = xdir
        self.ydir = ydir
        self.xpos = xpos
        self.ypos = ypos

    def __repr__(self):
        return '{}{} {}{}'.format(self.ydir, self.ypos, self.xdir, self.xpos)

class Navigation:
    def __init__(self, ship, waypoint):
        self.ship = ship
        self.waypoint = waypoint

        self.compass = ['NE', 'SE', 'SW', 'NW']

    def execute(self, command):
        symbol, value = command[0], int(command[1:])

        if command[0] == 'F':
            self._move_ship(value)
        elif command[0] == 'L' or command[0] == 'R':
            self._turn_waypoint(symbol, value)
        else:
            self._move_waypoint(symbol, value)

    def _move_ship(self, value):
        xamount = self.waypoint.xpos * value
        yamount = self.waypoint.ypos * value

        self.ship.xpos += xamount if self.ship.xdir == self.waypoint.xdir else -xamount
        if self.ship.xpos < 0:
            if self.ship.xdir == 'W':
                self.ship.xdir = 'E'
            else:
                self.ship.xdir = 'W'
            self.ship.xpos = -self.ship.xpos

        self.ship.ypos += yamount if self.ship.ydir == self.waypoint.ydir else -yamount
        if self.ship.ypos < 0:
            if self.ship.ydir == 'N':
                self.ship.ydir = 'S'
            else:
                self.ship.ydir = 'N'

            self.ship.ypos = -self.ship.ypos

    def _turn_waypoint(self, direction ,degrees):
        cur_dir = self.waypoint.ydir + self.waypoint.xdir
        ix = self.compass.index(cur_dir)

        if degrees == 90:
            temp = self.waypoint.xpos
            self.waypoint.xpos = self.waypoint.ypos
            self.waypoint.ypos = temp

            if direction == 'R':
                self.waypoint.ydir, self.waypoint.xdir = list(self.compass[(ix + 1) % len(self.compass)])
            elif direction == 'L':
                self.waypoint.ydir, self.waypoint.xdir = list(self.compass[(ix - 1) % len(self.compass)])
        elif degrees == 180:
            if direction == 'R':
                self.waypoint.ydir, self.waypoint.xdir = list(self.compass[(ix + 2) % len(self.compass)])
            elif direction == 'L':
                self.waypoint.ydir, self.waypoint.xdir = list(self.compass[(ix - 2) % len(self.compass)])
        elif degrees == 270:
            temp = self.waypoint.xpos
            self.waypoint.xpos = self.waypoint.ypos
            self.waypoint.ypos = temp

            if direction == 'R':
                self.waypoint.ydir, self.waypoint.xdir = list(self.compass[(ix + 3) % len(self.compass)])
            elif direction == 'L':
                self.waypoint.ydir, self.waypoint.xdir = list(self.compass[(ix - 3) % len(self.compass)])

    def _move_waypoint(self, direction, value):
        if direction == 'W' or direction == 'E':
            self.waypoint.xpos += value if self.waypoint.xdir == direction else -value

            if self.waypoint.xpos < 0:
                self.waypoint.xdir = direction
                self.waypoint.xpos = -self.waypoint.xpos
        elif direction == 'N' or direction == 'S':
            self.waypoint.ypos += value if self.waypoint.ydir == direction else -value

            if self.waypoint.ypos < 0:
                self.waypoint.ydir = direction
                self.waypoint.ypos = -self.waypoint.ypos



ship = CoordinateSystem('E', 'E', 'N', 0, 0)
waypoint = CoordinateSystem('E', 'E', 'N', 10, 1)

navigation = Navigation(ship, waypoint)

for instruction in instructions:
    navigation.execute(instruction)

print(navigation.ship.xpos + navigation.ship.ypos)

