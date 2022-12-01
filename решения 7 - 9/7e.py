a = int(input())
lst = list(map(int, input().split()))
nl = [lst[-1]]
lst = lst[:-1]
for i in lst:
    nl.append(i)
print(*nl)