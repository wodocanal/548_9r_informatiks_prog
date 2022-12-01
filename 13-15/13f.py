from math import sqrt
def divisors(n):
    ans = [n]
    if n % 2 == 0:
        ans.append(2)
    for i in range(3, int(sqrt(n)+1), 2):
        if n % i == 0:
            ans.append(i)

    return ans
    
a = divisors(int(input()))
print(min(a))