import sys

m, n = list(map(int, sys.stdin.readline().split()))

def is_prime(x):
    if x < 2:
        return 0

    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return 0
    return 1

for i in range(m, n+1):
    if is_prime(i):
        print(i)