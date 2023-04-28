import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\Krafton04\\input.txt", "r")

n, k = map(int, sys.stdin.readline().split())
stuff = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] *(k+1) for _ in range(n+1)]       #2차원 배열

for i in range(n+1):
    for j in range(k+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif stuff[i-1][0] <= j:
            dp[i][j] = max(stuff[i-1][1] + dp[i-1][j-stuff[i-1][0]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

# for z in dp:
#     print(*z)
print(dp[i][j])