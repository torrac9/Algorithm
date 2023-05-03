import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\Krafton04\\input.txt", "r")

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

dp = [1001]*(n)
dp[0] = 0

for i in range(n):
  for j in range(a[i]+1):
    if i+j < n and dp[i+j] > dp[i] + 1:
      #print(dp)
      dp[i+j] = dp[i] + 1



if dp[n-1] >= 1001:
  print(-1)
else:
  print(dp[n-1])