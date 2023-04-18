import sys
from collections import deque
from queue import PriorityQueue

n = int(sys.stdin.readline())
q = PriorityQueue()

for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if q.empty():
            print('0')
        else:
            print(-q.get())
    else:
        q.put(-x)