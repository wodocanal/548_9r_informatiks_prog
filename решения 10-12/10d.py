fin = open('input.txt', 'r')
lst = fin.read().split()
cords = [0, 0]
for i in range(0, len(lst), 2):
    if lst[i] == 'South':
        cords[1] -= int(lst[i + 1])
    elif lst[i] == 'North':
        cords[1] += int(lst[i + 1])
    elif lst[i] == 'East':
        cords[0] += int(lst[i + 1])
    elif lst[i] == 'West':
        cords[0] -= int(lst[i + 1])
print(*cords)