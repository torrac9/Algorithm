import sys

def binary(array, target, start, end):
    if start > end:
        print('0')
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        print('1')
        return mid
    
    elif array[mid] > target:
        return binary(array, target, start, mid-1)
    else:
        return binary(array, target, mid+1, end)

n = int(sys.stdin.readline())
array = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))

for i in target:
    binary(array, i, 0, n - 1)