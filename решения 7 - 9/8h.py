lst = list(map(int, input().split()))
lst = lst[:-1]
a = [0] * 10
for i in lst:
    a[i] += 1
a = a[1:]
print(*a)