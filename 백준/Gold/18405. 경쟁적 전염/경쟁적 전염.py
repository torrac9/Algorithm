import sys
from collections import deque
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\Krafton03\\input.txt", "r")

n, m = map(int, sys.stdin.readline().split())
queue = deque()
virus = []
visited = [[0]*n for _ in range(n)]
for i in range(n):
    virus.append(list(map(int, sys.stdin.readline().split())))
s, x, y = map(int, sys.stdin.readline().split())

def bfs():
    dx = [1, -1, 0 ,0]
    dy = [0, 0, 1, -1]

    while queue:
        xx, yy = queue.popleft()
        v = virus[xx][yy]

        for i in range(4): # 십자
            a = xx + dx[i]
            b = yy + dy[i]

            if a >= n or a < 0 or b >= n or b < 0:
                continue
            if virus[a][b] == 0:
                virus[a][b] = v
            if virus[a][b] != 0 and not visited[a][b]:
                #queue.append([a, b])
                if virus[a][b] > v:
                    virus[a][b] = v

for _ in range(s):
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and virus[i][j] != 0:
                visited[i][j] = 1
                queue.append((i, j))
    bfs()
    # for z in virus:
    #     print(z)
    # print()
print(virus[x-1][y-1])