import sys
from collections import deque
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\Krafton03\\input.txt", "r")

n, m = map(int, sys.stdin.readline().split())
queue = deque()
graph=[]
shark = []
for i in range(n):
    shark.append(list(map(int, sys.stdin.readline().split())))
    for j in range(m):
        if shark[i][j] == 1:
            queue.append([i, j])
graph.append(shark)

def bfs():
    dx = [1, -1, 0 ,0]
    dy = [0, 0, 1, -1]
    ddx = [1, -1, 1 ,-1]
    ddy = [-1, 1, 1, -1]

    while queue:
        x, y = queue.popleft()

        for i in range(4): # 십자
            a = x + dx[i]
            b = y + dy[i]

            if 0 <= a < n and 0 <= b < m and shark[a][b] == 0:
                queue.append([a, b])
                shark[a][b] = shark[x][y] + 1

        for i in range(4):  # 대각선
            a = x + ddx[i]
            b = y + ddy[i]

            if 0 <= a < n and 0 <= b < m and shark[a][b] == 0:
                queue.append([a, b])
                shark[a][b] = shark[x][y] + 1
    
    cnt = 0

    for i in shark:
        for j in i:
            if j == 0:
                continue
        cnt = max(cnt, max(i))
    print(cnt-1)

bfs()
# for i in shark:
#     print(*i)