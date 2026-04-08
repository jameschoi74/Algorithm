import sys

def dfs(arr, s, e):
    if e-s <= 1:
        return

    d = (e-s+1) // 3
    for i in range(s+d, e-d+1):
        arr[i] = " "

    dfs(arr, s, s+d-1)
    dfs(arr, e-d+1, e)

    return

while True:
    try:
        n = int(sys.stdin.readline().strip())
        arr = ["-" for _ in range(3**n)]

        dfs(arr, 0, 3**n - 1)

        print(''.join(arr))
    except:
        break