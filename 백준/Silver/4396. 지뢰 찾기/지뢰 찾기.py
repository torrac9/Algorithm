import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\BOJ\\input.txt", "r")

n = int(sys.stdin.readline())
mine = [list(sys.stdin.readline().strip()) for _ in range(n)]
graph = [list(sys.stdin.readline().strip()) for _ in range(n)]
mine_arr = []
for i in range(n):
    for j in range(n):
        if mine[i][j] == '*':
            mine_arr.append([i, j])
#print(mine_arr)

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'x':
            if mine[i][j] == '.':
                graph[i][j] = 0
                for k in range(8):
                    if 0 <= i+dx[k] < n and 0 <= j+dy[k] < n:
                        if mine[i+dx[k]][j+dy[k]] == '*':
                            graph[i][j] += 1
            else:
                for k in mine_arr:
                    graph[k[0]][k[1]] = '*'

for i in graph:
    print(*i, sep='')