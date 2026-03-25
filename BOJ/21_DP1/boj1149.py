import sys

n = int(sys.stdin.readline().strip())

prices = [[0, 0, 0]]
for _ in range(n):
    prices.append(list(map(int, sys.stdin.readline().strip().split())))

dp = [[0, 0, 0] for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + prices[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + prices[i][1]
    dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + prices[i][2]

print(min(dp[n]))