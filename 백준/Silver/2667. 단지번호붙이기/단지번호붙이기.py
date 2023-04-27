import sys
from collections import deque
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\Krafton03\\input.txt", "r")

n = int(sys.stdin.readline())
visited = [[0]*n for _ in range(n)]
graph = [list(map(int, sys.stdin.readline().strip()))for _ in range(n)]
result = 0

def bfs(x,y):
    global result
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
            
            if nx <= -1 or nx >= n or ny <= -1 or ny >=n:
                continue
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny]=1
                cnt += 1
                queue.append((nx,ny))
    result += 1
    return cnt

arr = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            sol = bfs(i, j)
            arr.append(sol)
print(result)
arr.sort()
for i in arr:
    print(i)
#print(graph)