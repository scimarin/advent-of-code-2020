#!/usr/bin/python

passports = []

passport_fields = set([
    'byr', 'iyr', 'eyr',
    'hgt', 'hcl', 'ecl',
    'pid', 'cid',
])

with open('input.txt', 'r') as fin:
    passport = {}
    for line in fin.readlines():
        line = line.strip()
        if line == '':
            passports.append(passport)
            passport = {}

        idents = line.split()
        for ident in idents:
            key, value = ident.split(':')
            passport[key] = value

ans = 0
for passport in passports:
    keys = set(passport.keys())
    diff = passport_fields.difference(keys)
    if len(diff) == 0 or \
            (len(diff) == 1 and 'cid' in diff):
        ans += 1

print(ans)
