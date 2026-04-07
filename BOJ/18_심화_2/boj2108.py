import sys

n = int(sys.stdin.readline().strip())

nums = []
cnts = [0 for _ in range(8002)]

for _ in range(n):
    number = int(sys.stdin.readline().strip())
    nums.append(number)
    cnts[number+4000] += 1
nums.sort()

print(int(round(sum(nums) / n, 0)))
print(nums[n//2])

frequent_value = max(cnts)
cnt = 0
temp = 0
for i in range(8002):
    if cnts[i] == frequent_value:
        cnt += 1
        temp = i - 4000
        if cnt == 2:
            print(temp)
            break
if cnt == 1:
    print(temp)

print(max(nums) - min(nums))