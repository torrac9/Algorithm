import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\Krafton04\\input.txt", "r")

arr1 = sys.stdin.readline().strip()
arr2 = sys.stdin.readline().strip()
n, m = len(arr1), len(arr2) 
                                        #Introduction to algorithm
dp = [[0] *(m+1) for _ in range(n+1)]       #2차원 배열

for i in range(1, n+1):
    for j in range(1, m+1):
        if arr1[i-1] == arr2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# for i in dp:
#     print(*i)
print(dp[n][m])