import sys

n = int(sys.stdin.readline().strip())
wires = []
for _ in range(n):
    wires.append(list(map(int, sys.stdin.readline().strip().split())))

wires.sort(key=lambda x: x[0])

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if wires[i][1] > wires[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))