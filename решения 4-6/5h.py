a = int(input())
x = []
for i in range(1,a+1):
    q = i**2
    if q<=a:
        x.append(q)
print(*x, sep = '\n')