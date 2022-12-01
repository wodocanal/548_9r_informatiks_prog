a = list(input().split())
b = [len(i) for i in a]
print(a[b.index(max(b))])
print(max(b))