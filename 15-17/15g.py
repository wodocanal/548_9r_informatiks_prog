n = int(input())
n-=2
def f(a, b, n):
    if n == -2:
        return 0
    if n == -1:
        return 1
    if n == 0:
        return a + b
    c = a  + b
    n -= 1
    return f(b, c, n)

print(f(0, 1, n))