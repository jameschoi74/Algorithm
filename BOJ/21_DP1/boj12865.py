import sys

n, k = list(map(int, sys.stdin.readline().strip().split()))

things = [[0, 0]]
for _ in range(n):
    things.append(list(map(int, sys.stdin.readline().strip().split())))

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        w = things[i][0]
        v = things[i][1]

        if w > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(max(dp[-1]))
