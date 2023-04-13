import sys

N, M = map(int, input().split())
num = list(map(int, sys.stdin.readline().split()))
arr = []
num.sort()
def combination(start):
    if len(arr) == M and arr == sorted(arr):
        print(' '.join(map(str,arr)))
        return
    else:
        for i in num: 
            if i not in arr:
                arr.append(i) 
                combination(i)
                arr.pop()
            
combination(1)