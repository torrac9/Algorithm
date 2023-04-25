import sys
import heapq
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\Krafton03\\input.txt", "r")

n, m, k, x = map(int, sys.stdin.readline().split())
inf = sys.maxsize
distance = [inf] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append((b, 1))

def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0
    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue
        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))


dijkstra(x)
ans = []
for i in range(1, len(distance)):
    if distance[i] == k:
        ans.append(i)
if len(ans) == 0:
    print('-1')
else: 
    for i in ans:
        print(i)