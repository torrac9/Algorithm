import sys
from collections import deque
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\Krafton03\\input.txt", "r")
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
arr = sys.stdin.readline().strip()
graph = [[] for i in range(n+1)]
cnt = 0

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(s):
    global cnt
    for i in graph[s]:
        if visited[i] == 0:
            visited[i] = i
            if arr[i-1] == '1':
                cnt += 1
            else:   
                dfs(i)

for i in range(1, n+1):
    visited = [0]*(n+1)
    if arr[i-1] == '1':
        visited[i] = 1
        dfs(i)

print(cnt)