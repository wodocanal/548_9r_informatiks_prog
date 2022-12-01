n = int(input())
h = n // 60
m = n - h*60
h = h % 24
print(h, m)