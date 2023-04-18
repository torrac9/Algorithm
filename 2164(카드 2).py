import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque()

for i in range(n):
    q.append(i+1)
for i in range(n-1):
    q.popleft()
    n = q.popleft()
    q.append(n)

print(*q)