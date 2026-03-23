import sys

n = int(sys.stdin.readline().strip())

res = set()
for _ in range(n):
    name, status = list(sys.stdin.readline().strip().split())
    if status == 'enter':
        res.add(name)
    else:
        res.remove(name)

res = list(res)
res.sort(reverse=True)

for name in res:
    print(name)