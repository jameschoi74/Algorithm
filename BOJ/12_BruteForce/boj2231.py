n = int(input())

res = 1
while True:
    if res == 1000001:
        print(0)
        break

    temp = res
    for each in str(res):
        temp += int(each)
    if temp == n:
        print(res)
        break
    res += 1