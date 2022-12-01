s1, s2 = '', ''
c = 0
for i in input()[:-1]:
    c += 1
    if c % 2:
        s1 += i
    else:
        s2 = i + s2
print(s1 + s2)