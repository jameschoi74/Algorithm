import sys
from math import gcd

n = int(sys.stdin.readline().strip())

nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline().strip()))

d = []
for i in range(n-1):
    d.append(nums[i+1] - nums[i])

gcd_value = d[0]
for i in range(1, len(d)):
    gcd_value = gcd(gcd_value, d[i])

print((nums[-1] - nums[0]) // gcd_value - len(nums) + 1)