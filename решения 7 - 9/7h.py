a = int(input())
lst = list(map(int, input().split()))
ul = []
for i in lst:
    if i not in ul:
        ul.append(i)
print(len(ul))