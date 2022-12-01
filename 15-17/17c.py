def solve(n, i, j, k):
    if n == 1:
        move(i, i + 1)
        move(i + 1, j)
    else:
        solve(n-1, i, k, j)
        move(i, i + 1)
        move(i + 1, j)
        solve(n - 1, k, j, i)


def move(i, j):
    print(h[i][-1], i, j)
    h[j].append(h[i].pop())



n = int(input())
h = [[], [i for i in range(n, 0, -1)], [], []]
solve(n, 1, 3, 2)