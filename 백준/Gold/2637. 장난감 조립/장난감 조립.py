import sys
from collections import deque
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\Krafton03\\input.txt", "r")

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
needs = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    x, y, k = map(int, sys.stdin.readline().split())
    graph[y].append([x, k])
    indegree[x] += 1

def topology_sort():
    global n
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()

        for next, need in graph[now]:
            if needs[now].count(0) == n + 1:
                needs[next][now] += need
            else:
                for i in range(1, n+1):
                    needs[next][i] += needs[now][i] * need
            
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)
    
    for i in enumerate(needs[n]):
        if i[1] > 0:
            print(*i)            
topology_sort()