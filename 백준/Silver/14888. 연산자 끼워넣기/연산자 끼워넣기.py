import sys
#from collections import deque
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\Krafton03\\input.txt", "r")
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
p, m, t, d = map(int, sys.stdin.readline().split())

max_value = -sys.maxsize
min_value = sys.maxsize

def dfs(i, arr):
    global p, m, t, d, max_value, min_value

    if i == n:
        max_value = max(max_value, arr)
        min_value = min(min_value, arr)
    else:
        if p > 0:
            p -= 1
            dfs(i+1, arr + num[i])
            p += 1
        if m > 0:
            m -= 1
            dfs(i+1, arr - num[i])
            m += 1
        if t > 0:
            t -= 1
            dfs(i+1, arr * num[i])
            t += 1
        if d > 0:
            d -= 1
            if arr > 0:
                dfs(i+1, arr // num[i])
            else: dfs(i+1, -(-arr // num[i]))
            d += 1

dfs(1, num[0])


print(max_value)
print(min_value)