a = int(input())
lst1 = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
lst2 = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
if a == 100:
    print("C")
else:
    b = a % 10 - 1
    c = a // 10 - 1
    if a > 9:
        if a % 10 != 0:
            print(lst2[c] + lst1[b])
        else:
            print(lst2[c])
    else:
        print(lst1[b])
