import sys
from collections import deque
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\Krafton03\\input.txt", "r")
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
graph = [[] for i in range(n+1)]

for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

#dfs
visited = [0]*(n+1)

arr = []

def dfs(s):
    for i in graph[s]:
        if visited[i] == 0:
            visited[i] = s
            dfs(i)

dfs(1)

for x in range(2, n+1):
    print(visited[x])

#bfs
# queue = deque()
# queue.append(1)

# ans = [0]*(n+1)

# def bfs():
#     while queue:
#         now = queue.popleft()
#         for j in graph[now]:
#             if ans[j] == 0:
#                 ans[j] == now
#                 queue.append(j)

# bfs()
# result = ans[2:]
# for i in result:
#     print(i)