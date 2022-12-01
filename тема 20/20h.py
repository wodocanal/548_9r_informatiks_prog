n, a = map(int, input().split())
lst = []
def f(lst):
    return lst[0]
for i in range(n):
    lst.append(list(map(int, input().split())))
lst = sorted(lst, key=f, reverse=False)
c = 0
for i in lst:
    if a >= i[0]:
        c += 1
        a += i[1]
print(c)