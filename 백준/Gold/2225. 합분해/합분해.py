import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\BOJ\\input.txt", "r")

n, k = map(int, sys.stdin.readline().split())

dp = [[0] * (k+1) for _ in range(n+1)]
dp[0][0] = 1
for i in range(0, n+1):
    for j in range(1, k+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
#print(*dp)
print(dp[n][k] % 1000000000)