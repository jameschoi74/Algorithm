import sys
import math

t = int(sys.stdin.readline().strip())

for _ in range(t):
    a, b = list(map(int, sys.stdin.readline().strip().split()))
    print(math.lcm(a,b))