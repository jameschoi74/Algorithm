import sys
from collections import deque

n = int(sys.stdin.readline().strip())

lines = deque(list(map(int, sys.stdin.readline().strip().split())))
stk = []

order = 1
while True:
    if lines:
        if lines[0] == order:
            lines.popleft()
            order += 1
        else:
            if stk and stk[-1] == order:
                stk.pop()
                order += 1
            else:
                stk.append(lines.popleft())
    else:
        if stk:
            if stk.pop() == order:
                order += 1
            else:
                print("Sad")
                break
        else:
            print("Nice")
            break
