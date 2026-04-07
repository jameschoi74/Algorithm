import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    s = sys.stdin.readline().strip()

    stk = []
    status = "YES"

    for l in s:
        if l == "(":
            stk.append(l)
        else:
            if not stk:
                status = "NO"
                break

            stk.pop()
    if stk:
        status = "NO"
    print(status)