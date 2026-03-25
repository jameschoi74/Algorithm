import sys

n, m = list(map(int, sys.stdin.readline().strip().split()))

dex_name = {}
dex_number = {}
for i in range(1, n+1):
    name = sys.stdin.readline().strip()
    dex_name[name] = i
    dex_number[i] = name

for _ in range(m):
    p = sys.stdin.readline().strip()
    if p.isdigit():
        print(dex_number[int(p)])
    else:
        print(dex_name[p])
