import sys

n = int(sys.stdin.readline().strip())

words = set()
for _ in range(n):
    words.add(sys.stdin.readline().strip())

words = list(words)
words.sort(key=lambda x: (len(x), x))

for word in words:
    print(word)