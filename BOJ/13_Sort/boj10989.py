import sys

n = int(sys.stdin.readline())

cnt = [0 for _ in range(10001)]

for _ in range(n):
    cnt[int(sys.stdin.readline())] += 1

res = []
for i in range(len(cnt)):
    for _ in range(cnt[i]):
        print(i)