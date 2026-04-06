import sys

n, m = list(map(int, sys.stdin.readline().strip().split()))

board = []
for _ in range(n):
    board.append(sys.stdin.readline().strip())

def check_garbage(i, j):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for k in range(4):
        i_check = i + dy[k]
        j_check = j + dx[k]
        if 0 <= i_check < n and 0 <= j_check < m and board[i_check][j_check] == 'g':
            return True
    return False

for i in range(n):
    for j in range(m):
        if board[i][j] == 'S':
            q = [[i, j, 0, 0]]
        if board[i][j] == 'F':
            i_target = i
            j_target = j

visited = [[0 for _ in range(m)] for _ in range(n)]

res = []
while q:
    cur = q.pop(0)

    if cur[0] == i_target and cur[1] == j_target:
        res.append(cur)
        continue

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, - 1]

    for k in range(4):
        i_check = cur[0] + dy[k]
        j_check = cur[1] + dx[k]
        if 0 <= i_check < n and 0 <= j_check < m and not visited[i_check][j_check]:
            if board[i_check][j_check] == 'g':
                q.append([i_check, j_check, cur[2] + 1, cur[3]])
            elif check_garbage(i_check, j_check):
                q.append([i_check, j_check, cur[2], cur[3] + 1])
            else:
                q.append([i_check, j_check, cur[2], cur[3]])
            visited[i_check][j_check] = 1

print(res)