import sys

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        a = 20
        b = 20
        c = 20

    if board[a][b][c] != 0:
        return board[a][b][c]
    else:
        if a < b and b < c:
            board[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
            return board[a][b][c]
        else:
            board[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
            return board[a][b][c]

board = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
board[0][0][0] = 1

while True:
    a, b, c = map(int, sys.stdin.readline().strip().split())
    if a == -1 and b == -1 and c == -1:
        break

    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")