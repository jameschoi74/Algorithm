import sys
from collections import deque

n = int(sys.stdin.readline().strip())
arr_a = list(map(int, sys.stdin.readline().strip().split()))
arr_b = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
to_add = list(map(int, sys.stdin.readline().strip().split()))


q = deque([])
for i in range(n):
    if arr_a[i] == 0:
        q.append(arr_b[i])

for num in to_add:
    q.appendleft(num)
    print(q.pop(), end=" ")
