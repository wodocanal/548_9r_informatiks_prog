'''import math
def divisors(n):
    ans = [1]
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            ans.append(i)
    return ans


    


a, b = map(int, input().split())
c = divisors(a)
d = divisors(b)
if sum(c) == b and sum(d) == a:
    print('YES')
else:
    print('NO')'''




from math import sqrt
a, b = map(int, input().split())

def divisors(n):
    ans = [1]
    if n % 2 == 0:
        ans.append(2)
        ans.append(n//2)
        for i in range(3, int(sqrt(n)+ 1)):
            if n % i == 0:
                ans.append(i)
                if n // i not in ans:
                    ans.append(n // i)

    else:
        for i in range(3, int(sqrt(n)+ 1), 2):
            if n % i == 0:
                ans.append(i)
                if n // i not in ans:
                    ans.append(n // i)

    return ans

if sum(divisors(a)) == b and sum(divisors(b)) == a:
    print('YES')
else:
    print('NO')