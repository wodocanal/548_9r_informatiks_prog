m, n = map(int, input().split())
lst = []
for i in range(m):
    lst.append([])
    for j in range(n):
        lst[i].append(0)

for i in range(m):
    for j in range(n):
        if i == 0:
            lst[i][j] = 1
        else:
            lst[i][j] = lst[i-1][j] + lst[i][j-1]
for i in lst:
    print(*i)