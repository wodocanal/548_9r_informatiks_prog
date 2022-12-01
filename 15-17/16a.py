a, b = map(int, input().split())
if b > a:
    a, b = b, a
def f(a, b):
    if b == 0:
        return a
    return f(b, a%b)

print(f(a, b))