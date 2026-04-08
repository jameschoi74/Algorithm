import sys

n, k = list(map(int, sys.stdin.readline().strip().split()))
arr = list(map(int, sys.stdin.readline().strip().split()))

temp = [0 for _ in range(n + 1)]
cnt = 0
res = -1

def merge_sort(arr, p, r):
    if p < r:
        q = (p+r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)
    return

def merge(arr, p, q, r):
    global cnt
    global res

    i = p
    j = q + 1
    t = 1

    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            temp[t] = arr[i]
            t += 1
            i += 1
        else:
            temp[t] = arr[j]
            t += 1
            j += 1

    while i <= q:
        temp[t] = arr[i]
        t += 1
        i += 1
    while j <= r:
        temp[t] = arr[j]
        t += 1
        j += 1

    i = p
    t = 1

    while i <= r:
        arr[i] = temp[t]
        cnt += 1
        if cnt == k:
            res = temp[t]
        i += 1
        t += 1

    return

merge_sort(arr, 0, n-1)

print(res)
