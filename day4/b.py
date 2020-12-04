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

def fields_present(passport):
    keys = set(passport.keys())
    diff = passport_fields.difference(keys)
    if len(diff) == 0 or \
            (len(diff) == 1 and 'cid' in diff):
        return True
    return False

def fields_valid(passport):
    for key, value in passport.items():
        if key == 'byr':
            if len(value) != 4: return False
            ival = int(value)
            if not (1920 <= ival and ival <= 2002):
                return False
        elif key == 'iyr':
            if len(value) != 4: return False
            ival = int(value)
            if not (2010 <= ival and ival <= 2020):
                return False
        elif key == 'eyr':
            if len(value) != 4: return False
            ival = int(value)
            if not (2020 <= ival and ival <= 2030):
                return False
        elif key == 'hgt':
            unit = value[-2:]
            if unit == 'cm':
                ival = int(value[:-2])
                if not(150 <= ival and ival <= 193):
                    return False
            elif unit == 'in':
                ival = int(value[:-2])
                if not(59 <= ival and ival <= 76):
                    return False
            else:
                return False
        elif key == 'hcl':
            if not(len(value) == 7 and value[:1] == '#' and value[1:].isalnum()):
                return False
        elif key == 'ecl':
            if value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return False
        elif key == 'pid':
            if not(len(value) == 9 and value.isnumeric()):
                return False
        elif key == 'cid':
            pass
    return True

ans = 0
for passport in passports:
    if fields_present(passport) and fields_valid(passport):
        ans += 1

print(ans)
