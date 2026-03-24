import sys
import math


a, b = list(map(int, sys.stdin.readline().strip().split()))
print(math.lcm(a,b))