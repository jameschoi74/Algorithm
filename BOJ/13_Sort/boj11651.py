import sys

n = int(sys.stdin.readline())

board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

board.sort(key=lambda x: (x[1], x[0]))

for each in board:
    print(each[0], each[1])