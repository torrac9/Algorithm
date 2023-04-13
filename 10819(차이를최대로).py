import sys

n = int(sys.stdin.readline())
nums = sorted(list(map(int, sys.stdin.readline().split())))
visited = [False] * n
temp = []
arr = []
sol = 0

def dfs():
    sum = 0
    global sol
    if len(temp) == n:
        for i in range(n-1):
            sum += abs(temp[i-1] - temp[i])
        sol = max(sol, sum)
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
print(sol)