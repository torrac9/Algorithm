import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\Krafton04\\input.txt", "r")

m, n = map(int, sys.stdin.readline().split())
height = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
dp = [[-1]*n for _ in range(m)]
dp[-1][-1] = 1
dp[0][0] = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and height[nx][ny] < height[x][y]:
            if dp[nx][ny] == -1:
                dp[nx][ny] = 0
                dfs(nx, ny)
                dp[x][y] += dp[nx][ny]
            else:
                dp[x][y] += dp[nx][ny]

dfs(0, 0)

print(dp[0][0])