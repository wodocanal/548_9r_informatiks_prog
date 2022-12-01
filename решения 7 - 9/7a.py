a = int(input())
lst = list(map(int, input().split()))
l = lst[::2]
print(*l)