import sys

n = int(sys.stdin.readline().strip())

numbers = {}
temp = list(map(int, sys.stdin.readline().strip().split()))
for number in temp:
    if number not in numbers:
        numbers[number] = 1
    else:
        numbers[number] += 1

m = int(sys.stdin.readline().strip())

temp = list(map(int, sys.stdin.readline().strip().split()))
for number in temp:
    if number not in numbers:
        print(0, end=' ')
    else:
        print(numbers[number], end=' ')