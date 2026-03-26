import sys

n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))

dp = [0 for _ in range(n)]
dp[0] = 1

for i in range(1, n):
    temp = 0
    for j in range(i):
        if nums[j] < nums[i]:
            temp = max(temp, dp[j])
    dp[i] = temp + 1

print(max(dp))