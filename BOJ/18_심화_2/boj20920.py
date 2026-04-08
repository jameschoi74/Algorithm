import sys

n, m = list(map(int, sys.stdin.readline().strip().split()))

dict = {}
words = []

for _ in range(n):
    s = sys.stdin.readline().strip()
    if s not in dict:
        dict[s] = 1
    else:
        dict[s] += 1

    if len(s) >= m:
        words.append(s)

words.sort(key=lambda x: (-dict[x], -len(x), x))

history = set()
for word in words:
    if word not in history:
        print(word)
        history.add(word)