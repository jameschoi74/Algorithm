import sys
import math

a, b = map(int, sys.stdin.readline().strip().split())
c, d = map(int, sys.stdin.readline().strip().split())

numerator = a*d + b*c
denominator = b*d
divisor = math.gcd(numerator, denominator)

print(numerator//divisor, denominator//divisor)