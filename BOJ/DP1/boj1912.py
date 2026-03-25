import sys

n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))

dp = [0 for _ in range(n)]
dp[0] = nums[0]

for i in range(1, n):
    dp[i] = max(dp[i-1]+nums[i], nums[i])

print(max(dp))