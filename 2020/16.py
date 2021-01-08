with open("input/16.txt") as f:
    lines = f.read().splitlines()
r2 = 20
n1 = 25

# 1
valid_numbers = []
# Rules
for line in lines[0:r2]:
    valid_values = line.split(': ')[1]
    valid_values = valid_values.split(' or ')
    for value_range in valid_values:
        start = int(value_range.split('-')[0])
        end = int(value_range.split('-')[1])
        valid_numbers += list(range(start, end+1))
        valid_numbers = list(set(valid_numbers))
# Nearby tickets
invalid_values = []
for line in lines[n1:]:
    values = [int(x) for x in line.split(',')]
    for v in values:
        if v not in valid_numbers:
            invalid_values += [v]
answer = 0
for x in invalid_values:
    answer += x
print(answer)

# 2
valid_numbers = []
# Rules
for line in lines[0:r2]:
    valid_values = line.split(': ')[1]
    valid_values = valid_values.split(' or ')
    for value_range in valid_values:
        start = int(value_range.split('-')[0])
        end = int(value_range.split('-')[1])
        valid_numbers += list(range(start, end+1))
        valid_numbers = list(set(valid_numbers))
# Get only valid tickets
invalid_values = []
valid_tickets = []
for line in lines[n1:]:
    valid_ticket = True
    values = [int(x) for x in line.split(',')]
    for v in values:
        if v not in valid_numbers:
            valid_ticket = False
            invalid_values += [v]
    if valid_ticket:
        valid_tickets += [line]
        
# Rules again
rules = {}
for line in lines[0:r2]:
    name = line.split(": ")[0]
    valid_values = line.split(': ')[1]
    valid_values = valid_values.split(' or ')
    vrange = []
    for value_range in valid_values:
        start = int(value_range.split('-')[0])
        end = int(value_range.split('-')[1])
        vrange += list(range(start, end+1))
    rules[name] = vrange

# Check valid tickets
fields = {}
for name in rules.keys():
    fields[name] = list(range(0, len(rules)))
found_fields = {}
for ticket in valid_tickets:
    values = [int(x) for x in ticket.split(',')]
    fields_to_remove = []
    for i, v in enumerate(values):
        for field in fields:
            if v not in rules[field]:
                # Remove possibility for this field
                remaining_values = fields[field]
                remaining_values.remove(i)
                fields[field] = remaining_values
                if len(remaining_values) == 1:
                    fields_to_remove += [field]
                    found_fields[field] = remaining_values[0]
    for field in list(set(fields_to_remove)):
        del fields[field]

# Resolve all fields
while len(found_fields) < len(rules):
    fields_to_remove = []
    found_fields_new = found_fields.copy()
    for field in found_fields:
        col = found_fields[field]
        for field in fields:
            if col in fields[field]:
                # Remove possibility for this field
                remaining_values = fields[field]
                remaining_values.remove(col)
                fields[field] = remaining_values
                if len(remaining_values) == 1:
                    fields_to_remove += [field]
                    found_fields_new[field] = remaining_values[0]
    for field in list(set(fields_to_remove)):
        del fields[field]
    found_fields = found_fields_new.copy()

your_ticket = [int(x) for x in lines[22].split(',')]
answer = 1
for field in found_fields:
    if 'departure' in field:
        answer *= your_ticket[found_fields[field]]
print(answer)