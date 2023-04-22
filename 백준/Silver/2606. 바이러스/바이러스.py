import sys
from collections import deque
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\Krafton03\\input.txt", "r")
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
num = sorted([sorted(list(map(int, sys.stdin.readline().split()))) for i in range(M)])
num = deque(num)
num1 = num.copy()   #깊은 복사
p = [0] #상호배타적 집합

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
    n1, m1 = num1.pop()
    if find(n1) != find(m1):
        union(n1, m1)

print(p.count(1)-1)