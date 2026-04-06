# 에라토스테네스의 체

import sys

m, n = list(map(int, sys.stdin.readline().split()))

isPrime = [1 for _ in range(n+1)]
isPrime[1] = 0

for i in range(2, int(n**0.5)+1):
    if isPrime[i] == 0:
        continue

    for j in range(i*i, n+1, i): # i*2, i*3 이런 건 앞에서 이미 지워짐!!
        isPrime[j] = 0

for i in range(m, n+1):
    if isPrime[i]:
        print(i)