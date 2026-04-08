from math import log

def dfs(n, s):
    if n == 1:
        return

    for i in range(s[0] + n//3, s[0] + 2 * (n//3)):
        for j in range(s[1] + n//3, s[1] + 2 * (n//3)):
            arr[i][j] = " "

    dfs(n//3, [s[0], s[1]])
    dfs(n//3, [s[0], s[1] + n//3])
    dfs(n//3, [s[0], s[1] + 2 * (n//3)])
    dfs(n//3, [s[0] + n//3, s[1]])
    dfs(n//3, [s[0] + n//3, s[1] + 2 * (n//3)])
    dfs(n//3, [s[0] + 2 * (n//3), s[1]])
    dfs(n//3, [s[0] + 2 * (n//3), s[1] + n//3])
    dfs(n//3, [s[0] + 2 * (n//3), s[1] + 2 * (n//3)])

    return

n = int(input())

arr = [["*" for _ in range(n)] for _ in range(n)]

dfs(n, [0, 0])

for line in arr:
    print(''.join(line))