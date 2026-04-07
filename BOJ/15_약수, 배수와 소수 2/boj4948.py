import sys

isPrime = [1 for _ in range(123456*2 + 1)]
isPrime[1] = 0

for i in range(2, int((123456*2) ** 0.5)+1):
    if isPrime[i] == 0:
        continue

    for j in range(i * i, 123456 * 2 + 1, i):
        isPrime[j] = 0

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    cnt = 0
    for i in range(n+1, 2*n + 1):
        if isPrime[i]:
            cnt += 1
    print(cnt)