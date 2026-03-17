from itertools import combinations

n, m = list(map(int, input().split()))
nums = list(map(int, input().split()))

res = 0
for each in list(combinations(nums, 3)):
    if sum(each) <= m:
        res = max(res, sum(each))
print(res)