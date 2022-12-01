l = int(input())
lst = []
for i in range(l):
    lst.append(list(map(int, input().split())))
for col in zip(*lst):
    print(*col[::-1], sep = ' ')
