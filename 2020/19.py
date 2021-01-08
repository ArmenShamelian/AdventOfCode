with open("input/19.txt") as f:
    lines = f.read().splitlines()

# 1
# Parse rules
rules = {}
end_rules = 0
for i, line in enumerate(lines):
    if line == '':
        end_rules = i+1
        break
    name, rule = line.split(': ')
    rules[int(name)] = rule.strip()
    end_rules += 1

def evaluate(rule, line):
    if '|' in rule:
        rule_1, rule_2 = rule.split(' | ')
        correct_1, remaining_1 = evaluate(rule_1, line)
        correct_2, remaining_2 = evaluate(rule_2, line)
        if correct_1:
            return correct_1, remaining_1
        if correct_2:
            return correct_2, remaining_2
        else:
            return False, ''
    elif ' ' in rule:
        this_rules = rule.split(' ')
        remaining = line
        for rule in this_rules:
            correct, remaining = evaluate(rules[int(rule)], remaining)
            if not correct:
                return False, ''
        return correct, remaining
    elif "a" in rule:
        try:
            if line[0] == "a":
                try:
                    return True, line[1:]
                except:
                    return False, ''
        except:
            return False, ''
        else:
            return False, line
    elif "b" in rule:
        try:
            if line[0] == "b":
                try:
                    return True, line[1:]
                except:
                    return False, ''
        except:
            return False, ''
        else:
            return False, line
    else:
        # Rule must be just an int
        correct, remaining = evaluate(rules[int(rule)], line)
        return correct, remaining
    
# Check lines
total_correct = 0
for i, line in enumerate(lines[end_rules:]):
    correct, remaining = evaluate(rules[0], line)
    if correct and (remaining == ''):
        total_correct += 1
print(total_correct)

# 2
# Parse rules
rules = {}
end_rules = 0
for i, line in enumerate(lines):
    if line == '':
        end_rules = i+1
        break
    elif line == '8: 42':
        rules[8] = "42 | 42 8"
    elif line == "11: 42 31":
        rules[11] = "42 31 | 42 11 31"
    else:
        name, rule = line.split(': ')
        rules[int(name)] = rule.strip()
    end_rules += 1

def evaluate(rule, line):
    if '|' in rule:
        rule_1, rule_2 = rule.split(' | ')
        results_1 = evaluate(rule_1, line)
        results_2 = evaluate(rule_2, line)
        return results_1 + results_2
    elif ' ' in rule:
        this_rules = rule.split(' ')
        remaining = [line]
        for rule in this_rules:
            results = []
            for r in remaining:
                results += evaluate(rules[int(rule)], r)
            remaining = results
        return remaining
    elif "a" in rule:
        try:
            if line[0] == "a":
                try:
                    return [line[1:]]
                except:
                    return []
        except:
            return []
        else:
            return []
    elif "b" in rule:
        try:
            if line[0] == "b":
                try:
                    return [line[1:]]
                except:
                    return []
        except:
            return []
        else:
            return []
    else:
        # Rule must be just an int
        results = evaluate(rules[int(rule)], line)
        return results
    
# Check lines
total_correct = 0
for i, line in enumerate(lines[end_rules:]):
    results = evaluate(rules[0], line)
    if '' in results:
        total_correct += 1
print(total_correct)