def summ(n):
    s = 0
    while n != 0:
        s += n % 10
        n = n // 10
    return s

def f(n):
    lst = [2, 3, 4, 5, 6, 7, 8, 9]
    su = summ(n)
    for i in lst:
        if su != summ(n * i):
            return False
        else:
            pass
    return True

a, b = map(int, input().split())
for i in range(a, b + 1):
    if f(i):
        print(i)
'''


a, b = map(int, input().split())
for i in range(a, b+1):
    if i % 9 == 0:
        print(i)'''