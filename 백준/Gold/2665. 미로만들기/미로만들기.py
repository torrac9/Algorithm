import sys
import heapq
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\Krafton03\\input.txt", "r")

n = int(sys.stdin.readline())
room = []
for _ in range(n):
    room.append(list(map(int, input().rstrip())))
visited = [[0]*n for _ in range(n)]

def dijkstra():
    hq = []
    heapq.heappush(hq, [0, 0, 0])
    visited[0][0] = 1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while hq:
        a, x, y = heapq.heappop(hq)
        if x == n-1 and y == n-1:
            print(a)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = 1
                if not room[nx][ny]: 
                    heapq.heappush(hq, [a+1, nx, ny])
                else:   heapq.heappush(hq, [a, nx, ny])

dijkstra()