import sys

a, b = list(map(int, sys.stdin.readline().strip().split()))

set_a = set(map(int, sys.stdin.readline().strip().split()))
set_b = set(map(int, sys.stdin.readline().strip().split()))

res = (set_a-set_b) | (set_b-set_a)
print(len(res))
