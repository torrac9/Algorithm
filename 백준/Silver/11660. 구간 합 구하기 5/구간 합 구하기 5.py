import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\BOJ\\input.txt", "r")

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
calculate = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
cnt = 0
dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] += graph[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
# for i in dp:
#     print(*i)    

while (cnt < m):
    x1, y1, x2, y2 = calculate[cnt]
    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])

    #print(x1, y1, x2, y2)
    cnt += 1