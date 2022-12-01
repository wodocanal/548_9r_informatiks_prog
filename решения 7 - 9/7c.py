a = int(input())
lst = list(map(int, input().split()))
c = 0
for i in range(1, len(lst)):
    if lst[i] > lst[i - 1]:
        c += 1
print(c)