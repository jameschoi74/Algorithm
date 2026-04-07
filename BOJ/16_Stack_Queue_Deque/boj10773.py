import sys

k = int(sys.stdin.readline().strip())

stk = []
for _ in range(k):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        stk.pop()
    else:
        stk.append(num)

print(sum(stk))