N, M = map(int, input().split())
arr = []

def permutation(start):
    if len(arr) == M:
        print(' '.join(map(str,arr)))
        return
    else:
        for i in range(start,N+1): 
            #if i not in arr:
                arr.append(i) 
                permutation(i)
                arr.pop()
            
permutation(1)