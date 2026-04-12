import sys

n, k = list(map(int, sys.stdin.readline().strip().split()))
temps = list(map(int, sys.stdin.readline().strip().split()))

sums = [0 for _ in range(n+1)]
for i in range(n):
    sums[i+1] = sums[i] + temps[i]

res = -1e9
for i in range(k, n+1):
    res = max(res, sums[i] - sums[i-k])

print(res)