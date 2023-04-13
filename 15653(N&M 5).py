import sys

N, M = map(int, input().split())
num = list(map(int, sys.stdin.readline().split()))
arr = []

def permutation():
    if len(arr) == M:
        print(' '.join(map(str,arr)))
        return
    else:
        for i in sorted(num): 
            if i not in arr:
                arr.append(i) 
                permutation()
                arr.pop()
            
permutation()