import sys
from collections import deque

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
apple = deque()
command = deque()
position = deque([1, 1])

for i in range(k):
    apple.append(list(map(int, sys.stdin.readline().split())))
l = int(sys.stdin.readline())
for i in range(l):
    command.append(list(map(str, sys.stdin.readline().split())))

#def move(x, c):


print(position)
print(apple)
print(command)