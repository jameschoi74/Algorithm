import sys

n = int(input())

nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort()

for number in nums:
    print(number)