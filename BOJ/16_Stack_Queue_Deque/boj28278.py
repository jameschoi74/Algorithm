import sys

n = int(sys.stdin.readline().strip())

stk = []
for _ in range(n):
    command = list(map(int, sys.stdin.readline().strip().split()))
    if len(command) == 2:
        x = command[1]
        stk.append(x)
    elif command[0] == 2:
        if stk:
            print(stk.pop())
        else:
            print(-1)
    elif command[0] == 3:
        print(len(stk))
    elif command[0] == 4:
        if stk:
            print(0)
        else:
            print(1)
    elif command[0] == 5:
        if stk:
            print(stk[-1])
        else:
            print(-1)
