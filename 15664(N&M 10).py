import sys

n, m = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))
visited = [False] * n
temp = []

def dfs(s):
    if len(temp) == m:
        print(*temp)
        return
    remember_me = 0
    for i in range(s, n+1):
        if not visited[i-1] and remember_me != nums[i-1]:
            visited[i-1] = True
            temp.append(nums[i-1])
            remember_me = nums[i-1]
            dfs(i)
            visited[i-1] = False
            temp.pop()

dfs(1)