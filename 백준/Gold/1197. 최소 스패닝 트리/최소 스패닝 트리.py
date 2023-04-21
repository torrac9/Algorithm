import sys

v, e = map(int, sys.stdin.readline().split())
num = [list(map(int, sys.stdin.readline().split())) for i in range(e)]
num.sort(key = lambda x: x[2])  #가중치로 간선 정렬
p = [0] #상호배타적 집합
arr = []
edge = 0
cost = 0

for i in range(1, v+1):
    p.append(i)

def find(n):
    if n != p[n]:
        p[n] = find(p[n])
    return p[n]

def union(n, m):
    root1 = find(n)
    root2 = find(m)
    p[root2] = root1

while 1:
    if edge == v-1:
        break
    n, m ,o = num.pop(0)
    if find(n) != find(m):
        union(n, m)
        arr.append((n, m))
        cost += o
        edge += 1

print(cost)