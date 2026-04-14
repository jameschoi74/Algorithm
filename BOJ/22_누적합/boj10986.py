import sys

n, m = list(map(int, sys.stdin.readline().strip().split()))
nums = list(map(int, sys.stdin.readline().strip().split()))

sums = [0 for _ in range(n+1)]
for i in range(n):
    sums[i+1] = sums[i] + nums[i]

r = [0 for _ in range(m)]
for i in range(1, n+1):
    r[sums[i] % m] += 1

res = r[0]
for i in range(m):
    res += (r[i] * (r[i]-1)) // 2
print(res)