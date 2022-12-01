n, m = map(int, input().split())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))
m = -1
x = 0
y = 0
for i in lst:
    q = max(i)
    if q>m:
        m = q
        x = i.index(m)
        y = lst.index(i)
print(m)
print(y, x)
