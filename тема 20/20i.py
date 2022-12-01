n = int(input())
c = 0
q = True
def f(n):
    return n[3]
a = list(map(int, input().split()))
b = list(map(int, input().split()))
u = [i for i in range(1, n+1)]
lst = [[u[i], a[i], b[i], a[i]+b[i]] for i in range(n)]
lst = sorted(lst, key=f, reverse=True)
for i in range(n-1, -1, -1):
    e = lst[i][2] - c
    c = lst[i][1]
    if e <= 0:
        print(-1)
        q = False
        break
if q:
    for i in lst:
        print(i[0], end=' ')