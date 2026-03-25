import sys

n = int(sys.stdin.readline().strip())

tri = []
dp = []
for _ in range(n):
    tri.append(list(map(int, sys.stdin.readline().strip().split())))
    dp.append([0 for _ in range(len(tri[-1]))])

dp[0][0] = tri[0][0]
for i in range(1, n):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] = dp[i-1][j] + tri[i][j]
        elif j == len(dp[i]) - 1:
            dp[i][j] = dp[i-1][j-1] + tri[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + tri[i][j]

print(max(dp[-1]))