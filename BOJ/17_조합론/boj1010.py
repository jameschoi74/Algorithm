import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n, m = list(map(int, sys.stdin.readline().strip().split()))

    res = 1
    for i in range(m, m-n, -1):
        res *= i

    for i in range(1, n+1):
        res //= i

    print(res)