a = int(input())
lst = list(map(int, input().split()))
l = []
for i in lst:
    if i%2==0:
        l.append(i)
print(*l)