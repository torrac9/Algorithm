import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\Krafton03\\input.txt", "r")
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())
wood = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
cnt = 0

def dfs(board, x, y):
    if board == '-':
        check = [0, 1]
    else:
        check = [1, 0]

    dx = x + check[0]
    dy = y + check[1]
    if 0 <= dx < n and 0 <= dy < m and not visited[dx][dy] and wood[dx][dy] == board:
        visited[dx][dy] = 1
        dfs(board, dx, dy)

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            cnt += 1
            visited[i][j] = 1
            dfs(wood[i][j], i, j)
#print(wood)
print(cnt)