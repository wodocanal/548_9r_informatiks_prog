a = int(input())
lst = []
for i in range(a):
    lst.append(list(map(int, input().split())))
ans = True
for i in range(a):
    for j in range(a):
        if lst[i][j] != lst[j][i]:
            ans = False
print('yes' if ans else 'no')
