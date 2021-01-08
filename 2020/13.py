with open("input/13.txt") as f:
    lines = f.read().splitlines()

# 1
start = int(lines[0])
time = start
buses = [int(bus) for bus in lines[1].split(',') if bus != 'x']
buses.sort()
first_bus = 0
first_time = 9999999999999
for bus in buses:
    this_time = start + bus - (time % bus)
    if this_time < first_time:
        first_bus = bus
        first_time = this_time
print(first_bus * (first_time - time))

from math import gcd


# 2
def compute_lcm(a):
    lcm = a[0]
    for i in a[1:]:
        lcm = lcm * i // gcd(lcm, i)
    return lcm

def part_two(ids):
    buses = []
    for bus in ids:
        if bus != 'x':
            buses.append(int(bus))
        else:
            buses.append('x')
    timestamp = 0
    matched_buses = [buses[0]]
    while True:
        print(matched_buses, compute_lcm(matched_buses))
        timestamp += compute_lcm(matched_buses)
        for i, bus in enumerate(buses):
            if bus != 'x':
                if (timestamp + i) % bus == 0:
                    if bus not in matched_buses:
                        matched_buses.append(bus)
        if len(matched_buses) == len(buses) - buses.count('x'):
            break
    return timestamp

print(part_two(lines[1].split(',')))