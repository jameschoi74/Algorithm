import sys
from collections import deque

n = int(sys.stdin.readline().strip())

q = deque([])
for _ in range(n):
    command = list(sys.stdin.readline().strip().split())

    if len(command) == 2:
        x = command[1]
        q.append(x)
    elif command[0] == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(q))
    elif command[0] == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif command[0] == "back":
        if q:
            print(q[-1])
        else:
            print(-1)