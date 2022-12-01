a = int(input())
x = []
q = 1
while True:
    if q>a:
        break
    x.append(q)
    q+=q
print(*x)