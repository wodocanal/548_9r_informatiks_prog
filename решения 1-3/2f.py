a=int(input())
print(((a // 1000) ^ (a % 10)) + ((a // 100 % 10) ^ (a % 100 // 10)) + 1)