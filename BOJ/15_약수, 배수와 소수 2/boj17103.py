import sys

MAX_VALUE = 1000000

isPrime = [1 for _ in range(MAX_VALUE+1)]
isPrime[1] = 0

for i in range(2, int(MAX_VALUE**0.5) + 1):
    if isPrime[i] == 0:
        continue

    for j in range(i*i, MAX_VALUE+1, i):
        isPrime[j] = 0

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())

    cnt = 0
    for i in range(2, n//2 + 1):
        if isPrime[i] and isPrime[n-i]:
            cnt += 1
    print(cnt)

