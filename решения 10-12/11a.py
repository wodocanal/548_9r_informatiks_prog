a = int(input())
lst = []
for i in range(a):
    a2 = []
    for j in range(a):
        a2.append(0)
    lst.append(a2)
for i in range(a):
    for j in range(a):
        if i+j+1>a:
            lst[i][j] = 2
        if i+j+1==a:
            lst[i][j]=1

for i in lst:
    print(*i)