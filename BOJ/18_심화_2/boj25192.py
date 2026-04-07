import sys

n = int(sys.stdin.readline().strip())

cnt = 0
for _ in range(n):
    s = sys.stdin.readline().strip()
    if s == "ENTER":
        users = set()

    else:
        if s not in users:
            users.add(s)
            cnt += 1

print(cnt)