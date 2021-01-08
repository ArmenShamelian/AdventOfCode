with open("input/04.txt") as f:
    passports_lines = f.read().splitlines()

# 1
# Parse passports
passports = []
start = 0
end = 0

def parse_passport(start, end):
    p = ''
    for i in range(start, end+1):
        p += ' ' + passports_lines[i]
    return p

for l in passports_lines:
    if l == '':
        this_pp = parse_passport(start, end)
        passports += [this_pp]
        start = end+1
        end = start
    else:
        end += 1
        
# Attach last passport too
this_pp = parse_passport(start, len(passports_lines)-1)
passports += [this_pp]

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid = 0
for p in passports:
    correct_so_far = True
    for field in required_fields:
        if field + ':' not in p:
            correct_so_far = False
    if correct_so_far:
        valid += 1
print(valid)

# 2
import re

def byr(p):
    try:
        year = int(p.split("byr:")[1][0:4])
        if (year >= 1920) and (year <= 2002):
            return True
        return False
    except:
        return False
def iyr(p):
    try:
        year = int(p.split("iyr:")[1][0:4])
        if (year >= 2010) and (year <= 2020):
            return True
        return False
    except:
        return False
def eyr(p):
    try:
        year = int(p.split("eyr:")[1][0:4])
        if (year >= 2020) and (year <= 2030):
            return True
        return False
    except:
        return False
def hgt(p):
    try:
        height = p.split("hgt:")[1].split(" ")[0]
        number = int(height[:-2])
        unit = height[-2:]
        if (unit == 'cm') and (number >= 150) and (number <= 193):
            return True
        if (unit == "in") and (number >= 59) and (number <= 76):
            return True
        else:
            return False
    except Exception as e:
        return False
def hcl(p):
    try:
        ex = r"(hcl:#[0-9a-f]{6})"
        if re.search(ex, p) is not None:
            return True
        return False
    except: return False
def ecl(p):
    try:
        color = p.split("ecl:")[1][0:3]
        if color in ["amb","blu","brn","gry","grn","hzl","oth"]:
            return True
        return False
    except: return False
def pid(p):
    try:
        ex = r"(pid:[0-9]{9})"
        if re.search(ex, p) is not None:
            return True
        return False
    except: return False

valid = 0
for p in passports:
    correct_so_far = True
    for field in required_fields:
        if field + ':' not in p:
            correct_so_far = False
    if not (byr(p) and iyr(p) and eyr(p) and hgt(p) and hcl(p) and ecl(p) and pid(p)):
        correct_so_far = False
    if correct_so_far:
        valid += 1
print(valid)