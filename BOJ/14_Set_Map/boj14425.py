import sys

n, m = list(map(int, sys.stdin.readline().strip().split()))

letters = set()
for _ in range(n):
    letters.add(sys.stdin.readline().strip())

cnt = 0
for _ in range(m):
    if sys.stdin.readline().strip() in letters:
        cnt += 1

print(cnt)