import sys

N = int(sys.stdin.readline())
li = []

for i in range(N):
    li.append(int(sys.stdin.readline()))
li.sort()
for i in li:
    print(i)