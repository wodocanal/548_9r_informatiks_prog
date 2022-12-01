from math import sqrt
def isprime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True
ans = True
a = int(input())
while a != 0:
    if isprime(a) == False:
        ans = False
        break
    a = a // 10
    
print('YES' if ans == True else 'NO')