import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\Krafton04\\input.txt", "r")

n, m = map(int, sys.stdin.readline().split())
small = []
for _ in range(m):
    small.append(int(sys.stdin.readline()))
dp = [[float('inf')] * (int((2*n)**0.5)+2) for _ in range(n+1)]
dp[1][0] = 0

for i in range(2, n+1):
    if i in small:
        continue
    for j in range(1, int((2*i)**0.5)+1):
        dp[i][j] = min(dp[i-j][j-1], dp[i-j][j], dp[i-j][j+1]) + 1

if min(dp[n]) == float('inf'):
    print(-1)
else:
    print(min(dp[n]))