import sys
#sys.stdin = open("input.txt", "rt")

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            jump = arr[i][j]
            if i+jump < n:
                dp[i+jump][j] += dp[i][j]
            if j+jump < n:
                dp[i][j+jump] += dp[i][j]
# for i in dp:
#     print(*i)
print(dp[-1][-1])