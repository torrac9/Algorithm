import sys
sys.setrecursionlimit(10000)

N, M = list(map(int, sys.stdin.readline().split()))
array = sorted(list(map(int, sys.stdin.readline().split())))

def binary(array, start, end):
    sum = 0
    if end-start == 1:
        return start
    mid = (start + end) // 2
    for i in array:
        if i > mid:
            sum += i-mid
    if M > sum:
        return binary(array, start, mid)
    else:
        return binary(array, mid, end)

height = binary(array, 0, 1000000000)

print(height)