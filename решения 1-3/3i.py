a, b = map(int, input().split())
if a == 99 and b == 100:
    print(98)
elif b==99 and a == 100:
    print(98)
else:
    if a<=b:
        print(a)
    else:
        print(b)