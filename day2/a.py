#!/usr/bin/python

class Policy:
    def __init__(self, min_span, max_span, letter):
        self.min_span = min_span
        self.max_span = max_span
        self.letter = letter

def parse(entry):
    policy, password = [e.strip() for e in entry.split(':')]
    span, letter = policy.split()
    min_span, max_span = [int(i) for i in span.split('-')]
    return Policy(min_span, max_span, letter), password

def valid(policy, password):
    letter = policy.letter
    count = 0
    for i in password:
        if i == letter:
            count += 1
    if policy.min_span <= count and count <= policy.max_span:
        return True
    return False

entries = []
with open('input.txt', 'r') as fin:
    for line in fin.readlines():
        entries.append(line.strip())

ans = 0
for entry in entries:
    policy, password = parse(entry)
    if valid(policy, password):
        ans += 1

print(ans)
