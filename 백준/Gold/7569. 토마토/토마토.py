import sys
from collections import deque
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\Krafton03\\input.txt", "r")

m, n ,h = map(int, sys.stdin.readline().split())
queue = deque()
graph = []

for i in range(h):
    tomato = []
    for j in range(n):
        tomato.append(list(map(int, input().split())))
        for k in range(m):
            if tomato[j][k] == 1:
                queue.append([i, j, k])
    graph.append(tomato)

def bfs():
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            a = x + dx[i]
            b = y + dy[i]
            c = z + dz[i]
            if 0 <= a < h and 0 <= b < n and 0 <= c < m and graph[a][b][c] == 0:
                queue.append([a, b, c])
                graph[a][b][c] = graph[x][y][z] + 1
    
    day = 0
    for i in graph:
        for j in i:
            for k in j:
                if k == 0:
                    print(-1)
                    exit()
            day = max(day, max(j))
    print(day-1)

bfs()