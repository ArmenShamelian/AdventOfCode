input_min = 248345
input_max = 746315

def has_double(i):
    s = str(i)
    for n in range(len(s)-1):
        if s[n] == s[n+1]:
            return True
    return False

def all_increasing(i):
    s = str(i)
    for n in range(len(s)-1):
        if int(s[n]) <= int(s[n+1]):
            continue
        else:
            return False
    return True

def check_password(i):
    a = has_double(i)
    b = all_increasing(i)
    return a and b

pw = []
for i in range(input_min, input_max+1):
    if check_password(i):
        pw += [i]

print(len(pw))

def has_real_double(i):
    s = str(i)
    if s[0] == s[1] and s[1] != s[2]:
        return True
    elif s[-1] == s[-2] and s[-2] != s[-3]:
        return True
    for n in range(1,len(s)-2):
        if s[n] == s[n+1] and s[n-1] != s[n] and s[n+1] != s[n+2]:
            return True
    return False

def check_password_2(i):
    a = has_real_double(i)
    b = all_increasing(i)
    return a and b

pw = []
for i in range(input_min, input_max+1):
    if check_password_2(i):
        pw += [i]

print(len(pw))