import sys
from collections import deque
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\Krafton03\\input.txt", "r")
sys.setrecursionlimit(10**6)

k = int(sys.stdin.readline())

def dfs(s):
    global result
    for i in graph[s]:
        if visited[i] == 0:
            if visited[s] == 1:
                visited[i] =2
            elif visited[s] == 2:
                visited[i] = 1
            dfs(i)
        else:
            if visited[i] == visited[s]:
                result = 0
                return
                

while k:
    k -= 1
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for i in range(v+1)] 
    visited = [0]*(v+1)
    result = 1
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v+1):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)

    if result == 0:
        print("NO")
    else: print("YES")