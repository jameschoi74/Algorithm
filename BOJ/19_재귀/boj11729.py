def dfs(n, s, e):
    if n == 0:
        return

    dfs(n-1, s, 6-s-e)
    print(s, e)
    dfs(n - 1, 6 - s - e, e)

n = int(input())

print(2**n - 1)
dfs(n, 1, 3)