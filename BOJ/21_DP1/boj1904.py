import sys

n = int(sys.stdin.readline())

dp = [[0, 1], [1, 1]]
if n == 1 or n == 2:
    print((dp[n-1][0] + dp[n-1][1]) % 15746)
else:
    for i in range(3, n+1):
        dp = [dp[1], [(dp[0][0] + dp[0][1]) % 15746, (dp[0][0] + dp[0][1] + dp[1][0]) % 15746]]

    print((dp[1][0] + dp[1][1]) % 15746)
