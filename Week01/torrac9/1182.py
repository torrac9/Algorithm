import sys

n, m = list(map(int, sys.stdin.readline().split()))
cnt = 0

nums = sorted(list(map(int, sys.stdin.readline().split())))
visited = [False] * n
temp = []
arr = []

def dfs(s, num):
    global cnt, arr
    if len(temp) == num and sum(temp)==m:
        print(*temp)
        cnt += 1
        return
    remember_me = 0
    for i in range(s, n+1):
        if not visited[i-1]:
            visited[i-1] = True
            temp.append(nums[i-1])
            remember_me = nums[i-1]
            dfs(i, num)
            visited[i-1] = False
            temp.pop()

for i in range(0, len(nums)): #모든 부분수열 찾기
    dfs(1, i)
if sum(nums) == 0: #전체 합이 0
    cnt += 1
if m == 0:
    cnt -= 1     # ''제외
print(cnt)