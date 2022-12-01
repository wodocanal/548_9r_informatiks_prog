s = int(input())
t=1
k=1
x = []
while k<s:
    for i in range(t):
        x.append(t)
    t=t+1
    k=k+t

for i in range(k-t,s):
    x.append(t)

print(*x)