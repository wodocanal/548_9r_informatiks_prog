a = int(input())
q = 1
w = 'NO'
while q<=a:
    if q == a:
        w = 'YES'
        break
    q+=q
print(w)