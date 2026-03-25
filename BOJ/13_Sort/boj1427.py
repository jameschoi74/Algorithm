import sys

n = sys.stdin.readline()

ls = []
for l in n:
    ls.append(l)

ls.sort(reverse=True)

res = ''
for l in ls:
    res += l

print(res)

