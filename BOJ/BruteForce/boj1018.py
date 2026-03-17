n, m = list(map(int, input().split()))

board = []
for _ in range(n):
    board.append(input())

res = 64
for i in range(n-7):
    for j in range(m-7):

        cnt_b = 0
        cnt_w = 0
        flag_b = 1
        flag_w = 1
        for p in range(8):
            for q in range(8):
                if flag_b and board[i+p][j+q] == 'W':
                    cnt_b += 1
                if not flag_b and board[i+p][j+q] == 'B':
                    cnt_b += 1

                if flag_w and board[i+p][j+q] == 'B':
                    cnt_w += 1
                if not flag_w and board[i+p][j+q] == 'W':
                    cnt_w += 1

                if q == 7:
                    continue
                if flag_b:
                    flag_b = 0
                else:
                    flag_b = 1

                if flag_w:
                    flag_w = 0
                else:
                    flag_w = 1
        res = min(res, min(cnt_b, cnt_w))
print(res)