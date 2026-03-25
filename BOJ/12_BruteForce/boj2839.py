n = int(input())

cnt = n//5
left = n%5

res = -1
while cnt >= 0:

    if left%3 == 0:
        res = cnt + left//3
        break

    left += 5
    cnt -= 1
print(res)