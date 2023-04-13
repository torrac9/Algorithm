import sys

N, M = map(int, input().split())
num = list(map(int, sys.stdin.readline().split()))
arr = []
num.sort()
def combination(start):
    if len(arr) == M:
        #if arr == sorted(arr):
        print(' '.join(map(str,arr)))
        return
    else:
        for i in range(start, N+1): 
            #if i not in arr:
                arr.append(num[i-1]) 
                combination(i)
                arr.pop()
            
combination(1)