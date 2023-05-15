import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\BOJ\\input.txt", "r")

r, c, t = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
ac = []
for i in range(r):
    if graph[i][0] == -1:
        ac.append(i)
acu = ac[0]
acd = ac[1]

while t > 0:
    n_graph = [[0]*c for _ in range(r)]
    t -= 1

    for i in range(r):
        for j in range(c):
            val = graph[i][j]
            cnt = 0
            if val > 4:
                if 0 <= i-1 < r and graph[i-1][j] != -1:
                    n_graph[i-1][j] += val // 5
                    cnt += 1
                if 0 <= i+1 < r and graph[i+1][j] != -1:
                    n_graph[i+1][j] += val // 5
                    cnt += 1
                if 0 <= j-1 < c and graph[i][j-1] != -1:
                    n_graph[i][j-1] += val // 5
                    cnt += 1
                if 0 <= j+1 < c and graph[i][j+1] != -1:
                    n_graph[i][j+1] += val // 5
                    cnt += 1
                n_graph[i][j] -= (val//5)*cnt
    
    for i in range(r):
        for j in range(c):
            graph[i][j] += n_graph[i][j]
    graph[acu][0] = -1
    graph[acd][0] = -1

    n_graph = [[0]*c for _ in range(r)]
    for i in range(2, c):
        n_graph[acu][i] = graph[acu][i-1]
        graph[acu][i-1] = 0
    for i in range(acu):
        n_graph[i][c-1] = graph[i+1][c-1]
        graph[i+1][c-1] = 0
    for i in range(c-1):
        n_graph[0][i] = graph[0][i+1]
        graph[0][i+1] = 0
    for i in range(1, acu+1):
        n_graph[i][0] = graph[i-1][0]
        graph[i-1][0] = 0
    
    for i in range(2, c):
        n_graph[acd][i] = graph[acd][i-1]
        graph[acd][i-1] = 0
    for i in range(acd, r-1):
        n_graph[i+1][c-1] = graph[i][c-1]
        graph[i][c-1] = 0
    for i in range(c-1):
        n_graph[r-1][i] = graph[r-1][i+1]
        graph[r-1][i+1] = 0
    for i in range(acd, r-1):
        n_graph[i][0] = graph[i+1][0]
        graph[i+1][0] = 0



    n_graph[acu][0] = 0
    n_graph[acd][0] = 0
    
    for i in range(r):
        for j in range(c):
            graph[i][j] += n_graph[i][j]

    # for i in graph:
    #     print(*i)
    # print()

# for i in n_graph:
#     print(*i)
# print()
result = 0
for i in range(r):
    for j in range(c):
        result += graph[i][j]
print(result+2)