n, m, k = map(int,input().split())
lst = []
for i in range(n):
    lst.append([])
for i in range(len(lst)):
    l = list(map(int, input().split()))
    for j in l:
        lst[i].append(j)

def f(n):
    for i in lst:
        ma = len(max(''.join(map(str,i)).split('1'), key = len))
        if ma >= k:
            return True
    return False
 
print('YES' if f(n) else 'NO')