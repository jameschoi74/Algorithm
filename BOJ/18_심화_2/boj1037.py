import sys

cnt = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))

nums.sort()

if len(nums) == 1:
    print(nums[0]**2)
else:
    print(nums[0] * nums[-1])