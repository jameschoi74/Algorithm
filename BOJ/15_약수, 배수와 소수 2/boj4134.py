import sys

def is_prime(number):
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return 0
    return 1

n = int(sys.stdin.readline().strip())

for _ in range(n):
    num = int(sys.stdin.readline().strip())
    if num == 0 or num == 1:
        num = 2

    while not is_prime(num):
        num += 1
    print(num)