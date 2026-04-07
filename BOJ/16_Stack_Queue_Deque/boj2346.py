from collections import deque
import sys

n = int(sys.stdin.readline().strip())
nums = deque(list(map(int, sys.stdin.readline().strip().split())))

q = deque([i for i in range(1, n+1)])

for _ in range(n):
    idx = q.popleft() - 1
    print(idx + 1, end=" ")

    if not q:
        break

    amount = nums[idx]
    if amount > 0:
        q.rotate(-(amount-1))
    else:
        q.rotate(-amount)
