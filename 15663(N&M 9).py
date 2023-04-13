import sys

n, m = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))
visited = [False] * n
temp = []

def dfs():
    if len(temp) == m:
        print(*temp)
        return
    remember_me = 0
    for i in range(n):
        if not visited[i] and remember_me != nums[i]:
            visited[i] = True
            temp.append(nums[i])
            remember_me = nums[i]
            dfs()
            visited[i] = False
            temp.pop()

dfs()