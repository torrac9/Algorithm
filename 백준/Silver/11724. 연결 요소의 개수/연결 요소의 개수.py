import sys
from collections import deque
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\Krafton03\\input.txt", "r")
N , M = map(int, sys.stdin.readline().split())
num = sorted([sorted(list(map(int, sys.stdin.readline().split()))) for i in range(M)])
num = deque(num)
p = [0] #상호배타적 집합
arr = []
ele = 0
edge = 0

for i in range(1, N+1):
    p.append(i)

def find(n):
    if n != p[n]:
        p[n] = find(p[n])
    return p[n]

def union(n, m):
    root1 = find(n)
    root2 = find(m)
    if root1 >= root2:
        p[root1] = root2
    else:
        p[root2] = root1
    #print(p)

while 1:
    if len(num) == 0:
        break
    #print(num)
    n, m = num.popleft()
    if find(n) != find(m):
        union(n, m)
        arr.append((n, m))
        edge += 1

#print(set(p))
print(len(set(p))-1)