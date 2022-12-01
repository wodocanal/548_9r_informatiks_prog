a = int(input())
b = int(input())
n = int(input())

r = a * n
k = b * n
r += (k//100)
k = (k%100)
print(r, k)