import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\Krafton03\\input.txt", "r")
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
x, y = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(n+1)
cnt = 0

#print(graph)
#print(visited)
def dfs(s):
     visited[s] = s
     global cnt, y
     for i in graph[s]:
        if visited[i] == 0:
            visited[i] = s
            cnt += 1
            dfs(i)
            if i == y:
                print(cnt)
                exit()
            else: cnt -= 1
   
dfs(x)
print('-1')