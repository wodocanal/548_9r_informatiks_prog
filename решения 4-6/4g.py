
k = int(input())
m = int(input())
n = int(input())
if n<=k:
    ans = 2*m
elif (n * 2) % k == 0:
    ans = m *(n * 2 // k)
else:
    ans = m *(1 + (n * 2 // k))
    

print(ans)

