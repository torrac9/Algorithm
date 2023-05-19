import sys
from collections import deque
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\BOJ\\input.txt", "r")

n, m, k = map(int, sys.stdin.readline().split())
graph = [[0]*m for _ in range(n)]
for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    graph[r-1][c-1] = 1
visited = [[0]*m for _ in range(n)]
result = 0

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y]=1
    cnt = 1
    
    while queue:
        p,q=queue.popleft() #fifo
        dx= [0,1,0,-1]
        dy = [1,0,-1,0]
        
        for i in range(4):  #인접한 블럭 검사
            nx = p + dx[i]
            ny = q + dy[i]
            
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny]=1
                cnt += 1
                queue.append((nx,ny))
    return cnt

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            a = bfs(i, j)
            result = max(a, result)

# for i in graph:
#     print(i)
print(result)