import sys

n = int(sys.stdin.readline().strip())

nums_1 = list(map(int, sys.stdin.readline().strip().split()))
nums_2 = nums_1[::-1]

dp_1 = [0 for _ in range(n)]
dp_1[0] = 1

for i in range(1, n):
    temp = 1
    for j in range(i):
        if nums_1[j] < nums_1[i]:
            temp = max(temp, dp_1[j] + 1)
    dp_1[i] = temp

dp_2 = [0 for _ in range(n)]
dp_2[0] = 1

for i in range(1, n):
    temp = 1
    for j in range(i):
        if nums_2[j] < nums_2[i]:
            temp = max(temp, dp_2[j] + 1)
    dp_2[i] = temp

res = 0
for i in range(n):
    res = max(res, dp_1[i] + dp_2[-i-1] - 1)
print(res)
