import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
q = deque()
sol = deque()

for i in range(n):
    q.append(i+1)

for i in range(n):
    q.rotate(-(k-1))
    num = q.popleft()
    sol.append(num)

print('<', end='')
for i in range(len(sol)-1):
    print(sol[i], end=', ')
print(sol[-1], end='')
print('>')