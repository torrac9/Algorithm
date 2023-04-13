import sys
from collections import deque

def bfs(x,y):
    global result
    queue = deque()
    queue.append((x,y))
    visited[x][y]=1
    
    while queue:
        p,q=queue.popleft() #fifo
        dx= [0,1,0,-1]
        dy = [1,0,-1,0]
        
        for i in range(4):  #인접한 블럭 검사
            nx = p + dx[i]
            ny = q + dy[i]
            
            if nx <= -1 or nx >= n or ny <= -1 or ny >=n:
                continue    #continue와 return False의 차이?
            if graph[nx][ny] > k and not visited[nx][ny]:
            
                visited[nx][ny]=1
                queue.append((nx,ny))
                
    result +=1        
        
    return True

n= int(sys.stdin.readline())
graph=[]

for i in range(n):
    graph.append(list(map(int,input().split())))

sum=1 #초기값 1
for k in range(1,101):
    result=0    #수위마다 result 초기화
    visited=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and not visited[i][j]: 
                bfs(i,j)
    
    sum = max(sum,result)                


print(sum)