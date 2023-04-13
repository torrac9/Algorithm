N, M = map(int, input().split())
arr = []

def permutation():
    if len(arr) == M:
        print(' '.join(map(str,arr)))
        return
    else:
        for i in range(1,N+1): 
          #  if i not in arr:
                arr.append(i) 
                permutation()
                arr.pop()
            
permutation()