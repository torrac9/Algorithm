import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\BOJ\\input.txt", "r")

t = int(sys.stdin.readline())

# def dfs(s):
#     for i in graph[s]:
        

#     return

while t > 0:
    t -= 1

    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    print(n-1)
    # for i in range(1, n+1):
    #     if visited[i] == 0:
    #         visited[i] = 1
    #         dfs(i)

    # print(graph)
    # print(visited)