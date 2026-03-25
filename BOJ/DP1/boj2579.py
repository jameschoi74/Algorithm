import sys

n = int(sys.stdin.readline().strip())

stairs = []
for _ in range(n):
    stairs.append(int(sys.stdin.readline().strip()))

dp = [0 for _ in range(n)]

dp[0] = stairs[0]
if n == 1:
    print(dp[0])
elif n == 2:
    print(max([stairs[1], dp[0] + stairs[1]]))
else:
    dp[1] = [stairs[1], dp[0] + stairs[1]]
    dp[2] = [dp[0] + stairs[2], dp[1][0] + stairs[2]]

    for i in range(3, n):
        dp[i] = [max(dp[i-2]) + stairs[i], dp[i-1][0] + stairs[i]]

    print(max(dp[n-1]))
