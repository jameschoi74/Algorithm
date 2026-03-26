import sys

n = int(sys.stdin.readline())

dp = {}
for i in range(10):
    dp[i] = 0

for i in range(1, 10):
    dp[i] += 1

for _ in range(2, n+1):
    temp = [0 for j in range(10)]
    temp[0] += dp[1]
    for i in range(1, 9):
        temp[i] += dp[i-1] + dp[i+1]
    temp[9] += dp[8]

    for i in range(10):
        dp[i] = temp[i]

print(sum(dp.values()) % 1000000000)

# 1 2 3 4 5 6 7 8 9
#
# 10
# 21
# 12 32
# 23 43
# 34 54
# 45 65
# 56 76
# 67 87
# 78 98
# 89

