import sys
from collections import deque
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\Krafton03\\input.txt", "r")

n, m = map(int, sys.stdin.readline().split())
laby = [list(map(int, sys.stdin.readline().strip()))for _ in range(n)]
visited = [[0]*m for _ in range(n)]

def bfs(x, y):
    global result
    cnt = 0
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        #print(queue)
        p, q = queue.popleft()
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        for i in range(4):
            nx = p + dx[i]
            ny = q + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if laby[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                laby[nx][ny] = laby[p][q] + 1
                queue.append((nx, ny))
        
    return

bfs(0, 0)

print(laby[n-1][m-1])