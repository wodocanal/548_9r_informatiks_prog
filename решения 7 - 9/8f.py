a = int(input())
lst = list(map(int, input().split()))
count = 0

for i in range(len(lst)-1):
    if lst[i] > lst[i+1]:
        count+=1
print(count)