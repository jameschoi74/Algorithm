from collections import deque

n, k = list(map(int, input().split()))

nums = deque([i for i in range(1, n+1)])

res = []

while nums:
    for _ in range(k-1):
        nums.append(nums.popleft())
    res.append(nums.popleft())

ans = "<"
for i in range(len(res)-1):
    ans += f"{res[i]}, "
ans += f"{res[-1]}>"

print(ans)