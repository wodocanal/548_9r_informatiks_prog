a = int(input())
b = int(input())
x = []
for i in range(a,b+1):
    if i%2 == 0:
        x.append(i)
print(*x)