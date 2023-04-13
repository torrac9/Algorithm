N, M = map(int, input().split())
arr = []

def combination(s):
    if len(arr) == M:
        print(' '.join(map(str,arr)))
        return
    else:
        for i in range(s,N+1): 
            if i not in arr:
                arr.append(i) 
                combination(i)
                arr.pop()
            
combination(1)