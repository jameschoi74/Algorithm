import sys

n, m = list(map(int, sys.stdin.readline().strip().split()))

names_n = set()
for _ in range(n):
    names_n.add(sys.stdin.readline().strip())

names_m = set()
for _ in range(m):
    names_m.add(sys.stdin.readline().strip())

res = list(names_n & names_m)
res.sort()

print(len(res))
for name in res:
    print(name)