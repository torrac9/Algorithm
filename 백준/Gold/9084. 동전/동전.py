import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\Krafton04\\input.txt", "r")

t = int(sys.stdin.readline())

for _ in range(t):      
    n = int(sys.stdin.readline().rstrip())
    coin = list(map(int, sys.stdin.readline().split()))
    #coin.insert(0,0)
    m = int(sys.stdin.readline())

    # dp = [[0] *(m+1) for _ in range(n+1)]       #2차원 배열
    # for i in range(n+1):
    #     dp[i][0] = 1
    # for i in range(1, n+1):
    #     for j in range(1, m+1):
    #         dp[i][j] = dp[i-1][j]
    #         if j - coin[i] >= 0:
    #             dp[i][j] += dp[i][j-coin[i]]
    # print(dp[n][m])

    dp = [0]*(m+1)      #1차원 배열
    dp[0] = 1
    for c in coin:
        for i in range(1, m+1):
            if i >= c:
                dp[i] += dp[i-c]
    print(dp[m])