a = int(input())
lst = list(map(int, input().split()))
r = int(input())
pos = 0
while pos < len(lst) and lst[pos] >= r:
    pos += 1
print(pos + 1)
