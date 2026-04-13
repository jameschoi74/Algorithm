import sys

s = sys.stdin.readline().strip()
q = int(sys.stdin.readline().strip())

sums = [[0 for _ in range(26)]]
for i in range(len(s)):
    letter = s[i]
    sums.append(sums[i][:])
    sums[i+1][ord(letter) - ord('a')] += 1

for _ in range(q):
    alpha, l, r = list(sys.stdin.readline().strip().split())
    l = int(l)
    r = int(r)

    print(sums[r+1][ord(alpha) - ord('a')] - sums[l][ord(alpha) - ord('a')])