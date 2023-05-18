import sys
import heapq
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\BOJ\\input.txt", "r")

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
inf = int(1e9)
distance = [inf] * (n+1)
graph = [[]for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
start, end = map(int, sys.stdin.readline().split())
arr = [[start] for _ in range(n+1)]

def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start, [start]))
    distance[start] = 0

    while q:
        dist, node, lst = heapq.heappop(q)
        if node == end:
            return distance[end], lst
        for next, l in graph[node]:
            cost = dist + l
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next, lst + [next]))

asw, lst = dijkstra(start, end)

print(asw)
print(len(lst))
print(*lst)