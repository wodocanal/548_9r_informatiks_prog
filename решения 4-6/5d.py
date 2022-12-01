a = int(input())
q = []
for i in range(1, a+1):
    if a%i==0:
        q.append(i)
print(*q)