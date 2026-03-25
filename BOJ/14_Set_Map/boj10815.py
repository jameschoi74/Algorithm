import sys

n = int(sys.stdin.readline().strip())
cards_n = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))

flag = [0 for _ in range(20000001)]
for number in cards_n:
    flag[number+10000000] = 1

for number in nums:
    print(flag[number+10000000], end=" ")

# dictionary로 풀어도 됨 (키 중에 있는지 확인하는 것은 O(1))