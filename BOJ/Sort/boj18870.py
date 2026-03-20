import sys
from copy import deepcopy

n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))

cnt = list(set(nums))
cnt.sort()

dic = {}
for i in range(len(cnt)):
    dic[cnt[i]] = i

for number in nums:
    print(dic[number], end=" ")