import sys

s = sys.stdin.readline().strip()

res = set()
for length in range(1, len(s)+1):
    for i in range(len(s) - length+1):
        res.add(s[i:i+length])

print(len(res))

