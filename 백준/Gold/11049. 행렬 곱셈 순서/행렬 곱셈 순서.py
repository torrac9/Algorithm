import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\Krafton04\\input.txt", "r")

n = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] *(n) for _ in range(n)]       #2차원 배열

for i in range(1, n):
    for j in range(n-i):
        x = j+i
        dp[j][x] = 2**32
        for k in range(j,x):
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k+1][x] + matrix[j][0]*matrix[k][1]*matrix[x][1])

print(dp[0][n-1])