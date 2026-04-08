import sys

def dfs(s, l, r):
    global cnt
    cnt += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return dfs(s, l+1, r-1)

t = int(sys.stdin.readline().strip())

for _ in range(t):
    s = sys.stdin.readline().strip()

    cnt = 0
    res = dfs(s, 0, len(s)-1)

    print(res, cnt)