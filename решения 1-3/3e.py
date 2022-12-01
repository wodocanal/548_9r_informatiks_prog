a = int(input())
b = int(input())
c = int(input())
if c > a and c > b:
    print(c)
else:
    print(a if a > b else b)